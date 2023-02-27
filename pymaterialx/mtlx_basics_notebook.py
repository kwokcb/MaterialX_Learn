# %% [markdown]
# # MaterialX Basics
# 
# ## Summary
# 
# This notebook covers the following:
# 
# 1. Essential Setup
#    * Loading in MaterialX
#    * Creating documents
#    * Loading in "standard" library definitions
# 3. Creating nodes and editing input values
# 5. Saving out a document and examining it's contents

# %% [markdown]
# ## 1. Setting up MaterialX
# 
# ### Importing MaterialX
# 
# When using MaterialX, the very first thing that must be done is to import the package.
# After loading in the package, the API version available can be found in the `__version__`
# module information. This is equivalent to calling the `getVersionString()` utility.

# %%
import MaterialX as mx
    
# Print out MaterialX API version
print ('MaterialX API version %s' % mx.__version__)
print ('MaterialX API version %s' % mx.getVersionString())

# %% [markdown]
# ### Creating a Document
# 
# In order to perform any action using MaterialX, a `Document` must be created using the `createDocument()`
# interface. In this example a new document is created and then the version of the document 
# is checked using `getVersionString()`.
# 
# This document will be the "working" document used for the rest of this book.
# 
# > As noted in the `Documents` learning material this is the version of the document and not the package version.

# %%
import MaterialX as mx

# Print the version of MaterialX
doc = mx.createDocument()
print('Hello MaterialX (Version %s)' % doc.getVersionString())   


# %% [markdown]
#  ### Loading In Standard Libraries
# 
# To do any useful operations, the standard MaterialX libraries need to be loaded.
# There libraries are found in in the 'libraries' folder in the installation location.
# 
# The key interface to load in library definitions is called: `loadLibraries()` where:
#   * An input `FilePath` list specifies the library folders to load. 
#   * An input `FileSearchPath()` specifies where to search for libraries. 
#   * The names of files loaded is returned.

# %%
# Load library files under the `libraries` folder into a new "library" document
# called "stdlib". We assume that no additional search paths are required for this example.
stdlib = mx.createDocument()
libraryPath = mx.FilePath('libraries')
searchPath = mx.FileSearchPath()

# The list of library files loaded which which is returned is checked.
libFiles = mx.loadLibraries([ libraryPath ], searchPath, stdlib)
if libFiles:
    print('Loaded %d library files.' % len(libFiles))
else:
    print('No library files loaded.')

# %% [markdown]
# A document can use a definition library by "importing" them in using the `importLibrary()` interface.
# 
# To check for proper loading a query to get the list of node definitions is performed
# using the `getNodeDefs()` interface.

# %%

# Check node definition count before loading
nodeDefinitionCount = len(doc.getNodeDefs())
print('Definition count before import: %d' % nodeDefinitionCount) 

# Import the library document into the document
doc.importLibrary(stdlib)

# Check node definition count
nodeDefinitionCount = len(doc.getNodeDefs())
print('Definition counst after import : %d ' % nodeDefinitionCount) 

# %% [markdown]
#  ## 2. Reading and Writing Documents
# 
#  Documents can be saved or loaded to/from a string, stream or to a file location.
#  The native format supported is 'XML'.
# 
#  Please refer to the learning material about "Documents" for details about document management.
# 
#  ### Reading and writing from file
#  For reading and writing:
#  * `writeToXmlFile()` can be used for writing to a file
#  * `readFromXmlFile()` can be used for reading from a file
# 
# 

# %%
# Write out sample file
filename = 'testfile.mtlx'
mx.writeToXmlFile(doc, filename)

# Read in a sample file
testfileDoc = mx.createDocument()
mx.readFromXmlFile(testfileDoc, filename)

# %% [markdown]
#  ### Document Validation
# 
#  When dealing with document content it is a useful to check if the contents are valid using the `validate()` function.
#  A status code is returned along with a string containing error information if the validation checks failed.

# %%
status, errors = doc.validate()
if not status:
    print('Invalid document. Errors: "%s"' %errors)
else:
    print('Document has no errors.')


# %% [markdown]
#  ### 1.1.3 Writing and reading from string
# 
#  The functions `writeToXmlString()` and `readFromXmlString()` can be used to write and read from a string. It can be useful to transfer the contents of a document via a string for interoperability as well as for debugging purposes.
# 
#  In this example we write the document (`doc`) to a string, read it back in to a new document (`doc1`) and print it's contents as a string.
#  
#  Note that documents loaded in from the standard libraries show up as XML `include` references in the main document.

# %%
# Write file to a document
documentContents = mx.writeToXmlString(doc)

# Read back into a new document and write to string again
doc1 = mx.createDocument()
mx.readFromXmlString(doc1, documentContents)
documentContents = mx.writeToXmlString(doc1)
print(documentContents)

# %% [markdown]
# To remove these desired references to the library a "filter" can be specified when writing. 
# 
# It is recommended that this **always be performed** to avoid adding explicit dependencies on definitions and/or file locations.
# 
# To add the filter create an options structure called (`XmlWriteOptions`). 
# To this a "predicate" function can be added. This predicate is called for every element in the document,
# and returns whether to write out a given element. 
# 
# A custom predicate is used to skip writing out "library elements", which can be found by testing the existence of 
# a "source URI" indicating that it was "imported".  
# 
# > Refer to Documents learning guide for more details.

# %%
# Declare write predicate for write filter test.
# Elements which were imported via importLibrary() will have a "source URI" which is not empty.
def skipLibraryElement(elem):
    return not elem.hasSourceUri()

# Declare write options and set the predicate.
writeOptions = mx.XmlWriteOptions()
writeOptions.writeXIncludeEnable = False
writeOptions.elementPredicate = skipLibraryElement

# Perform write
documentContents = mx.writeToXmlString(doc, writeOptions)

# Read back into a new document and write to string again.
# Due to the predicate usage the document no longer outputs library definitions.
doc1 = mx.createDocument()
mx.readFromXmlString(doc1, documentContents)
documentContents = mx.writeToXmlString(doc1)
print(documentContents)

# %% [markdown]
#  ## 3 Node Creation
# 
# A node must always be created under a "parent" graph. This can be at the top level under the document or within a node graph.
# Any node created must have a unique name among all the children of the parent.
# 
# The `createValidChildName()` can be used to guarantee that a unique "child" name is generated.
# 
# > In the examples given the utility `prettyPrint()` will be used to view the contents of
# an element (in XML format).

# %% [markdown]
#  ### Creating Nodes Using `addNodeInstance()`
# 
#  The recommended logic to create a node is to 
# 
#  1. Determine the `category` of node to create. 
#  2. Find all possible node definitions for the `category` using the interface `getMatchingNodeDefs()`.
#  3. If multiple variants exist, choose one based criteria such as `type` and/or `version`
#  4. Use the appropriate definition to create the node using the `addNodeInstance()` interface.
# 
# This approach only requires the user to know the category and type or version. Node definition names do not need to be known, and
# it is not possible to create invalid data.
# 
# Steps 2 and 3, can be done for an entire library to create a dictionary of definitions which can be reused. Both the "Library" reference found here and the MaterialX Node Editor builds such dictionaries. The `mxdoc.py` sample utility has sample code of building such a dictionary which is grouped by `category`. 

# %% [markdown]
# 
#   In this example all the variants of [image](https://kwokcb.github.io/MaterialX_Learn/documents/definitions/image.html) are queried with the `color3` variant being chosen to be created. 
#   
#   Steps 2 and 3 are encapsulated into a reusable utility called `getNodeDefinition()`  

# %%
def getNodeDefinition(category, desiredType):
    
    # 1. Search for appropriate 'image' catetory node definitions (nodedefs) 
    nodedefs = doc.getMatchingNodeDefs(category)

    # 2. Filter by the desired type
    foundNodeDef = None
    for nodedef in nodedefs:
        if nodedef.getType() == desiredType:
            foundNodeDef = nodedef
            break

    return foundNodeDef

searchCategory = 'image'
searchType = 'color3'
print('1. Scan for nodedef with category %s, type %s' % (searchCategory, searchType))
desiredNodedef = getNodeDefinition(searchCategory, searchType)

if desiredNodedef:
    print('2. Found matching definition:\n %s' % mx.prettyPrint(desiredNodedef)) 

    # 3. Create a node using the node definition found. Use `createValidChildName` to
    # avoid duplicate name clashes
    name = doc.createValidChildName(searchCategory)
    newNode = doc.addNodeInstance(desiredNodedef, name)
    if newNode:
        print('3. Created node: %s' % mx.prettyPrint(newNode))
else:
    print('Failed to find desired nodedef.')


# %% [markdown]
#  ### Minimal Logic
# 
#  When node definition names are known before-hand (as noted for the dictionary workflow), the minimal logic is to find the definition using the `getNodeDef()` interface, and then calling `addNodeInstance()`. 
# 
#  This will be the logic used here and in other tutorials assuming we know ahead of time what the names are.
#  
#  >  Please refer to the node [library documentation](https://kwokcb.github.io/MaterialX_Learn/documents/definitions/definitions_by_group.html) for available node definition names.
# 
#  In this example a [standard_surface](https://kwokcb.github.io/MaterialX_Learn/documents/definitions/standard_surface.html) node will be created.

# %%
shaderNode = None
shadername = doc.createValidChildName("test_shader")

# Find the definition with the given name.
nodedef = doc.getNodeDef('ND_standard_surface_surfaceshader')
#print(mx.prettyPrint(nodedef))

# Create an instance of the definition found.
if nodedef:
    shaderNode = doc.addNodeInstance(nodedef, shadername)    
if shaderNode:
    shaderName = shaderNode.getName()
    print('Created node via nodedef "%s"' % nodedef.getName())
    print(' - %s' % mx.prettyPrint(shaderNode))


# %% [markdown]
# **Performance Tip**
#  
# As the instance has the definition directly specified, this can result in faster node creation when a document is being read.

# %% [markdown]
# ## 4 Modifying Input Values
# 
# This example will show a simple change on one of the input parameters on the shader `test_shader` just created.
# 
# As mentioned in the specification and the `Node and NodeGraphs` learning material, a node instance
# will only create and store inputs if they have non-default values. Thus in this example
# there are no inputs to set on `test_shader`. 
# 
# To avoid having to worry whether an input exists or not, the most robust approach is to either pre-create all the inputs on a node instance using `addInputsFromNodeDef()` or individually using `addInputFromNodeDef()` 
# 

# %% [markdown]
# **Example 1** : Adding only the input of interest

# %%
# Color to set input to
color = mx.Color3(0.4, 0.3, 0.2)

# Add the input if it does not exist. Then modify it's value
baseColorInput = shaderNode.addInputFromNodeDef('base_color')
if baseColorInput:
    baseColorInput.setValue(color)
    print('1a. Add / modified input on:\n%s' % mx.prettyPrint(shaderNode))

    # Note that the input once found can be used for additional modifications
    color = mx.Color3(0.9, 0.8, 0.7)
    baseColorInput.setValue(color)
    print('1b. Modified input on:\n%s' % mx.prettyPrint(shaderNode))


# %% [markdown]
# > Note: The inputs can be removed from the instance to restore the default value. 

# %%
# Removing the input on the "instance" does not mean it has not value.
    # The value is the default value.
if baseColorInput and shaderNode:
    print('Before: Shader node instance has: %d explcit inputs' % len(shaderNode.getInputs()))    
    shaderNode.removeInput(baseColorInput.getName())
    print('After: Shader node instance has: %d explcit inputs' % len(shaderNode.getInputs()))
    print('   %s' % mx.prettyPrint(shaderNode))

# %% [markdown]
# **Example 2** : Adding all inputs based on the definition
# 
# Creating all of the  inputs removes the overhead of worrying if an input exists as well as not "hiding" inputs from users.
# However all inputs will be written to file, even if they have default values so file size can be relatively larger as shown in the sample output.

# %%
# Add all inputs to see all the default values
shadername2 = doc.createValidChildName("test_shader")
shaderNode2 = doc.addNodeInstance(nodedef, shadername2)   
shaderNode2.addInputsFromNodeDef()
print('2. Add all default input values on:\n%s' % mx.prettyPrint(shaderNode2))

# Clean up all inputs
for input in shaderNode2.getInputs():
    shaderNode2.removeInput(input.getName())

# %% [markdown]
# It is **not recommended** to simply set the input using the `setInputValue()` interface as this interface always creates an input even if it does not exist on the definition resulting in an invalid node. 
# 
# An additional step of pre-checking to see if the input is on the definition can be done manually, but this
# is automatically done by `addInputFromNodeDef()` so this is an unnecessary additional manual step.
# 

# %%
color = mx.Color3(0.1, 0.2, 0.3)

# Set an input value. The input does not exist but is still allowed to be set
shaderNode.setInputValue('unknown_input', color)
getcolor = shaderNode.getInputValue('unknown_input')
print('Error: Added an invalid input on:\n%s' % mx.prettyPrint(shaderNode))
shaderNode.removeInput('unknown_input')

# Check the defintion first before added.
nodedef = shaderNode.getNodeDef()
if nodedef.getInput('base_color'):
    shaderNode.setInputValue('base_color', color)
    getcolor = shaderNode.getInputValue('base_color')
    print('Add and modified a valid input on:\n%s' % mx.prettyPrint(shaderNode))
    shaderNode.removeInput('base_color')


# %% [markdown]
#  ## 5 Finding Nodes
# 
# To check on the state of a document while editing, it is useful to query information back without writing the entire document out
# to file or string. This section includes some common interfaces for finding nodes in a document.
# 
#  ### Individual Nodes
# 
#  Individual nodes can be found in a variety of ways:
#  * By path ( `getDescendant` ): The most "robust" way to find a node is to use a `path` that explicitly points to where in the document hierarchy the node resides. All paths are relative to the element where `getDescendent` is being called from.
#  * By child name ( `getChild` ): Is suitable for finding the direct child of a document or node graph but does search through hierarchies.
#  
# 
#  Please see documentation about paths found [here](https://kwokcb.github.io/MaterialX_Learn/documents/nodes_and_nodegraphs.html)

# %%
# Method 1: Get descendent using name.
shadernode = doc.getChild(shadername)
if shadernode:
    print('- Found node by name:', shadername)
shadernode = doc.getDescendant(shadername)
if shadernode:
    print('- Found node by path:', shadername)


# %% [markdown]
#  ### Finding List of Nodes
# 
#  To get a list of all children of a document or node graph:
#  * `getNodes()` returns all child nodes. 
#  * `getChildrenOfType()` returns a list of all children of a given type
#  * `getChildren()` returns all children of any type. 

# %%
# Multiple element query
print('Find using getNodes()')
nodes = doc.getNodes()
if nodes:
    names = [ node.getName() for node in nodes ]
    print("-", names)

# The type of a node is Node
print('Find using getChildrenOfType()')
nodes = doc.getChildrenOfType(mx.Node)
if nodes:
    names = [ node.getName() for node in nodes ]
    print("-", names)

print('Find using getChildren()')
elements = doc.getChildren()
names = []
for element in elements:
    if element.isA(mx.Node):
        names.append(element.getName())
print("-", names)



# %% [markdown]
#  ### Addendum : Node Creation Issues
# 
# This addendum includes an alternative interface which should be avoided for editing workflows as it is possible to create invalid data. 
# Handing of `LookupError` exceptions, which can be thrown by MaterialX, is used in the examples.
#  
# > Note however that these interfaces are used for file I/O and "copy" interface where validation is performed document as a separate step.

# %% [markdown]
# **addNode() Example**
# 
#  `addNode()` is a low-level way to create a node using `category` string and `type` string.
#  
#  This method is error prone as it is possible to use undefined or invalid `category` and `type` identifiers. 

# %%
category = 'invalid_category'
type = "invalid_type"
name = ''
newNode = doc.addNode(category, '', type)
if newNode:
    print('Created node with invalid category and type: %s' % mx.prettyPrint(newNode))
    doc.removeNode(newNode.getName())

# %% [markdown]
# If an empty `name` is used this results in a new unique name generated for the node. 
# However, if a child name is specified that already exists then creation will fail and throw an error exception.

# %%
category = 'standard_surface'
name = 'myname'
try:
    newNode = doc.addNode(category, name, 'surface_shader')
except LookupError as err:
    print(err)
if newNode:
    print('1. Created node with name: "%s"' % newNode.getName())

# Creation fails as a node with the name already exist 
name = newNode.getName()
try:
    newNode = doc.addNode(category, name, type)
except LookupError as err:
    print('2. Failed trying to creae note with same name: "%s"' % err)


