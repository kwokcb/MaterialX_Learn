# %% [markdown]
# ## Graph Connectivity
# 
# <img src="./images/cascade_graph_example.svg">
# 
# This notebook will look at how to extract out connectivity information from a MaterialX document. 
# 
# 1. The first goal is to extract out the list of nodes for each node graph in a document, noting that the "top-level" document is itself a node graph (a GraphElement). Issues addressed include how to navigate the "unduly complex" representation of connections as the representation is geared towards
# a text representation suitable for storage rather than a run-time representation. Note that both `compound` and `functional` graphs (used by definitions are handled).
# 
# 2. Once extracted the connectivity information can be used for various purposes. This book will examine the information to produce a node graph in Mermaid format. Issues addressed include how to map the node and connectivity information to a graph syntax which has no concept of "ports" or "pins". Additionally meta data is examined to provide for graphs which are visually easier to examine by adding attributes such as user coloring of different node types. 
# 
# The logic shown here has been encapsulated as two Python classes in the `mtlxutils` library insdie `traversal.py`:
# 1. `MtlxGraphBuilder` : Class which builds the connectivity information and allows for serialization to JSON format.
# 2. `MxMermaidGraphExporter` : Class which can read and parse the connectivity information to produce Mermaid graphs. <img src="../documents/images/mermaid-logo.png" width=24px>
# 
# For this site:
# - The utilities (including Mermaid generation) in this tutorial are collected in the `mtlxutils` file: `mxtraversal.py`.
# - The command `mxgraphio.py` found in the `pymaterialx` folder wraps up these utilities.  
# - All Mermaid diagrams on this site are generated using the `mxgraphio.py` command line utility or the `mtlxutils` library.
# - The Javascript module `JsMaterialGraph` is used for interactive graph generation on the <a href="../javascript/graphing_utilities.html">Graph Editing</a> page.

# %% [markdown]
# ### Setup
# 
# The basic setup includes loading MaterialX as well as support libraries. The assumption is that at least version 1.38.7 of MaterialX has been installed.

# %%
# Helpers
import os
from IPython.display import display_markdown # For markdown display in Jupyter

# MaterialX imports
import MaterialX as mx
from mtlxutils.mxbase import *

# Do a version check
haveVersion1387 = haveVersion(1, 38, 7) 
if not haveVersion1387:
    print("** Warning: Recommended minimum version is 1.38.7 for tutorials. Have version: ", mx.__version__)
else:
    print("Using MaterialX version:", mx.__version__)

# %% [markdown]
# ### Definition Library Requirement
# 
# To be able to handle any non-explicitly defined inputs and outputs and node information, the standard MaterialX node library is required. 
# As a first step we load in libraries and create a working document.

# %%
def createWorkingDocument():
    stdlib = mx.createDocument()
    searchPath = mx.getDefaultDataSearchPath()
    libraryFolders = mx.getDefaultDataLibraryFolders()
    try:
        libFiles = mx.loadLibraries(libraryFolders, searchPath, stdlib)
        print('Create working document and loaded in: %s standard library definitions' % len(stdlib.getNodeDefs()))
    except mx.Exception as err:
        print('Failed to load standard library definitions: "', err, '"')

    doc = mx.createDocument()
    doc.importLibrary(stdlib)

    return doc

doc = createWorkingDocument()

# %% [markdown]
# ### Graph "Dictionary"
# 
# As a first step a "dictionary" containing all the nodes in a document, grouped by graph is generated.
# Each dictionary is of the form:
# ```
# <graph path string> [ <node path string >... ]
# ```
# such that for each graph (keyed by path), a list of node paths is kept.
# As the root `Document` has no path name an emptry string indicates the root graph.
# 
# Two functions are shown below to for graph dictionary building:
# 1. `updateGraphDictionaryPath()` : Add a child node path to the list of node paths for a given graph path.
# 2. `updateGraphDictionaryItem()` : Add a new graph / node pair. 

# %%
def updateGraphDictionaryPath(key, item, nodetype, type, value, graphDictionary):
    '''
    Add a parent / child to the GraphElement dictionary

    Arguments:
    key: The parent graph path
    value: The graph node path
    nodetype: The type of the node
    graphDictionary: The dictionary to add the Element to.
    '''
    if key in graphDictionary:
        #print('add:', key, value, nodetype)
        graphDictionary[key].append([item, nodetype, type, value])
    else:
        #print('add:', key, value, nodetype)
        graphDictionary[key] = [[item, nodetype, type, value]]

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
    itemType = item.getType()
    itemCategory = item.getCategory()
    itemValue = ''
    if item.isA(mx.Node):
        inputs = item.getInputs()
        if len(inputs) == 1:
            itemValue = inputs[0].getValueString()
    elif item.isA(mx.Input):
        itemValue = item.getValueString()

    updateGraphDictionaryPath(key, value, itemCategory, itemType, itemValue, graphDictionary)

# %% [markdown]
# To examine the contents of the dictionay a `printGraphDictionary()` function is added. 

# %%
def printGraphDictionary(graphDictionary: dict):
    """
    Print out the graph dictionary
    """
    for graphPath in graphDictionary:
        if graphPath == '':
            print('Root Document:')
        else:
            print(graphPath + ':')

        filter = 'input'
        # Top level document has not path, so just output some identifier string
        for item in graphDictionary[graphPath]:
            if item[1] != filter:
                continue
            print('- ', item)
        filter = 'output'
        # Top level document has not path, so just output some identifier string
        for item in graphDictionary[graphPath]:
            if item[1] != filter:
                continue
            print('- ', item)
        filter = ['output', 'input']
        # Top level document has not path, so just output some identifier string
        for item in graphDictionary[graphPath]:
            if item[1] not in filter:
                print('- ', item)

def getParentGraph(elem):
    '''
    Find the parent graph of the given element
    '''
    while (elem and not elem.isA(mx.GraphElement)):
        elem = elem.getParent()
    return elem


# %% [markdown]
# ### Connection Utlities
# 
# To aid with building connection information a few additional functions are added below.

# %% [markdown]
# #### Finding Default Upstream Output
# 
# To handle when an output is not explicitly specified for a graph or node, a utility function called `getDefaultOutput()` is added.
# It will simply return the first output found. 
# 
# This is useful when trying to find the upstream output port connecged to downstream output, but the name of the output is not explicitly specified.
# This is an inconsistency which must be handled where only for upstream nodes or graphs which have more than one output allows for a output to be specified -- otherwise validation fails.

# %%

def getDefaultOutput(node: mx.Element) -> str:
    '''
    Get the default output of a node or nodegraph. Returns the first output found. 
    '''
    if not node:
        return ''

    defaultOutput = None
    if node.isA(mx.Node):
        nodedef = node.getNodeDef()
        if nodedef:
            defaultOutput = nodedef.getActiveOutputs()[0]
        else:
            print('Cannot find nodedef for node:', node.getNamePath())
    elif node.isA(mx.NodeGraph):
        defaultOutput = node.getOutputs()[0]

    if defaultOutput:
        return defaultOutput.getName()
    return ''    


# %% [markdown]
# #### Appending Path Identifiers
# 
# A utility called `appendPath()` is added as a simple helper as there is no formal API for manipulating graph paths. It is assumed that `/` is always the path seperator.

# %%
def appendPath(p1: str, p2: str) -> str:
    '''
    Append two paths together, with a '/' separator.

    Arguments:
    p1: The first path
    p2: The second path

    Returns:
    The appended path
    '''
    PATH_SEPARATOR = '/'

    if p2:
        return p1 + PATH_SEPARATOR + p2
    return p1


# %% [markdown]
# ### Core Connection Logic
# 
# The function `buildPortConnection()` contains the core logic to determine what output node / graph and port is connected to an downstream node / nodegraph port.
# 
# Each connection is of the form:
# ```
# [ <upstream element>, [<upstream output>], <downstream element>, <downstream input>, <type of connection>]
# ```
# where the `<upstream element>` may be path to  `input` or `output` or other node type, `<upstream output` is any output port on the upstream element (if it's not an `input` or `output` node), `<downstream element>` a path to an `input`, `output` or other node type, and `<downdsteam input` is the input port on the downstream element (if it's not an `input` or `output` node). The `<type of connection` is additional meta-data to reflect the original connection syntax encountered.
# 
# Additional "undue" complexity is added as:
# 
# 1. Only relative paths are provided so parent graph searching is required.
# 2. There are multiple keywords used to indicate the type of item that is connected to upstream.
# 3. The output port is only specified if the upstream element has multiple outputs
# 4. Input nodes under a graph (nodegraph or document)  must be handled differently from Inputs which are chilren of nodes. The latter are not nodes.
# 
# This differs from say `OpenUSD` where a full path to a specific port is specified making it simple to just find the correct descendent from the root.

# %%
def buildPortConnection(doc: mx.GraphElement, graphDictionary: dict, portPath: str, connections: list, portIsNode: bool):
    '''
    Build a list of connections for the given graphElement.

    Arguments:
    - doc: The document to search for the portPath
    - portPath: The path to the port to search for connections
    - connections: The list of connections to append to. Returned.
    - portIsNode: If True, the portPath is a node, otherwise it is a port 
    '''

    root = doc.getDocument()
    port = root.getDescendant(portPath)
    if not port:
        print('Element not found:', portPath)
        return
    
    if not (port.isA(mx.Input) or port.isA(mx.Output)):
        print('Element is not an input or output')
        return

    parent = port.getParent()
    parentPath = parent.getNamePath()
    parentGraph = getParentGraph(port)

    # Need to "jump out" of current graph if considering an input interfae
    # on a graph
    if port.isA(mx.Input) and parent.isA(mx.NodeGraph):
        parentGraph = parentGraph.getParent()

    if not parentGraph:
        print('Cannot find parent graph of port', port)
    parentGraphPath = parentGraph.getNamePath()

    outputName = port.getOutputString()

    destNode = portPath if portIsNode else parentPath
    destPort = '' if portIsNode else port.getName()

    nodename = port.getAttribute('nodename')
    if nodename:
        if len(parentGraphPath) == 0:
            result = [appendPath(nodename, ''), outputName, destNode, destPort, 'nodename']
        else:
            result = [appendPath(parentGraphPath, nodename), outputName, destNode, destPort, 'nodename']
        connections.append(result)
        return
    
    nodegraph = port.getNodeGraphString()
    if nodegraph:
        if not outputName:
            outputName = getDefaultOutput(parentGraph.getChild(nodegraph))
        if len(parentGraphPath) == 0:
            result = [appendPath(nodegraph, outputName), '', destNode, destPort, 'nodename']
        else:
            result = [appendPath(parentGraphPath, nodegraph), outputName, destNode, destPort, 'nodegraph']
        connections.append(result)
        return            
    
    interfaceName = port.getInterfaceName()
    if interfaceName:
        if len(parentGraphPath) == 0:
            if not outputName:
                outputName = getDefaultOutput(parentGraph.getChild(interfaceName))
            result = [appendPath(interfaceName, outputName), '', destNode, destPort, 'nodename']
        else:
            outputName = ''
            # This should be invalid but you can have an input name on a nodedef be the
            # same a node in the functional braph. Emit a warning and rename it.
            itemValue = ''
            if destNode == (parentGraphPath + '/' + interfaceName):
                dictItem = graphDictionary.get(parentGraphPath)
                if dictItem:
                    found = False
                    for item in dictItem:
                        if item[0] == parentGraphPath + '/' + interfaceName:
                            found = True
                            break
                    if found:
                        print('Warning: Rename duplicate interface:', parentGraphPath + '/' + interfaceName + ':in')
                        interfaceName = interfaceName + ':in'                

            found = False
            dictItem = graphDictionary.get(parentGraphPath)
            if dictItem:
                for item in dictItem:
                    if item[0] == parentGraphPath + '/' + interfaceName:
                        found = True
                        break

            if not found:
                # TODO: Grab the input value from the nodedef.
                #print('- Dyanmically add in interfaceName:', interfaceName, 'to  graph:', parentGraphPath, '.Value: ', itemValue)
                updateGraphDictionaryPath(parentGraphPath, parentGraphPath + '/' + interfaceName, 'input', port.getType(), itemValue, graphDictionary)
            result = [appendPath(parentGraphPath, interfaceName), outputName, destNode, destPort, 'interfacename']
        #if portIsNode:
        #print('append interface connection:', result)
        connections.append(result)
        return

    if outputName:
        if len(parentGraphPath) == 0:
            result = [appendPath(outputName, ''), '', parentPath, port.getName(), 'nodename']
        else:
            result = [appendPath(parentGraphPath, outputName), '', parentPath, port.getName(), 'output']
        #if portIsNode:
        #print('append connection:', result)
        connections.append(result)
        return

    #if port.isA(mx.Input):
    #    portValue = port.getValueString()
    #    if portValue:
    #        result = [portValue, '', destNode, destPort, 'value']
    #        connections.append(result)



# %% [markdown]
# The `buildConnections()` utility will find all connections for a graph by scanning all children elements as necessary:
# 
# 1. For a `Input` or `Output` nodes we directly check for connections
# 2. For other `Node` types we scan all child `Inputs`
# 3. For `NodeGraphs` we recursively call `buildConnectons()`. This will handle nested `GraphElements` such as Document / NodeGraph relationships as well as NodeGraph / NodeGraph relationships. Note that any `GraphElement` can be passed in -- not just the top level Document to allow connection introspection of arbitrary graphs. 

# %%

def buildConnections(doc, graphDictionary, graphElement, connections):
    
    #print('get children for graph: "%s"' % graphElement.getNamePath())
    root = doc.getDocument()
    for elem in graphElement.getChildren():            
        if not elem.hasSourceUri():
            if elem.isA(mx.Input):
                buildPortConnection(root, graphDictionary, elem.getNamePath(), connections, True)
            elif elem.isA(mx.Output):
                buildPortConnection(root, graphDictionary, elem.getNamePath(), connections, True)
            elif elem.isA(mx.Node):
                nodeInputs = elem.getInputs()
                for nodeInput in nodeInputs:
                    buildPortConnection(root, graphDictionary, nodeInput.getNamePath(), connections, False)
            elif elem.isA(mx.NodeGraph):
                nodedef = elem.getNodeDef()
                if nodedef:
                    connections.append([elem.getNamePath(), '', nodedef.getName(), '', 'nodedef'])
                visited = set()
                path = elem.getNamePath()
                if path not in visited:
                    visited.add(path)
                    buildConnections(root, graphDictionary, elem, connections)

# %% [markdown]
# ### Example 
# 
# In the example below load in an example which can be found in the unit test suite for MaterialX. It contains a few nodegraphs that are connected in a cascading manner and is used for testing graph traversal for shader code generation. 

# %%
filename = './data/cascade_nodegraphs.mtlx'
if os.path.exists(filename):
    mx.readFromXmlFile(doc, filename)
    print("Read file: ", filename)
else:
    print("File not found: ", filename)

# %% [markdown]
# The utility function will build the graph dictionary by scan through all the children of a GraphElement and building dictionary entries.
# 
# We group the entries by scanning by child type. e.g. grouping all input connections together.
# After building the graph we print outs it's contents.

# %%
def buildGraphDictionary(doc):
    '''
    Build a dictionary of the graph elements in the document. The dictionary
    has the graph path as the key, and a list of child elements as the value.

    Arguments:
    - doc: The document to build the graph dictionary from

    Returnes:
    - The graph dictionary    
    '''
    graphDictionary = {}

    # Traverse all edges and add up and downstream nodes to
    # the graph dictionary
    root = doc.getDocument()
    skipped = []

    for elem in doc.getChildren():
        if elem.hasSourceUri():
            skipped.append(elem.getNamePath())
        else:
            if elem.isA(mx.Input) or elem.isA(mx.Output) or elem.isA(mx.Node):
                updateGraphDictionaryItem(elem, graphDictionary)
            elif (elem.isA(mx.NodeGraph)):
                # Temporarily copy over inputs and from nodedef this is a
                # functional graph
                if elem.getAttribute('nodedef'):
                    nodeDef = elem.getAttribute('nodedef')
                    nodeDef = root.getDescendant(nodeDef)
                    if nodeDef:
                        nodeDefName = nodeDef.getName()
                        for nodeDefInput in nodeDef.getInputs():                        
                            newInput = elem.addInput(nodeDefInput.getName(), nodeDefInput.getType())
                            newInput.copyContentFrom(nodeDefInput)

                for node in elem.getInputs():
                    updateGraphDictionaryItem(node, graphDictionary)
                for node in elem.getOutputs():
                    updateGraphDictionaryItem(node, graphDictionary)
                for node in elem.getNodes():
                    updateGraphDictionaryItem(node, graphDictionary)
                for node in elem.getTokens():
                    updateGraphDictionaryItem(node, graphDictionary)
            elif elem.isA(mx.NodeDef):
                updateGraphDictionaryItem(elem, graphDictionary)
            elif elem.isA(mx.Token):            
                updateGraphDictionaryItem(elem, graphDictionary)
    
    return graphDictionary

# %%
# Build and print out dictionary
graphDictionary = buildGraphDictionary(doc)
printGraphDictionary(graphDictionary)


# %% [markdown]
# Next we build the connection information and again print out each connection.

# %%

connections = []
buildConnections(doc, graphDictionary, doc, connections)
for connection in connections:
    print(connection) 

# %% [markdown]
# To allow for this information to be stored out the utility function `exporGraphAsJSON()` is shown below.
# Content in this form can be used with or without MaterialX runtime as desired. 

# %%
# Export as JSON
import json

def exportGraphAsJSON(graphDictionary, connections, filename):
    data = {}
    data['graph'] = graphDictionary
    data['connections'] = connections

    with open(filename, 'w') as outfile:
        # Write json with indentation
        json.dump(data, outfile, indent=2)

filename = './data/sample_graph_connections.json'
print('Write graph in JSON format:', filename)
exportGraphAsJSON(graphDictionary, connections, filename)

# %% [markdown]
#  <h4>JSON Export</h4>
# 
# Below is the graph dictionary contents written to file:
# 
#  <iframe class="rounded" src="./data/sample_graph_connections.json" title="JSON Export" width="80%"
#               height="400"></iframe>
# 
# > Note that it is possible to view this output with better formatting by installing an appropriate plug-in
# when viewed from a browser.

# %% [markdown]
# ### Mermaid Graph Visualization 
# 
# To demonstrate how to parse the dictionary and connections a sample `Mermaid` diagram generator is provided below.
# 
# The general logic:
# 1. Outputs all nodes and graphs first, adding in various user formatting.
# 2. Outputs the connections, again adding in various user formatting.
# 
# Of note is that the original path information is used as element identifiers with "nice" names being generated as necessary.
# 
# > Note that there is no dependence on MaterialX for any of the parsing or display logic. 

# %%
class MxMermaidGraphExporter:
    def __init__(self, graphDictionary, connections):
        self.graphDictionary = graphDictionary
        self.connections = connections
        self.mermaid = []
        self.orientation = 'LR'
        self.emitCategory = False
        self.emitType = False

    def setOrientation(self, orientation):
        self.orientation = orientation

    def setEmitCategory(self, emitCategory):
        self.emitCategory = emitCategory

    def setEmitType(self, emitType):
        self.emitType = emitType

    def execute(self):
        mermaid = []
        mermaid.append('graph %s' % self.orientation)
        for graphPath in self.graphDictionary:
            isSubgraph = graphPath != ''
            if isSubgraph:
                mermaid.append('    subgraph %s' % graphPath)
            for item in self.graphDictionary[graphPath]:
                path = mx.FilePath(item[0])
                label = path.getBaseName()
                if self.emitCategory:
                    label = item[1]
                if self.emitType:
                    label += ":" + item[2]
                if item[3]:
                    label += ":" + item[3]
                # Color nodes
                if item[1] == 'input' or item[1] == 'output':
                    if item[1] == 'input':
                        mermaid.append('    %s([%s])' % (item[0], label))
                        mermaid.append('    style %s  fill:#09D, color:#111' % item[0])
                    else:
                        mermaid.append('    %s([%s])' % (item[0], label))
                        mermaid.append('    style %s   fill:#0C0, color:#111' % item[0])
                elif item[1] == 'surfacematerial':
                    mermaid.append('    %s([%s])' % (item[0], label))
                    mermaid.append('    style %s   fill:#090, color:#111' % item[0])
                elif item[1] == 'nodedef':
                    mermaid.append('    %s[[%s]]' % (item[0], label))
                    mermaid.append('    style %s  fill:#00C, color:#111' % item[0])
                elif item[1] in ['ifequal', 'ifgreatereq', 'switch']:
                    mermaid.append('    %s{%s}' % (item[0], label))
                    mermaid.append('    style %s   fill:#C72, color:#111' % item[0])
                elif item[1] == 'token':
                    mermaid.append('    %s{{%s}}' % (item[0], label))
                    mermaid.append('    style %s  fill:#222, color:#111' % item[0]) 
                elif item[1] == 'constant':
                    mermaid.append('    %s([%s])' % (item[0], label))
                    mermaid.append('    style %s  fill:#500, color:#111' % item[0])               
                else:
                    mermaid.append('    %s[%s]' % (item[0], label))

            if isSubgraph:
                mermaid.append('    end')
        self.mermaid = mermaid
        
        for connection in self.connections:
            source = ''

            # Set source node. If nodes is in a graph then we use <graph>/<node> as source
            source = connection[0]
            
            # Set destination node
            dest = connection[2]

            # Edge can be combo of source output port + destination input port
            if len(connection[1]) > 0:
                if len(connection[3]) > 0:
                    edge = connection[1] + '-->' + connection[3]
                else:
                    edge = connection[1]
            else:
                edge = connection[3]

            if connection[4] == 'value':
                sourceNode = mx.createValidName(source)
                if len(edge) == 0:                
                    connectString = '    %s["%s"] --> %s' % (sourceNode, source, dest)
                else:
                    connectString = '    %s["%s"] --%s--> %s' % (sourceNode, source, edge, dest)
            else:
                if len(edge) > 0:                
                    connectString = '    %s --"%s"--> %s' % (source, edge, dest)
                else:
                    connectString = '    %s --> %s' % (source, dest)
            mermaid.append(connectString)

        return mermaid

    def write(self, filename):
        with open(filename, 'w') as f:
            for line in self.export():
                f.write('%s\n' % line)

    def getGraph(self, wrap=True):
        result = ''
        if wrap:
            result = '```mermaid\n' + '\n'.join(self.mermaid) + '\n```'
        else:
            result = '\n'.join(self.mermaid)
        # Sanitize
        result = result.replace('/default', '/default1')
        return result

    #def display(self):
    #    display_markdown(self.getGraph(), raw=True)

     # Export mermaid
    def export(self, filename):
        mermaidGraph = self.getGraph()
        with open(filename, 'w') as outFile:
            outFile.write(mermaidGraph)

# %% [markdown]
# To visualize the Mermaid graph we export the graph to Markdown within a HTML document.

# %%
exporter = MxMermaidGraphExporter(graphDictionary, connections)
exporter.setOrientation('TB')
exporter.execute()

# In order to get the proper mermaid rendering, we need to add the mermaid script, and write to another file.
result = exporter.getGraph()
result = result.replace('```mermaid', '<div class="mermaid">')
result = result.replace('```', '</div>')
result = "<script src='https://cdn.jsdelivr.net/npm/mermaid@9/dist/mermaid.min.js'></script>\n" + result
with open('./data/graphtest_output.html', 'w') as f:
    f.write(result)

print('Write graph to HTML file: ./data/graphtest_output.html')

# %% [markdown]
# <h4>Resulting Graph</h4>
# 
#  <iframe class="rounded" src="./data/graphtest_output.html" title="Graph" width="100%"
#               height="500"></iframe>

# %% [markdown]
# #### Visualization Options
# 
# As part of the utility some display options have been included. These include:
# 
# 1. Emitting the node category as the node label as opposed to the node's name
# 2. Emitting the node type.
# 3. Emitting the graph in different orientations.

# %%
exporter = MxMermaidGraphExporter(graphDictionary, connections)
exporter.setOrientation('BT')
exporter.setEmitCategory(True)
exporter.setEmitType(True)
exporter.execute()

result = exporter.getGraph()
result = result.replace('```mermaid', '<div class="mermaid">')
result = result.replace('```', '</div>')
result = "<script src='https://cdn.jsdelivr.net/npm/mermaid@9/dist/mermaid.min.js'></script>\n" + result
with open('./data/graphtest_output2.html', 'w') as f:
    f.write(result)

print('Write graph to HTML file: ./data/graphtest_output2.html')

# %% [markdown]
#  <iframe class="rounded" src="./data/graphtest_output2.html" title="Graph With Options" width="100%"
#               height="200"></iframe>


