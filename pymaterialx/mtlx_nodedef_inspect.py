import MaterialX as mx
import os
import json
import argparse

def extractSourceURL(implementation):
    srcfile = implementation.getAttribute('file')
    srcURL = implementation.getSourceUri()
    hrefString = ''
    if len(srcfile) > 0:    
        isURL = srcfile.startswith('http')
        if not isURL:
            sourceUri = mx.FilePath(implementation.getSourceUri())
            sourceUri = sourceUri.getParentPath()
            # Look for path starting from 'libraries' downwards 
            leafPath = sourceUri.getBaseName()
            totalPath = leafPath
            while leafPath != 'libraries':
                sourceUri = sourceUri.getParentPath()
                leafPath = sourceUri.getBaseName()
                totalPath = leafPath + '/' + totalPath 

            libraryName = "https://github.com/AcademySoftwareFoundation/MaterialX/tree/main"
            libraryName = "https://raw.githubusercontent.com/AcademySoftwareFoundation/MaterialX/refs/heads/main/"
            libraryName = libraryName + '/' + totalPath
            libraryName = libraryName + '/' + srcfile
            hrefString = libraryName 
            #print(f"{implementation.getName()} impl source file: {srcfile}. Source URI: {srcURL}")                    
        else:
            hrefString = srcfile

    return hrefString 

def extractSource(implementation):
    src = implementation.getAttribute('sourcecode')
    return src

def compute_image_names(nodedef):
    outputList = nodedef.getActiveOutputs() #if opts.showInherited  else nd.getOutputs()
    image_list = []
    #multiimage = len(outputList) > 1
    for out in outputList:
        outName = out.getName()

        imageName = 'material_' + nodedef.getName().removeprefix('ND_') + '_' + outName + '_genglsl.png'
        find_imageName = '../resources/mtlx/nodedef_materials/' + imageName                
        if not os.path.exists(find_imageName):
            #print('-- Missing image: ', imageName)
            imageName = 'images/no_image.png'
        else:
            imageName = 'https://kwokcb.github.io/MaterialX_Learn/resources/mtlx/nodedef_materials/' + imageName
            image_list.append( { "output": outName, "imageurl" : imageName })
            
    #if image_list:
    #    print('---- Found images for nodedef:', nodedef.getName(), [img["imageurl"] for img in image_list])       
    return image_list

def add_nodegraph_node(parent, implementation):
    if "children" not in parent:
        parent["children"] = []
    icon = "bi-diagram-3"
    impl_string = implementation.getName()

    nodegraph = {
        "target" : "all", 
        "type": "nodegraph",
        #"output_type": implementation.getType(),
        "icon": icon, 
        "name": impl_string
    }
    parent["children"].append(nodegraph)

def add_implementation_node(parent, nodedef, implementation, targetNames):
    '''
    Add implementation node to the parent node with all targets.
    If a child with the same name already exists, append the target to the "target" string.
    If no child exists, create a new child node with the implementation name and target.
    @param parent: The parent node to which the implementation node will be added.
    @param nodedef: The definitions for the implementation.
    @param implementation: The implementation to be added.
    @param targetNames: List of target names to be associated with the implementation.
    '''
    if not implementation or not targetNames:
        #print(f'---- No implementation for target: {target} in nodedef: {nodedef.getName()}')
        if "children" not in parent:
            parent["children"] = []
        new_node = {
            "icon": "bi-exclamation-diamond",
            "name": "Undefined",
            "target": 'all',
            "type": "implementation",
        }
        parent["children"].append(new_node)    
        return

    for target in targetNames:
        implementation = nodedef.getImplementation(target)
        if implementation:
            implementation_name = implementation.getName()
            # Add "children" array to new_child
            if "children" not in parent:
                parent["children"] = []

            # Check if a child with the same name and type already exists
            existing_child = next(
                (c for c in parent["children"]
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
                new_node = {
                    "icon": "bi-file-code",
                    "name": implementation_name,
                    "target": target,
                    "type": "implementation",
                }

                # Get source file if any
                hrefString = extractSourceURL(implementation)
                if len(hrefString) > 0:
                    new_node["linkurl"] = hrefString
                else:
                    code = extractSource(implementation)
                    if len(code) > 0:
                        new_node["doc"] = code

                parent["children"].append(new_node)    
        else:
            #print(f'---- No implementation for target: {target} in nodedef: {nodedef.getName()}')
            if "children" not in parent:
                parent["children"] = []
            new_node = {
                "icon": "bi-exclamation-diamond",
                "name": "Undefined: " + target,
                "target": target,
                "type": "implementation",
            }
            parent["children"].append(new_node)    


def add_geompropdefs(doc, parent):
    geompropdefs = doc.getGeomPropDefs()
    if geompropdefs:
        
        geompropdef_group = {
            "icon": "bi-journals",
            "name": "geompropdefs",
            "type": "geompropdef_group",
            "children": []
        }
        for geompropdef in geompropdefs:
            geompropdef_entry = {
                "icon": "bi-circle-square",
                "name": geompropdef.getName(),
                "type": geompropdef.getType(),
                "geomprop": geompropdef.getGeomProp(),
                "space": geompropdef.getSpace(),
                "index": geompropdef.getIndex()
            }
            geompropdef_group["children"].append(geompropdef_entry)
        parent["children"].append(geompropdef_group)
        #print("GeomPropDefs:", [geompropdef.getName() for geompropdef in geompropdefs])

def add_typedefs(doc, parent):
    typedefs = doc.getTypeDefs()
    if typedefs:
        typedef_group = {
            "icon": "bi-journals",            
            "name": "typedefs",
            "type": "typedef_group",
            "children": []
        }
        for typedef in typedefs:
            typedef_entry = {
                "icon": "bi-braces",
                "name": typedef.getName(),
                "type": "typedef"
            }
            typedef_group["children"].append(typedef_entry)
        
        parent["children"].append(typedef_group)
        #print("TypeDefs:", [typedef.getName() for typedef in typedefs])

def add_library(doc, library_version):
    library_name = library_version + " Libraries"
    library_dict = {"icon" : "bi-database","name": library_name, "version": library_version, "children": []}
    currTargets = []
    targetNames = []
    for target in doc.getTargetDefs():
        currTargets.append( { 'name' : target.getName(), 'type' : 'targetdef' } )
        target_name = target.getName()
        targetNames.append(target_name)
                
    # Append "targets" to the library_dict
    targetNameString = ', '.join(targetNames)
    library_dict['targets']  = targetNameString

    return library_dict, targetNames

def get_library_names(libFiles, path_list):
    library_names = []
    if libFiles:
        for libFile in libFiles:
            # Find the path that matches the most characters in the libFile
            searchPath = ''
            for path in path_list:
                norm_path = os.path.normpath(path)
                # Find the longest matching path
                if libFile.startswith(norm_path):
                    if len(norm_path) > len(searchPath):
                        searchPath = norm_path

            # remove search path from the file name
            #print('searchpath:', searchPath, ' libFile:', libFile)
            libFile = os.path.relpath(libFile, searchPath)
            # The first child path is the library name
            library_name = libFile.split(os.sep)[0]
            #print('Library name:', library_name)
            if library_name not in library_names:
                library_names.append(library_name)
    else:
        print('No library files loaded.')
    return library_names      

def load_libraries():
    return

def build_nodedef_info(insert_nodegroup=True, input_path='', libraryFolders=['libraries'], addLinks=True):

    path_list = []
    if not input_path:
        searchPath = mx.getDefaultDataSearchPath().asString() 
        searchPath = os.path.normpath(searchPath)
        # Append 'libraries' to the search path
        searchPath = mx.FileSearchPath(os.path.join(searchPath, 'libraries'))
        path_list.append(searchPath.asString())

        libraryPath = mx.getDefaultDataSearchPath()
        libraryFolders = mx.getDefaultDataLibraryFolders()
        version = mx.getVersionString()
    else:
        searchPath = os.path.normpath(input_path)
        path_list.append(searchPath)
        for lib in libraryFolders:
            path_list.append(os.path.join(searchPath, lib))
        
        libraryPath = searchPath
        base_folder_name = os.path.basename(os.path.normpath(input_path))
        version = base_folder_name
        # Remove all non-numbers. Leave '.'
        version = ''.join(c for c in version if c.isdigit() or c in ['.'])
        if not version:
            version = base_folder_name

    print(f'Search path {path_list}. libraryPath: {libraryPath}. libraryFolders: {libraryFolders}. version: {version}')

    stdlib = mx.createDocument()
    libFiles = mx.loadLibraries(libraryFolders, libraryPath, stdlib)
    #for l in libFiles:
    #    print("Loaded library file:", l)

    # Create main document and import the library document
    doc = mx.createDocument()
    doc.importLibrary(stdlib)

    # Extract names of the library files based on files loaded
    library_names = get_library_names(libFiles, path_list)
    print("Loaded libraries:", library_names)

    library_dict, targetNames = add_library(doc, version)
    print("Target List:", targetNames)

    # Emit support definitions
    add_typedefs(doc, library_dict)
    add_geompropdefs(doc, library_dict)

    # Build a mapping from library name to its node entry in the children list
    library_entries = {}
    for library_name in library_names:
        entry = {"icon": "bi-journals", "name": library_name, "type": "library", "children": []}
        if library_name == 'targets':
            # Append target names as children of the library entry
            for target in targetNames:
                entry["children"].append({"icon": "bi-bullseye", "name": target, "type": "target"})
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
                        nodegroup_entry["icon"] = "bi-collection"
                        lib_entry["children"].append(nodegroup_entry)
                    parent_container = nodegroup_entry
                else:
                    # Use library as parent container (either no nodegroup or insert_nodegroup is False)
                    parent_container = lib_entry

                # Find or create node entry under the parent container
                url = ''
                if addLinks:
                    url = "https://kwokcb.github.io/MaterialX_Learn/documents/definitions/" + node_name + ".html"
                    #print("Add URL ", url)
                node_entry = next((item for item in parent_container["children"] if item["name"] == node_name and item["type"] == "node"), None)
                if node_entry is None:
                    node_entry = {"icon": "bi-key", "name": node_name, "type": "node", "output_type": nodedef.getType(), "linkurl" : url}
                    node_entry["children"] = []
                    parent_container["children"].append(node_entry)

                # Add nodedef as a child if not already present
                if not any(child["name"] == nodedef_name for child in node_entry["children"]):
                    new_child = {"icon" : "bi-usb-plug", "name": nodedef_name, "type": "nodedef"}
                    image_list = []
                    if addLinks:
                        image_list = compute_image_names(nodedef)
                    for image in image_list:
                        #print('- Adding image for nodedef:', nodedef_name, image["imageurl"])
                        new_child["imageurl"] = image["imageurl"]
                        break # Fix to add all

                    version = nodedef.getVersionString()
                    if version:
                        new_child["version"] = version
                    
                    # Add nodegroup as metadata when not inserting nodegroup level
                    if nodegroup and not insert_nodegroup:
                        new_child["nodegroup"] = nodegroup
                        
                    docstring = nodedef.getAttribute('doc')
                    if docstring:
                        new_child["doc"] = docstring

                    # Add implementation children if they exist
                    implementation = nodedef.getImplementation()
                    if implementation:

                        # Add nodegraph
                        if implementation.isA(mx.NodeGraph):
                            add_nodegraph_node(new_child, implementation)

                        # Add non-nodegraph implementation
                        else:
                            add_implementation_node(new_child, nodedef, implementation, targetNames)
                    else:
                        print(f'-- No implementation for nodedef: {nodedef_name}')
                        add_implementation_node(new_child, nodedef, None, None)

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
    parser.add_argument('-ip', '--input_path', type=str, default='', help="Input path for MaterialX libraries. If not specified will use default search path.")
    parser.add_argument('-ng', '--insert_nodegroup', action='store_true', help="Insert nodegroup entries in the JSON output")
    parser.add_argument('-op', '--output_path', type=str, default='.', help="Output path for the JSON file")
    parser.add_argument('-lf', '--library_folder', type=str, action='append', help="Library folder to load from the input path")
    parser.add_argument('-al', '--add_links', action='store_true', help="Add links to online documentation in the JSON output")
    args = parser.parse_args()

    print("Using MaterialX Version:", mx.__version__)
    insert_nodegroup = args.insert_nodegroup
    if insert_nodegroup:
        print("Inserting nodegroup entries in the JSON output.")
    else:
        print("Not inserting nodegroup entries in the JSON output.")

    input_path = args.input_path
    # Convert opts.library_folder from set to list
    library_list = []
    if args.library_folder:
        for folder in args.library_folder:
            print("Adding library folder to load:", folder)
            library_list.append(folder)
    print("Library folders to load:", library_list)

    addLinks = False
    if args.add_links:
        addLinks = True
    library_dict = build_nodedef_info(insert_nodegroup, input_path, library_list, addLinks=addLinks)
    if library_dict:
        version = library_dict.get("version")
        version = mx.createValidName(version)
        if insert_nodegroup:
            output_file = f"nodedef_introspection_{version}.json"
        else:
            output_file = f"nodedef_introspection_{version}_no_nodegroup.json"
        if args.output_path:
            # Create output directory if it doesn't exist
            os.makedirs(args.output_path, exist_ok=True)
            output_file = os.path.join(args.output_path, output_file)
        with open(output_file, 'w') as f:
            json.dump(library_dict, f, indent=2)
        print(f"Definition introspection JSON written to {output_file}")

if __name__ == "__main__":
    main()
