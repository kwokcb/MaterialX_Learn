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
        #if not output_slots:
        #    output_slots.add('out')
        #if not input_slots:
        #    input_slots.add('in')

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
        #if conn_type == 'nodedef':
        #    edge_style = 'strokeColor=#4ecdc4;strokeWidth=3;'

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
        Create definition nodes.
        TODO: This creates a implementation node connected to a nodedef.
        Instead we want a reference from the graph created.
        '''
        if self.diagram is None:
            raise ValueError("Diagram not created. Call create_diagram() first.")

        value_nodes = {}
        
        fill_color = self.node_colors['nodedef'][0]
        font_color = self.node_colors['nodedef'][1]
        NODE_STYLE = f'fontColor={font_color};fillColor={fill_color};strokeColor=#fbc02d;html=1;whiteSpace=wrap;'

        for i, conn in enumerate(self.connections):
            if len(conn) > 4 and conn[4] in ['nodedef']:
                value_id = self.sanitize_id(f"value_{conn[0]}")
                self._debug_print('Creating value node for connection:' + str(conn))
                if value_id not in value_nodes:
                    # Create a simple value node (not a class instance)
                    x = self.next_x
                    y = self.next_y
                    
                    value_cell = ET.SubElement(self.diagram, 'mxCell')
                    value_cell.set('id', value_id)
                    value_cell.set('value', f"{conn[0]}")
                    value_cell.set('style', NODE_STYLE)
                    value_cell.set('vertex', '1')
                    value_cell.set('parent', '1')
                    
                    value_geom = ET.SubElement(value_cell, 'mxGeometry')
                    value_geom.set('x', str(x))
                    value_geom.set('y', str(y))
                    value_geom.set('width', str(self.class_width))
                    value_geom.set('height', str(self.header_height))
                    value_geom.set('as', 'geometry')
                    
                    value_nodes[value_id] = True
                    self.node_positions[value_id] = (x, y, 80, 40)
                    
                    # Store mapping
                    self.node_name_to_id[conn[0]] = value_id
                    
                    # For value nodes, we need to create an output slot
                    self.existing_slots[(value_id, 'out', 'output')] = value_id
                    
                    self.update_layout_position(80, 40)
        
        return value_nodes
    
    def group_nodes(self, group_name, node_ids, fill_color='#f4f1f7'):
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
        self._debug_print(f"\nGrouping nodes for group '{group_name}':")
        for node_id in node_ids:
            if node_id in self.node_positions:
                x, y, width, height = self.node_positions[node_id]
                self._debug_print(f"  Node '{node_id}': x={x}, y={y}, w={width}, h={height}")
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x + width)
                max_y = max(max_y, y + height)
            else:
                self._debug_print(f"  Node '{node_id}' not found in node_positions!")
        # Add padding
        padding = 30
        group_x = min_x - padding
        group_y = min_y - padding - 20  # Extra space for group label
        group_width = (max_x - min_x) + (padding * 2)
        group_height = (max_y - min_y) + (padding * 2)
        self._debug_print(f"  Computed group bounds: x={group_x}, y={group_y}, w={group_width}, h={group_height}")

        # Adjust all child node positions to be relative to the group origin
        for node_id in node_ids:
            if node_id in self.node_positions:
                abs_x, abs_y, width, height = self.node_positions[node_id]
                rel_x = abs_x - group_x
                rel_y = abs_y - group_y
                self.node_positions[node_id] = (rel_x, rel_y, width, height)
                # Update mxGeometry for this node
                for cell in self.diagram.findall(f".//mxCell[@id='{node_id}']"):
                    geom = cell.find('mxGeometry')
                    if geom is not None:
                        geom.set('x', str(rel_x))
                        geom.set('y', str(rel_y))
        
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
                self.group_nodes(graph_path, node_ids_in_group)

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
        self.next_x = 50
        self.next_y = 50
        self.current_row_nodes = 0
        
        self.create_mxfile()
        self.create_diagram()
        
        # Create nodes first
        # - Cache graph path -> node pairs for grouping later
        node_ids = []
        graph_info = []
        for graph_path in self.graphDictionary:
            #print(f'Scan path:', graph_path)
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
        print('\nCreating connections...')
        for i, connection in enumerate(self.connections):
            edge_id = self.create_connection(connection, i)
            self._debug_print(f"  Connection {i}: {connection}. Created edge: {edge_id if edge_id else 'Failed'}")
            if edge_id:
                created_edges += 1
        
        self._debug_print(f"Created {created_edges} connections out of {len(self.connections)}")
        
        # Layout nodes 
        print("\nPerforming node layout...")
        self.layout_nodes()

        # Create groups based on graph paths
        self.create_groups(graph_info)

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

import json
import os
from collections import defaultdict

class MxD3GraphExporter(MxBaseGraphExporter):
    '''
    Class to export a MaterialX graph to interactive D3.js HTML format
    '''
    def __init__(self, graphDictionary, connections):
        super().__init__(graphDictionary, connections)
        self.graph_data = {}
        self.node_width = 200
        self.node_header_height = 40
        self.slot_height = 25
        self.slot_margin = 4
        
        # Slot colors
        self.slot_colors = {
            'input': '#3498db',  # Blue
            'output': '#2ecc71',  # Green
            'default': '#95a5a6'  # Gray
        }
        background_color = "#969aee"
        text_color = "#000000"
        self.default_node_colors = [background_color, text_color]
        
    def _get_node_slots(self, node_path):
        """Extract input and output slots for a node from connections"""
        input_slots = {}
        output_slots = {}
        
        for conn in self.connections:
            src_path = conn[0]
            dst_path = conn[2]
            src_slot = conn[1] if conn[1] else 'out'
            dst_slot = conn[3] if conn[3] else 'in'
            
            # Check if this node is the source (has outputs)
            if src_path == node_path:
                output_slots[src_slot] = {
                    'name': src_slot,
                    'type': 'output',
                    'connections': []
                }
            
            # Check if this node is the target (has inputs)
            if dst_path == node_path:
                input_slots[dst_slot] = {
                    'name': dst_slot,
                    'type': 'input',
                    'connections': []
                }
        
        return list(input_slots.values()), list(output_slots.values())
    
    def _build_graph_data(self):
        """Build the complete graph data structure"""
        nodes = []
        links = []
        node_id_map = {}
        
        # First pass: create all nodes
        for graph_path in self.graphDictionary:
            for item in self.graphDictionary[graph_path]:
                node_path = item[0]
                
                # If node_path doesn't contain graph_path, prepend it
                if graph_path and not node_path.startswith(graph_path):
                    node_path = f"{graph_path}/{node_path}" if graph_path else node_path
                
                # Sanitize ID
                node_id = node_path.replace('/', '_').replace(' ', '_')
                
                # Get slot information
                input_slots, output_slots = self._get_node_slots(node_path)
                
                # Calculate node height based on slots
                max_slots = max(len(input_slots), len(output_slots))
                node_height = self.node_header_height + (max_slots * self.slot_height) + 20
                
                # Create node data
                color = self.node_colors.get(item[1], self.default_node_colors)[0]
                textColor = self.node_colors.get(item[1], self.default_node_colors)[1]
                print(f'Color for node {node_path} of type {item[1]}: {color}, textColor: {textColor}')

                node = {
                    'id': node_id,
                    'path': node_path,
                    'label': node_path.split('/')[-1],  # Base name
                    'type': item[1] if len(item) > 1 else 'node',
                    'value': item[3] if len(item) > 3 else '',
                    'graph': graph_path,
                    'slots': {
                        'inputs': input_slots,
                        'outputs': output_slots
                    },
                    'position': {
                        'x': 0,  # Will be set by layout
                        'y': 0,
                        'width': self.node_width,
                        'height': node_height
                    },
                    'color': color,
                    'textColor': textColor
                }
                
                nodes.append(node)
                node_id_map[node_path] = node_id
        
        # Second pass: create links between nodes
        for i, conn in enumerate(self.connections):
            src_path = conn[0]
            dst_path = conn[2]
            
            src_id = node_id_map.get(src_path)
            dst_id = node_id_map.get(dst_path)
            
            if src_id and dst_id:
                link = {
                    'id': f'link_{i}',
                    'source': src_id,
                    'target': dst_id,
                    'sourceSlot': conn[1] if conn[1] else 'out',
                    'targetSlot': conn[3] if conn[3] else 'in',
                    'type': conn[4] if len(conn) > 4 else 'connection',
                    'color': '#95a5a6',
                    'width': 2
                }
                
                # Style based on connection type
                if conn[4] == 'value':
                    link['color'] = '#e74c3c'
                    link['dashed'] = True
                elif conn[4] == 'nodedef':
                    link['color'] = '#9b59b6'
                    link['width'] = 3
                
                links.append(link)
        
        return {
            'nodes': nodes,
            'links': links,
            'metadata': {
                'totalNodes': len(nodes),
                'totalLinks': len(links),
                'nodeWidth': self.node_width,
                'nodeHeaderHeight': self.node_header_height,
                'slotHeight': self.slot_height
            }
        }
    
    def _apply_auto_layout(self, graph_data):
        """Apply automatic layout to nodes"""
        nodes = graph_data['nodes']
        links = graph_data['links']
        
        # Build adjacency lists
        successors = defaultdict(list)
        predecessors = defaultdict(list)
        
        for link in links:
            successors[link['source']].append(link['target'])
            predecessors[link['target']].append(link['source'])
        
        # Find nodes with no incoming edges (sources)
        source_nodes = [node for node in nodes if len(predecessors.get(node['id'], [])) == 0]
        
        # Simple grid layout
        cols = 4
        node_spacing_x = 250
        node_spacing_y = 200
        
        for i, node in enumerate(nodes):
            row = i // cols
            col = i % cols
            node['position']['x'] = 50 + col * node_spacing_x
            node['position']['y'] = 50 + row * node_spacing_y
        
        return graph_data
    
    def layout_nodes_hierarchical(self, x_spacing=80, y_spacing=40, start_x=50, start_y=50):
        """
        Layout nodes in columns based on connection dependencies (topological sort), using actual node sizes.
        Updates node['position']['x'] and node['position']['y'] for each node in self.graph_data['nodes'].
        """
        nodes = self.graph_data.get('nodes', [])
        links = self.graph_data.get('links', [])
        node_map = {n['id']: n for n in nodes}
        # Build adjacency and reverse adjacency
        from collections import defaultdict, deque
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        all_nodes = set(node_map.keys())
        for link in links:
            graph[link['source']].append(link['target'])
            reverse_graph[link['target']].append(link['source'])
            all_nodes.add(link['source'])
            all_nodes.add(link['target'])

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
        from collections import defaultdict
        columns = defaultdict(list)
        for n in topo_order:
            col = node_column.get(n, 0)
            columns[col].append(n)

        # Assign x/y positions using node sizes
        for col in sorted(columns):
            y = start_y
            for nid in columns[col]:
                node = node_map.get(nid)
                if not node:
                    continue
                width = node['position']['width']
                height = node['position']['height']
                node['position']['x'] = start_x + col * (width + x_spacing)
                node['position']['y'] = y
                y += height + y_spacing

        return self.graph_data

    def execute(self):
        """Generate the complete D3.js graph data"""
        self.graph_data = self._build_graph_data()
        self.graph_data = self.layout_nodes_hierarchical()
        # Alternatively, use simple auto layout
        #self.graph_data = self._apply_auto_layout(self.graph_data)
        return self.graph_data
    
    def export_json(self, filename):
        """Export graph data as JSON"""
        data = self.execute()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def export_html(self, filename, title="MaterialX Graph"):
        """Export complete interactive HTML visualization"""
        data = self.execute()
        
        html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <script src="https://unpkg.com/d3-drag@3"></script>
    <script src="https://unpkg.com/d3-zoom@3"></script>
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: #111111;
            color: #EEEEEE;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            min-height: 100vh;
            padding: 4px;
        }
        
        .header {
            padding: 20px;
            border-radius: 0px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            margin-bottom: 10px;
        }
        
        .stats {
            display: flex;
            gap: 20px;
            font-size: 14px;
        }
        
        .container {
            display: flex;
            gap: 20px;
            height: calc(100vh - 180px);
        }
        
        .graph-container {
            flex: 1;
            background: rgb(20, 40, 60);
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            position: relative;
        }
        
        #graph-svg {
            width: 100%;
            height: 100%;
            display: block;
        }
        
        .sidebar {
            width: 300px;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            overflow-y: auto;
        }
        
        .controls {
            margin-bottom: 20px;
        }
        
        .control-group {
            margin-bottom: 15px;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
        }
        
        select, input[type="range"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 0px;
            background: white;
        }
        
        .node-list {
            max-height: 400px;
            overflow-y: auto;
        }
        
        .node-item {
            padding: 10px;
            margin-bottom: 5px;
            border-radius: 0px;
            border-left: 4px solid #3498db;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .node-item:hover {
            /* background: #e3f2fd; */
            background: rgba(152, 152, 219, 0.1);
            transform: translateX(5px);
        }
        
        .node-type {
            font-size: 12px;
            margin-top: 2px;
        }
        
        .node-slots {
            font-size: 11px;
            margin-top: 5px;
        }
        
        /* Node styling */
        .node {
            cursor: move;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
        }
        
        .node-header {
            stroke-width: 2;
            rx: 5;
            ry: 5;
        }
        
        .node-body {
            fill: rgb(250, 250, 250);
            stroke: #bdc3c7;
            stroke-width: 1;
            rx: 5;
            ry: 5;
        }
        
        .node-title {
            fill: white;
            font-size: 14px;
            font-weight: bold;
            text-anchor: middle;
            dominant-baseline: middle;
            pointer-events: none;
        }
        
        .slot-row {
            cursor: pointer;
        }
        
        .input-slot {
            fill: #3498db;
        }
        
        .output-slot {
            fill: #2ecc71;
        }
        
        .slot-rect {
            rx: 3;
            ry: 3;
        }
        
        .slot-text {
            fill: white;
            font-size: 11px;
            text-anchor: middle;
            dominant-baseline: middle;
            pointer-events: none;
        }
        
        .port {
            fill: white;
            stroke: #7f8c8d;
            stroke-width: 2;
            r: 8;
            cursor: crosshair;
        }
        
        .link {
            fill: none;
            stroke: #95a5a6;
            stroke-width: 2;
            marker-end: url(#arrowhead);
        }
        
        .link:hover {
            stroke: #e74c3c;
            stroke-width: 3;
        }
        
        .dashed-link {
            stroke-dasharray: 5,5;
        }
        
        .tooltip {
            position: absolute;
            padding: 10px;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            border-radius: 5px;
            pointer-events: none;
            font-size: 12px;
            max-width: 300px;
            z-index: 1000;
            backdrop-filter: blur(5px);
        }
        
        .legend {
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            margin-bottom: 5px;
        }
        
        .legend-color {
            width: 20px;
            height: 10px;
            margin-right: 10px;
            border-radius: 2px;
        }
        
        /* Zoom controls */
        .zoom-controls {
            position: absolute;
            top: 20px;
            right: 20px;
            background: white;
            border-radius: 0px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 5px;
        }
        
        .zoom-btn {
            width: 30px;
            height: 30px;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 0px;
            margin: 2px;
            cursor: pointer;
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .zoom-btn:hover {
            background: #2980b9;
        }
        
        /* Highlight styles */
        .highlighted {
            stroke: #f39f12 !important;
            stroke-width: 3 !important;
        }
        
        .selected {
            filter: drop-shadow(0 0 10px rgba(243, 243, 60, 1.0));
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{TITLE}}</h1>
        <div class="stats">
            <div>Nodes: <span id="node-count">0</span></div>
            <div>Connections: <span id="link-count">0</span></div>
            <div>Last Updated: <span id="update-time">{{TIMESTAMP}}</span></div>
        </div>
    </div>
    
    <div class="container">
        <div class="graph-container">
            <div class="zoom-controls">
                <button class="zoom-btn" onclick="zoomIn()">+</button>
                <button class="zoom-btn" onclick="zoomOut()">-</button>
                <button class="zoom-btn" onclick="resetZoom()">↺</button>
            </div>
            <svg id="graph-svg"></svg>
            <div class="tooltip" id="tooltip"></div>
        </div>
        
        <div class="sidebar">
            <div class="controls">
                <div class="control-group">
                    <label for="layout">Layout:</label>
                    <select id="layout" onchange="changeLayout(this.value)">
                        <option value="force">Force-Directed</option>
                        <option value="grid">Grid</option>
                        <option value="hierarchical">Hierarchical</option>
                    </select>
                </div>
                
                <div class="control-group">
                    <label for="node-size">Node Size:</label>
                    <input type="range" id="node-size" min="100" max="300" value="200" oninput="updateNodeSize(this.value)">
                </div>
                
                <div class="control-group">
                    <label for="show-values">Show Values:</label>
                    <input type="checkbox" id="show-values" checked onchange="toggleValues(this.checked)">
                </div>
                
                <div class="control-group">
                    <label for="highlight-path">Highlight Path:</label>
                    <input type="text" id="highlight-path" placeholder="Enter node path..." oninput="highlightPath(this.value)">
                </div>
            </div>
            
            <div class="legend">
                <h3>Node Types</h3>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #09D;"></div>
                    <span>Input</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #0C0;"></div>
                    <span>Output</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #090;"></div>
                    <span>Surface Material</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #00C;"></div>
                    <span>Node Definition</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #500;"></div>
                    <span>Constant</span>
                </div>
            </div>
            
            <div class="node-list">
                <h3>Nodes ({{NODE_COUNT}})</h3>
                <div id="node-list-container"></div>
            </div>
        </div>
    </div>
    
    <script>
        // Graph data loaded from Python
        const graphData = {{GRAPH_DATA}};
        
        // Initialize variables
        let nodes = graphData.nodes;
        let links = graphData.links;
        let metadata = graphData.metadata;
        
        let selectedNode = null;
        let simulation = null;
        let zoom = null;
        
        // Update stats
        document.getElementById('node-count').textContent = metadata.totalNodes;
        document.getElementById('link-count').textContent = metadata.totalLinks;
        
        // Initialize visualization
        initGraph();
        
        function initGraph() {
            const svg = d3.select('#graph-svg');
            const width = svg.node().getBoundingClientRect().width;
            const height = svg.node().getBoundingClientRect().height;
            
            // Clear previous content
            svg.selectAll('*').remove();
            
            // Create main group
            const g = svg.append('g');
            
            // Add arrowhead marker
            svg.append('defs').append('marker')
                .attr('id', 'arrowhead')
                .attr('viewBox', '-0 -5 10 10')
                .attr('refX', 15)
                .attr('refY', 0)
                .attr('orient', 'auto')
                .attr('markerWidth', 6)
                .attr('markerHeight', 6)
                .append('path')
                .attr('d', 'M 0,-5 L 10,0 L 0,5')
                .attr('fill', '#95a5a6');
            
            // Create zoom behavior
            zoom = d3.zoom()
                .scaleExtent([0.1, 4])
                .on('zoom', (event) => {
                    g.attr('transform', event.transform);
                });
            
            svg.call(zoom);
            
            // Draw links first (so they appear behind nodes)
            const link = g.selectAll('.link')
                .data(links)
                .enter().append('path')
                .attr('class', d => `link ${d.type === 'value' ? 'dashed-link' : ''}`)
                .attr('stroke', d => d.color)
                .attr('stroke-width', d => d.width)
                .attr('id', d => d.id)
                .on('mouseover', function(event, d) {
                    d3.select(this).classed('highlighted', true);
                    showTooltip(event, `
                        <strong>Connection</strong><br>
                        Source: ${d.source}<br>
                        Target: ${d.target}<br>
                        Type: ${d.type}<br>
                        From: ${d.sourceSlot} → To: ${d.targetSlot}
                    `);
                })
                .on('mouseout', function() {
                    d3.select(this).classed('highlighted', false);
                    hideTooltip();
                });
            
            // Draw nodes
            const node = g.selectAll('.node')
                .data(nodes)
                .enter().append('g')
                .attr('class', 'node')
                .attr('id', d => d.id)
                .attr('transform', d => `translate(${d.position.x}, ${d.position.y})`)
                .call(d3.drag()
                    .on('start', dragStarted)
                    .on('drag', dragged)
                    .on('end', dragEnded))
                .on('click', function(event, d) {
                    selectNode(d);
                    event.stopPropagation();
                });
            
            // Draw node background
            node.append('rect')
                .attr('class', 'node-header')
                .attr('width', d => d.position.width)
                .attr('height', metadata.nodeHeaderHeight)
                .attr('fill', d => d.color)
                .attr('stroke', d => d.textColor);
            
            // Draw node title
            node.append('text')
                .attr('class', 'node-title')
                .attr('x', d => d.position.width / 2)
                .attr('y', metadata.nodeHeaderHeight / 2)
                .attr('fill', d => d.textColor)
                .text(d => {
                    let label = d.label;
                    if (d.value) label += ` = ${d.value}`;
                    return label;
                });
            
            // Draw node body
            node.append('rect')
                .attr('class', 'node-body')
                .attr('x', 0)
                .attr('y', metadata.nodeHeaderHeight)
                .attr('width', d => d.position.width)
                .attr('height', d => d.position.height - metadata.nodeHeaderHeight);
            
            // Draw slots
            nodes.forEach((nodeData, nodeIndex) => {
                const nodeGroup = d3.select(`#${nodeData.id}`);
                const inputSlots = nodeData.slots.inputs;
                const outputSlots = nodeData.slots.outputs;
                const maxSlots = Math.max(inputSlots.length, outputSlots.length);
                
                // Calculate starting position for slots
                const startY = metadata.nodeHeaderHeight + 10;
                
                // Draw input slots (left side)
                inputSlots.forEach((slot, i) => {
                    const y = startY + (i * metadata.slotHeight);
                    
                    const slotGroup = nodeGroup.append('g')
                        .attr('class', 'slot-row')
                        .attr('transform', `translate(0, ${y})`);
                    
                    // Input port
                    slotGroup.append('circle')
                        .attr('class', 'port input-port')
                        .attr('cx', 0)
                        .attr('cy', metadata.slotHeight / 2)
                        .attr('data-slot', slot.name)
                        .attr('data-node', nodeData.id)
                        .attr('data-type', 'input');
                    
                    // Slot rectangle
                    slotGroup.append('rect')
                        .attr('class', 'slot-rect input-slot')
                        .attr('x', 10)
                        .attr('width', 80)
                        .attr('height', metadata.slotHeight - 2);
                    
                    // Slot text
                    slotGroup.append('text')
                        .attr('class', 'slot-text')
                        .attr('x', 50)
                        .attr('y', metadata.slotHeight / 2)
                        .text(slot.name);
                });
                
                // Draw output slots (right side)
                outputSlots.forEach((slot, i) => {
                    const y = startY + (i * metadata.slotHeight);
                    
                    const slotGroup = nodeGroup.append('g')
                        .attr('class', 'slot-row')
                        .attr('transform', `translate(${nodeData.position.width}, ${y})`);
                    
                    // Output port
                    slotGroup.append('circle')
                        .attr('class', 'port output-port')
                        .attr('cx', 0)
                        .attr('cy', metadata.slotHeight / 2)
                        .attr('data-slot', slot.name)
                        .attr('data-node', nodeData.id)
                        .attr('data-type', 'output');
                    
                    // Slot rectangle
                    slotGroup.append('rect')
                        .attr('class', 'slot-rect output-slot')
                        .attr('x', -90)
                        .attr('width', 80)
                        .attr('height', metadata.slotHeight - 2);
                    
                    // Slot text
                    slotGroup.append('text')
                        .attr('class', 'slot-text')
                        .attr('x', -50)
                        .attr('y', metadata.slotHeight / 2)
                        .text(slot.name);
                });
            });
            
            // Update link paths after nodes are drawn
            updateLinkPaths();
            
            // Populate node list
            populateNodeList();
        }
        
    function updateLinkPaths() {
            d3.selectAll('.link').attr('d', function(d) {
                // Helper to get port absolute position from node/slot data
                function getPortPos(nodeId, slotName, type) {
                    const node = nodes.find(n => n.id === nodeId);
                    if (!node) return null;
                    const startY = metadata.nodeHeaderHeight + 10;
                    let slotIdx = -1;
                    let x = node.position.x;
                    let y = node.position.y;
                    if (type === 'input') {
                        slotIdx = node.slots.inputs.findIndex(s => s.name === slotName);
                        if (slotIdx === -1) return null;
                        x += 0; // input port at left edge
                        y += startY + slotIdx * metadata.slotHeight + metadata.slotHeight / 2;
                    } else if (type === 'output') {
                        slotIdx = node.slots.outputs.findIndex(s => s.name === slotName);
                        if (slotIdx === -1) return null;
                        x += node.position.width; // output port at right edge
                        y += startY + slotIdx * metadata.slotHeight + metadata.slotHeight / 2;
                    } else {
                        return null;
                    }
                    return { x, y };
                }

                const src = getPortPos(d.source, d.sourceSlot, 'output');
                const tgt = getPortPos(d.target, d.targetSlot, 'input');
                if (!src || !tgt) {
                    console.log('Missing port for link', d.source, d.target, d.sourceSlot, d.targetSlot);
                    return '';
                }
                // Draw a simple straight line (or a curve if you prefer)
                const midX = (src.x + tgt.x) / 2;
                return `M ${src.x},${src.y} C ${midX},${src.y} ${midX},${tgt.y} ${tgt.x},${tgt.y}`;
            });
        }

        function updateLinkPaths2() {
            d3.selectAll('.link').attr('d', function(d) {
                // Find the SVG port elements for the source output and target input slots
                const sourcePort = d3.select(`circle[data-node="${d.source}"][data-slot="${d.sourceSlot}"][data-type="output"]`);
                const targetPort = d3.select(`circle[data-node="${d.target}"][data-slot="${d.targetSlot}"][data-type="input"]`);

                if (sourcePort.empty() || targetPort.empty()) return '';

                // Get the absolute position of each port
                function getPortCenter(portSel) {
                    const nodeGroup = portSel.node().closest('g.node');
                    const nodeTransform = d3.select(nodeGroup).attr('transform');
                    const match = nodeTransform.match(/translate\(([^,]+),\s*([^)]+)\)/);
                    const nodeX = parseFloat(match[1]);
                    const nodeY = parseFloat(match[2]);
                    const cx = parseFloat(portSel.attr('cx'));
                    const cy = parseFloat(portSel.attr('cy'));
                    return { x: nodeX + cx, y: nodeY + cy };
                }

                const src = getPortCenter(sourcePort);
                const tgt = getPortCenter(targetPort);

                // Draw a simple straight line (or a curve if you prefer)
                const midX = (src.x + tgt.x) / 2;
                return `M ${src.x},${src.y} C ${midX},${src.y} ${midX},${tgt.y} ${tgt.x},${tgt.y}`;
            });
        }
        
        function dragStarted(event, d) {
            if (!event.active) simulation?.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }
        
        function dragged(event, d) {
            //d.fx = event.x;
            //d.fy = event.y;
            d.position.x = event.x;
            d.position.y = event.y;            
            d3.select(this).attr('transform', `translate(${d.position.x}, ${d.position.y})`);
            updateLinkPaths();
        }
        
        function dragEnded(event, d) {
            d3.select(this).attr('transform', `translate(${d.position.x}, ${d.position.y})`);
            if (!event.active) simulation?.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }
        
        function selectNode(node) {
            // Remove previous selection
            d3.selectAll('.node').classed('selected', false);
            
            // Highlight selected node
            d3.select(`#${node.id}`).classed('selected', true);
            selectedNode = node;
            
            // Update sidebar with node details
            document.getElementById('node-list-container').innerHTML = `
                <div class="node-item">
                    <strong>${node.label}</strong>
                    <div class="node-type">Type: ${node.type}</div>
                    <div class="node-type">Path: ${node.path}</div>
                    <div class="node-slots">
                        Inputs: ${node.slots.inputs.map(s => s.name).join(', ')}<br>
                        Outputs: ${node.slots.outputs.map(s => s.name).join(', ')}
                    </div>
                </div>
            `;
        }
        
        function showTooltip(event, content) {
            const tooltip = d3.select('#tooltip');
            tooltip.html(content)
                .style('left', (event.pageX + 10) + 'px')
                .style('top', (event.pageY - 10) + 'px')
                .style('opacity', 1);
        }
        
        function hideTooltip() {
            d3.select('#tooltip').style('opacity', 0);
        }
        
        function populateNodeList() {
            const container = document.getElementById('node-list-container');
            container.innerHTML = '';
            
            nodes.forEach(node => {
                const div = document.createElement('div');
                div.className = 'node-item';
                div.innerHTML = `
                    <strong>${node.label}</strong>
                    <div class="node-type">${node.type}</div>
                    <div class="node-slots">
                        ${node.slots.inputs.length} inputs, 
                        ${node.slots.outputs.length} outputs
                    </div>
                `;
                div.onclick = () => {
                    // Center view on node
                    const svg = document.getElementById('graph-svg');
                    const nodeEl = document.getElementById(node.id);
                    if (nodeEl) {
                        const bbox = nodeEl.getBBox();
                        const transform = d3.zoomTransform(svg);
                        const centerX = bbox.x + bbox.width / 2;
                        const centerY = bbox.y + bbox.height / 2;
                        
                        svg.transition()
                            .duration(750)
                            .call(zoom.transform, 
                                transform.translate(
                                    svg.clientWidth / 2 - centerX,
                                    svg.clientHeight / 2 - centerY
                                )
                            );
                    }
                    selectNode(node);
                };
                container.appendChild(div);
            });
        }
        
        // Control functions
        function changeLayout(layoutType) {
            // Implement different layouts
            if (layoutType === 'force') {
                // Force-directed layout
                simulation = d3.forceSimulation(nodes)
                    .force('link', d3.forceLink(links).id(d => d.id).distance(150))
                    .force('charge', d3.forceManyBody().strength(-300))
                    .force('center', d3.forceCenter(
                        document.getElementById('graph-svg').clientWidth / 2,
                        document.getElementById('graph-svg').clientHeight / 2
                    ))
                    .on('tick', () => {
                        d3.selectAll('.node')
                            .attr('transform', d => `translate(${d.x}, ${d.y})`);
                        updateLinkPaths();
                    });
            } else if (layoutType === 'grid') {
                // Grid layout
                const cols = Math.ceil(Math.sqrt(nodes.length));
                nodes.forEach((node, i) => {
                    const row = Math.floor(i / cols);
                    const col = i % cols;
                    node.x = 100 + col * 250;
                    node.y = 100 + row * 150;
                    node.fx = node.x;
                    node.fy = node.y;
                });
                updateLinkPaths();
            } else if (layoutType === 'hierarchical') {
                // Hierarchical (topological) layout
                // Build adjacency and reverse adjacency
                const graph = {};
                const reverseGraph = {};
                const allNodes = new Set(nodes.map(n => n.id));
                links.forEach(link => {
                    if (!graph[link.source]) graph[link.source] = [];
                    if (!reverseGraph[link.target]) reverseGraph[link.target] = [];
                    graph[link.source].push(link.target);
                    reverseGraph[link.target].push(link.source);
                    allNodes.add(link.source);
                    allNodes.add(link.target);
                });

                // Kahn's algorithm for topological sort
                const inDegree = {};
                allNodes.forEach(n => { inDegree[n] = 0; });
                Object.values(graph).forEach(dsts => {
                    dsts.forEach(dst => { inDegree[dst] += 1; });
                });
                const queue = [];
                allNodes.forEach(n => { if (inDegree[n] === 0) queue.push(n); });
                const topoOrder = [];
                while (queue.length > 0) {
                    const n = queue.shift();
                    topoOrder.push(n);
                    (graph[n] || []).forEach(m => {
                        inDegree[m] -= 1;
                        if (inDegree[m] === 0) queue.push(m);
                    });
                }

                // Assign columns by longest path from any input node
                const nodeColumn = {};
                function getColumn(n) {
                    if (!reverseGraph[n] || reverseGraph[n].length === 0) return 0;
                    if (nodeColumn[n] !== undefined) return nodeColumn[n];
                    let col = 1 + Math.max(...reverseGraph[n].map(getColumn));
                    nodeColumn[n] = col;
                    return col;
                }
                topoOrder.forEach(n => { getColumn(n); });

                // Group nodes by column
                const columns = {};
                topoOrder.forEach(n => {
                    const col = nodeColumn[n] || 0;
                    if (!columns[col]) columns[col] = [];
                    columns[col].push(n);
                });

                // Assign x/y positions using node sizes
                const x_spacing = 80, y_spacing = 40, start_x = 50, start_y = 50;
                Object.keys(columns).sort((a,b)=>a-b).forEach(col => {
                    let y = start_y;
                    columns[col].forEach(nid => {
                        const node = nodes.find(nn => nn.id === nid);
                        if (!node) return;
                        const width = node.position.width;
                        const height = node.position.height;
                        node.x = start_x + col * (width + x_spacing);
                        node.y = y;
                        node.fx = node.x;
                        node.fy = node.y;
                        y += height + y_spacing;
                    });
                });
                updateLinkPaths();
            }
        }
        
        function updateNodeSize(size) {
            metadata.nodeWidth = parseInt(size);
            nodes.forEach(node => {
                node.position.width = metadata.nodeWidth;
            });
            initGraph();
        }
        
        function toggleValues(show) {
            d3.selectAll('.node-title').text(d => {
                if (show && d.value) {
                    return `${d.label} = ${d.value}`;
                }
                return d.label;
            });
        }
        
        function highlightPath(path) {
            // Reset all highlights
            d3.selectAll('.node').classed('highlighted', false);
            
            if (!path) return;
            
            // Highlight nodes matching the path
            nodes.forEach(node => {
                if (node.path.toLowerCase().includes(path.toLowerCase())) {
                    d3.select(`#${node.id}`).classed('highlighted', true);
                }
            });
        }
        
        function zoomIn() {
            const svg = d3.select('#graph-svg');
            svg.transition().call(zoom.scaleBy, 1.2);
        }
        
        function zoomOut() {
            const svg = d3.select('#graph-svg');
            svg.transition().call(zoom.scaleBy, 0.8);
        }
        
        function resetZoom() {
            const svg = d3.select('#graph-svg');
            svg.transition().duration(750).call(zoom.transform, d3.zoomIdentity);
        }
        
        // Initialize with force layout
        //setTimeout(() => changeLayout('force'), 100);
    </script>
</body>
</html>'''
        
        # Format the timestamp
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Replace placeholders
        html_content = html_template\
            .replace('{{TITLE}}', title)\
            .replace('{{TIMESTAMP}}', timestamp)\
            .replace('{{NODE_COUNT}}', str(len(data['nodes'])))\
            .replace('{{GRAPH_DATA}}', json.dumps(data, indent=2))
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"HTML visualization exported to: {filename}")
        print(f"Open this file in your web browser to view the interactive graph.")
    
    def export_single_file(self, filename):
        """
        Export everything as a single HTML file for easy sharing
        This includes all CSS and JavaScript inline
        """
        self.export_html(filename)

