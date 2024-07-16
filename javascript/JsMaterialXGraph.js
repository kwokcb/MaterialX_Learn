//
// @class: MxGraphBuilder
// Class which will build node graph connectivity information from a MaterialX document.
//
class MxGraphBuilder 
{
    /**
     * @constructor
     * @param {Document} doc MaterialX document
     */
    constructor(doc) {
        this.doc = doc;
        this.graphDictionary = {};
        this.connections = [];
        this.includeGraphs = '';
    }

    /** 
     * Set graphs to include
     * @param {String} graphs Graphs to include
     * @return {void} 
     */
    setIncludeGraphs(graphs) {
        this.includeGraphs = graphs;
    }

    /**
     * Get the graph dictionary
     * @return {Object} Graph dictionary
     */
    getDictionary() {
        return this.graphDictionary;
    }

    /**
     * Get graph connections
     * @return {Array} Graph connections
     */
    getConnections() {
        return this.connections;
    }

    /**
     * Update the graph dictionary with a new item
     * @param {String} key Key for the dictionary
     * @param {String} item Item to add
     * @param {String} nodetype Node type
     * @param {String} type Type of the node
     * @param {String} value Value of the node
     * @param {Object} graphDictionary Graph dictionary
     * @return {void}
     */
    updateGraphDictionaryPath(key, item, nodetype, type, value, graphDictionary) {
        if (key in graphDictionary) {
            graphDictionary[key].push([item, nodetype, type, value]);
        } else {
            graphDictionary[key] = [[item, nodetype, type, value]];
        }
    }

    /** 
     * Update the graph dictionary with a new item
     * @param {Object} item Item to add
     * @param {Object} graphDictionary Graph dictionary
     * @return {void}
     */
    updateGraphDictionaryItem(item, graphDictionary) {
        if (!item) return;

        let parentElem = item.getParent();
        if (!parentElem || !(parentElem instanceof mx.GraphElement)) return;

        let key = parentElem.getNamePath();
        let value = item.getNamePath();
        let itemType = item.getType();
        let itemCategory = item.getCategory();
        let itemValue = '';

        if (item instanceof mx.Node) {
            let inputs = item.getInputs();
            if (inputs.length === 1) {
                itemValue = inputs[0].getValueString();
            }
        } else if (item instanceof mx.Input) {
            itemValue = item.getValueString();
        }

        this.updateGraphDictionaryPath(key, value, itemCategory, itemType, itemValue, graphDictionary);
    }

    /**
     * Print the graph dictionary
     * @param {Object} graphDictionary Graph dictionary
     * @return {void}
     */
    printGraphDictionary(graphDictionary) {
        for (let graphPath in graphDictionary) {
            if (graphPath === '') {
                console.log('Root Document:');
            } else {
                console.log(graphPath + ':');
            }

            let filter = 'input';
            for (let item of graphDictionary[graphPath]) {
                if (item[1] !== filter) continue;
                console.log('- ', item);
            }

            filter = 'output';
            for (let item of graphDictionary[graphPath]) {
                if (item[1] !== filter) continue;
                console.log('- ', item);
            }

            filter = ['output', 'input'];
            for (let item of graphDictionary[graphPath]) {
                if (!filter.includes(item[1])) {
                    console.log('- ', item);
                }
            }
        }
    }

    /** 
     * Get the parent graph of an element
     * @param {Object} elem Element to check
     * @return {Object} Parent graph
     */
    getParentGraph(elem) {
        while (elem && !(elem instanceof mx.GraphElement)) {
            elem = elem.getParent();
        }
        return elem;
    }

    /** 
     * Get the default output of a node
     * @param {Object} node Node to check
     * @return {String} Default output
     */
    getDefaultOutput(node) {
        if (!node) return '';

        let defaultOutput = null;
        if (node instanceof mx.Node) {
            let nodedef = node.getNodeDef();
            if (nodedef) {
                defaultOutput = nodedef.getActiveOutputs()[0];
            } else {
                console.log('Cannot find nodedef for node:', node.getNamePath());
            }
        } else if (node instanceof mx.NodeGraph) {
            defaultOutput = node.getOutputs()[0];
        }

        return defaultOutput ? defaultOutput.getName() : '';
    }

    /** 
     * Append two paths together
     * @param {String} p1 Path 1
     * @param {String} p2 Path 2
     * @return {String} Appended path
     */
    appendPath(p1, p2) {
        return p2 ? p1 + '/' + p2 : p1;
    }

    /**
     * Store a port connection
     * @param {Object} doc Document
     * @param {String} portPath Path of the port
     * @param {Array} connections Set of connections
     * @param {Boolean} portIsNode Port is a node
     * @return {void}
     */
    buildPortConnection(doc, portPath, connections, portIsNode) {
        let root = doc.getDocument();
        let port = root.getDescendant(portPath);
        if (!port) {
            console.log('Element not found:', portPath);
            return;
        }
    
        if (!(port instanceof mx.Input) && !(port instanceof mx.Output)) {
            console.log('Element is not an input or output');
            return;
        }
    
        let parent = port.getParent();
        let parentPath = parent.getNamePath();
        let parentGraph = this.getParentGraph(port);
    
        if ((port instanceof mx.Input) && (parent instanceof mx.NodeGraph)) {
            parentGraph = parentGraph.getParent();
        }
    
        if (!parentGraph) {
            console.log('Cannot find parent graph of port', port);
            //return;
        }
        let parentGraphPath = parentGraph.getNamePath();
    
        let outputName = port.getOutputString();
    
        let destNode = portIsNode ? portPath : parentPath;
        let destPort = portIsNode ? '' : port.getName();
    
        let nodename = port.getAttribute('nodename');
        if (nodename) {
            let result;
            if (!parentGraphPath) {
                result = [this.appendPath(nodename, ''), outputName, destNode, destPort, 'nodename'];
            } else {
                result = [this.appendPath(parentGraphPath, nodename), outputName, destNode, destPort, 'nodename'];
            }
            connections.push(result);
            return;
        }
    
        let nodegraph = port.getNodeGraphString();
        if (nodegraph) {
            if (!outputName) {
                outputName = this.getDefaultOutput(parentGraph.getChild(nodegraph));
            }
            let result;
            if (!parentGraphPath) {
                result = [this.appendPath(nodegraph, outputName), '', destNode, destPort, 'nodename'];
            } else {
                result = [this.appendPath(parentGraphPath, nodegraph), outputName, destNode, destPort, 'nodegraph'];
            }
            connections.push(result);
            return;
        }
    
        let interfaceName = port.getInterfaceName();
        if (interfaceName) {
            let result;
            if (!parentGraphPath) {
                if (!outputName) {
                    outputName = this.getDefaultOutput(parentGraph.getChild(interfaceName));
                }
                result = [this.appendPath(interfaceName, outputName), '', destNode, destPort, 'nodename'];
            } else {
                let outputName = '';
                let itemValue = '';
                if (destNode === parentGraphPath + '/' + interfaceName) {
                    let dictItem = this.graphDictionary[parentGraphPath];
                    if (dictItem) {
                        let found = false;
                        for (let item of dictItem) {
                            if (item[0] === parentGraphPath + '/' + interfaceName) {
                                found = true;
                                break;
                            }
                        }
                        if (found) {
                            console.log('Warning: Rename duplicate interface:', parentGraphPath + '/' + interfaceName + ':in');
                            interfaceName = interfaceName + ':in';
                        }
                    }
                }
    
                let found = false;
                let dictItem = this.graphDictionary[parentGraphPath];
                if (dictItem) {
                    for (let item of dictItem) {
                        if (item[0] === parentGraphPath + '/' + interfaceName) {
                            found = true;
                            break;
                        }
                    }
                }
    
                if (!found) {
                    this.updateGraphDictionaryPath(parentGraphPath, parentGraphPath + '/' + interfaceName, 'input', port.getType(), itemValue, this.graphDictionary);
                }
                result = [this.appendPath(parentGraphPath, interfaceName), outputName, destNode, destPort, 'interfacename'];
            }
            connections.push(result);
            return;
        }
    
        if (outputName) {
            let result;
            if (!parentGraphPath) {
                result = [this.appendPath(outputName, ''), '', parentPath, port.getName(), 'nodename'];
            } else {
                result = [this.appendPath(parentGraphPath, outputName), '', parentPath, port.getName(), 'output'];
            }
            connections.push(result);
            return;
        }
    }    

    /** 
     * Build the connections between graph elements
     * @param {Object} doc Document
     * @param {Object} graphElement Graph element
     * @param {Array} connections Set of connections
     * @return {void}
    */
    buildConnections(doc, graphElement, connections) {
        let root = doc.getDocument();

        for (let elem of graphElement.getChildren()) {
            if (!elem.hasSourceUri()) {
                if (elem instanceof mx.Input) {
                    this.buildPortConnection(root, elem.getNamePath(), connections, true);
                } else if (elem instanceof mx.Output) {
                    this.buildPortConnection(root, elem.getNamePath(), connections, true);
                } else if (elem instanceof mx.Node) {
                    let nodeInputs = elem.getInputs();
                    for (let nodeInput of nodeInputs) {
                        this.buildPortConnection(root, nodeInput.getNamePath(), connections, false);
                    }
                } else if (elem instanceof mx.NodeGraph) {
                    let nodedef = elem.getNodeDef();
                    if (nodedef) {
                        connections.push([elem.getNamePath(), '', nodedef.getName(), '', 'nodedef']);
                    }
                    let visited = new Set();
                    let path = elem.getNamePath();
                    if (!visited.has(path)) {
                        visited.add(path);
                        this.buildConnections(root, elem, connections);
                    }
                }
            }
        }
    }

    /**
     * Build the graph dictionary
     * @param {Object} doc Document
     * @return {Object} Graph dictionary
     */
    buildGraphDictionary(doc) {
        let graphDictionary = {};
        let root = doc.getDocument();
        let skipped = [];

        for (let elem of doc.getChildren()) {
            if (elem.hasSourceUri()) {
                skipped.push(elem.getNamePath());
            } else {
                if ((elem instanceof mx.Input) || (elem instanceof mx.Output) || (elem instanceof mx.Node)) {
                    //console.log('Scan element:', elem.getNamePath(), elem.getCategory(), mx.NodeGraph);
                    this.updateGraphDictionaryItem(elem, graphDictionary);
                } else if (elem instanceof mx.NodeGraph) {
                    //console.log('Scan graph:', elem.getNamePath(), elem.getCategory(), mx.NodeGraph);
                    if (elem.getAttribute('nodedef')) {
                        let nodeDef = elem.getAttribute('nodedef');
                        nodeDef = root.getDescendant(nodeDef);
                        if (nodeDef) {
                            for (let nodeDefInput of nodeDef.getInputs()) {
                                if (elem.getChild("def_" + nodeDefInput.getName())) {
                                    continue;
                                }
                                let newInput = elem.addInput("def_" + nodeDefInput.getName(), nodeDefInput.getType());
                                newInput.copyContentFrom(nodeDefInput);
                            }
                        }
                    }

                    for (let node of elem.getInputs()) {
                        this.updateGraphDictionaryItem(node, graphDictionary);
                    }
                    for (let node of elem.getOutputs()) {
                        this.updateGraphDictionaryItem(node, graphDictionary);
                    }
                    for (let node of elem.getNodes()) {
                        this.updateGraphDictionaryItem(node, graphDictionary);
                    }
                    for (let node of elem.getTokens()) {
                        this.updateGraphDictionaryItem(node, graphDictionary);
                    }
                } else if ((elem instanceof mx.NodeDef) || (elem instanceof mx.Token)) {
                    this.updateGraphDictionaryItem(elem, graphDictionary);
                }
            }
        }

        return graphDictionary;
    }

    /**
     * Build the graph information
     * @return {void}
     */
    execute() {
        this.connections = [];
        this.graphDictionary = {};

        let graphElement = this.doc;
        if (this.includeGraphs) {
            let graph = this.includeGraphs;
            graphElement = this.doc.getDescendant(graph);
            if (graphElement) {
                graphElement.setSourceUri('');
                console.log('Scan graph:', graphElement.getNamePath());
            } else {
                console.log('Graph not found:', graph);
            }
        }

        this.graphDictionary = this.buildGraphDictionary(graphElement);
        this.buildConnections(this.doc, graphElement, this.connections);
    }

    /** 
     * Get the JSON representation of the graph information
     * @param {String} inputFileName Input file name
     * @return {String} JSON string
     */
    getJSON(inputFileName) {
        let data = {
            doc: 'Graph connections for: ' + inputFileName,
            //copyright: 'Copyright 2024, NanMu Consulting. kwokcb@gmail.com',
            graph: this.graphDictionary,
            connections: this.connections
        };
        return JSON.stringify(data, null, 4);
    }

    /** 
     * Export the graph information to a JSON file
     * @param {String} filename Output file name
     * @param {String} inputFileName Input file name
     * @return {void}
     */
    exportToJSON(filename, inputFileName) {
        let data = {
            doc: 'Graph connections for: ' + inputFileName,
            //copyright: 'Copyright 2024, NanMu Consulting. kwokcb@gmail.com',
            graph: this.graphDictionary,
            connections: this.connections
        };

        //let fs = require('fs');
        //fs.writeFileSync(filename, JSON.stringify(data, null, 2));

        let dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(data, null, 2));
        let downloadAnchorNode = document.createElement('a');
        downloadAnchorNode.setAttribute("href", dataStr);
        downloadAnchorNode.setAttribute("download", filename);
        document.body.appendChild(downloadAnchorNode); // required for firefox
        downloadAnchorNode.click();
        downloadAnchorNode.remove();
    }

    /** 
     * Import the graph information from a JSON file
     * @param {String} filename Input file name
     * @return {void}
     */
    importFromJSON(filename) {
        let fs = require('fs');
        let data = JSON.parse(fs.readFileSync(filename, 'utf8'));
        this.graphDictionary = data.graph;
        this.connections = data.connections;
    }
}

/**
 * @class: MxMermaidGraphExporter
 * Class which will export a graph to Mermaid format
 */
class MxMermaidGraphExporter 
{
    /** 
     * @constructor
     * @param {Object} graphDictionary Set of graph elements organized by node graph
     * @param {Array} connections Set of connections between graph elements
     * @return {void}
     */
    constructor(graphDictionary, connections) {
        this.graphDictionary = graphDictionary;
        this.connections = connections;
        this.mermaid = [];
        this.orientation = 'LR';
        this.emitCategory = false;
        this.emitType = false;
    }

    /** 
     * Set the orientation of the graph
     * @param {String} orientation
     * @return {void}
     */
    setOrientation(orientation) {
        this.orientation = orientation;
    }

    /**
     * Set the emit the category versus the node name
     * @param {Boolean} emitCategory
     * @return {void}
     */
    setEmitCategory(emitCategory) {
        this.emitCategory = emitCategory;
    }

    /**
     * Emit the type of each node in the graph
     * @param {Boolean} emitType
     * @return {void}
     */
    setEmitType(emitType) {
        this.emitType = emitType;
    }

    /**
     * Sanitize the a node path to be safe to use with Mermaid
     * @param {String} path Original path
     * @return {String} sanitized path
     */
    sanitizeString(path)
    {
        path = path.replace('/default', '/default1');
        path = path.replace('/', '_');
        path = path.replace(' ', '_');
        return path;
    }

    /** 
     * Build the graph
     * 
     * Scans the graph dictionary to create the list of nodes per graph and
     * then scans the connections to create the list of connections between nodes.
     * Specific shapes and colours are assigned for different node types.
     * 
     * @return {Array} Mermaid graph
     */
    execute() {
        let mermaid = [];
        mermaid.push(`graph ${this.orientation}`);
        
        for (let graphPath in this.graphDictionary) {
            let isSubgraph = graphPath !== '';
            if (isSubgraph) {
                mermaid.push(`    subgraph ${graphPath}`);
            }
            
            for (let item of this.graphDictionary[graphPath]) {
                let path = item[0];
                let label = path.split('/').pop();
                // Sanitize the path name
                path = this.sanitizeString(path)
                
                if (this.emitCategory) {
                    label = item[1];
                }
                
                if (this.emitType) {
                    label += `:${item[2]}`;
                }
                
                if (item[3]) {
                    label += `:${item[3]}`;
                }
                
                if (['input', 'output'].includes(item[1])) {
                    mermaid.push(`    ${path}([${label}])`);
                    mermaid.push(`    style ${path}  fill:#09D, color:#FFF`);
                } else if (item[1] === 'surfacematerial') {
                    mermaid.push(`    ${path}([${label}])`);
                    mermaid.push(`    style ${path}   fill:#090, color:#FFF`);
                } else if (item[1] === 'nodedef') {
                    mermaid.push(`    ${path}[[${label}]]`);
                    //mermaid.push(`    style ${path}  fill:#02F, color:#FFF`);
                } else if (['ifequal', 'ifgreatereq', 'switch'].includes(item[1])) {
                    mermaid.push(`    ${path}{${label}}`);
                    mermaid.push(`    style ${path}   fill:#C72, color:#FFF`);
                } else if (item[1] === 'token') {
                    mermaid.push(`    ${path}{{${label}}}`);
                    mermaid.push(`    style ${path}  fill:#222, color:#FFF`);
                } else if (item[1] === 'constant') {
                    mermaid.push(`    ${path}([${label}])`);
                    mermaid.push(`    style ${path}  fill:#888, color:#000`);
                } else {
                    mermaid.push(`    ${path}[${label}]`);
                }
            }
            
            if (isSubgraph) {
                mermaid.push('    end');
            }
        }
        
        this.mermaid = mermaid;
        
        for (let connection of this.connections) 
        {
            // Sanitize path names
            connection[0] = this.sanitizeString(connection[0])
            connection[2] = this.sanitizeString(connection[2])

            let source = connection[0];
            let dest = connection[2];
            let edge = '';

            if (connection[1].length > 0) {
                if (connection[3].length > 0) {
                    edge = `${connection[1]}-->${connection[3]}`;
                } else {
                    edge = connection[1];
                }
            } else {
                edge = connection[3];
            }

            let connectString = '';

            if (connection[4] === 'value') {
                let sourceNode = source.split('/').pop();
                connectString = edge.length > 0 
                    ? `    ${sourceNode}["${source}"] --${edge}--> ${dest}`
                    : `    ${sourceNode}["${source}"] --> ${dest}`;
            } else {
                connectString = edge.length > 0 
                    ? `    ${source} --"${edge}"--> ${dest}`
                    : `    ${source} --> ${dest}`;
            }

            mermaid.push(connectString);
        }

        return mermaid;
    }

    /**
     * Write the graph to a file
     * @param {String} filename
     * @return {void}
     */
    write(filename) {
        let fs = require('fs');
        fs.writeFileSync(filename, this.export());
    }

    /**
     * Get the graph wrapped in a code block if desired
     * @param {Boolean} wrap Wrap the graph in a Markdown code block
     */
    getGraph(wrap = true) {
        let result = wrap 
            ? '```mermaid\n' + this.mermaid.join('\n') + '\n```'
            : this.mermaid.join('\n');

        result = result.replace('/default', '/default1');
        return result;
    }

    export() {
        return this.getGraph();
    }
}

/** 
 * Create a Mermaid graph from a MaterialX document
 * @param {Document} doc MaterialX document
 * @param {Object} opts Write options. This includes:
 * - saveJSON: Save the graph to JSON file
 * - inputFileName: Input file name
 * - orientation: Orientation of the graph
 * - emitCategory: Emit the category of the node
 * - emitType: Emit the type of the node
 * - graphs: Write sub graphs
 * @return {Array} Mermaid graph and JSON string
 */
function createMermaidGraphFromDocument(doc, opts) 
{
    let graphBuilder = new MxGraphBuilder(doc);
    //graphBuilder.importFromJSON(filename);
    graphBuilder.setIncludeGraphs(opts.graphs)
    console.log('Creating graph from MaterialX document...')
    graphBuilder.execute()
    if (opts.saveJSON)
    {
        console.log('Exporting graph to JSON (graph.json)...')
        graphBuilder.exportToJSON('graph.json', opts.inputFileName)
    }
    jsonString = graphBuilder.getJSON(opts.inputFileName)

    //console.log('Dictionary\n', graphBuilder.getDictionary())
    //console.log('COnnetions\n', graphBuilder.getConnections())

    let exporter = new MxMermaidGraphExporter(
        graphBuilder.getDictionary(),
        graphBuilder.getConnections()
    );

    console.log('Creating Mermaid from graph...')
    exporter.setOrientation(opts.orientation);
    exporter.setEmitCategory(opts.emitCategory);
    exporter.setEmitType(opts.emitType);
    exporter.execute();
    
    result = exporter.getGraph(false)
    return [result, jsonString];
}

/**
 * @class: MxDefinitionCreator
 * Class which will create a MaterialX definition from a node graph
 */
class MxDefinitionCreator
{
    /** 
     * @constructor 
     */
    constructor(compoundGraph) {
        this.compoundGraph = compoundGraph;
        this.options = this.getDefaultOptions();

        this.DEFINITION_NAME = 'definitionName';
        this.NODEGROUP = 'nodeGroup';
        this.VERSION = 'version';
        this.DEFAULT_VERSION = 'defaultVersion';
        this.DEFINITION_PREFIX = 'definitionPrefix';
        this.NODEGRAPH_PREFIX = 'nodegraphPrefix';   
        this.DOCUMENTATION = 'documentation';     
    }

    /** 
     * Get the default options for definition creation
     * @return {Object} Default options
     */
    getDefaultOptions() {
        let options = {};
        options[this.DEFINITION_NAME] = '';
        options[this.VERSION] = '1.0';
        options[this.DEFAULT_VERSION] = true;
        options[this.NODEGROUP] = 'procedural';
        options[this.DEFINITION_PREFIX] = 'ND_';
        options[this.NODEGRAPH_PREFIX] = 'NG_';
        options[this.DOCUMENTATION] = '';
        return options;
    }

    /**
     * Set the options for definition creation
     * @param {Object} new_options Options to set
     * @return {void}
     */
    setOptions(new_options)
    {
        //console.log('Set options:', new_options)
        if (new_options) {
            this.options = {};
            for (let key in new_options) {
                this.options[key] = new_options[key];
            }
        }        
    }
 
    /** 
     * Create a new definition
     * @return {Document} MaterialX document with the definition, or null if no graph supplied
     */
    execute()
    {
        if (!this.compoundGraph) {
            return null;
        }
        //console.log('Options:', this.options)
        let nodeGraph = this.compoundGraph;

        let category = nodeGraph.getName();
        if (this.options['definitionName']) {
            category = this.options['definitionName'];
        }

        let identifier = category;
        if (this.options[this.VERSION])
            identifier = identifier + '_' + this.options['version'];

        let parameter_signature = '';
        let outputs = nodeGraph.getOutputs();
        for (let output of outputs) {
            let outputType = output.getType();
            parameter_signature = parameter_signature + '_' + outputType;
        }
        identifier = identifier + parameter_signature;
        identifier = mx.createValidName(identifier)

        let nodeDefName = this.options[this.DEFINITION_PREFIX] + identifier;
        let nodegraphName = this.options[this.NODEGRAPH_PREFIX] + identifier;
        let defaultVersion = this.options[this.DEFAULT_VERSION];
        let nodeGroup = this.options[this.NODEGROUP];
        let version = this.options[this.VERSION]

        let definitionDoc = mx.createDocument();

        // Note that the pre 1.39 equivalent was removed. 
        let definition = definitionDoc.addNodeDefFromGraph(nodeGraph, nodeDefName, category, nodegraphName)
        definition.setVersionString(version);
        definition.setDefaultVersion(defaultVersion);
        definition.setNodeGroup(nodeGroup); 
        let functionalGraph = definitionDoc.getNodeGraph(nodegraphName);

        let docString = this.options[this.DOCUMENTATION]
        if (docString)
        {
            definition.setDocString(docString)
            functionalGraph.setDocString(docString)
        }

        /*
        // Cleanup the result
        let filterAttributes = ['nodegraph', 'nodename', 'channels', 'interfacename', 'xpos', 'ypos']

        // Transfer input interface from the graph to the nodedef
        for (let input of functionalGraph.getInputs()) {
            let nodeDefInput = definition.addInput(input.getName(), input.getType())
            if (nodeDefInput) {
                nodeDefInput.copyContentFrom(input)
                for (let filterAttribute of filterAttributes) {
                    nodeDefInput.removeAttribute(filterAttribute);
                }
                nodeDefInput.setSourceUri('')
                input.setInterfaceName(nodeDefInput.getName())
            }
        }
        for (let input of functionalGraph.getInputs()) {
            functionalGraph.removeInput(input.getName())
        }

        for (let output of nodeGraph.getOutputs()) {
            let nodeDefOutput = definition.getOutput(output.getName())
            if (nodeDefOutput)
                definition.removeOutput(output.getName())
            definition.addOutput(output.getName(), output.getType())
            if (nodeDefOutput)
                nodeDefOutput.copyContentFrom(output)
            for (let filterAttribute in filterAttributes)
                nodeDefOutput.removeAttribute(filterAttribute)
            nodeDefOutput.setSourceUri('')
        }
        for (let graphChild of functionalGraph.getChildren()) {
            graphChild.removeAttribute('xpos');
            graphChild.removeAttribute('ypos');
        }      
        */
        return definitionDoc;
    }
}

/**
 * Utility to create a MaterialX definition from a node graph
 * @param {Document} doc MaterialX document
 * @param {String} nodeGraphName Name of the node graph
 * @param {Object} options Options for the definition creation. Default value is null.
 * @return {Document} MaterialX document with the definition
 */
function createMaterialXDefinitionFromNodeGraph(doc, nodeGraphName, options=null) 
{
    let graph = doc.getDescendant(nodeGraphName)
    console.log('Creating MaterialX definition from NodeGraph...', 
        graph.getName())
    let creator = new MxDefinitionCreator(graph);
    if (options)
        creator.options = options;
    return creator.execute();
}