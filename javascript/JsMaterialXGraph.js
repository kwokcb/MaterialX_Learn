//
// Class: MaterialXGraphBuilder
// - buildGraphDictionary(doc) : Build graph dictionary from MaterialX document
// - buildConnections(doc, graphElement, connections) : Build connections from MaterialX document
// - execute() : Execute the graph building process
// - exportToJSON(filename, inputFileName) : Export the graph to JSON file
// - importFromJSON(filename) : Import the graph from JSON file
// - getDictionary() : Get the graph dictionary
// - getConnections() : Get the connections
// - getParentGraph(elem) : Get the parent graph element
// - getDefaultOutput(node) : Get the default output of a node
// - appendPath(p1, p2) : Append path p2 to p1
// - updateGraphDictionaryPath(key, item, nodetype, type, value, graphDictionary) : Update graph dictionary path
// - updateGraphDictionaryItem(item, graphDictionary) : Update graph dictionary item
// - printGraphDictionary(graphDictionary) : Print the graph dictionary
// - setIncludeGraphs(graphs) : Set the include graphs
//
// Class: MermaidGraphExporter
// - setOrientation(orientation) : Set the orientation
// - setEmitCategory(emitCategory) : Set the emit category
// - setEmitType(emitType) : Set the emit type
// - execute() : Execute the graph building process
// - write(filename) : Write the graph to file
// - getGraph(wrap) : Get the graph
// - export() : Export the graph
//
class MaterialXGraphBuilder 
{
    constructor(doc) {
        this.doc = doc;
        this.graphDictionary = {};
        this.connections = [];
        this.includeGraphs = '';
    }

    setIncludeGraphs(graphs) {
        this.includeGraphs = graphs;
    }

    getDictionary() {
        return this.graphDictionary;
    }

    getConnections() {
        return this.connections;
    }

    updateGraphDictionaryPath(key, item, nodetype, type, value, graphDictionary) {
        if (key in graphDictionary) {
            graphDictionary[key].push([item, nodetype, type, value]);
        } else {
            graphDictionary[key] = [[item, nodetype, type, value]];
        }
    }

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

    getParentGraph(elem) {
        while (elem && !(elem instanceof mx.GraphElement)) {
            elem = elem.getParent();
        }
        return elem;
    }

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

    appendPath(p1, p2) {
        return p2 ? p1 + '/' + p2 : p1;
    }

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

    getJSON(inputFileName) {
        let data = {
            doc: 'Graph connections for: ' + inputFileName,
            //copyright: 'Copyright 2024, NanMu Consulting. kwokcb@gmail.com',
            graph: this.graphDictionary,
            connections: this.connections
        };
        return JSON.stringify(data, null, 4);
    }

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

    importFromJSON(filename) {
        let fs = require('fs');
        let data = JSON.parse(fs.readFileSync(filename, 'utf8'));
        this.graphDictionary = data.graph;
        this.connections = data.connections;
    }
}

///

class MermaidGraphExporter 
{
    constructor(graphDictionary, connections) {
        this.graphDictionary = graphDictionary;
        this.connections = connections;
        this.mermaid = [];
        this.orientation = 'LR';
        this.emitCategory = false;
        this.emitType = false;
    }

    setOrientation(orientation) {
        this.orientation = orientation;
    }

    setEmitCategory(emitCategory) {
        this.emitCategory = emitCategory;
    }

    setEmitType(emitType) {
        this.emitType = emitType;
    }


    sanitizeString(path)
    {
        path = path.replace('/default', '/default1');
        path = path.replace('/', '_');
        path = path.replace(' ', '_');
        return path;
    }

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

    write(filename) {
        let fs = require('fs');
        fs.writeFileSync(filename, this.export());
    }

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

function createMermaidGraphFromDocument(doc, opts) 
{
    let graphBuilder = new MaterialXGraphBuilder(doc);
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

    let exporter = new MermaidGraphExporter(
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

class MaterialXDefinitionCreator
{
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

    setOptions(new_options)
    {
        console.log('Set options:', new_options)
        if (new_options) {
            this.options = {};
            for (let key in new_options) {
                this.options[key] = new_options[key];
            }
        }        
    }
 
    execute()
    {
        if (!this.compoundGraph) {
            return null;
        }
        console.log('Options:', this.options)
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

        let definition = definitionDoc.addNodeDefFromGraph(nodeGraph, nodeDefName, category, version, defaultVersion, nodeGroup, nodegraphName)
        let functionalGraph = definitionDoc.getNodeGraph(nodegraphName);

        let docString = this.options[this.DOCUMENTATION]
        if (docString)
        {
            definition.setDocString(docString)
            functionalGraph.setDocString(docString)
        }

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
        
        return definitionDoc;
    }
}

function createMaterialXDefinitionFromNodeGraph(doc, nodeGraphName, options=null) 
{
    let graph = doc.getDescendant(nodeGraphName)
    console.log('Creating MaterialX definition from NodeGraph...', 
        graph.getName())
    let creator = new MaterialXDefinitionCreator(graph);
    if (options)
        creator.options = options;
    return creator.execute();
}