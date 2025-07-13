import MaterialX as mx
import os
import json
import argparse

def build_nodedef_info(insert_nodegroup=True):

    searchPath = mx.getDefaultDataSearchPath().asString()
    searchPath = os.path.normpath(searchPath)
    # Append 'libraries' to the search path
    searchPath = os.path.join(searchPath, 'libraries')

    stdlib = mx.createDocument()
    libFiles = mx.loadLibraries(mx.getDefaultDataLibraryFolders(), mx.getDefaultDataSearchPath(), stdlib)

    # Create main document and import the library document
    doc = mx.createDocument()
    doc.importLibrary(stdlib)

    # Print out the names of the library files loaded
    library_names = []
    if libFiles:
        for libFile in libFiles:
            # remove search path from the file name
            libFile = os.path.relpath(libFile, searchPath)
            #print('Loaded library file: %s' % libFile)
            # The first child path is the library name
            library_name = libFile.split(os.sep)[0]
            if library_name not in library_names:
                library_names.append(library_name)
    else:
        print('No library files loaded.')

    print("Loaded libraries:", library_names)

    library_dict = {"name": "Definitions", "version" :mx.getVersionString(), "children": []}
    currTargets = []
    targetNames = []
    for target in doc.getTargetDefs():
        currTargets.append( { 'name' : target.getName(), 'type' : 'targetdef' } )
        targetNames.append(target.getName())
    # Append "targets" to the library_dict
    targetNameString = ', '.join(targetNames)
    library_dict['targets']  = targetNameString

    print("Target List:", targetNames)

    # Emit typedefs if they exist
    typedefs = doc.getTypeDefs()
    if typedefs:
        typedef_group = {
            "name": "typedefs",
            "type": "typedef_group",
            "children": []
        }
        for typedef in typedefs:
            typedef_entry = {
                "name": typedef.getName(),
                "type": "typedef"
            }
            typedef_group["children"].append(typedef_entry)
        library_dict["children"].append(typedef_group)
        print("TypeDefs:", [typedef.getName() for typedef in typedefs])

    geompropdefs = doc.getGeomPropDefs()
    if geompropdefs:
        
        geompropdef_group = {
            "name": "geompropdefs",
            "type": "geompropdef_group",
            "children": []
        }
        for geompropdef in geompropdefs:
            geompropdef_entry = {
                "name": geompropdef.getName(),
                "type": geompropdef.getType(),
                "geomprop": geompropdef.getGeomProp(),
                "space": geompropdef.getSpace(),
                "index": geompropdef.getIndex()
            }
            geompropdef_group["children"].append(geompropdef_entry)
        library_dict["children"].append(geompropdef_group)
        print("GeomPropDefs:", [geompropdef.getName() for geompropdef in geompropdefs])

    # Build a mapping from library name to its node entry in the children list
    library_entries = {}
    for library_name in library_names:
        entry = {"name": library_name, "type": "library", "children": []}
        library_dict["children"].append(entry)
        library_entries[library_name] = entry    

    # For each nodedef, add to the correct library and node
    for nodedef in doc.getNodeDefs():
        sourceuri = nodedef.getSourceUri()
        for library_name in library_names:
            if library_name in sourceuri:
                node_name = nodedef.getNodeString()
                nodedef_name = nodedef.getName()
                nodegroup = nodedef.getNodeGroup()
                lib_entry = library_entries[library_name]

                # Determine the parent container based on whether nodegroup exists and option is enabled
                if nodegroup and insert_nodegroup:
                    # Find or create nodegroup entry under library
                    nodegroup_entry = next((item for item in lib_entry["children"] if item["name"] == nodegroup and item["type"] == "nodegroup"), None)
                    if nodegroup_entry is None:
                        nodegroup_entry = {"name": nodegroup, "type": "nodegroup", "children": []}
                        lib_entry["children"].append(nodegroup_entry)
                    parent_container = nodegroup_entry
                else:
                    # Use library as parent container (either no nodegroup or insert_nodegroup is False)
                    parent_container = lib_entry

                # Find or create node entry under the parent container
                node_entry = next((item for item in parent_container["children"] if item["name"] == node_name and item["type"] == "node"), None)
                if node_entry is None:
                    node_entry = {"name": node_name, "type": "node", "children": []}
                    parent_container["children"].append(node_entry)

                # Add nodedef as a child if not already present
                if not any(child["name"] == nodedef_name for child in node_entry["children"]):
                    new_child = {"name": nodedef_name, "type": "nodedef"}
                    version = nodedef.getVersionString()
                    if version:
                        new_child["version"] = version
                    
                    # Add nodegroup as metadata when not inserting nodegroup level
                    if nodegroup and not insert_nodegroup:
                        new_child["nodegroup"] = nodegroup
                        
                    docstring = nodedef.getAttribute('doc')
                    if docstring:
                        # Escape any quotes in the docstring
                        #docstring = docstring.replace('"', '\\"')
                        #docstring = docstring.replace("'", '\\"')
                        new_child["doc"] = docstring

                    # Add implementation children if they exist
                    implementation = nodedef.getImplementation()
                    if implementation:

                        # Add nodegraph
                        if implementation.isA(mx.NodeGraph):
                            if "children" not in new_child:
                                new_child["children"] = []
                            # Append children to node_entry if implementation exists
                            icon = "bi-diagram-3"
                            impl_string = implementation.getName()
                            new_child["children"].append({"target" : "all", "type": "nodegraph", "icon": icon, "name": impl_string})

                        # Add non-nodegraph implementation
                        else:
                            for target in targetNames:
                                implementation = nodedef.getImplementation(target)
                                if implementation:
                                    implementation_name = implementation.getName()
                                    # Add "children" array to new_child
                                    if "children" not in new_child:
                                        new_child["children"] = []
                                    # Check if a child with the same name and type already exists
                                    existing_child = next(
                                        (c for c in new_child["children"]
                                         if c.get("name") == implementation_name),
                                        None
                                    )
                                    if existing_child:
                                        # Append the target to the "target" string (comma-separated, unique)
                                        targets = set(existing_child["target"].split(", ")) if existing_child["target"] else set()
                                        targets.add(target)
                                        existing_child["target"] = ", ".join(sorted(targets))
                                    else:
                                        # Append new implementation entry
                                        new_item = {
                                            "icon": "bi-file-code",
                                            "name": implementation_name,
                                            "target": target,
                                            "type": "implementation",
                                        }

                                        # Check for source file
                                        srcfile = implementation.getAttribute('file')
                                        hrefString = ''
                                        if len(srcfile) > 0:                        
                                            isURL = srcfile.startswith('http')
                                            if not isURL:
                                                sourceUri = mx.FilePath(implementation.getSourceUri())
                                                sourceUri = sourceUri.getParentPath()
                                                # Scan starring from based name. Keep track of each parent in leafPath
                                                # Stop when reaching 'libraries' directory
                                                leafPath = sourceUri.getBaseName()
                                                totalPath = leafPath
                                                while leafPath != 'libraries':
                                                    sourceUri = sourceUri.getParentPath()
                                                    leafPath = sourceUri.getBaseName()
                                                    totalPath = leafPath + '/' + totalPath 

                                                print("... Leaft URI:", totalPath)
                                                libraryName = "https://github.com/AcademySoftwareFoundation/MaterialX/tree/main"
                                                libraryName = libraryName + '/' + totalPath
                                                libraryName = libraryName + '/' + srcfile
                                                print("Source URI:", sourceUri.asString(), "Source File:", srcfile, "Library Name:", libraryName)
                                                hrefString = libraryName 
                                            else:
                                                hrefString = srcfile
                                        if len(hrefString) > 0:
                                            new_item["linkurl"] = hrefString

                                        new_child["children"].append(new_item)

                    node_entry["children"].append(new_child)
                break

    # Create json string from the library_dict

    # Sort all children by name
    def sort_children(children):
        children.sort(key=lambda x: x['name'])
        for child in children:
            if 'children' in child:
                sort_children(child['children'])
    
    sort_children(library_dict["children"])

    return library_dict                                        

def main():
    parser = argparse.ArgumentParser(description="Build MaterialX NodeDef Introspection JSON")
    parser.add_argument('-ng', '--insert_nodegroup', action='store_true', help="Insert nodegroup entries in the JSON output")
    args = parser.parse_args()

    print("MaterialX Version:", mx.__version__)
    insert_nodegroup = args.insert_nodegroup
    if insert_nodegroup:
        print("Inserting nodegroup entries in the JSON output.")
    else:
        print("Not inserting nodegroup entries in the JSON output.")

    library_dict = build_nodedef_info(insert_nodegroup)  
    if library_dict:
        if insert_nodegroup:
            output_file = "nodedef_introspection.json"
        else:
            output_file = "nodedef_introspection_no_nodegroup.json"
        with open(output_file, 'w') as f:
            json.dump(library_dict, f, indent=2)
        print(f"NodeDef introspection JSON written to {output_file}")

if __name__ == "__main__":
    main()
