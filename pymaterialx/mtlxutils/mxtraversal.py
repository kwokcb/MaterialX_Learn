import re
import datetime
from collections import defaultdict, deque

import MaterialX as mx
import xml.etree.ElementTree as ET
from xml.dom import minidom
import json

class MtlxTraversal:
    @staticmethod
    def print_edge(edge):
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

    @staticmethod
    def find_edge(edge, processedEdges):
        "Edge equality comparitor"
        for pe in processedEdges:
            # Note: the comparison (pe == edge) does not work 
            if (pe.getUpstreamElement() == edge.getUpstreamElement() and
                pe.getDownstreamElement() == edge.getDownstreamElement() and
                pe.getConnectingElement() == edge.getConnectingElement()):
                return True
        return False

    @staticmethod
    def update_graph_dictionary_path(key, value, graphDictionary):
        """
        Add a parent / child to the GraphElement dictionary
        """
        if key in graphDictionary:
            graphDictionary[key].add(value)
        else:
            graphDictionary[key] = {value}

    @staticmethod
    def add_style(key, value, styleDictionary):
        if key in styleDictionary:
            styleDictionary[key].add(value)
        else:
            styleDictionary[key] = {value}

    @staticmethod
    def update_graph_dictionary_item(item, graphDictionary):
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
        MtlxTraversal.update_graph_dictionary_path(key, value, graphDictionary)

    @staticmethod
    def update_graph_dictionary(edge, graphDictionary):
        """
        Add nodes from either end of the connection to a GraphElement dictionary
        """
        ends = [edge.getUpstreamElement(), edge.getDownstreamElement()]
        for end in ends:
            MtlxTraversal.update_graph_dictionary_item(end, graphDictionary)

    @staticmethod
    def print_graph_dictionary(graphDictionary):
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

class MtlxGraphBuilder():
    '''
    Class to extract out the list of nodes and connections from a MaterialX document
    '''
    def __init__(self, doc):
        self.doc = doc
        self.graphDictionary = {}
        self.connections = []
        self.includeGraphs = ''

    def set_include_graphs(self, graphs):
        self.includeGraphs = graphs

    def get_dictionary(self):
        return self.graphDictionary
    
    def get_connections(self):
        return self.connections

    def update_graph_dictionary_path(self, key, item, nodetype, type, value, graphDictionary):
        """
        Add a parent / child to the GraphElement dictionary
        """
        if key in graphDictionary:
            #print('add:', key, value, nodetype)
            graphDictionary[key].append([item, nodetype, type, value])
        else:
            #print('add:', key, value, nodetype)
            graphDictionary[key] = [[item, nodetype, type, value]]


    def update_graph_dictionary_item(self, item, graphDictionary):
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
                #if itemValue:
                #    print('Scan node input:', inputs[0].getNamePath(), ' = ', itemValue)
        elif item.isA(mx.Input):
            itemValue = item.getValueString()
            #if itemValue:
            #    print('Scan input:', item.getNamePath(), ' = ', itemValue)
        #if itemCategory == 'constant':
        #    itemInput = item.getInput('value')
        #    if itemInput:
        #        itemValue =  itemInput.getValueString()
        self.update_graph_dictionary_path(key, value, itemCategory, itemType, itemValue, graphDictionary)

        #if item.isA(mx.Input):
        #    valueString = item.getActiveValueString()
        #    print('Got value: ' + valueString + ' for item:' + item.getNamePath())
        #    if valueString:
        #        update_graph_dictionary_path(key, mx.createValidName(valueString), 'value', graphDictionary)

    def print_graph_dictionary(self, graphDictionary):
        """
        Print out the sub-graph dictionary
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

    def get_parent_graph(self, elem):
        while (elem and not elem.isA(mx.GraphElement)):
            elem = elem.getParent()
        return elem

    def get_default_output(self, node):

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

    def append_path(self, p1, p2):
        if p2:
            return p1 + '/' + p2
        return p1

    def build_port_connection(self, doc, portPath, connections, portIsNode):
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
        parentGraph = self.get_parent_graph(port)

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
                result = [self.append_path(nodename, ''), outputName, destNode, destPort, 'nodename']
            else:
                #if not doc.getDescendant(parentGraphPath + '/' + nodename):
                #    print('Cannot find nodename:', nodename, 'in graph:', parentGraphPath)
                result = [self.append_path(parentGraphPath, nodename), outputName, destNode, destPort, 'nodename']
            #if portIsNode:
            #print('append nodename connection:', result)
            connections.append(result)
            return
        
        nodegraph = port.getNodeGraphString()
        if nodegraph:
            if not outputName:
                outputName = self.get_default_output(parentGraph.getChild(nodegraph))
            if len(parentGraphPath) == 0:
                result = [self.append_path(nodegraph, outputName), '', destNode, destPort, 'nodename']
            else:
                #if not doc.getDescendant(parentGraphPath + '/' + interfaceName):
                #    print('- Dyanmically add in nodegraph:', nodegraph, 'to  graph:', parentGraphPath)
                result = [self.append_path(parentGraphPath, nodegraph), outputName, destNode, destPort, 'nodegraph']
            #if portIsNode:
            #print('append nodegraph connection:', result)
            connections.append(result)
            return            
        
        interfaceName = port.getInterfaceName()
        if interfaceName:
            if len(parentGraphPath) == 0:
                if not outputName:
                    outputName = self.get_default_output(parentGraph.getChild(interfaceName))
                #print('- Dyanmically add in interfaceName:', interfaceName, 'to NO graph:', parentGraphPath)
                result = [self.append_path(interfaceName, outputName), '', destNode, destPort, 'nodename']
            else:
                outputName = ''
                # This should be invalid but you can have an input name on a nodedef be the
                # same a node in the functional braph. Emit a warning and rename it.
                itemValue = ''
                if destNode == (parentGraphPath + '/' + interfaceName):
                    dictItem = self.graphDictionary.get(parentGraphPath)
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
                dictItem = self.graphDictionary.get(parentGraphPath)
                if dictItem:
                    for item in dictItem:
                        if item[0] == parentGraphPath + '/' + interfaceName:
                            found = True
                            break

                if not found:
                    # TODO: Grab the input value from the nodedef.
                    #print('- Dyanmically add in interfaceName:', interfaceName, 'to  graph:', parentGraphPath, '.Value: ', itemValue)
                    self.update_graph_dictionary_path(parentGraphPath, parentGraphPath + '/' + interfaceName, 'input', port.getType(), itemValue, self.graphDictionary)
                result = [self.append_path(parentGraphPath, interfaceName), outputName, destNode, destPort, 'interfacename']
            #if portIsNode:
            #print('append interface connection:', result)
            connections.append(result)
            return

        if outputName:
            if len(parentGraphPath) == 0:
                result = [self.append_path(outputName, ''), '', parentPath, port.getName(), 'nodename']
            else:
                result = [self.append_path(parentGraphPath, outputName), '', parentPath, port.getName(), 'output']
            #if portIsNode:
            #print('append connection:', result)
            connections.append(result)
            return

        #if port.isA(mx.Input):
        #    portValue = port.getValueString()
        #    if portValue:
        #        result = [portValue, '', destNode, destPort, 'value']
        #        connections.append(result)

    def build_connections(self, doc, graphElement, connections):
        
        #print('get children for graph: "%s"' % graphElement.getNamePath())
        root = doc.getDocument()
        for elem in graphElement.getChildren():            
            if not elem.hasSourceUri():
                if elem.isA(mx.Input):
                    self.build_port_connection(root, elem.getNamePath(), connections, True)
                elif elem.isA(mx.Output):
                    self.build_port_connection(root, elem.getNamePath(), connections, True)
                elif elem.isA(mx.Node):
                    nodeInputs = elem.getInputs()
                    for nodeInput in nodeInputs:
                        self.build_port_connection(root, nodeInput.getNamePath(), connections, False)
                elif elem.isA(mx.NodeGraph):
                    nodedef = elem.getNodeDef()
                    if nodedef:
                        connections.append([elem.getNamePath(), '', nodedef.getName(), '', 'nodedef'])
                    visited = set()
                    path = elem.getNamePath()
                    if path not in visited:
                        visited.add(path)
                        self.build_connections(root, elem, connections)

    def build_graph_dictionary(self, doc):
        '''
        Build a dictionary of the graph elements in the document. The dictionary
        has the graph path as the key, and a list of child elements as the value.

        Arguments:
        - doc: The document to build the graph dictionary from

        Returnes:
        - The graph dictionary    
        '''
        graphDictionary = {}

        root = doc.getDocument()
        skipped = []

        for elem in doc.getChildren():
            if elem.hasSourceUri():
                skipped.append(elem.getNamePath())
            else:
                if elem.isA(mx.Input) or elem.isA(mx.Output) or elem.isA(mx.Node):
                    self.update_graph_dictionary_item(elem, graphDictionary)
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
                        self.update_graph_dictionary_item(node, graphDictionary)
                    for node in elem.getOutputs():
                        self.update_graph_dictionary_item(node, graphDictionary)
                    for node in elem.getNodes():
                        self.update_graph_dictionary_item(node, graphDictionary)
                    for node in elem.getTokens():
                        self.update_graph_dictionary_item(node, graphDictionary)
                elif elem.isA(mx.NodeDef):
                    self.update_graph_dictionary_item(elem, graphDictionary)
                elif elem.isA(mx.Token):            
                    self.update_graph_dictionary_item(elem, graphDictionary)
        
        return graphDictionary
    
    def execute(self):
        '''
        Build the graph dictionary and connections
        '''
        self.connections = []
        self.graphDictionary = {}

        graphElement = self.doc
        if self.includeGraphs:
            graph = self.includeGraphs
            graphElement = self.doc.getDescendant(graph)
            if graphElement:
                #suri = graphElement.getSourceUri()
                graphElement.setSourceUri('')
                print('Scan graph:', graphElement.getNamePath())
                #graphElement.setSourceUri(suri)
            else:
                print('Graph not found:', graph)

        self.graphDictionary = self.build_graph_dictionary(graphElement)
        self.build_connections(self.doc, graphElement, self.connections)

    def export_to_json(self, filename, inputFileName):
        data = {}
        data['doc'] = 'Graph connections for: ' + inputFileName
        data['copyright'] = 'Copyright 2026, NanMu Consulting. kwokcb@gmail.com'
        data['graph'] = self.graphDictionary
        data['connections'] = self.connections

        with open(filename, 'w') as outfile:
            # Write json with indentation
            json.dump(data, outfile, indent=2)
            outfile.write('\n')
            outfile.close()

    def import_from_json(self, filename):
        with open(filename, 'r') as infile:
            data = json.load(infile)
            infile.close()
            self.graphDictionary = data['graph']
            self.connections = data['connections']

class MxBaseGraphExporter:
    '''
    Base class for exporting a MaterialX graph
    Uses as input the graph dictionary and connections from MtlxGraphBuilder
    '''
    def __init__(self, graphDictionary, connections):

        self.graphDictionary = graphDictionary
        self.connections = connections

        # Layout options
        self.orientation = 'LR'
        self.emitCategory = False
        self.emitType = False
        self.emitValue = True

        # Coloring options
        self.node_colors = dict()
        self.node_colors['input'] = ['#09D', '#FFF']
        self.node_colors['output'] = ['#0C0', '#FFF']
        self.node_colors['surfacematerial'] = ['#090', '#FFF']
        self.node_colors['nodedef'] = ['#00C', '#FFF']
        self.node_colors['token'] = ['#222', '#FFF']
        self.node_colors['constant'] = ['#500', '#FFF']
        self.node_colors['ifequal'] = ['#C72', '#FFF']
        self.node_colors['ifgreatereq'] = ['#C72', '#FFF']
        self.node_colors['switch'] = ['#C72', '#FFF']
        self.default_node_colors = ['#e1d5e7', '#000']
        self.default_port_colors = ['#FFF', '#000']

    def set_orientation(self, orientation):
        self.orientation = orientation

    def set_emit_category(self, emitCategory):
        self.emitCategory = emitCategory

    def set_emit_type(self, emitType):
        self.emitType = emitType

    def set_emit_value(self, emitValue):
        self.emitValue = emitValue

    def get_node_colors(self):
        return self.node_colors
    
    def set_node_colors(self, colors):
        self.node_colors = colors

    def execute(self):
        raise NotImplementedError("Subclasses should implement this!")
    

class MxMermaidGraphExporter (MxBaseGraphExporter):
    '''
    Class to export a MaterialX graph to Mermaid format
    Uses as input the graph dictionary and connections from MtlxGraphBuilder
    '''
    def __init__(self, graphDictionary, connections):
        super().__init__(graphDictionary, connections)

        self.graphDictionary = graphDictionary
        self.connections = connections
        self.mermaid = []

        # Node shape options
        self.FONT_COLOR = '#FFF'
        self.RECT_START = '['
        self.RECT_END = ']'
        self.ROUNDED_RECT_START = '(['
        self.ROUNDED_RECT_END = '])'
        self.SQUARE_RECT_START = '[['
        self.SQUARE_RECT_END = ']]'
        self.DIAMOND_START = '{'
        self.DIAMOND_END = '}'        

        self.node_shapes = dict()
        self.node_shapes['input'] = [self.ROUNDED_RECT_START, self.ROUNDED_RECT_END]
        self.node_shapes['output'] = [self.ROUNDED_RECT_START, self.ROUNDED_RECT_END]
        self.node_shapes['surfacematerial'] = [self.ROUNDED_RECT_START, self.ROUNDED_RECT_END]
        self.node_shapes['nodedef'] = [self.SQUARE_RECT_START, self.SQUARE_RECT_END]
        self.node_shapes['token'] = [self.DIAMOND_START, self.DIAMOND_END]
        self.node_shapes['constant'] = [self.ROUNDED_RECT_START, self.ROUNDED_RECT_END]
        self.node_shapes['ifequal'] = [self.DIAMOND_START, self.DIAMOND_END]
        self.node_shapes['ifgreatereq'] = [self.DIAMOND_START, self.DIAMOND_END]
        self.node_shapes['switch'] = [self.DIAMOND_START, self.DIAMOND_END]

    def get_node_shapes(self):
        return self.node_shapes
    
    def set_node_shapes(self, shapes):
        self.node_shapes = shapes

    def sanitize_string(self, path):
        #return path
        path = path.replace('/default', '/default1')
        path = path.replace('/', '_')
        path = path.replace(' ', '_')
        return path

    def edge_string(self, label):
        if len(label) > 0:
            return '--"%s"-->' % (label)
        else:
            return '-->'

    def execute(self):

        CATEGORY_INDEX = 1
        TYPE_INDEX = 2
        VALUE_INDEX = 3       

        mermaid = []
        mermaid.append('graph %s' % self.orientation)
        for graphPath in self.graphDictionary:
            isSubgraph = graphPath != ''
            if isSubgraph:
                mermaid.append('    subgraph %s' % graphPath)
            
            for item in self.graphDictionary[graphPath]:
                path = item[0]
                # Get "base name" of the path
                label = path.split('/')[-1]
                # Sanitize the path name
                path = self.sanitize_string(path)

                if self.emitCategory:
                    label = item[CATEGORY_INDEX]
                if self.emitType:
                    label += ":" + item[TYPE_INDEX]
                if self.emitValue and item[3]:
                    label += ":" + item[VALUE_INDEX]
                
                # Emit formatted nodes 
                if (item[CATEGORY_INDEX] in self.node_colors):
                    colors = self.node_colors[item[CATEGORY_INDEX]]
                    mermaid.append('    style %s  fill:%s, color:%s' % (path, colors[0], colors[1]))
                
                if (item[CATEGORY_INDEX] in self.node_shapes):
                    shape = self.node_shapes[item[CATEGORY_INDEX]]
                    mermaid.append('    %s%s%s%s' % (path, shape[0], label, shape[1]))
                else:
                    mermaid.append('    %s[%s]' % (path, label))

            if isSubgraph:
                mermaid.append('    end')
        self.mermaid = mermaid
        
        for connection in self.connections:
            source = ''

            # Sanitize path names
            connection[0] = self.sanitize_string(connection[0])
            connection[2] = self.sanitize_string(connection[2])

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

            sourceNode = mx.createValidName(source)
            if connection[4] == 'value':
                connectString = '    %s["%s"] %s %s' % (sourceNode, source, self.edge_string(edge), dest)
            else:
                connectString = '    %s %s %s' % (sourceNode, self.edge_string(edge), dest)
            mermaid.append(connectString)

        return mermaid

    def write(self, filename):
        with open(filename, 'w') as f:
            for line in self.export():
                f.write('%s\n' % line)

    def get_graph(self, wrap=True):
        result = ''
        if wrap:
            result = '```mermaid\n' + '\n'.join(self.mermaid) + '\n```'
        else:
            result = '\n'.join(self.mermaid)
        # Sanitize
        result = result.replace('/default', '/default1')
        return result

    #def display(self):
    #    display_markdown(self.get_graph(), raw=True)

     # Export mermaid
    def export(self, filename):
        mermaidGraph = self.get_graph()
        with open(filename, 'w') as outFile:
            outFile.write(mermaidGraph)

### Old graph builder.
class MtlxMermaid:

    @staticmethod
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
        outVal = indent + upstreamPathM + '([' + upstreamPath + '])' + connectionString + downstreamPathM + '([' + downstreamPath + '])'
        return outVal

    @staticmethod
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

    @staticmethod
    def generateMermaidGraph_nointerfaces(roots, orientation):
        """
        Output a Mermaid graph diagram given a set of root nodes
        """ 
        subgraphs = {}
        processedEdges = set()

        # Find all edges, and build up the GraphElement dictionary
        for root in roots:
            for edge in root.traverseGraph():
                if not MtlxTraversal.find_edge(edge,processedEdges):
                    processedEdges.add(edge)
                    MtlxMermaid.updateGraphDictionary(edge, subgraphs)

        # Get string output for each edge in Mermaid format
        edgeOutput = set()
        for edge in processedEdges:
            outVal = MtlxMermaid.emitMermaidEdge_nointerfaces('    ', edge)
            if outVal not in edgeOutput:
                edgeOutput.add(outVal)

        # Print graph header, edges, and sub-graphs
        outputGraph = []
        outputGraph.append('  graph %s;' % orientation)
        for outVal in edgeOutput:
            outputGraph.append(outVal)
        for line in MtlxMermaid.emitMermaidSubgraphs(subgraphs):
            outputGraph.append(line)

        return outputGraph

    @staticmethod
    def emitInterfaceInputs(indent, edge, subgraphs, edgeOutput, styleOutput):
        '''Emit interface inputs:
        - All inputerface inputs are colored "blue"
        - The links from interface inputs are drawn with thicker lines.
        '''
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
                outVal = indent + interfaceNameM + '([' + interfaceName + ']) ==".' + input.getName() + '"==> ' + nodeName
                if outVal not in edgeOutput:
                    edgeOutput.add(outVal)
                    styleOutput.add(indent + 'style ' + interfaceNameM + ' fill:#0CF, color:#111')

                # Update subgraphs to include this input
                MtlxTraversal.update_graph_dictionary_item(interfaceInput, subgraphs)

        return outVal

    @staticmethod
    def emitMermaidEdge(indent, edge, subgraphs, edgeOutput, styleOutput):
        "Sample utility to print out edge information in Mermaid format"
        "The interface getConnectedOuput() is used to determine what output the dowstream input is connected to"

        outVal = ''

        # Current set of conditionals.
        # Will work even if the standard library is not loaded.
        conditionals = ['ifequal', 'ifgreater', 'ifgreatereq', 'switch']

        upstreamElem = edge.getUpstreamElement()
        if upstreamElem.getType() == mx.MATERIAL_TYPE_STRING:
            print('Material upstream: ' + upstreamElem.getNamePath())
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
                leftBrace = '(['
                rightBrace = '])'
                if upstreamElem.getCategory() in conditionals:
                    leftBrace = '{'
                    rightBrace = '}'
                    styleOutput.add(indent + 'style ' + mx.createValidName(upstreamPath) + ' fill:#F80, color:#111')
                    
                upstreamOutput = downstreamElem.getConnectedOutput(connectingElem.getName())
                if upstreamOutput:
                    upstreamOutputName = upstreamOutput.getName()
                    upstreamOutputNameM = mx.createValidName(upstreamOutput.getNamePath())
                    outConnectionString =  upstreamOutputNameM + leftBrace + upstreamOutputName + rightBrace

                    outVal = indent + upstreamPathM + leftBrace + upstreamPath + rightBrace + ' --> ' + outConnectionString
                    if outVal not in edgeOutput:
                        edgeOutput.add(outVal)
                        styleOutput.add(indent + 'style ' + upstreamOutputNameM + ' fill:#0C0, color:#111')

                    MtlxTraversal.update_graph_dictionary_item(upstreamOutput, subgraphs)

                    # The upstream output is the upstream path instead of the node.
                    upstreamPath = upstreamOutput.getNamePath()
                    upstreamElem = upstreamOutput

                # <output> is not explicitly specified. This occurs for Node outputs
                else:
                    upstreamOutputName = outputString
                    graphElementPath = upstreamElem.getParent().getNamePath()
                    upstreamOutputPath = graphElementPath + '/' + outputString
                    upstreamOutputNameM = mx.createValidName(upstreamOutputPath)
                    outConnectionString =  upstreamOutputNameM + '([' + upstreamOutputName + '])'

                    outVal = indent + upstreamPathM + leftBrace + upstreamPath + rightBrace + ' --> ' + outConnectionString
                    if outVal not in edgeOutput:
                        edgeOutput.add(outVal)
                        styleOutput.add(indent + 'style ' + upstreamOutputNameM + ' fill:#0C0, color:#111')

                    MtlxTraversal.update_graph_dictionary_path(graphElementPath, upstreamOutputPath, subgraphs)

                    # The upstream output is the upstream path instead of the node.
                    upstreamPath = upstreamOutputPath
                    upstreamElem = upstreamOutput

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
        upConditional = False
        leftBrace = '(['
        rightBrace = '])'
        if upstreamElem and upstreamElem.getCategory() in conditionals:
            upConditional = True
            leftBrace = '{'
            rightBrace = '}'
        outVal = indent + upstreamPathM
        outVal = outVal + leftBrace + upstreamPath + rightBrace
        
        outVal = outVal + inputConnectionString + downstreamPathM 

        downConditional = False
        leftBrace = '(['
        rightBrace = '])'
        if downstreamElem and downstreamElem.getCategory() in conditionals:
            downConditional = True
            leftBrace = '{'
            rightBrace = '}'
        outVal = outVal + leftBrace + downstreamPath + rightBrace

        if outVal not in edgeOutput:
            edgeOutput.add(outVal)
            if downstreamElem.getType() == mx.MATERIAL_TYPE_STRING:
                styleOutput.add(indent + 'style ' + downstreamPathM + ' fill:#0C0, color:#111')
            else:
                if downConditional:
                    styleOutput.add(indent + 'style ' + downstreamPathM + ' fill:#F80, color:#111')
                if upConditional:
                    styleOutput.add(indent + 'style ' + upstreamPathM + ' fill:#F80, color:#111')

    @staticmethod
    def generateMermaidGraph(roots, orientation):
        """
        Output a Mermaid graph diagram given a set of root nodes
        """ 
        subgraphs = {}
        processedEdges = set()

        # Find all edges, and build up the GraphElement dictionary
        for root in roots:
            for edge in root.traverseGraph():
                if not MtlxTraversal.find_edge(edge,processedEdges):
                    processedEdges.add(edge)
                    MtlxTraversal.update_graph_dictionary(edge, subgraphs)

        # Get string output for each edge in Mermaid format
        edgeOutput = set()
        styleOutput = set()
        for edge in processedEdges:
            outVal = MtlxMermaid.emitMermaidEdge('    ', edge, subgraphs, edgeOutput, styleOutput)
            if outVal not in edgeOutput:
                edgeOutput.add(outVal)

        # Include interface input edges
        for edge in processedEdges:
            MtlxMermaid.emitInterfaceInputs('    ', edge, subgraphs, edgeOutput, styleOutput)            

        # Print graph header, edges, sub-graphs, and styling
        outputGraph = []
        outputGraph.append('  graph %s;' % orientation)
        for outVal in edgeOutput:
            outputGraph.append(outVal)

        outputGraph.append('%% Subgraphs')
        for line in MtlxMermaid.emitMermaidSubgraphs(subgraphs):
            outputGraph.append(line)

        outputGraph.append('%% Style')
        for line in styleOutput:
            outputGraph.append(line)

        return outputGraph
    
class MxDrawIOExporter(MxBaseGraphExporter):    
    '''
    Class to export a MaterialX graph to Draw.io format
    Uses as input the graph dictionary and connections from MtlxGraphBuilder
    '''
    def __init__(self, graphDictionary, connections):
        super().__init__(graphDictionary, connections)

        self.graphDictionary = graphDictionary
        self.connections = connections
        self.xml_root = None
        self.mxfile = None
        self.diagram = None
        
        # Draw.io specific settings for class instances
        self.class_width = 140
        self.header_height = 30
        self.value_height = 20
        self.slot_height = 30
        self.separator_height = 8
        self.horizontal_spacing = 200
        self.vertical_spacing = 150
        
        # Orientation settings
        self.orientation = 'TB'  # Default: Left to Right
        
        # Tracking for layout and port reuse
        self.node_positions = {}
        self.slot_positions = {}  # Maps slot_id -> (x, y)
        self.existing_slots = {}  # Maps (node_id, slot_name, 'input'/'output') -> slot_id
        self.used_ids = set()
        self.node_name_to_id = {}  # Maps simple node name to class ID
        
        self.next_x = 50
        self.next_y = 50
        self.current_row_nodes = 0
        self.max_nodes_per_row = 4

        self.debug = True
        
    def set_debug(self, debug):
        self.debug = debug

    def _debug_print(self, message):
        if self.debug:
            print(message)

    def set_orientation(self, orientation):
        """Set the graph orientation (LR, RL, TB, BT)"""
        if orientation in ['LR', 'RL', 'TB', 'BT']:
            self.orientation = orientation
            # Reset layout variables
            self.next_x = 50
            self.next_y = 50
            self.current_row_nodes = 0
            
            # Adjust spacing based on orientation
            if orientation in ['LR', 'RL']:
                self.horizontal_spacing = 200
                self.vertical_spacing = 150
                self.max_nodes_per_row = 4
            else:
                self.horizontal_spacing = 150
                self.vertical_spacing = 200
                self.max_nodes_per_row = 6
        else:
            self._debug_print(f"Warning: Unknown orientation '{orientation}'. Using default 'LR'.")
            
    def get_unique_id(self, base_id):
        """Generate a unique ID"""
        if base_id not in self.used_ids:
            self.used_ids.add(base_id)
            return base_id
        
        print('----------------- ID is not unique ', base_id)
        #counter = 1
        #while True:
        #    new_id = f"{base_id}_{counter}"
        #    if new_id not in self.used_ids:
        #        self.used_ids.add(new_id)
        #        return new_id
        #    counter += 1    

    def sanitize_id(self, path):
        """Create a valid ID for draw.io cells"""
        #id_str = re.sub(r'[\/\s:\.\(\)\[\]\{\}]', '_', path)
        #if id_str and id_str[0].isdigit():
        #    id_str = 'id_' + id_str
        #return self.get_unique_id(id_str)
        return self.get_unique_id(path)
    
    def create_mxfile(self):
        """Create the root mxfile structure"""
        self.xml_root = ET.Element('mxfile')
        self.xml_root.set('host', 'app.diagrams.net')
        date_time =  datetime.date.today().strftime("%B %d, %Y")
        self.xml_root.set('modified', date_time)    
        self.xml_root.set('agent', 'MaterialX DrawIO Exporter')
        self.xml_root.set('version', '0.1.39.5')
        self.xml_root.set('copyright', 'Copyright 2026, NanMu Consulting. kwokcb@gmail.com')
        
    def create_diagram(self, name="MaterialX Graph"):
        """Create a diagram within the mxfile"""
        diagram_id = "diagram_" + str(len(self.xml_root) + 1)
        self.mxfile = ET.SubElement(self.xml_root, 'diagram')
        self.mxfile.set('id', diagram_id)
        self.mxfile.set('name', name)
        
        # Create the mxGraphModel
        mxGraphModel = ET.SubElement(self.mxfile, 'mxGraphModel')
        mxGraphModel.set('dx', '1422')
        mxGraphModel.set('dy', '879')
        mxGraphModel.set('grid', '1')
        mxGraphModel.set('gridSize', '10')
        mxGraphModel.set('guides', '1')
        mxGraphModel.set('tooltips', '1')
        mxGraphModel.set('connect', '1')
        mxGraphModel.set('arrows', '1')
        mxGraphModel.set('fold', '1')
        mxGraphModel.set('page', '1')
        mxGraphModel.set('pageScale', '1')
        mxGraphModel.set('pageWidth', '827')
        mxGraphModel.set('pageHeight', '1169')
        mxGraphModel.set('math', '0')
        mxGraphModel.set('shadow', '0')
        
        root = ET.SubElement(mxGraphModel, 'root')
        
        # Create layer 0 (background)
        layer0 = ET.SubElement(root, 'mxCell')
        layer0.set('id', '0')
        
        # Create layer 1 (default layer)
        layer1 = ET.SubElement(root, 'mxCell')
        layer1.set('id', '1')
        layer1.set('parent', '0')
        
        self.diagram = root
        
    
    def create_slots(self, slot_type, fill_colors, class_id, slots, current_y, x, y):
        '''
        Create slots for a class instance
        @param slot_type: 'input' or 'output'
        @param fill_color: Fill and font colors for the slot
        @param class_id: The class instance ID
        @param slots: List of slot names
        @param current_y: Current Y position within the class instance
        @param x: X position of the class instance
        @param y: Y position of the class instance
        @return List of slot IDs and updated current_y
        '''
        if self.diagram is None:
            raise ValueError("Diagram not created. Call create_diagram() first.")

        slot_ids = []
        fillc = fill_colors[0]
        fontc = fill_colors[1]
        for i, slot_name in enumerate(slots):
            #slot_id = self.get_unique_id(f"{class_id}_{slot_type}_{i}")
            slot_id = f"{class_id}/{slot_name}"

            slot_cell = ET.SubElement(self.diagram, 'mxCell')
            slot_cell.set('id', slot_id)
            slot_cell.set('value', slot_name)
            slot_cell.set('style', f'html=1;strokeColor=none;fontColor={fontc};fillColor={fillc};align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;points=[[0,0.5],[1,0.5]];resizeWidth=1;whiteSpace=wrap;')
            slot_cell.set('vertex', '1')
            slot_cell.set('parent', class_id)
            
            slot_geom = ET.SubElement(slot_cell, 'mxGeometry')
            slot_geom.set('y', str(current_y))
            slot_geom.set('width', str(self.class_width))
            slot_geom.set('height', str(self.slot_height))
            slot_geom.set('as', 'geometry')
            
            # Store slot position for connections
            slot_center_x = x + (self.class_width / 2)
            slot_center_y = y + current_y + (self.slot_height / 2)
            self.slot_positions[slot_id] = (slot_center_x, slot_center_y)
            
            # Store in existing slots map
            self.existing_slots[(class_id, slot_name, slot_type)] = slot_id
            slot_ids.append(slot_id)
            
            current_y += self.slot_height

        return slot_ids, current_y        
    
    def create_class_instance(self, class_id, class_name, class_type, x, y, input_slots, output_slots, parent="1", header_height=None):
        '''
        Create a class instance (swimlane) with input and output slots
        @param class_id: Unique ID for the class instance
        @param class_name: Name of the class instance
        @param class_type: Type/category of the class instance
        @param x: X position of the class instance
        @param y: Y position of the class instance
        @param input_slots: List of input slot names
        @param output_slots: List of output slot names
        @param parent: Parent ID in the diagram
        @param header_height: Optional header height
        @return class_id, list of input slot IDs, list of output slot IDs
        '''
        if self.diagram is None:
            raise ValueError("Diagram not created. Call create_diagram() first.")

        # Calculate total height
        total_slots = len(input_slots) + len(output_slots)
        if header_height is None:
            header_height = self.header_height
        total_height = header_height + (total_slots * self.slot_height) + self.separator_height
        
        # Create the swimlane (class container)
        swimlane = ET.SubElement(self.diagram, 'mxCell')
        swimlane.set('id', class_id)
        swimlane.set('value', class_name)
        
        # Set header style. Make sure to use the proper header height for start size.
        fill_color = self.node_colors.get(class_type, self.default_node_colors)[0]
        font_color = self.node_colors.get(class_type, self.default_node_colors)[1]

        swimlane_style = f'swimlane;fontColor={font_color};fillColor={fill_color};fontStyle=4;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize={header_height};horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;whiteSpace=wrap;'
        swimlane.set('style', swimlane_style)
        swimlane.set('vertex', '1')
        swimlane.set('parent', parent)
        
        geometry = ET.SubElement(swimlane, 'mxGeometry')
        geometry.set('x', str(x))
        geometry.set('y', str(y))
        geometry.set('width', str(self.class_width))
        geometry.set('height', str(total_height))
        geometry.set('as', 'geometry')
        
        # Create input slots
        current_y = header_height
        fill_colors = self.default_port_colors
        input_slot_ids, current_y =  self.create_slots('input', fill_colors, class_id, input_slots, current_y, x, y)

        # Create output slots
        fill_colors = self.default_port_colors
        output_slot_ids, current_y = self.create_slots('output', fill_colors, class_id, output_slots, current_y, x, y)
        
        # Create separator line
        need_separator = False
        if need_separator:
            separator_id = self.get_unique_id(f"{class_id}_separator")
            separator = ET.SubElement(self.diagram, 'mxCell')
            separator.set('id', separator_id)
            separator.set('value', '')
            separator.set('style', 'line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;')
            separator.set('vertex', '1')
            separator.set('parent', class_id)
            
            separator_geom = ET.SubElement(separator, 'mxGeometry')
            separator_geom.set('y', str(current_y))
            separator_geom.set('width', str(self.class_width))
            separator_geom.set('height', str(self.separator_height))
            separator_geom.set('as', 'geometry')
        
        # Store node position
        self.node_positions[class_id] = (x, y, self.class_width, total_height)
        
        return class_id, input_slot_ids, output_slot_ids

    def create_edge(self, edge_id, source, target, parent="1"):
        """Create an edge (connection) between slots"""

        if self.diagram is None:
            raise ValueError("Diagram not created. Call create_diagram() first.")

        edge = ET.SubElement(self.diagram, 'mxCell')
        edge.set('id', edge_id)
        
        # Set edge style based on orientation
        edge_style = 'edgeStyle=orthogonalEdgeStyle;html=1;'
        
        if self.orientation == 'LR':
            edge_style += 'entryX=0;entryY=0.5;entryDx=0;entryDy=0;'
        elif self.orientation == 'RL':
            edge_style += 'entryX=1;entryY=0.5;entryDx=0;entryDy=0;'
        elif self.orientation == 'TB':
            edge_style += 'entryX=0.5;entryY=0;entryDx=0;entryDy=0;'
        elif self.orientation == 'BT':
            edge_style += 'entryX=0.5;entryY=1;entryDx=0;entryDy=0;'
        
        edge_style += 'curved=1;'
        
        edge.set('style', edge_style)
        edge.set('edge', '1')
        edge.set('parent', parent)
        edge.set('source', source)
        edge.set('target', target)
        
        geometry = ET.SubElement(edge, 'mxGeometry')
        geometry.set('relative', '1')
        geometry.set('as', 'geometry')
        
        return edge
    
    def update_layout_position(self, node_width, node_height):
        '''
        Update layout position based on orientation
        '''
        if self.orientation in ['LR', 'RL']:
            # Horizontal layout
            self.next_x += node_width + self.horizontal_spacing
            self.current_row_nodes += 1
            
            if self.current_row_nodes >= self.max_nodes_per_row:
                self.next_x = 50
                self.next_y += node_height + self.vertical_spacing
                self.current_row_nodes = 0
        else:
            # Vertical layout
            self.next_y += node_height + self.vertical_spacing
            self.current_row_nodes += 1
            
            if self.current_row_nodes >= self.max_nodes_per_row:
                self.next_y = 50
                self.next_x += node_width + self.horizontal_spacing
                self.current_row_nodes = 0
    
    def collect_node_slots(self, node_name):
        '''
        Collect unique input and output slots for a node from connections
        '''
        input_slots = {}
        output_slots = {}
        
        for conn in self.connections:
            source_node = conn[0].split('/')[-1] if '/' in conn[0] else conn[0]
            target_node = conn[2].split('/')[-1] if '/' in conn[2] else conn[2]
            
            # Check if this node is the source (has outputs)
            if source_node == node_name:
                slot_name = conn[1] if conn[1] else "out"
                if slot_name not in output_slots:
                    output_slots[slot_name] = []
                output_slots[slot_name].append(conn)
            
            # Check if this node is the target (has inputs)
            if target_node == node_name:
                slot_name = conn[3] if conn[3] else "in"
                if slot_name not in input_slots:
                    input_slots[slot_name] = []
                input_slots[slot_name].append(conn)

        # Return sorted lists of slot names
        return list(input_slots.keys()), list(output_slots.keys())
    
    def extract_base_node_name(self, node_path):
        '''
        Extract the base node name from a path, removing any numeric suffix
        '''
        # Get the last part of the path
        node_name = node_path.split('/')[-1]
        # Remove any numeric suffix like _1, _2, etc.
        if '_' in node_name and node_name.split('_')[-1].isdigit():
            # Remove the numeric suffix
            parts = node_name.split('_')
            if len(parts) > 1 and parts[-1].isdigit():
                node_name = '_'.join(parts[:-1])
        return node_name
    
    def create_node_instance(self, node_path, node_info):
        '''
        Create a class instance for a node. This includes:
        - Create the header with node name/type/value
        - Collect input/output slots from connections
        @param node_path: The full path of the node
        @param node_info: The node information tuple/list
        @return: The class ID of the created node
        '''
        class_id = self.sanitize_id(node_path)
        self.node_name_to_id[node_path] = class_id
        node_type = node_info[1] if len(node_info) > 1 else 'node'
        node_value = node_info[3] if len(node_info) > 3 else ''
        header_height = self.header_height
        class_name = node_path
        if self.emitType:
            class_name = node_type
        if self.emitValue and node_value:
            class_name += f' = "{node_value}"'
            header_height += self.value_height

        # Collect all slots from all connections for this node (using full path)
        input_slots = set()
        output_slots = set()
        for conn in self.connections:
            src = conn[0]
            target = conn[2]
            src_slot = conn[1] if conn[1] else 'out'
            target_slot = conn[3] if conn[3] else 'in'
            if src == node_path:
                output_slots.add(src_slot)
            if target == node_path:
                input_slots.add(target_slot)
        if not output_slots:
            output_slots.add('out')
        if not input_slots:
            input_slots.add('in')

        x = self.next_x
        y = self.next_y
        class_id, input_slot_ids, output_slot_ids = self.create_class_instance(
            class_id=class_id,
            class_name=class_name,
            class_type=node_type,
            x=x,
            y=y,
            input_slots=list(input_slots),
            output_slots=list(output_slots),
            parent="1",
            header_height=header_height
        )
        total_slots = len(input_slot_ids) + len(output_slot_ids)
        node_height = header_height + (total_slots * self.slot_height) + self.separator_height
        self.update_layout_position(self.class_width, node_height)
        return class_id
    
    def find_node_id_for_connection(self, connection_node):
        '''
        Find the class ID for a connection node reference
        - Use the full node path for lookup
        '''
        return self.node_name_to_id.get(connection_node)
    
    def create_connection(self, connection, connection_index):
        '''
        Create a connection between slots
        '''
        if self.diagram is None:
            raise ValueError("Diagram not created. Call create_diagram() first.")

        source_path = connection[0]
        source_slot = connection[1]
        target_path = connection[2]
        target_slot = connection[3]
        conn_type = connection[4] if len(connection) > 4 else ''

        # Find the node IDs using our mapping (full path)
        source_node_id = self.find_node_id_for_connection(source_path)
        if not source_node_id:
            source_node_id = self.find_node_id_for_connection(source_path+"/"+source_slot)
        target_node_id = self.find_node_id_for_connection(target_path)

        if not source_node_id:
            self._debug_print(f"Warning: Could not find source node for '{source_path}'. {source_slot}")
            self._debug_print(f"Available nodes: {list(self.node_name_to_id.keys())}")
            return None
        if not target_node_id:
            self._debug_print(f"Warning: Could not find target node for '{target_path}'")
            self._debug_print(f"Available nodes: {list(self.node_name_to_id.keys())}")
            return None

        # Use slot names as-is
        source_slot_name = source_slot if source_slot else "out"
        target_slot_name = target_slot if target_slot else "in"

        # Look up existing slot IDs
        source_slot_key = (source_node_id, source_slot_name, 'output')
        target_slot_key = (target_node_id, target_slot_name, 'input')

        source_id = self.existing_slots.get(source_slot_key)
        target_id = self.existing_slots.get(target_slot_key)

        # If slot doesn't exist, create it on the fly
        if not source_id:
            id = self.get_unique_id(f"{source_node_id}_{source_slot_name}_out")
            slot_cell = ET.SubElement(self.diagram, 'mxCell')
            slot_cell.set('id', str(id))
            slot_cell.set('value', source_slot_name)
            slot_cell.set('style', f'html=1;strokeColor=none;fontColor=#000;fillColor=#FFF;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;resizeWidth=1;whiteSpace=wrap;')
            slot_cell.set('vertex', '1')
            slot_cell.set('parent', source_node_id)
            slot_geom = ET.SubElement(slot_cell, 'mxGeometry')
            slot_geom.set('y', str(self.header_height))
            slot_geom.set('width', str(self.class_width))
            slot_geom.set('height', str(self.slot_height))
            slot_geom.set('as', 'geometry')
            self.existing_slots[source_slot_key] = slot_cell.get('id')
            source_id = slot_cell.get('id')

        if not target_id:
            id = self.get_unique_id(f"{target_node_id}_{target_slot_name}_in")
            slot_cell = ET.SubElement(self.diagram, 'mxCell')
            slot_cell.set('id', str(id))
            slot_cell.set('value', target_slot_name)
            slot_cell.set('style', f'html=1;strokeColor=none;fontColor=#000;fillColor=#FFF;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;resizeWidth=1;whiteSpace=wrap;')
            slot_cell.set('vertex', '1')
            slot_cell.set('parent', target_node_id)
            slot_geom = ET.SubElement(slot_cell, 'mxGeometry')
            slot_geom.set('y', str(self.header_height))
            slot_geom.set('width', str(self.class_width))
            slot_geom.set('height', str(self.slot_height))
            slot_geom.set('as', 'geometry')
            self.existing_slots[target_slot_key] = slot_cell.get('id')
            target_id = slot_cell.get('id')

        # Create edge if both source and target exist
        edge_id = self.get_unique_id(f"edge_{connection_index}")

        # Set edge style based on connection type
        edge_style = ''
        if conn_type == 'value':
            edge_style = 'strokeColor=#ff6b6b;strokeWidth=2;dashed=1;'
        elif conn_type == 'nodedef':
            edge_style = 'strokeColor=#4ecdc4;strokeWidth=3;'

        edge = self.create_edge(
            edge_id=edge_id,
            source=source_id,
            target=target_id,
            parent="1"
        )

        # Update edge style if needed
        if edge_style:
            current_style = edge.get('style', '')
            edge.set('style', current_style + edge_style)

        return edge_id
    
    def create_definition_nodes(self):
        '''
        Create definition nodes 
        '''
        if self.diagram is None:
            raise ValueError("Diagram not created. Call create_diagram() first.")

        value_nodes = {}
        
        NODE_STYLE = 'shape=ellipse;fillColor=#ffeb3b;strokeColor=#fbc02d;html=1;whiteSpace=wrap;'

        non_value = ['nodename', 'interfacename']
        for i, conn in enumerate(self.connections):
            if len(conn) > 4 and conn[4] not in non_value:
                value_id = self.sanitize_id(f"value_{conn[0]}")
                self._debug_print('Creating value node for connection:' + conn)
                if value_id not in value_nodes:
                    # Create a simple value node (not a class instance)
                    x = self.next_x
                    y = self.next_y
                    
                    value_cell = ET.SubElement(self.diagram, 'mxCell')
                    value_cell.set('id', value_id)
                    value_cell.set('value', f"Value: {conn[0]}")
                    value_cell.set('style', NODE_STYLE)
                    value_cell.set('vertex', '1')
                    value_cell.set('parent', '1')
                    
                    value_geom = ET.SubElement(value_cell, 'mxGeometry')
                    value_geom.set('x', str(x))
                    value_geom.set('y', str(y))
                    value_geom.set('width', '80')
                    value_geom.set('height', '40')
                    value_geom.set('as', 'geometry')
                    
                    value_nodes[value_id] = True
                    self.node_positions[value_id] = (x, y, 80, 40)
                    
                    # Store mapping
                    self.node_name_to_id[conn[0]] = value_id
                    
                    # For value nodes, we need to create an output slot
                    self.existing_slots[(value_id, 'out', 'output')] = value_id
                    
                    self.update_layout_position(80, 40)
        
        return value_nodes
    
    def _group_nodes(self, group_name, node_ids, fill_color='#f4f1f7'):
        '''
        Create a group around existing nodes
        @param group_name: Name of the group
        @param node_ids: List of node IDs to include in the group
        '''
        if self.diagram is None:
            raise ValueError("Diagram not created. Call create_diagram() first.")
        
        if not node_ids:
            return
        
        # Find bounds of all nodes in the group
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        
        for node_id in node_ids:
            if node_id in self.node_positions:
                x, y, width, height = self.node_positions[node_id]
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x + width)
                max_y = max(max_y, y + height)
        
        # Add padding
        padding = 30
        group_x = min_x - padding
        group_y = min_y - padding - 20  # Extra space for group label
        group_width = (max_x - min_x) + (padding * 2)
        group_height = (max_y - min_y) + (padding * 2)
        
        # Create group ID
        group_id = self.sanitize_id(f"group_{group_name}")
        
        # Create the group cell (a simple rectangle)
        group_cell = ET.SubElement(self.diagram, 'mxCell')
        group_cell.set('id', group_id)
        group_cell.set('value', group_name)  # Group label
        
        group_style = f'rounded=0;whiteSpace=wrap;html=1;fillColor={fill_color};strokeColor=#9673a6;fontStyle=1;fontSize=12;opacity=80;'
        
        group_cell.set('style', group_style)
        group_cell.set('vertex', '1')
        group_cell.set('parent', '1')
        
        geometry = ET.SubElement(group_cell, 'mxGeometry')
        geometry.set('x', str(group_x))
        geometry.set('y', str(group_y))
        geometry.set('width', str(group_width))
        geometry.set('height', str(group_height))
        geometry.set('as', 'geometry')
        
        # Store group position
        self.node_positions[group_id] = (group_x, group_y, group_width, group_height)
        
        # Move nodes to be children of the group (optional, but keeps hierarchy clean)
        # Note: In draw.io, connections still work even if nodes are inside groups
        for node_id in node_ids:
            # Find the node cell and update its parent
            for cell in self.diagram.findall(f".//mxCell[@id='{node_id}']"):
                cell.set('parent', group_id)
                break
        
        self._debug_print(f"Created group '{group_name}' with {len(node_ids)} nodes")

    def create_groups(self, graph_info):
        '''
        Create groups based on graph paths
        @param graph_info: List of tuples (graph_path, node_id)
        '''
        # Create groups around nodes that share the same non-empty graph path
        groups_created = {}
        
        # Find all nodes in each group
        for graph_path, node_id in graph_info:
            if graph_path:  # Skip empty graph paths as nodes are at root level
                if graph_path not in groups_created:
                    groups_created[graph_path] = []
                groups_created[graph_path].append(node_id)
        
        # Create groups for each graph path
        for graph_path, node_ids_in_group in groups_created.items():
            if len(node_ids_in_group) > 0:
                self._group_nodes(graph_path, node_ids_in_group)

    def layout_nodes(self, x_spacing=80, y_spacing=40, start_x=50, start_y=50):
        """
        Layout nodes in columns based on connection dependencies (topological sort), using actual node sizes.
        Updates self.node_positions and mxGeometry for each node.
        """
        # Build adjacency and reverse adjacency
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        all_nodes = set(self.node_positions.keys())
        for conn in self.connections:
            src_id = self.find_node_id_for_connection(conn[0])
            dst_id = self.find_node_id_for_connection(conn[2])
            if src_id and dst_id:
                graph[src_id].append(dst_id)
                reverse_graph[dst_id].append(src_id)
                all_nodes.add(src_id)
                all_nodes.add(dst_id)

        # Kahn's algorithm for topological sort
        in_degree = {n: 0 for n in all_nodes}
        for dsts in graph.values():
            for dst in dsts:
                in_degree[dst] += 1
        queue = deque([n for n in all_nodes if in_degree[n] == 0])
        topo_order = []
        while queue:
            n = queue.popleft()
            topo_order.append(n)
            for m in graph[n]:
                in_degree[m] -= 1
                if in_degree[m] == 0:
                    queue.append(m)

        # Assign columns by longest path from any input node
        node_column = {}
        def get_column(n):
            if n not in reverse_graph or not reverse_graph[n]:
                return 0
            if n in node_column:
                return node_column[n]
            col = 1 + max(get_column(p) for p in reverse_graph[n])
            node_column[n] = col
            return col
        for n in topo_order:
            get_column(n)

        # Group nodes by column
        columns = defaultdict(list)
        for n in topo_order:
            col = node_column.get(n, 0)
            columns[col].append(n)

        # Assign x/y positions using node sizes
        for col in sorted(columns):
            nodes = columns[col]
            y = start_y
            for n in nodes:
                width, height = self.node_positions[n][2], self.node_positions[n][3]
                x = start_x + col * (self.class_width + x_spacing)
                # Update node_positions
                self.node_positions[n] = (x, y, width, height)
                # Update mxGeometry for this node
                for cell in self.diagram.findall(f".//mxCell[@id='{n}']"):
                    geom = cell.find('mxGeometry')
                    if geom is not None:
                        geom.set('x', str(x))
                        geom.set('y', str(y))
                y += height + y_spacing

    def execute(self):
        '''
        Main execution method to create the draw.io diagram
        '''
        # Reset tracking structures
        self.used_ids.clear()
        self.existing_slots.clear()
        self.node_positions.clear()
        self.slot_positions.clear()
        self.node_name_to_id.clear()
        self.next_x = 30
        self.next_y = 30
        self.current_row_nodes = 0
        
        self.create_mxfile()
        self.create_diagram()
        
        # Create nodes first
        # - Cache graph path -> node pairs for grouping later
        node_ids = []
        graph_info = []
        for graph_path in self.graphDictionary:
            print(f'Scan path:', graph_path)
            for item in self.graphDictionary[graph_path]:
                node_path = item[0]
                # Prepend graph path if was not in name
                # to give a full path
                if graph_path and graph_path not in node_path:
                    node_path = graph_path + '/' + node_path
                node_id = self.create_node_instance(node_path, item)
                node_ids.append((node_id))

                # Cache path, node id pair for grouping
                graph_info.append((graph_path, node_id))
        
        # Create definition nodes if any
        self.create_definition_nodes()    

        # Debug: Print node mappings
        self._debug_print(f"Created {len(self.node_name_to_id)} nodes:")
        for name, node_id in self.node_name_to_id.items():
            self._debug_print(f"  Path: {name} -> Id: {node_id}")    

        # Debug: Print slot mappings
        self._debug_print(f"\nCreated {len(self.existing_slots)} slots:")
        for key, slot_id in self.existing_slots.items():
            self._debug_print(f"  Path: {key[0]}/{key[1]}. Type: {key[2]} -> Id: {slot_id}")        
        
        # Create connections (edges)
        created_edges = 0
        for i, connection in enumerate(self.connections):
            self._debug_print(f"\n...Processing connection {i}: {connection}")
            edge_id = self.create_connection(connection, i)
            if edge_id:
                created_edges += 1
                self._debug_print(f"  Created edge: {edge_id}")
        
        self._debug_print(f"\nCreated {created_edges} connections out of {len(self.connections)}")
        
        # Layout nodes 
        self.layout_nodes()

        # Create groups based on graph paths
        #self.create_groups(graph_info)

        return self.xml_root
    
    def export(self, filename):
        '''
        Export to draw.io XML file
        '''        
        xml_str = self.get_xml_string()        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(xml_str)
    
    def get_xml_string(self):
        '''
        Get the XML as a string
        '''
        if self.xml_root is None:
            raise ValueError("XML root not created. Call execute() first.")

        xml_str = ET.tostring(self.xml_root, encoding='unicode')
        dom = minidom.parseString(xml_str)
        return dom.toprettyxml(indent='  ')



