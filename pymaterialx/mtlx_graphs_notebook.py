# %% [markdown]
#  # Creating Material Graphs
# 
# The following topics will be covered in this book:
# 1. Creating a node graph containers.
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
    print("** Warning: Recommended minimum version is 1.38.7 for tutorials. Have version: ", mx.__version__)

libraryPath = mx.FilePath('libraries')
stdlib = mx.createDocument()
searchPath = mx.FileSearchPath()
libFiles = mx.loadLibraries([ libraryPath ], searchPath, stdlib)

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
    print('Created nodegraph:', nodeGraph.getNamePath()) 

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
text = mx.prettyPrint(nodeGraph).split("\n")
for t in text:
    print(t)

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
def addNode(definitionName, parent, name):
    "Utility to create a node under a given parent using a definition name and desired instance name"
    nodeName = parent.createValidChildName(name)
    nodedef = doc.getNodeDef(definitionName)
    if nodedef:
        newNode = parent.addNodeInstance(nodedef, nodeName)
        if newNode:
            return newNode
    else:
        print('Cannot find nodedef:',  definitionName)
    return None

shaderNode = addNode('ND_standard_surface_surfaceshader', nodeGraph, 'test_shader')
if shaderNode:
    print('- Create shader node with path:', shaderNode.getNamePath())

# Print contents of graph
print('- Graph contents:\n')
text = mx.prettyPrint(nodeGraph).split("\n")
for t in text:
    print('  ', t)    

# %% [markdown]
# ## Connecting Nodes To Output Interfaces
# 
# To allow output data from the shader node to be accessible the shader node's **output** is connected to the 
# graph containers **output**.
# 
# A  utility called `connectOutput()` is used to hide the syntactic differences between connecting to an upstream node graph as
# opposed to a node, and to check for "type compatibility", where "compatible" means both ports are of the exact same type. 
# 
# > Unfortunately, adding explicit outputs to nodes is not recommended, otherwise these can be pre-populated on a node to avoid the constant search on the definition if it is not found on the node. Basically a `addOutputFromNodeDef()` utility could be called before
# making any connections.

# %%
def connectOutputToOutput(outputPort, upstream, upstreamOutputName):
    "Utility to connect a downstream output to an upstream node / node output"
    "If the types differ then no connection is made"

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
text = mx.prettyPrint(nodeGraph).split("\n")
for t in text:
    print(t)

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
# Additionally it is considered "amibiguous" to have both a `value` and a connection on an input, so
# if a value has been set it must be removed. Conversely when a connection is removed a value must be
# reassigned. 
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
text = mx.prettyPrint(nodeGraph).split("\n")
print('\n')
for t in text:
    print(t)

# %% [markdown]
# ## Adding Input Interfaces
# 
# Just as child outputs can be added to a `NodeGraph`, child inputs (`Input`) can also be added.
# Adding inputs can be thought of as exposing the internal inputs as "public" interfaces.
# 
# The interface `addInput()` can be used to add one or more inputs. These inputs can then be connected to inputs on node children within the node graph container.
# 
# > Note that <a href="https://materialx.org/docs/api/class_node_graph.html" target="_blank">`NodeGraph.addInterfaceName()`</a> can **only** be used for a graph which represents an implementation of a definition ('functional nodegraph'). An error condition will always be thrown
# otherwise. It would be useful if this interface handled non-functional nodegraphs as well.) 

# %%
def addInputInterface(name, typeString, parent):
    "Add a type input interface. Will always create a new interface"
    validName = parent.createValidChildName(name)
    typedefs = parent.getDocument().getTypeDefs()
    validType = False
    for t in typedefs:
        if typeString in t.getName():
            validType = True
            break

    if validType:
        parent.addInput(validName, typeString)
    
# Add interfaces
addInputInterface('input_file', 'filename', nodeGraph)
addInputInterface('color_scale', 'float', nodeGraph)

# Check the graph
text = mx.prettyPrint(nodeGraph).split("\n")
print('\n')
for t in text:
    print(t)


# %% [markdown]
# The connection for interfaces is slightly different in that instead of an `Output` an `Input` is being connected to a downstream `Input`.
# 
# We will again write a utility to hide some of the syntactic peculiarities.

# %%
def publishInterface(nodegraph, interfaceName, internalInput):
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
    # Remove undesired attributes  as this is not desired to be copied
    interfaceInput.copyContentFrom(internalInput)
    interfaceInput.removeAttribute('sourceUri')
    interfaceInput.removeAttribute('interfacename')

    # Long logic to get the value from the internal input if it exists.
    # If not get the default value
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

# Add a 'file' input to the child node 
imageFileInput = imageNode.addInputFromNodeDef('file')
imageFileInputType = imageFileInput.getType()
imageFileInput.setValue("checker.png", imageFileInputType)
# Connect it to interface intput on "input_file"  
publishInterface(nodeGraph, "input_file", imageNode.getInput('file'))


# Second example to publish 'base' as an interface. "Transfer"
# the default value from 'base' on the shader node to the interfce input. 
baseInput = shaderNode.addInputFromNodeDef('base')
publishInterface(nodeGraph, "color_scale", baseInput)

# Check the graph
text = mx.prettyPrint(nodeGraph).split("\n")
for t in text:
    print(t)

# Variation of above, where a non-default value is published
baseInput.setValue(0.2, baseInput.getType())
publishInterface(nodeGraph, "color_scale", baseInput)

# Check the graph
text = mx.prettyPrint(nodeGraph).split("\n")
for t in text:
    print(t)    

# %%
# Check the entire document
doc.validate()
writeOptions = mx.XmlWriteOptions()
writeOptions.writeXIncludeEnable = False
writeOptions.elementPredicate = skipLibraryElement
documentContents = mx.writeToXmlString(doc, writeOptions)
print(documentContents)

# Save document
mx.writeToXmlFile(doc, 'data/sample_nodegraph.mtlx', writeOptions)

# %% [markdown]
# ## Connecting Node to a NodeGraph
# 
# To complete this book, a material node (`Material`) will be create and connected to the shader output on the graph.

# %%
# Create  material node 
materialNode = addNode('ND_surfacematerial', doc, 'my_material')
if materialNode:
    print('Create material node:', materialNode.getName())

# Connect the material node to the output of the graph
connectNodeToNode(materialNode, 'surfaceshader', nodeGraph, 'out')

# Check results
print(mx.prettyPrint(materialNode))
text = mx.prettyPrint(nodeGraph).split("\n")
for t in text:
    print(t)

# %% [markdown]
# ## Material Graph Result
# 
# As a last step we write the document out to see the final results in diagram and rendered form. (Render is done using the `MaterialXView` utility)
# 
# <img src="images/nodegraph_book_sample_graph.svg" width=70%>
# <img src="images/nodegraph_book_sample_graph.png" width=40%>

# %%
# Check the entire document
doc.validate()
writeOptions = mx.XmlWriteOptions()
if haveVersion1387:
    writeOptions.writeXIncludeEnable = False
    writeOptions.elementPredicate = skipLibraryElement
documentContents = mx.writeToXmlString(doc, writeOptions)
print(documentContents)

# Save document
mx.writeToXmlFile(doc, 'data/sample_nodegraph.mtlx', writeOptions)

# %% [markdown]
#  ## Removing Input Interfaces
#  
#  These interfaces can be "unpublished" by removing them from the graph and breaking any connections to
#  downstream nodes or outputs. To attempt to keep the behaviour the same the interface's value is copied to
#  the input. 

# %%
def unpublishInterface(nodegraph, interfaceName):
    
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

    nodegraph.removeChild(interfaceName)


unpublishInterface(nodeGraph, "color_scale")

# Check the graph
text = mx.prettyPrint(nodeGraph).split("\n")
for t in text:
    print(t)
    


