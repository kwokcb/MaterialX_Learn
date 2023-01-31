'''
    Test example to add and remove nodes of a given category and type.
'''
import sys, os, argparse
import MaterialX as mx

def createNodeMethod1(doc):
    # Creating Nodes: Method 1
    # ------------------------
    # Method 1 : Create a node using category and type.
    # - This method can be error prone as if the type is not specified then a string type is assumed.
    # - An empty name implies a new unique name will be generated within scope the document. 
    category = 'standard_surface'
    name = ''
    newNode = doc.addNode(category, name)
    if newNode:
        print('Created erroneous node: (%s), path(%s), type(%s) ' % (newNode.getName(), newNode.getNamePath(), newNode.getType()))
        doc.removeNode(newNode.getName())
    type = 'surfaceshader'
    newNode = doc.addNode(category, name, type)
    if newNode:
        print('Created correct node: (%s), path(%s), type(%s) ' % (newNode.getName(), newNode.getNamePath(), newNode.getType()))

    # Method 1a: Supply a name
    name = doc.createValidChildName(category)
    newNode = doc.addNode(category, name, type)
    if newNode:
        print('Created node with explicit name: (%s), path(%s):' % (newNode.getName(), newNode.getNamePath()))

    # Validate
    result = doc.validate()
    if not result[0]:
        print('Invalid document. Errors: "%s"' % result[1])        

def createNodeMethod2(doc):
    # Creating Nodes: Method 2
    # ------------------------
    # Method 2: Use node definition name
    # - This method requires knowledge of the actual nodedef name that easy to find.
    category = 'standard_surface'
    name = doc.createValidChildName(category)
    nodedef = doc.getNodeDef('ND_standard_surface_surfaceshader_100')
    if nodedef:
        newNode = doc.addNodeInstance(nodedef, name)
    if newNode:
        print('Created node via nodedef name: (%s), path(%s):' % (newNode.getName(), newNode.getNamePath()))

    # Method 2a: Search for appropriate nodedefs.
    category = 'image'
    nodedefs = doc.getMatchingNodeDefs(category)
    desiredType = 'color3'
    desiredNodedef = None
    print('Scan for nodedef with category %s, type %s' % (category, desiredType))
    for nd in nodedefs:
        if nd.getType() == desiredType:
            print('- Nodedef name: %s. Version: %s, Type: %s. Match: %d' % 
                (nd.getName(), nd.getVersionString(), nd.getType(), nd.getType() == desiredType))
            desiredNodedef = nd

    if desiredNodedef:
        name = doc.createValidChildName(category)
        newNode = doc.addNodeInstance(desiredNodedef, name)
        if newNode:
            print('- Created node by scanning nodedefs: (%s), type(%s):' % (newNode.getName(), newNode.getType()))
    else:
        print('- Failed to find desirned nodedef.')

def deleteAllNodes(doc):
    # Deleting Nodes

    # There is no way to remove all nodes at the same time, so we remove them
    # one at a timme
    print('Clear document contents:')
    for node in doc.getNodes():
        print('- Remove node: %s. Type: %s. Version: %s. Nodedef: %s' %
        (node.getName(), node.getType(), node.getVersionString(), node.getNodeDefString()))
        doc.removeNode(node.getName())    

def main():
    parser = argparse.ArgumentParser(description="Test loading libraries.")
    parser.add_argument("--libraryPath", help="Path for MaterialX libraries.")

    opts = parser.parse_args()

    # Required setup of document and libraries
    libraryPath = mx.FilePath('libraries')
    if opts.libraryPath:
        libraryPath = opts.libraryPath
    stdlib = mx.createDocument()
    searchPath = mx.FileSearchPath()
    libFiles = mx.loadLibraries([ libraryPath ], searchPath, stdlib)

    doc = mx.createDocument()
    doc.importLibrary(stdlib)

    if not libFiles:
        print('Failed to load library definitions. Stopping')
        sys.exit(-1)

    createNodeMethod1(doc)
    createNodeMethod2(doc)
    deleteAllNodes(doc)   

if __name__ == '__main__':
    main()
