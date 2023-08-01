
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
    def addStyle(key, value, styleDictionary):
        if key in styleDictionary:
            styleDictionary[key].add(value)
        else:
            styleDictionary[key] = {value}

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
                MtlxTraversal.updateGraphDictionaryItem(interfaceInput, subgraphs)

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

                    MtlxTraversal.updateGraphDictionaryItem(upstreamOutput, subgraphs)

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

                    MtlxTraversal.updateGraphDictionaryPath(graphElementPath, upstreamOutputPath, subgraphs)

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
                if not MtlxTraversal.findEdge(edge,processedEdges):
                    processedEdges.add(edge)
                    MtlxTraversal.updateGraphDictionary(edge, subgraphs)

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

