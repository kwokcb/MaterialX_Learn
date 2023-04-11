# %% [markdown]
#  # Inspecting Node Graphs
#  
# Given a graph, traversal is a common task for many workflows including shader code generation.
#  
# This book will cover the basics of:
# 1. Traversing upstream from a "root" node.
# 2. Extracting connectivity information from a <a href="https://materialx.org/docs/api/class_edge.html" target="_blank"> Edge </a> structure during traversal.
# 3. Extracting grouping information (GraphElement membership) during traversal.
# 3. Traversing in to and out of graphs via interfaces.
# 4. Example logic for viewing nodegraphs using traversal logic.
# 
# Note that the key low level interfaces used for traversal are:
# 1. <a href="https://materialx.org/docs/api/class_port_element.html" target="_blank">Port getConnectedOutput()</a> for finding the output connected to an input.
# 2. <a href="https://materialx.org/docs/api/class_port_element.html" target="_blank">Port getConnectedNode()</a> for finding the node connected to an input. This uses the previous interface.
# 3. <a href="https://materialx.org/docs/api/class_input.html" target="_blank">Input getInterfaceInput()()</a>  for finding if an input is connected to an input interface on a node graph. 
# 
# > Note that for diagramming <a href="https://github.com/AcademySoftwareFoundation/MaterialX/pull/1263" target="_blank">there is a PR underway</a> to add in a new `GraphIO` interface which would encapsulate the supported required for Mermaid and GraphViz Dot support.
# For this site all Mermaid diagrams are generated using this interface.
# 
# > The utilities (including Mermaid generation) in this tutorial are collected in the `mtlxutils` file: <a href="./mtlxutils/mxtraversal.py" target="_blank">mtlxutils/mxtraversal</a>.
# 

# %% [markdown]
# ## Setup
# 
# The basic setup as outlined in the "Basics" book imports the MaterialX module, creates a working document, loads in the standard library definitions, and provides a predicate to skip definitions when writing documents. 

# %%
import MaterialX as mx

# Version check
from mtlxutils.mxbase import *
haveVersion1387 = haveVersion(1, 38,7) 
if not haveVersion1387:
    print("** Warning: Recommended version is 1.38.7 for tutorials. Have version: ", mx.__version__)

from mtlxutils.mxfile import MtlxFile as mxf
doc = mxf.creatwWorkingDocument()

# %% [markdown]
# ## GraphElement Traversal 
# 
# The easiest way to see what how a set of nodes is connected up is by using a <a href="https://materialx.org/docs/api/class_graph_iterator.html" target="_blank">GraphIterator</a> which can be accessed via the 
# <a href="https://materialx.org/docs/api/class_element.html" target="_blank">traverseGraph()</a> interface on an element. The iterator will traverse upstream starting from the element. Note that the iterator will only work on certain types of elements. A general rule is whatever is considered "renderable" by the utility <a href="https://materialx.org/docs/api/_material_x_gen_shader_2_util_8h.html" target="_blank">findRenderableElements()</a> can be used. Outputs and material nodes are the recommended starting points. 
# 
# In this example we load in an example graph, and traverse it this way.
# The key element that is returned from the iterator is an <a href="https://materialx.org/docs/api/class_edge.html" target="_blank">Edge</a>. The edge provides the connection information of what is:
# * the upstream node
# * the downstream node
# * the downstream `<input>`
# 
# The utility `printEdge()` is provided as an example of how to access information on an `Edge`.

# %%
def printEdge(edge):
    "Sample utility to print out the basic information about an edge"

    upstreamElem = edge.getUpstreamElement()
    downstreamElem = edge.getDownstreamElement()
    connectingElem = edge.getConnectingElement()

    downstreamPath = ''; 
    if connectingElem:
        downstreamPath = connectingElem.getNamePath()
    else:
        downstreamPath  = downstreamElem.getNamePath()

    # Print out information about the edge with an "arrow" to show direction
    # of data flow               
    print('Edge: ' + upstreamElem.getNamePath() + ' --> ' + downstreamPath)

# %% [markdown]
# This utility is used during the traversal of every edge. 
# 
# As it is possible to visit the same edge more than once, we keep a set of unique edges `processedEdges` to skip duplicates. To avoid this an additional utility `findEdge()` has been added to perform `Edge` comparisons. This explicit comparator is **only required in Python** as the C++ equality operator for `Edge` is not currently exposed in the Python API.

# %%

def findEdge(edge, processedEdges):
    "Edge equality comparitor"
    for pe in processedEdges:
        # Note: the comparison (pe == edge) does not work 
        if (pe.getUpstreamElement() == edge.getUpstreamElement() and
            pe.getDownstreamElement() == edge.getDownstreamElement() and
            pe.getConnectingElement() == edge.getConnectingElement()):
            return True
    return False

# %% [markdown]
# A simple usage example follows:
# 
# 1. The "marble" sample graph is read in. 
# 2. Within this graph we look for "material" nodes to use as the root for traversal.
# 3. For each root, a `GraphIterator` is used via `traverseGraph()`.
# 4. A list of edges is found and then printed out.

# %%
# Read in sample graph
mx.readFromXmlFile(doc, 'data/standard_surface_marble_solid.mtlx')

# Find the material nodes and traverse starting from them.
roots = doc.getMaterialNodes()

# Keep a list of edges already visited
processedEdges = set()
for root in roots:
    for edge in root.traverseGraph():
        if not findEdge(edge, processedEdges):
            processedEdges.add(edge)

# Examine the edge list
for edge in processedEdges:
    printEdge(edge)

# %% [markdown]
# Based on the path information printed out, it can be seen that traversal occurs not just at the document level but into (and out of) child nodegraph containers (`GraphElements`).
# 
# Tracking of what nodes are in which graphs can be added to see node groupings. The utility functions `updateSubgraphItem` and `updateSubgraph` are added to build a dictionary of `{ GraphElement, [ children Elements ]}`. Note that the top level `Document` has an empty string for it's path.

# %%
def updateGraphDictionaryPath(key, value, graphDictionary):
    """
    Add a parent / child to the GraphElement dictionary
    """
    if key in graphDictionary:
        graphDictionary[key].add(value)
    else:
        graphDictionary[key] = {value}


def updateGraphDictionaryItem(item, graphDictionary):
    """
    Add a Element to the GraphElement dictionary, where the keys are the GraphElement's path, and the value
    is a list of child Element paths
    """
    if not item:
        return

    parentElem = item.getParent()
    if not parentElem or not parentElem.isA(mx.GraphElement):
        return

    key = parentElem.getNamePath()
    value = item.getNamePath()
    updateGraphDictionaryPath(key, value, graphDictionary)

def updateGraphDictionary(edge, graphDictionary):
    """
    Add nodes from either end of the connection to a GraphElement dictionary
    """
    ends = [edge.getUpstreamElement(), edge.getDownstreamElement()]
    for end in ends:
        updateGraphDictionaryItem(end, graphDictionary)

def printGraphDictionary(graphDictionary):
    """
    Print out the sub-graph dictionary
    """
    for graphPath in graphDictionary:
        # Top level document has not path, so just output some identifier string
        if graphPath == '':
            print('Root Document:')
        else:
            print(graphPath + ':')
        for node in graphDictionary[graphPath]:
            print('- ', node)

# Travse all edges and add up and downstream nodes to
# the graph dictionary
graphDictionary = {}
processedEdges = set()
for root in roots:
    for edge in root.traverseGraph():
        if not findEdge(edge,processedEdges):
            processedEdges.add(edge)
            updateGraphDictionary(edge, graphDictionary)

# Examine the dictionary.
printGraphDictionary(graphDictionary)


# %% [markdown]
# Querying for the children of a `GraphElement` can be done using something like `getChildren()` as discussed in the "*Basics*" book. 
# 
# However, the purpose of using a traverser is to limit what is found in connected paths instead of just finding all children. This restrictive or filtered list is more optimal for workflows that involve finding exactly what affects the evaluation of a value and for sub-graph comparisons. 
# A workflow where both are useful is to determine what children in a graph are not used for evaluation (not encountered during traversal).

# %%
# Examine the entire contents of each graph element
for graphPath in graphDictionary:
    graph = doc.getDescendant(graphPath)
    graphName = graph.getNamePath()
    print(graphName if graphName else "Root Document")
    children = graph.getNodes()
    for child in children:
        print(' -', child.getNamePath())
    print(' ')

# %% [markdown]
# ## Viewing a Graph
# 
# As an example application, traversal information can be used to create diagrams
# of graphs. In this case we will create <a href="https://mermaid.js.org/" target="_blank">Mermaid</a> graphs.

# %% [markdown]
# The generic print function `printEdge()` is replaced by logic to output in Mermaid format. The additional logic added is to handle syntax restrictions for node naming, and to allow for a node name and a "UI" label. The former requires a sanitized string and the latter is the MaterialX path string.
# 
# Note that this same syntax is used for all Mermaid diagrams used for the node library reference.
# ```
# (upstream node path) --[downstream node input name]--> (downstream node path)
# ```

# %%
def emitMermaidEdge_nointerfaces(indent, edge):
    """
    Sample utility to print out edge information in Mermaid format
    Returns a string of form: `(upstream node path) --[downstream node input name]--> (downstream node path)`
    which represents a connection from an upstream node to a downstream one via a given input port.
    """
    outVal = ''

    upstreamElem = edge.getUpstreamElement()
    downstreamElem = edge.getDownstreamElement()
    connectingElem = edge.getConnectingElement()

    downstreamPath = ''
    connectionString = ''
    if connectingElem:
        connectionString = ' --".' + connectingElem.getName() + '"--> '
    else:
        connectionString = ' --> '
    downstreamPath  = downstreamElem.getNamePath()

    upstreamPath = upstreamElem.getNamePath()

    # Sanitize names for Mermaid output
    upstreamPathM = mx.createValidName(upstreamPath)
    downstreamPathM = mx.createValidName(downstreamPath)

    # Print out information about the edge with an "arrow" to show direction
    # of data flow  
    outVal = indent + upstreamPathM + '[' + upstreamPath + ']' + connectionString + downstreamPathM + '[' + downstreamPath + ']'
    return outVal


# %% [markdown]
# Mermaid supports output of children graphs via the use of the `subgraph` group declaration. The `emitMermaidSubgraphs()` variant 
# queries the node graph dictionary to output each `GraphElement` item as a `subgraph`.

# %%
def emitMermaidSubgraphs(subgraphs):
    """
    Emit GraphElement dictionary in Mermaid format
    """
    subGraphOutput = []

    for subgraph in subgraphs:
        if subgraph == '':
            continue
            
        subgraphM = mx.createValidName(subgraph)  
        subGraphOutput.append('subgraph ' + subgraphM + ':')
        for node in subgraphs[subgraph]:
            subGraphOutput.append('   ' + mx.createValidName(node))
        subGraphOutput.append('end')

    return subGraphOutput

# %% [markdown]
# These new utilities are used in a wrapper utility `generateMermaidGraph` which takes in the set of roots
# to output and generates a string list containing the text for the Mermaid graph. 

# %%
def generateMermaidGraph_nointerfaces(roots, orientation):
    """
    Output a Mermaid graph diagram given a set of root nodes
    """ 
    subgraphs = {}
    processedEdges = set()

    # Find all edges, and build up the GraphElement dictionary
    for root in roots:
        for edge in root.traverseGraph():
            if not findEdge(edge,processedEdges):
                processedEdges.add(edge)
                updateGraphDictionary(edge, subgraphs)

    # Get string output for each edge in Mermaid format
    edgeOutput = set()
    for edge in processedEdges:
        outVal = emitMermaidEdge_nointerfaces('    ', edge)
        if outVal not in edgeOutput:
            edgeOutput.add(outVal)

    # Print graph header, edges, and sub-graphs
    outputGraph = []
    outputGraph.append('  graph %s;' % orientation)
    for outVal in edgeOutput:
        outputGraph.append(outVal)
    for line in emitMermaidSubgraphs(subgraphs):
        outputGraph.append(line)

    return outputGraph

graph = generateMermaidGraph_nointerfaces(roots, 'TB')
for line in graph:
    if line:
        print(line)

# %% [markdown]
# The resulting diagram looks like this:
# 
# <img src="images/marble_mermaid_graph_generation_no_interfaces.svg" width="30%">

# %% [markdown]
# ## Handling Graph Interfaces
# 
# Traversal logic only return connections between nodes and **hides** any logic which is required to traverse through interface elements on
# `GraphElements` (`<input>` and `<output>`).  This includes connections to unconnected leaf level `<input>` interfaces .
# 
# Specifically, the `GraphIterator` does not supply this information directly on the `Edge` structure.
# An additional gap in information is that any upstream node's `<output>` is not provided. This is important **missing** information if
# the upstream node has multiple outputs, and would be useful to be addressed in a future release.
# 
# To extract out interface information additional logic is required. For this example: 
# 
# * For interface inputs: `emitInterfaceInputs()` checks the upstream node for any interface connections checking each of it's inputs for an interface input using the `Input` interface <a href="https://materialx.org/docs/api/class_input.html" target="_blank">`getInterfaceInput()`</a>. If the input is found then a call is made to add it to the appropriate graph list. 

# %%
def emitInterfaceInputs(indent, edge, subgraphs, edgeOutput):
    outVal = ''

    # Look for upstream interface inputs
    upstreamElem = edge.getUpstreamElement()
    for input in upstreamElem.getInputs():
        # getInterfaceInput() will find the interface input if it exists
        interfaceInput = input.getInterfaceInput()
        if interfaceInput:

            # Emit connection from interface input to node input
            interfaceName = interfaceInput.getName()
            interfaceNameM = mx.createValidName(interfaceInput.getNamePath())
            nodeName = mx.createValidName(upstreamElem.getNamePath())
            outVal = indent + interfaceNameM + '([' + interfaceName + ']) --".' + input.getName() + '"--> ' + nodeName
            if outVal not in edgeOutput:
                edgeOutput.add(outVal)

            # Update subgraphs to include this input
            updateGraphDictionaryItem(interfaceInput, subgraphs)

    return outVal

# %% [markdown]
# * For interface outputs: `emitMermaidEdge()` is a variation on `emitMermaidEdge_nointerfaces()` such that the downstream input is checked for any upstream output connection using the `Input` interface `getConnectedOutput()`. If an output is found then the a connection between this output to the input is emitted.
# 
# Note that during traversal the `Port` interface <a href="https://materialx.org/docs/api/class_port_element.html" target="_blank">`getConnectedOutput()`</a> is used to perform input to output traversal, however only the upstream node is returned as part of an `Edge`. Thus the need for extra logic after the fact to find out if an output interface has been traversed. 

# %%
def emitMermaidEdge(indent, edge, subgraphs, edgeOutput):
    "Sample utility to print out edge information in Mermaid format"
    "The interface getConnectedOuput() is used to determine what output the dowstream input is connected to"

    outVal = ''

    upstreamElem = edge.getUpstreamElement()
    downstreamElem = edge.getDownstreamElement()
    connectingElem = edge.getConnectingElement()

    downstreamPath  = downstreamElem.getNamePath()
    upstreamPath = upstreamElem.getNamePath()
    upstreamPathM = mx.createValidName(upstreamPath)

    # Add a connection from the upstream output to the downstream 
    upstreamOutput = None
    if connectingElem:
        outputString = connectingElem.getAttribute("output")
        if outputString:
            upstreamOutput = downstreamElem.getConnectedOutput(connectingElem.getName())
            if upstreamOutput:
                upstreamOutputName = upstreamOutput.getName()
                upstreamOutputNameM = mx.createValidName(upstreamOutput.getNamePath())
                outConnectionString =  upstreamOutputNameM + '[' + upstreamOutputName + ']'

                outVal = indent + upstreamPathM + '[' + upstreamPath + '] --> ' + outConnectionString
                if outVal not in edgeOutput:
                    edgeOutput.add(outVal)

                updateGraphDictionaryItem(upstreamOutput, subgraphs)

                # The upstream output is the upstream path instead of the node.
                upstreamPath = upstreamOutput.getNamePath()

            # <output> is not explicitly specified. This occurs for Node outputs
            else:
                upstreamOutputName = outputString
                graphElementPath = upstreamElem.getParent().getNamePath()
                upstreamOutputPath = graphElementPath + '/' + outputString
                upstreamOutputNameM = mx.createValidName(upstreamOutputPath)
                outConnectionString =  upstreamOutputNameM + '[' + upstreamOutputName + ']'

                outVal = indent + upstreamPathM + '[' + upstreamPath + '] --> ' + outConnectionString
                if outVal not in edgeOutput:
                    edgeOutput.add(outVal)

                updateGraphDictionaryPath(graphElementPath, upstreamOutputPath, subgraphs)

                # The upstream output is the upstream path instead of the node.
                upstreamPath = upstreamOutputPath

    inputConnectionString = ''
    if connectingElem:
        inputConnectionString = ' --".' + connectingElem.getName() + '"--> '
    else:
        inputConnectionString = ' --> '

    # Sanitize names for Mermaid output
    upstreamPathM = mx.createValidName(upstreamPath)
    downstreamPathM = mx.createValidName(downstreamPath)

    # Print out information about the edge with an "arrow" to show direction
    # of data flow  
    outVal = indent + upstreamPathM + '[' + upstreamPath + ']' + inputConnectionString + downstreamPathM + '[' + downstreamPath + ']'
    if outVal not in edgeOutput:
        edgeOutput.add(outVal)

# %% [markdown]
# The following code is the same as the previous example, except additional logic to call into the interface utilities.

# %%
def generateMermaidGraph(roots, orientation):
    """
    Output a Mermaid graph diagram given a set of root nodes
    """ 
    subgraphs = {}
    processedEdges = set()

    # Find all edges, and build up the GraphElement dictionary
    for root in roots:
        for edge in root.traverseGraph():
            if not findEdge(edge,processedEdges):
                processedEdges.add(edge)
                updateGraphDictionary(edge, subgraphs)

    # Get string output for each edge in Mermaid format
    edgeOutput = set()
    for edge in processedEdges:
        outVal = emitMermaidEdge('    ', edge, subgraphs, edgeOutput)
        if outVal not in edgeOutput:
            edgeOutput.add(outVal)

    # Include interface input edges
    for edge in processedEdges:
        emitInterfaceInputs('    ', edge, subgraphs, edgeOutput)            

    # Print graph header, edges, and sub-graphs
    outputGraph = []
    outputGraph.append('  graph %s;' % orientation)
    for outVal in edgeOutput:
        outputGraph.append(outVal)
    for line in emitMermaidSubgraphs(subgraphs):
        outputGraph.append(line)

    return outputGraph

from IPython.display import display_markdown
graph = generateMermaidGraph(roots, 'TB')
strgraph = '```mermaid\n'
for line in graph:
    if line:
        strgraph = strgraph + line + '\n'
strgraph = strgraph + '```\n' 
display_markdown(strgraph, raw=True)

# %% [markdown]
# The resulting diagram looks like this:
# 
# <img src="images/marble_mermaid_graph_generation.svg" width="50%">
# 
# with the same graph as seen in the graph editor:
# 
# <img src="images/marble_editor_preview.png" width="50%">
# 


