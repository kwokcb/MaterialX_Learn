# %% [markdown]
#  # Creating Material Graphs
# 
# The following topics will be covered in this book:
# 1. Creating a node graph container.
# 2. Creating container input and output interfaces.
# 3. Creating nodes in a graph.
# 4. Connecting nodes in a graph.
# 5. Creating a material and connecting the graph to the material.
# 
# At the end of this book, a simple shader graph will have been created. 
# 
# The utilities used in this tutorial are available in the `mtlxutils` file: <a href="./mtlxutils/mxnodegraph.py" target="_blank">mtlxutls/mxnodegraph.py</a> for reuse.

# %% [markdown]
# ## Setup
# 
# The following pre-requisite setup steps need to performed first:
# * Load MaterialX
# * Creating a working document
# * Loading in the standard library definitions
# * Setting up a predicate to filter definitions on write.

# %%
import MaterialX as mx

# Version check
from mtlxutils.mxbase import *
haveVersion1387 = haveVersion(1, 38, 7) 
if not haveVersion1387:
    print("** Warning: Minimum version is 1.38.7 for tutorials. Have version: ", mx.__version__)

stdlib = mx.createDocument()
searchPath = mx.getDefaultDataSearchPath()
libraryFolders = mx.getDefaultDataLibraryFolders()
try:
    libFiles = mx.loadLibraries(libraryFolders, searchPath, stdlib)
    print('MaterialX version %s. Loaded %d standard library definitions' % (mx.__version__, len(stdlib.getNodeDefs())))
except mx.Exception as err:
    print('Failed to load standard library definitions: "', err, '"')

doc = mx.createDocument()
doc.importLibrary(stdlib)

# Write predicate
def skipLibraryElement(elem):
    return not elem.hasSourceUri()

# %% [markdown]
# # Creating a Node Graph
# 
# ## Create `<nodegraph>` Container
# The first step to creating a useful node graph is to create the parent container (`NodeGraph`).
# The interface <a href="https://materialx.org/docs/api/class_document.html" target="_blank">`addNodeGraph()`</a> can be used to do so. 
# 
# As with documents, all children must be uniquely named. Name generation of child names uses the
# `createValidChildName()` interface which can be used for documents, nodes, and node graphs. 
# 

# %%
def addNodeGraph(parent, name):
    """
    Add named nodegraph under parent
    """
    # Create a uniquely named node graph container under the parent document
    childName = parent.createValidChildName(name)
    
    # Create the node graph
    nodegraph = parent.addChildOfCategory('nodegraph', childName)
    return nodegraph

nodeGraph = addNodeGraph(doc,"test_nodegraph")
if nodeGraph:
    print('Created nodegraph:', mx.prettyPrint(nodeGraph)) 

# %% [markdown]
# ## Creating Output Interfaces
# 
# A node graph container without any outputs <a href="https://materialx.org/docs/api/class_output.html" target="_blank">(`Output`)</a> isn't of much use as no data flow can occur.
# Thus, at a minimum a `NodeGraph`s should create at least one child output. 
# This can be done using the <a href="https://materialx.org/docs/api/class_interface_element.html" target="_blank">`addOutput()`</a> interface on a `NodeGraph`. 
# 
# The same considerations should be given for creating an output for nodes. Namely:
# * a unique name
# * a proper type 
# should be used. 
# 
# In this case we want to create a graph which outputs a `surfaceshader`.

# %%
def addNodeGraphOutput(parent, type, name='out'):
    """
    Create an output with a unique name and proper type
    """
    if not parent.isA(mx.NodeGraph):
        return None
    
    newOutput = None
    childName = parent.createValidChildName(name)
    newOutput = parent.addOutput(childName, type)
    return newOutput

type = 'surfaceshader'
graphOutput = addNodeGraphOutput(nodeGraph, type)

# Print the graph
text = mx.prettyPrint(nodeGraph)
print(text + '</nodegraph>')

# %% [markdown]
# Note that we are using <a href="https://materialx.org/docs/api/class_element.html" target="_blank">`getNamePath()`</a> to check parent / child relationships. 
# 
# The path string (`test_nodegraph/out`) indicates that the new output has been correctly added as a child under the node graph container `test_nodegraph`. (where `/` is the parent/child path separator) 

# %%
# Examine the path to the output
print('Path to output is: "%s"' % graphOutput.getNamePath())

# %% [markdown]
# ## Creating Graph Nodes
# 
# Nodes can now be created to add logic to the graph.
# 
# The basics book demonstrates how to create nodes as direct children of a `Document`.
# The same interfaces are reused here, with the key difference being that the
# they are created with respect to a `NodeGraph` instead of the `Document`.
# 
# That is, we call `NodeGraph.addNodeInstance()` instead of `Document.addNodeInstance()` to add
# a node under a graph instead of a document.
# 
# A utility called `createNode()` is added for reuse. 

# %%
def createNode(definitionName, parent, name):
    "Utility to create a node under a given parent using a definition name and desired instance name"
    nodeName = parent.createValidChildName(name)
    nodedef = doc.getNodeDef(definitionName)
    if nodedef:
        newNode = parent.addNodeInstance(nodedef, nodeName)
        if newNode:
            return newNode
    else:
        print('Cannot find definition:',  definitionName)
    return None

shaderNode = createNode('ND_standard_surface_surfaceshader', nodeGraph, 'test_shader')
if shaderNode:
    print('- Create shader node with path:', shaderNode.getNamePath())

# Print contents of graph
print('- Graph contents:\n')
text = mx.prettyPrint(nodeGraph)
print(text + '</nodegraph>')

# %% [markdown]
# ## Connecting Nodes To Output Interfaces
# 
# To allow output data from the shader node to be accessible the shader node's **output** is connected to the 
# graph containers **output**.
# 
# A  utility called `connectOutputToOutput()` is used to hide the syntactic differences between connecting to an upstream node graph as
# opposed to a node, and to check for "type compatibility", where "compatible" means both ports are of the exact same type. 
# 
# Note that only upstream nodes, and graphs can to a downstream output. Inputs cannot be directly connected to an output. A `dot` node
# should be used as a pass-through in this case.
# 
# > Unfortunately, adding explicit outputs to nodes is not recommended, otherwise these can be pre-populated on a node to avoid the constant search on the definition if it is not found on the node. Basically a `addOutputFromNodeDef()` utility could be called before
# making any connections.

# %%
def connectOutputToOutput(outputPort, upstream, upstreamOutputName):
    "Utility to connect a downstream output to an upstream node / node output"
    "If the types differ then no connection is made"
    if not upstream:
        return False
    
    # Cannot directly connect an input to an output
    if upstream.isA(mx.Input):
        return False

    upstreamType = upstream.getType()

    # Check for an explicit upstream output on the upstream node
    # or upstream node's definition
    if upstreamOutputName:
        upStreamPort = upstream.getActiveOutput(upstreamOutputName)
        if not upStreamPort:
            upstreamNodeDef = upstream.getNodeDef()
            if upstreamNodeDef:
                upStreamPort = upstreamNodeDef.getActiveOutput(upstreamOutputName)
            else:
                return False
        if upStreamPort:
            upstreamType = upStreamPort.getType()
        
    outputPortType  = outputPort.getType()    
    if upstreamType != outputPortType:
        return False
    
    upstreamName = upstream.getName()
    attributeName = 'nodename'
    if upstream.isA(mx.NodeGraph):
        attributeName = 'nodegraph'
    outputPort.setAttribute(attributeName, upstreamName)
    
    # If an explicit output is specified on the upstream node/graph then
    # set it.
    if upstreamOutputName and upstream.getType() == 'multioutput':
        outputPort.setOutputString(upstreamOutputName)    
    
    return True

# Make the connection
shaderNodeOutput = "out"
if connectOutputToOutput(graphOutput, shaderNode, shaderNodeOutput):
    print('Connected output "%s" to upstream output: %s.%s' % (graphOutput.getNamePath(), shaderNode.getNamePath(), shaderNodeOutput))
else:
    print('Failed to connected output "%s" to upstream output: %s.%s' % (graphOutput.getNamePath(), shaderNode.getNamePath(), shaderNodeOutput))


# Check the graph
text = mx.prettyPrint(nodeGraph)
print("")
print(text + '</nodegraph>')

# %% [markdown]
#  ## Making Connections Between Nodes
#  
#  Connections are formed from a downstream `input` to an upstream `output`. For this a wrapper function is
#  used to hide some of the syntactic peculiarities.
# 
# Setting a connection can be cumbersome for the same reason that setting a value can be cumbersome
# in that a node instance when created has no inputs instantiated. So a check
# must be made to see if it exists and if its not added. Then if input and outputs types match
# then the input can make the connection.
# 
# Additionally it is considered "invalid" to have both a `value` and a connection on an input, so
# if a value has been set it must be removed. Conversely when a connection is removed a value must be
# re-assigned. 
# 
# As with value setting, the interface `addInputFromNodeDef()` is used to add individual inputs
# if they do not exist. A utility called `createNode()` is added for convenience.
# 
# Having a `connectNodeToNode()` interface would be a useful to have in the core API to avoid having
# to rewrite this logic.
# 
# > Note that is currently considered undesirable to have explicit outputs defined on nodes which
# also adds undue complexity. 

# %%
def connectNodeToNode(inputNode, inputName, outputNode, outputName):
    "Connect an input on one node to an output on another node. Existence and type checking are performed."
    "Returns input port with connection set if succesful. Otherwise None is returned."

    if not inputNode or not outputNode:
        return None


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

    # Add an input to the downstream node if it does not exist
    inputPort = inputNode.addInputFromNodeDef(inputName)
    
    if inputPort.getType() != outputType:
        print('Input type (%s) and output type (%s) do not match: ' % (inputPort.getType(), outputType))
        return None

    if inputPort:
        # Remove any value, and set a "connection" but setting the node name
        inputPort.removeAttribute('value')
        attributeName = 'nodename' if outputNode.isA(mx.Node) else 'nodegraph'
        inputPort.setAttribute(attributeName, outputNode.getName())
        if outputNode.getType() == 'multioutput' and outputName:
            inputPort.setOutputString(outputName)
    return inputPort
    
# Create a unique child name under the node graph container
imageNode = createNode("ND_image_color3", nodeGraph, "test_image")
if imageNode and shaderNode:
    inputConnnected = connectNodeToNode(shaderNode, "base_color", imageNode, "")
    if inputConnnected:
        print('Connected "%s" to "%s" in node graph "%s"' % (imageNode.getNamePath(), shaderNode.getNamePath(), 
                                                          nodeGraph.getNamePath()))
        
# Check the graph
text = mx.prettyPrint(nodeGraph)
print('\n')
print(text + '</nodegraph>')

# %% [markdown]
# ## Adding Input Interfaces
# 
# Just as child outputs can be added to a `NodeGraph`, child inputs (`Input`) can also be added.
# Adding inputs can be thought of as exposing the internal inputs as "public" interfaces.
# 
# The interface `addInputInterface()` can be used to add one or more inputs. These inputs can then be connected to inputs on node children within the node graph container.
# 
# > Note that <a href="https://materialx.org/docs/api/class_node_graph.html" target="_blank">`NodeGraph.addInterfaceName()`</a> can **only** be used for a graph which represents an implementation of a definition ('functional nodegraph'). An error condition will always be thrown
# otherwise. It would be useful if this interface handled non-functional nodegraphs as well.) 

# %%
def addInputInterface(name, typeString, parent):
    "Add a type input interface. Will always create a new interface"

    validType = False
    typedefs = parent.getDocument().getTypeDefs()
    for t in typedefs:
        if typeString in t.getName():
            validType = True
            break

    if validType:
        validName = parent.createValidChildName(name)
        parent.addInput(validName, typeString)
    
# Add interfaces
addInputInterface('input_file', 'filename', nodeGraph)
addInputInterface('color_scale', 'float', nodeGraph)

# Check the graph
text = mx.prettyPrint(nodeGraph)
print('Added input interfaces: "input_file" and "color_scale"\n')
print(text + '</nodegraph>')

# %% [markdown]
# The connection for interfaces is slightly different in that instead of an `Output` an `Input` is being connected to a downstream `Input`.
# 
# We will again write a utility to hide some of the syntactic peculiarities.

# %%
def connectInterface(nodegraph, interfaceName, internalInput):
    "Add an interface input to a nodegraph if it does not already exist." 
    "Connect the interface to the internal input. Returns interface input"

    if not nodegraph or not interfaceName or not internalInput:
        return None

    interfaceInput = nodegraph.getInput(interfaceName)

    # Create a new interface with the desired type
    if not interfaceInput:
        interfaceName = nodeGraph.createValidChildName(interfaceName)    
        interfaceInput = nodegraph.addInput(interfaceName, internalInput.getType())

    # Copy attributes from internal input to interface. 
    # Remove undesired attributes.
    interfaceInput.copyContentFrom(internalInput)
    interfaceInput.removeAttribute('sourceUri')
    interfaceInput.removeAttribute('interfacename')

    # Logic transfer any value from the internal input to the interface.
    # If none is found then use the the default value as defined by the definition.
    internalInputType = internalInput.getType()
    if internalInput.getValue():
        internaInputValue = internalInput.getValue() 
        if internaInputValue:
            interfaceInput.setValue(internaInputValue, internalInputType)
        else:
            internalNode = internalInput.getParent() 
            internalNodeDef = internalNode.getNodeDef() if internalNode else None
            internalNodeDefInput = internalNodeDef.getInput(interfaceName) if internalNodeDef else None
            internaInputValue = internalNodeDefInput.getValue() if internalNodeDefInput else None
            if internaInputValue:
                interfaceInput.setValue(internaInputValue, internalInputType)

    # Remove "value" from internal input as it's value is via a connection
    internalInput.removeAttribute('value')

    # "Connect" the internal node's input to the interface. Remove any
    # specified value
    internalInput.setInterfaceName(interfaceName)

    return interfaceInput


# %% [markdown]
# First example exposes the 'file' input as an 'input_file' interface to the graph.

# %%
# Add a 'file' input to the child node 
imageFileInput = imageNode.addInputFromNodeDef('file')
imageFileInputType = imageFileInput.getType()
imageFileInput.setValue("checker.png", imageFileInputType)
# Connect it to interface intput on "input_file"  
connectInterface(nodeGraph, "input_file", imageNode.getInput('file'))

print(mx.prettyPrint(nodeGraph) + '</nodegraph>')

# %% [markdown]
# Second example to expose "base" as a "color_scale" input on the graph.

# %%
# Second example: Publish 'base' as an interface. "Transfer"
# the default value from 'base' on the shader node to the interfce input. 
baseInput = shaderNode.addInputFromNodeDef('base')
connectInterface(nodeGraph, "color_scale", baseInput)

print(mx.prettyPrint(nodeGraph) + '</nodegraph>')

# %% [markdown]
# Third example to add the 'color_scale' input with the non-default value from 'base_color'

# %%
# Set a non-default value to be added to the published interface
baseInput.setValue(0.2, baseInput.getType())
connectInterface(nodeGraph, "color_scale", baseInput)

print(mx.prettyPrint(nodeGraph) + '</nodegraph>')

# %% [markdown]
# As a final step, we check that the document is valid and then write out the entire document to a file.

# %%
# Check the entire document
isValid = doc.validate()
if not isValid:
    print('Document is not valid')
else:
    writeOptions = mx.XmlWriteOptions()
    writeOptions.writeXIncludeEnable = False
    writeOptions.elementPredicate = skipLibraryElement

    # Save document
    mx.writeToXmlFile(doc, 'data/sample_nodegraph.mtlx', writeOptions)

    print('Wrote document to file: data/sample_nodegraph.mtlx\n')
    documentContents = mx.writeToXmlString(doc, writeOptions)
    print(documentContents)

# %% [markdown]
# ## Connecting Node to a NodeGraph
# 
# Now that we have a graph with appropriate interfaces we can create a "material" by connecting it to a downstream material node (`material`).

# %%
# Create  material node 
materialNode = createNode('ND_surfacematerial', doc, 'my_material')
if materialNode:
    print('Create material node: %s\n' % materialNode.getName())

# Connect the material node to the output of the graph
connectNodeToNode(materialNode, 'surfaceshader', nodeGraph, 'out')

# Check results
print(mx.prettyPrint(materialNode) + '</material>')
print(mx.prettyPrint(nodeGraph) + '</nodegraph>')

# %% [markdown]
# ## Material Graph Result
# 
# The resulting document is shown in XML, diagram and rendered form. (The render is performed using the `MaterialXView` utility)
# 
# <img src="images/nodegraph_book_sample_graph.svg" width=70%>
# <img src="images/nodegraph_book_sample_graph.png" width=40%>

# %%
# Check the entire document
doc.validate()
writeOptions = mx.XmlWriteOptions()
writeOptions.writeXIncludeEnable = False
writeOptions.elementPredicate = skipLibraryElement

# Save document
mx.writeToXmlFile(doc, 'data/sample_nodegraph.mtlx', writeOptions)

print('Wrote document to file: data/sample_nodegraph.mtlx\n')
documentContents = mx.writeToXmlString(doc, writeOptions)
print(documentContents)

# %% [markdown]
#  ## Finding Input Interfaces
#  
#  Sometimes it can be useful to find what inputs nodegraph are connected downstream to a given interface input.
#  The `findInputsUsingInterface()` utility demonstrates how to do this.
# 

# %%
def findInputsUsingInterface(nodegraph, interfaceName):

    connectedInputs = []    
    connectedOutputs = []
    interfaceInput = nodegraph.getInput(interfaceName)
    if not interfaceInput:
        return
    
    # Find all downstream connections for this interface
    
    for child in nodegraph.getChildren():
        if child == interfaceInput:
            continue

        # Remove connection on node inputs and copy interface value
        # to the input value so behaviour does not change
        if child.isA(mx.Node):
            for input in child.getInputs():
                childInterfaceName = input.getAttribute('interfacename')
                if childInterfaceName == interfaceName:
                    connectedInputs.append(input.getNamePath())

        # Remove connection on the output. Value are not copied over.
        elif child.isA(mx.Output):
            childInterfaceName = child.getAttribute('interfacename')
            if childInterfaceName == interfaceName:
                connectedOutputs.append(child.getNamePath())

    return connectedInputs, connectedOutputs


# %%
connectedInputs, connectedOutputs = findInputsUsingInterface(nodeGraph, "input_file")
print('Connected inputs:', connectedInputs)
print('Connected outputs:', connectedOutputs)

# %% [markdown]
#  ## Disconnecting and Removing Input Interfaces
#  
#  These interfaces can be "unpublished" by removing them from the graph and breaking any connections to
#  downstream nodes or outputs. It is may be desirable to leave the interface input for later usage as well.
# 
# The `unconnectInterface()` utility demonstrates how to do this with the option to remove the interface input as well. 
# To attempt to keep the behaviour the same the interface's value is copied to the input. 

# %%

def unconnectInterface(nodegraph, interfaceName, removeInterface=True):
    
    interfaceInput = nodegraph.getInput(interfaceName)
    if not interfaceInput:
        return
    
    # Find all downstream connections for this interface
    
    for child in nodegraph.getChildren():
        if child == interfaceInput:
            continue

        # Remove connection on node inputs and copy interface value
        # to the input value so behaviour does not change
        if child.isA(mx.Node):
            for input in child.getInputs():
                childInterfaceName = input.getAttribute('interfacename')
                if childInterfaceName == interfaceName:
                    input.setValueString(interfaceInput.getValueString())
                    input.removeAttribute('interfacename')

        # Remove connection on the output. Value are not copied over.
        elif child.isA(mx.Output):
            childInterfaceName = child.getAttribute('interfacename')
            if childInterfaceName == interfaceName:
                input.removeAttribute('interfacename')

    if removeInterface:
        nodegraph.removeChild(interfaceName)


# %%
# Disconnect and remove the interface
unconnectInterface(nodeGraph, "input_file", True)

# Check the graph
print(mx.prettyPrint(nodeGraph) + '</nodegraph>')    

# %% [markdown]
# ## Connecting an upstream node to a graph
# 
# As a final connection example we look at connecting an upstream node to a graph. This is done by connecting the node's output to the graph's input.
# 
# 1. As noted previsouly, an `input` cannot have both a connection and a value. Thus if the graph input has a value it will be removed before the connection is made. 
# 2. The utility function has some additional logic to transfer the value to an input on the upstream node if desired. 
# 3. If the upstream node has multiple outputs, the correct output be specified by setting the `output` attribute on the graph's input. 
# 
# > This would be a good general practice to always specify the output but the validation logic currently considers this to be an error.

# %%
def connectToGraphINput(node, outputName, nodegraph, inputName, transferNodeInput):
    "Connect an output on a node to an input on a nodegraph"
    "Returns the input port on the nodegraph if successful, otherwise None"

    if not node or not nodegraph:
        print('No node or nodegraph specified')
        return None

    nodedef = node.getNodeDef()
    if not nodedef:
        print('Cannot find node definition for node:', node.getName())
        return None

    outputPort = nodedef.getOutput(outputName)
    if not outputPort:
        print('Cannot find output port:', outputName, 'for the node:', node.getName())
        return None

    inputPort = nodegraph.getInput(inputName)
    if not inputPort:
        print('Cannot find input port:', inputName, 'for the nodegraph:', nodegraph.getName())
        return None

    if outputPort.getType() != inputPort.getType():
        print('Output type:', outputPort.getType(), 'does not match input type:', inputPort.getType())
        return None

    # Transfer the value from the graph input to a specified upstream input
    if transferNodeInput: 
        if inputPort.getValue():
            newInput = node.addInputFromNodeDef(transferNodeInput)
            if newInput and (newInput.getType() == inputPort.getType()):
                newInput.setValueString(inputPort.getValueString())

    # Remove any value, and set a "connection" but setting the node name        
    inputPort.removeAttribute('value')
    inputPort.setAttribute('nodename', node.getName())
    if node.getType() == 'multioutput':
        inputPort.setOutputString(outputName)

    return inputPort

# %%
# Create an upstream constant float node
colorNode = createNode('ND_constant_float', doc, 'constant_float')
if colorNode:
    print('Create color node: %s\n' % colorNode.getName())
    # Connect the color node to the graph input
    result = connectToGraphINput(colorNode, 'out', nodeGraph, 'color_scale', 'value')
    if not result:
        print('Failed to connect color node to graph input\n')


# %% [markdown]
# The resulting document looks like this:
# <img src="./images/node_to_graph_connection.svg">

# %%

# Check the graph
documentContents = mx.writeToXmlString(doc, writeOptions)
print(documentContents)


