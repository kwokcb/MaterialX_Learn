
import MaterialX as mx

class MtlxTraversal:
    @staticmethod
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

    @staticmethod
    def findEdge(edge, processedEdges):
        "Edge equality comparitor"
        for pe in processedEdges:
            # Note: the comparison (pe == edge) does not work 
            if (pe.getUpstreamElement() == edge.getUpstreamElement() and
                pe.getDownstreamElement() == edge.getDownstreamElement() and
                pe.getConnectingElement() == edge.getConnectingElement()):
                return True
        return False

    @staticmethod
    def updateGraphDictionaryPath(key, value, graphDictionary):
        """
        Add a parent / child to the GraphElement dictionary
        """
        if key in graphDictionary:
            graphDictionary[key].add(value)
        else:
            graphDictionary[key] = {value}


    @staticmethod
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
        MtlxTraversal.updateGraphDictionaryPath(key, value, graphDictionary)

    @staticmethod
    def updateGraphDictionary(edge, graphDictionary):
        """
        Add nodes from either end of the connection to a GraphElement dictionary
        """
        ends = [edge.getUpstreamElement(), edge.getDownstreamElement()]
        for end in ends:
            MtlxTraversal.updateGraphDictionaryItem(end, graphDictionary)

    @staticmethod
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
        outVal = indent + upstreamPathM + '[' + upstreamPath + ']' + connectionString + downstreamPathM + '[' + downstreamPath + ']'
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
                if not MtlxTraversal.findEdge(edge,processedEdges):
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
                MtlxMermaid.updateGraphDictionaryItem(interfaceInput, subgraphs)

        return outVal

    @staticmethod
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

                    MtlxMermaid.updateGraphDictionaryItem(upstreamOutput, subgraphs)

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

                    MtlxMermaid.updateGraphDictionaryPath(graphElementPath, upstreamOutputPath, subgraphs)

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
                if not MtlxTraversal.findEdge(edge,processedEdges):
                    processedEdges.add(edge)
                    MtlxTraversal.updateGraphDictionary(edge, subgraphs)

        # Get string output for each edge in Mermaid format
        edgeOutput = set()
        for edge in processedEdges:
            outVal = MtlxMermaid.emitMermaidEdge('    ', edge, subgraphs, edgeOutput)
            if outVal not in edgeOutput:
                edgeOutput.add(outVal)

        # Include interface input edges
        for edge in processedEdges:
            MtlxMermaid.emitInterfaceInputs('    ', edge, subgraphs, edgeOutput)            

        # Print graph header, edges, and sub-graphs
        outputGraph = []
        outputGraph.append('  graph %s;' % orientation)
        for outVal in edgeOutput:
            outputGraph.append(outVal)
        for line in MtlxMermaid.emitMermaidSubgraphs(subgraphs):
            outputGraph.append(line)

        return outputGraph

