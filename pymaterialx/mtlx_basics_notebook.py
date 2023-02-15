# %% [markdown]
# # 1.0 MaterialX Basics
# 
# In this first "book", we will cover topics:
# 1. Setting up dependencies and creating a MaterialX document.
# 2. Read and writing document and validation.
# 2. Creating, finding, connetion, and deleting nodes.
# 

# %% [markdown]
# ### 1.0.1 Importing MaterialX
# 
# Test example to check that MaterialX modules are available and will run.

# %%
import MaterialX as mx

# Print the version of MaterialX
doc = mx.createDocument()
print('Hello MaterialX (Version %s)' % doc.getVersionString())   

# %% [markdown]
# ### 1.0.2 Loading In Standard Libraries
# 
# To do any useful operations, the standard MaterialX libraries need to be loaded.
# 
# The "standard" libraries are in the 'libraries' folder in the installation location. The key interfaces used in the example are:
# 
# * `loadLibraries()` to create a library document. File search paths `FileSearchPath()` can be provided to search for the libraries under these paths. A list of all the files loaded is returned.
# * `importLibrary()` to import the libraries into the current document.

# %%
# Create a library document called stdlib and load libraries into that document 
libraryPath = mx.FilePath('libraries')
stdlib = mx.createDocument()
searchPath = mx.FileSearchPath()
libFiles = mx.loadLibraries([ libraryPath ], searchPath, stdlib)

# Create main document and import the library document
doc = mx.createDocument()
doc.importLibrary(stdlib)

# Print out the names of the library files loaded
if libFiles:
    #for libFile in libFiles:
    print('Loaded %d library files.' % len(libFiles))
else:
    print('No libraries loaded.')

# %% [markdown]
# ## 1.1 Saving and Loading Documents
# 
# Documents can be saved either to a string, stream or to a file location. A document can  be loaded from a string, stream or file.
# The native format supported is 'XML'.
# 
# Please refer to the learning material about "Documents" for more details about document management. 
# 
# ### 1.1.1 Reading and writing from file
# For reading and writing:
# * `writeToXmlFile()` can be used for writing to file
# * `readFromXmlFile()` can be used for reading from file
# 
# 

# %%
# Write a a file
filename = 'testfile.mtlx'
mx.writeToXmlFile(doc, filename)

testfileDoc = mx.createDocument()
mx.readFromXmlFile(testfileDoc, filename)
print('Test file read properly: ', testfileDoc.validate()[0])

# %% [markdown]
# ### 1.1.2 Document Validation 
# 
# When deal with document content it is a useful to check the contents are valid using the `validate()` function.
# A status code is returned along with a string which will contain error information if validation checks failed.

# %%
result = doc.validate()
if not result[0]:
    print('Invalid document. Errors: "%s"' % result[1])
else:
    print('Document has no errors.')

# %% [markdown]
# ### 1.1.3 Writing and reading from string
# 
# The functions `writeToXmlString()` and `readFromXmlString()` can be used to write and read from string. It can be useful to transfer the contents of a document to string for interop as well as for debugging purposes. 
# 
# In this example we write the current document to a file, read it back in and then get the contents as a string, and then
# create another document from that string. 
# 
# Note that documents loaded in from the standard libraries show up as XML `include` references in the main document.

# %%
# Write file to a document
documentContents = mx.writeToXmlString(doc)

# Read back into a new document and write to string again
doc1 = mx.createDocument()
mx.readFromXmlString(doc1, documentContents)
documentContents = mx.writeToXmlString(doc1)
print(documentContents)


# %% [markdown]
# ## 1.2 Node Creation
# 
# There are a few options for creating a node:
# 1. By category and type.
# 2. By node definition name.
# 
# Please refer to the node [library documentation](https://kwokcb.github.io/MaterialX_Learn/documents/definitions/definitions_by_group.html) for available categories, types and definitions.
# 
# Every node created within the scope of a node graph or document must have a unique name. When no name is specified an 
# arbitrary unique name is assigned. It is often better to explicitly generate a name based on a desired name. This can be done using the `createValidChildName()` method which guarantees a unique name is generated.
# 
# The the following examples, `getName()`, `getNamePath()`, and `getType()` are used to get the name, the path and the type of the node in order to print output results.
# 
# In this example a [standard_surface](https://kwokcb.github.io/MaterialX_Learn/documents/definitions/standard_surface.html) node will be created.

# %% [markdown]
# ### 1.2.1 addNodeInstance() : Recommended Approach
# 
# We will first look what is considered to be the most "robust" as it does not require you to know the name of the node definition nor does it not allow creation of invalid nodes. 
# 
# Note that this is the basic approach used by the **MaterialX Graph Editor**, except that a dictionary of definitions is created using the category as the main grouping (key) to look up lists of definitions by type. This is done once and then reused to support node creation. The node definitions reference library uses the same approach. 
# 
# 1. The first step is to find all the candidate definitions of a given category. 
# In the example below we look for `image` definitions using the function `getMatchingNodeDefs()`. 
# 2. It is possible to have multiple results returned so the next step is to filter based on the desired type. In this case we are looking for `image` nodes which return `color3` output.
# 3. Finally, after the desired definition is found, an instance of that definition can be created using `addNodeInstance()`.

# %%
# 1. Search for appropriate nodedefs.
category = 'image'
nodedefs = doc.getMatchingNodeDefs(category)
desiredType = 'color3'
desiredNodedef = None
print('1. Scan for nodedef with category %s, type %s' % (category, desiredType))

# 2. Filter by the desired type
for nodedef in nodedefs:
    if nodedef.getType() == desiredType:
        print('2. Found matching definition: %s. Version: %s, Type: %s' % 
            (nodedef.getName(), nodedef.getVersionString(), nodedef.getType()))
        desiredNodedef = nodedef
        break

imageNodePath = ""

# 3. Create a node using the node definition found.
if desiredNodedef:
    name = doc.createValidChildName(category)
    newNode = doc.addNodeInstance(desiredNodedef, name)
    if newNode:
        imageNodePath = newNode.getNamePath()
        print('3. Created node by scanning nodedefs: name(%s), type(%s):' % (newNode.getName(), newNode.getType()))
else:
    print('Failed to find desired nodedef.')

# %% [markdown]
# **Explicit node definition name** 
# 
# A variation on this to find a definition using an explicit node definition name. The exact name of the definition is required to find the node definition using the `getNodeDef()` function. 

# %%
shaderNode = None
shadername = doc.createValidChildName(category)

# Find the definition with the given name.
nodedef = doc.getNodeDef('ND_standard_surface_surfaceshader_100')

# Create an instance of the definition found.
if nodedef:
    shaderNode = doc.addNodeInstance(nodedef, shadername)    
if shaderNode:
    shaderName = shaderNode.getName()
    print('Created node via nodedef name: name(%s), path(%s):' % (shaderName, shaderNode.getNamePath()))



# %% [markdown]
# ### 1.2.2 addNode() : Alternative Approach

# %% [markdown]
# #### 1.2.2.1 Explicit catagory and type string 
# 
# The most manual way to create a node is to create a node using category string and type string.
# - `addNode()` is the function used.
# - This method can be error prone if the `type` is not specified. A `string` type is then asssumed.
# - An empty name argument results in a new unique name generated for the node. 
# 
# 
# In this case standard_surface type is surfaceshader but instead the type is incorrectly set to color3.

# %%

category = 'standard_surface'
name = ''
newNode = doc.addNode(category, name)
if newNode:
    print('Created node with incorrect type: name(%s), path(%s), type(%s) ' % (newNode.getName(), newNode.getNamePath(), newNode.getType()))
    doc.removeNode(newNode.getName())


# %% [markdown]
# #### 1.2.2.2 Explicit category, type and name string
# 
# Specifying an explicit type is a bit better if the type to create is known. However it is still possible to set the incorrect type.

# %%

type = 'surfaceshader'
# the type is explicity specified 
newNode = doc.addNode(category, name, type)
if newNode:
    print('Created correct node: name(%s), path(%s), type(%s) ' % (newNode.getName(), newNode.getNamePath(), newNode.getType()))


# %% [markdown]
# #### 1.2.2.3 Explicit catagory and type with generated name 
# 
# As mentioned it is often better to generate a unique name using `createValidChildName()`.

# %%

name = doc.createValidChildName(category)
newNode = doc.addNode(category, name, type)
if newNode:
    print('Created node with explicit name: (%s), path(%s):' % (newNode.getName(), newNode.getNamePath()))


# %% [markdown]
# ## 1.3 Finding Nodes
# 
# ### 1.3.1 Individual Nodes
# 
# Individual nodes can be found in a variety of different ways:
# * By path (`getDescendant`): This is the best way to find a child is to use a path that explicitly points to where in the document hierarchy the node resides. Element paths are relative.
# * By child name (`getChild`): Is suitable for finding the direct child of a document or node graph.
# * By type(`getChildofType`). The singular version can be used but the other methods are prefered.
# 
# Please see documentation about paths found [here](https://kwokcb.github.io/MaterialX_Learn/documents/nodes_and_nodegraphs.html)

# %%
# Method 1: Get descendent using name.
shadernode = doc.getChild(shadername)
if shadernode:
    print('- Found node by name:', shadername)
shadernode = doc.getDescendant(shadername)
if shadernode:
    print('- Found node by path:', shadername)
shadernode = doc.getChildOfType(mx.Node, shadername)
if shadernode:
    print('- Found node by type:', shadername)


# %% [markdown]
# ### 1.3.2 List of Nodes
# 
# To get a list of all children of a document or node graph:
# * `getNodes()` returns all child nodes. This is the prefered method.
# * `getChildrenofType()` returns a list of all children of a given type
# * `getChildren()` returns all children of any type

# %%
# Multiple element query
nodes = doc.getNodes()
if nodes:
    names = [ node.getName() for node in nodes ]
    print("- Found child nodes by getNodes():", names)

# The type of a node is Node
nodes = doc.getChildrenOfType(mx.Node)
if nodes:
    names = [ node.getName() for node in nodes ]
    print("- Found child nodes by type:", names)

nodes = doc.getChildren()
if nodes:
    # Just print out a few nodes as all children including definitions are in this list.
    names = [ nodes[i].getName() for i in range(0,10) ]
    print("- Found child nodes:", names)


# %% [markdown]
# # 2 Making Connections
# 
# ## 2.1 Node Connections
# Connections are formed from a downstream `input` to an upstream `output`. For this a wrapper function is
# added to hide some of the syntactic peculiarities. It will be added to as the types of connections
# being considered is added.
# 
# One cumbersome thing is that a node instance when created as no inputs instantiated. So a check
# must be made to see if it exists and if not added it. Then if input and outputs types match 
# then the input can make the connection.
# 
# Additionally it is considered "invalid" to have both a `value` and a connection on an input, so
# if a value has been set it must be removed.
# 
# Something like the `connect()` method would be a useful utility to have in the core
# API.

# %%
def connect(inputNode, inputName, outputNode, outputName):
    if not inputNode or not outputNode:
        return None

    # Add an input to the downstream node if it does not exist
    inputPort = inputNode.addInputFromNodeDef(inputName)

    # Check for the type.
    outputType = outputNode.getType()  
    
    # If there is more than one output then we need to find the output type 
    # from the output with the name we are interested in.
    outputPortFound = None
    outputPorts = outputNode.getOutputs()
    if outputPorts:
        # Look for an output with a given name, or the first if not found                    
        if not outputName:
            outputPortFound = outputPorts[0]
        else:
            outputPortFound = outputNode.getOutput(outputName)

    # If the output port is not found on the node instance then
    # look for it the corresponding definition
    if not outputPortFound:
        outputNodedef = outputNode.getNodeDef()
        if outputNodedef:
            outputPorts = outputNodedef.getOutputs()
            
            if outputPorts:
                # Look for an output with a given name, or the first if not found                    
                if not outputName:
                    outputPortFound = outputPorts[0]
                else:
                    outputPortFound = outputNodedef.getOutput(outputName)

    if outputPortFound:
        outputType = outputPortFound.getType()
    else:
        print('No output port found matching: ', outputName)        

    if inputPort.getType() != outputType:
        print('Input type (%s) and output type (%s) do not match: ' % (inputPort.getType(), outputType))
        return None

    if inputPort:
        # Remove any value, and set a "connection" but setting the node name
        inputPort.removeAttribute('value')
        inputPort.setNodeName(outputNode.getName())
        if outputName:
            inputPort.setOutput(outputName)
    return inputPort

# Connect image node to shader node previously created
imageNode = doc.getDescendant(imageNodePath)
shaderNode = doc.getChild(shadername)
if imageNode and shaderNode:
    inputConnnected = connect(shaderNode, "base_color", imageNode, "")
    if inputConnnected:
        print(inputConnnected)


# %% [markdown]
# ## 2.2 Node Deletion
# 
# There is one option for removing nodes, and that is by name. It is not recommended to use low level
# APIs such as `removeChild()` as they can remove non-nodes.
# 
# In this example `getNodes()` is used to get the nodes and delete them one at a time.

# %%
# Deleting Nodes

print('Current document contents:')
mx.writeToXmlFile(doc, filename)
contents = mx.writeToXmlString(doc)
print(contents)

# There is no way to remove all nodes at the same time, so we remove them
# one at a timme
print('Clear document contents:')
for node in doc.getNodes():
    print('- Remove node: %s. Type: %s. Version: %s. Nodedef: %s' %
     (node.getName(), node.getType(), node.getVersionString(), node.getNodeDefString()))
    doc.removeNode(node.getName())    


