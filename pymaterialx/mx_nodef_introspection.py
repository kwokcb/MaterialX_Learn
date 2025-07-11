import MaterialX as mx
import os
import json

def build_nodedef_info():

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
    library_dict["targets"] = { "children" : currTargets }

    print("Target List:", currTargets)

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
                lib_entry = library_entries[library_name]
                # Find or create node entry
                node_entry = next((item for item in lib_entry["children"] if item["name"] == node_name), None)
                if node_entry is None:
                    node_entry = {"name": node_name, "type": "node", "children": []}
                    lib_entry["children"].append(node_entry)
                # Add nodedef as a child if not already present
                if not any(child["name"] == nodedef_name for child in node_entry["children"]):
                    new_child = {"name": nodedef_name, "type": "nodedef"}
                    for target in targetNames:
                        implementation = nodedef.getImplementation(target)
                        if implementation:
                            # Add "children" array to new_child
                            if "children" not in new_child:
                                new_child["children"] = []
                            # Append children to node_entry if implementation exists
                            new_child["children"].append({"target" : target, "type": "implementation", "name": implementation.getName()})                        

                    node_entry["children"].append(new_child)
                    #node_entry["children"].append({"name": nodedef_name})
                    #node_entry["children"].append({"type": "nodedef", "name": nodedef_name})                
                break

    # Create json string from the library_dict

    json_string = json.dumps(library_dict, indent=4)
    # Write the json string to a file    
    with open('materialX_libraries_dictionary.json', 'w') as f:
        f.write(json_string)

def main():
    print("MaterialX Version:", mx.__version__)

    build_nodedef_info()


if __name__ == "__main__":
    main()
