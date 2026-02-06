'''
    Set of utilities to perform MaterialX graph editing

    - Find definition to create
    - Add node instance based on category/type, or based on definition name    
    - Add nodegraph instance
    - Add nodegraph output
    - Connect an output to another output. For connections to nodegraph interface outputs
    - Connect an output to an input. Supports all permutations of connecting a node / nodegraph to another node / nodegraph. 
    - Add interface input to a nodegraph
    - Connect an node input to a interface input on a nodegraph ("publish")
    - Remove connection between a node input to a interface input on a nodegraph ("unpublish")

    Methods grouped under a MtxlNodeGraph class

    Requires: MaterialX package
'''
import MaterialX as mx

class MtlxNodeGraph:
    '''
    MaterialX <nodegraph> utilities
    '''

    @staticmethod
    def getNodeDefinition(doc, category, desiredType):
        '''
        Find a node definition given a category and a type
        '''
        nodedefs = doc.getMatchingNodeDefs(category)
        foundNodeDef = None
        for nodedef in nodedefs:
            if nodedef.getType() == desiredType:
                foundNodeDef = nodedef
                break

        return foundNodeDef

    @staticmethod
    def addNode(parent, category, desiredType, name):
        '''
        Add a named node under a given parent given a category and a type
        '''
        newNode = None
        doc = parent.getDocument() 
        nodedef = MtlxNodeGraph.getNodeDefinition(doc, category, desiredType)
        if nodedef:
            childName = parent.createValidChildName(name)
            newNode = parent.addNodeInstance(nodedef, childName)

        return newNode
    
    @staticmethod
    def addNode(parent, definitionName, name):
        '''
        Utility to create a node under a given parent using a definition name and desired instance name
        '''
        newNode = None
        doc = parent.getDocument()
        nodedef = doc.getNodeDef(definitionName)
        if nodedef:
            childName = parent.createValidChildName(name)
            newNode = parent.addNodeInstance(nodedef, childName)
        return newNode 

    @staticmethod
    def addNodeGraph(parent, name):
        '''
        Add named nodegraph under parent
        '''
        childName = parent.createValidChildName(name)
        nodegraph = parent.addChildOfCategory('nodegraph', childName)
        return nodegraph

    @staticmethod
    def addNodeGraphOutput(parent, type, name='out'):
        '''
        Create an output with a unique name and proper type
        '''
        if not parent.isA(mx.NodeGraph):
            return None
        
        newOutput = None
        childName = parent.createValidChildName(name)
        newOutput = parent.addOutput(childName, type)
        return newOutput    

    @staticmethod
    def connectOutputToOutput(outputPort, upstream, upstreamOutputName):
        '''
        Utility to connect a downstream output to an upstream node / node output
        If the types differ then no connection is made
        '''
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

    @staticmethod
    def connectNodeToNode(inputNode, inputName, outputNode, outputName):
        '''
        Connect an input on one node to an output on another node. Existence and type checking are performed.
        Returns input port with connection set if succesful. Otherwise None is returned.
        '''
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
        elif len(outputName) > 0:
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
    
    @staticmethod
    def addInputInterface(name, typeString, parent):
        '''
        Add a type input interface. Will always create a new interface
        '''
        validName = parent.createValidChildName(name)
        typedefs = parent.getDocument().getTypeDefs()
        validType = False
        for t in typedefs:
            if typeString in t.getName():
                validType = True
                break

        if validType:
            parent.addInput(validName, typeString)
    
    @staticmethod
    def connectInterface(nodegraph, interfaceName, internalInput):
        '''
        Add an interface input to a nodegraph if it does not already exist. 
        Connect the interface to the internal input. Returns interface input
        '''
        if not nodegraph or not interfaceName or not internalInput:
            return None

        interfaceInput = nodegraph.getInput(interfaceName)

        # Create a new interface with the desired type
        if not interfaceInput:
            interfaceName = nodegraph.createValidChildName(interfaceName)    
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

    @staticmethod
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

    @staticmethod
    def renameNode(node : mx.Node, newName : str, updateReferences : bool = True):
        '''
        Rename a node and update downstream references if desired
        '''

        if not node or not newName:
            return
        if not (node.isA(mx.Node) or node.isA(mx.NodeGraph)):
            return 
        if node.getName() == newName:
            return

        parent = node.getParent()
        if not parent:
            return

        newName = parent.createValidChildName(newName)

        if updateReferences:
            downStreamPorts = node.getDownstreamPorts()
            if downStreamPorts:
                for port in downStreamPorts:
                    if (port.getAttribute('nodename')):
                        port.setNodeName(newName)
                        node.setName(newName)
                    elif (port.getAttribute('nodegraph')):
                        port.setAttribute('nodegraph', newName)
                        node.setName(newName)
                    elif (port.getAttribute('interfacename')):
                        port.setAttribute('interfacename', newName)
                        node.setName(newName)
        else:
            node.setName(newName)

    @staticmethod
    def unconnectInterface(nodegraph, interfaceName, removeInterface=True):
        '''
        Remove an interface input from a nodegraph
        '''
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
                    child.removeAttribute('interfacename')

        if removeInterface:
            nodegraph.removeChild(interfaceName)

    @staticmethod
    def connectToGraphInput(node, outputName, nodegraph, inputName, transferNodeInput):
        '''
        Connect an output on a node to an input on a nodegraph
        @param node The node to connect from
        @param outputName The name of the output on the node
        @param nodegraph The nodegraph to connect to
        @param inputName The name of the input on the nodegraph
        @param transferNodeInput If specified, the name of an input on the node to transfer the value from the graph input
        @return The input port on the nodegraph if successful, otherwise None
        '''

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

    @staticmethod
    def ungroup(doc: mx.Document, graph: mx.NodeGraph):
        '''        
        Flatten a MaterialX NodeGraph into its parent graph.
        @param doc The MaterialX document
        @param graph The NodeGraph to ungroup
        '''

        parent = graph.getParent()
        if not isinstance(parent, (mx.Document, mx.NodeGraph)):
            return

        node_map = {}
        
        nodegraph_name = graph.getName()
        doc = graph.getDocument()

        # Promote the nodes to parent
        # Also create a map from old to new nodes.
        for node in graph.getNodes():
            new_name = f'{nodegraph_name}_{node.getName()}'
            new_name = parent.createValidChildName(new_name)

            new_node = parent.addNode(
                node.getCategory(),
                new_name,
                node.getType()
            )
            new_node.copyContentFrom(node)
            print(f'Add maping of old: {node.getNamePath()} to new: {new_node.getNamePath()}')

            node_map[node.getName()] = new_node

        # Rewrite internal node inputs.
        # - Handle references in new node inputs to other internal nodes which have been remapped to new names
        # - Handle graph input connections (interfacename) by routingg any upstream node to the input, or just eliding the value
        for new_node in node_map.values():
            for new_input in new_node.getInputs():
                nodeattribute = new_input.getAttribute('nodename')
                if nodeattribute in node_map:
                    print(f'node connection match: {nodeattribute} in {[node.getName() for node in node_map.values()]}')
                    mapped_node = node_map[nodeattribute]
                    if mapped_node:
                        #old_node_name = old_node.getName()
                        mapped_attribute = mapped_node.getName()
                        new_input.setAttribute('nodename', mapped_attribute)
                        print(f'Rename {nodeattribute}, to node: {mapped_attribute} on input {new_input.getNamePath()}')

                nodeinterface = new_input.getAttribute('interfacename')
                graph_input = graph.getInput(nodeinterface)
                if graph_input:
                    upstream_node = graph_input.getConnectedNode()
                    if upstream_node:
                        new_input.setAttribute('nodename', upstream_node.getName())
                        new_input.removeAttribute('interfacename')
                        print(f'Connect input {new_input.getNamePath()} to upstream node: {upstream_node.getNamePath()} from graph input: {graph_input.getNamePath()}')
                    else:
                        new_input.setValue(graph_input.getValue())
                        new_input.removeAttribute('interfacename')
                        print(f'Set value on input {new_input.getNamePath()} from graph input: {graph_input.getNamePath()}')

        # Restore any downstream graph connections
        downstream_ports = graph.getDownstreamPorts()
        print(f'Graph downstream ports: {[port.getNamePath() for port in downstream_ports]}')
        old_graph_outputs = graph.getOutputs()
        if old_graph_outputs:
            for port in downstream_ports:
                port_node = port.getParent()
                port_output = port.getOutputString()
                if port_output:
                    src = graph.getOutput(port_output).getConnectedNode()
                else:
                    src = old_graph_outputs[0].getConnectedNode()
                if src:
                    new_src = node_map[src.getName()]
                    print(f'Found downstream port: {port.getNamePath()} connected to graph output source node: {new_src.getNamePath()}')
                    port.removeAttribute('nodegraph')
                    port.setAttribute('nodename', new_src.getName())

        # Remove existing graph
        parent.removeNodeGraph(graph.getName())

    @staticmethod
    def group(parent: mx.GraphElement, nodes: list[mx.Node], nodegraph_name: str) :
        '''
        Group nodes in a MaterialX Document into a NodeGraph.
        @param parent The parent graph element containing the nodes to group
        @param nodes The list of nodes to group
        @param nodegraph_name The name of the new NodeGraph        
        '''
        graph : mx.NodeGraph = parent.addChildOfCategory('nodegraph', nodegraph_name)

        # Copy nodes into the graph
        node_map = {}
        for node in nodes:
            new_node = graph.addNode(
                node.getCategory(),
                node.getName(),
                node.getType()
            )
            new_node.copyContentFrom(node)

            # Keep mapping from old to new node
            node_map[node.getName()] = new_node

        # Find nodes under parent not in node_map
        for parent_node in parent.getNodes():
            if parent_node.getName() not in node_map:
                print(f'Parent node {parent_node.getNamePath()} is external to the group')
                # check if parent inputs reference any of the nodes in the group
                for parent_input in parent_node.getInputs():
                    nodeattribute = parent_input.getAttribute('nodename')
                    nodeoutput = parent_input.getOutputString()
                    if nodeattribute in node_map:
                        print(f'  > Parent input {parent_input.getNamePath()} references internal node: {nodeattribute}')
                        internal_node = node_map[nodeattribute]
                        # Create an interface output on the graph. Reuse the same output if the same node is referenced multiple times
                        output_name = graph.createValidChildName('out_' + nodeattribute + (('_' + nodeoutput) if nodeoutput else ''))
                        graph_output = graph.getOutput(output_name)
                        if not graph_output:
                            graph_output = graph.addOutput(
                                output_name,
                                parent_input.getType()
                            )

                        # Connect the graph output to the upstream internal node (output)
                        graph_output.setAttribute('nodename', internal_node.getName())
                        if nodeoutput:
                            graph_output.setOutputString(nodeoutput)

                        # Connect the parent input to the graph output
                        parent_input.setAttribute('nodegraph', graph.getName())
                        parent_input.removeAttribute('nodename')
                        #if len(graph.getOutputs()) > 1:
                        parent_input.setOutputString(output_name)
                        print(f'    > Created graph output: {graph_output.getNamePath()} and connected to input: {parent_input.getNamePath()}')


        # Check if any inputs reference nodes not in the graph
        connection_types = ['nodename', 'nodegraph']
        for new_node in graph.getNodes():
            for new_input in new_node.getInputs():

                for conn_type in connection_types:
                    nodeattribute = new_input.getAttribute(conn_type)
                    if nodeattribute and nodeattribute not in node_map:
                        node_output = new_input.getOutputString()

                        print(f'Input {new_input.getNamePath()} references external node: {nodeattribute}')

                        # Create an interface input on the graph. Reuse the same input if the same node + output is referenced multiple times
                        new_input_name = graph.createValidChildName('in' + '_' + nodeattribute + (('_' + node_output) if node_output else ''))
                        graph_input = graph.getInput(new_input_name)
                        if not graph_input:
                            graph_input = graph.addInput(
                                new_input_name,
                                new_input.getType()
                            )
                            # Connect graph input to external node. Add output port connection if needed
                            graph_input.setAttribute('nodename', nodeattribute)
                            if node_output:
                                graph_input.setOutputString(node_output)

                        # Connect the internal node's input to the new interface input 
                        new_input.setAttribute('interfacename', graph_input.getName())
                        new_input.removeAttribute('nodename')
                        print(f'  > Created graph input: {graph_input.getNamePath()} and connected to input: {new_input.getNamePath()}')