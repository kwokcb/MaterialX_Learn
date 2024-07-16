
// Globals
var ne_mx = null;       // MaterialX module
var doc = null;         // Working document
var stdlib = null;      // Standard libraries
var customlibs = [];    // Custom definition loaded in by user
var customDocLibs = []; // Definitions loaded in as part of document
var graph = null;       // Current graph
var graphcanvas = null; // Current graph canvas

/**
 * @class MxGraphMonitor
 * 
 * This class provides a monitoring interface for the graph editor.
 * It will monitor the following changes to the graph: 
 * - Connection changed
 * - Node added
 * - Node removed
 * - Node renamed
 * - Node selected
 * - Node deselected
 * - Property changed
 * - Property info changed
 */
class MxGraphMonitor 
{
    constructor(name) 
    {
        this.name = name;
        this.debug = true;
        this.monitoring = true;
        this.renderer = null;

        /** 
         * Output a debug message to the console.
         * 
         * @param {string} text - The text to output.
         * @param {string} path - The path to output.
         * @returns {void}
         */
        this.debugMessage = function(text, path)
        {
            if (this.debug) {
                console.log(text + path);
            }
        }

        /** 
         * Get a '/' separated path.
         * 
         * @param {Node} node - The node to get the path for.
         * @param {string} parentGraph - The parent graph of the node.
         * @returns {string} The path of the node.
         */
        this.getPath = function(node, parentGraph) {

            let path = '';
            if (parentGraph.length > 0)
                path = path + parentGraph + '/'            
            path += node.title;
            return path;
        }

        /**
         * Callback for when a scene / document level change is made
         * 
         * @param {string} attribute - The attribute that changed.
         * @param {string} value - The new value of the attribute.
         * @param {string} prevValue - The previous value of the attribute.
         * @returns {void}
         */
        this.onDocumentChange = function(attribute, value, prevValue)
        {
            if (!this.monitoring)
            {
                return;
            }
    
            if (this.debug) {
                this.debugMessage('Monitor> Document attribute "' + attribute + '" changed from: ' + prevValue + ' to: ' + value, '');
            }
        }

        /** 
         * Callback for when a connection changes in the graph.
         * 
         * @param {Node} node - The node where the connection changed.
         * @param {string} parentGraph - The parent graph of the node.
         * @returns {void}
         */
        this.onConnectionChange = function(node, parentGraph)
        {
            if (!this.monitoring)
            {
                return;
            }

            if (this.debug) {
                this.debugMessage('Monitor> Connection change: ', this.getPath(node, parentGraph));
            }
        }

        /** 
        * Callback for connection to output. 
        * 
        * @param {number} slot - The slot that was connected.
        * @param {string} input_type - The type of the input.
        * @param {any} input - The input that was connected.
        * @param {Node} target_node - The target node of the connection.
        * @param {number} target_slot - The target slot of the connection.
        * @returns {void}
        */
        this.onConnectOutput = function(slot, input_type, input, target_node, target_slot, node) 
        {
            if (!this.monitoring)
            {
                return;
            }

            if (this.debug) {
                let targetPath = this.getPath(node, this.getParentPath(node));
                let targetOutput = node.outputs[slot].name;
                let sourcePath = this.getPath(target_node, this.getParentPath(target_node));
                let sourceInput = input.name;

                this.debugMessage('Monitor> Output connection change: ' +
                    targetPath + "[" + slot + "]." + targetOutput + ' to: ' +
                    sourcePath + "[" + target_slot + "]." + sourceInput + " (" + input_type + ")", "");
            }
        }

        /** 
         * Callback for connection to output.
         * 
         * @param {number} target_slot - The target slot that was connected.
         * @param {string} output_type - The type of the output.
         * @param {any} output - The output that was connected.
         * @param {Node} source - The source node of the connection.
         * @param {number} slot - The slot of the source node.
         * @returns {void}
         */
        this.onConnectInput = function(target_slot, output_type, output, source, slot, node) {

            if (!this.monitoring)
            {
                return;
            }

            // checker -> input
            if (this.debug) {
                let sourcePath = this.getPath(source, this.getParentPath(source));
                let sourceOutput = output.name;
                let targetPath = this.getPath(node, this.getParentPath(node));
                let targetInput = node.inputs[target_slot].name;

                this.debugMessage('Monitor> Input connection change: ' +
                    sourcePath + "[" + slot + "]." + sourceOutput + ' to: ' +
                    targetPath + "[" + target_slot + "]." + targetInput + " (" + output_type + ")", "");
            }    
        }           


        /** 
         * Callback for when a node is added to the graph.
         * 
         * @param {Node} node - The node that was added.
         * @param {string} parentGraph - The parent graph of the node.
         */
        this.onNodeAdded = function(node, parentGraph)
        {
            if (!this.monitoring)
            {
                return;
            }

            // Go through all inputs on the node and remove hidden attribute
            // Needed to allow cut-paste of nodes which were loaded in with
            // hidden inputs.
            /* for (let i = 0; i < node.inputs.length; i++) {
                let input = node.inputs[i];
                if (input.hidden) {
                    // Remove hidden attribute
                    delete input.hidden;
                }
            } */
    
            if (this.debug) {
                this.debugMessage('Monitor> Node added: ', this.getPath(node, parentGraph));
            }
        }

        /** 
         * Callback for when a node is removed from the graph.
         * 
         * @param {Node} node - The node that was removed.
         * @param {string} parentGraph - The parent graph of the node.
         * @returns {void}
         */
        this.onNodeRemoved = function(node, parentGraph)
        {
            if (!this.monitoring)
            {
                return;
            }
    
            if (this.debug) {
                this.debugMessage('Monitor> Node removed: ', this.getPath(node, parentGraph));
            }
        }

        /** 
         * Get the parent path of a node.
         * 
         * @param {Node} node - The node to get the parent path for.
         * @returns {string} The parent path of the node.
         */
        this.getParentPath = function(node)
        {
            let path = '';
            var is_subgraph = graphcanvas.graph._is_subgraph;
            if (is_subgraph) {
                path = graphcanvas.graph._subgraph_node.title + '/';
            }
            else
            {
                if (node.graph)
                {
                    is_subgraph = node.graph._is_subgraph;
                    if (is_subgraph) {
                        path = node.graph._subgraph_node.title + '/';
                    }                            
                }
            }
            return path;
        }

        /** 
         * Callback for when a node is renamed in the graph.
         * 
         * @param {Node} node - The node that was renamed.
         * @param {string} newName - The new name of the node.
         * @returns {void}
         */
        this.onNodeRenamed = function(node, newName)
        {
            if (!this.monitoring)
            {
                return;
            }    

            let parentPath = this.getParentPath(node);
            let path = parentPath + node.title;
            let newpath = parentPath + newName;
            if (this.debug) {
                this.debugMessage('Monitor> Node renamed: ', path + ' to: ' + newpath);
            }
        }

        /**
         * Callback for when a node is selected in the graph.
         * 
         * @param {Node} node - The node that was selected.
         * @param {string} parentGraph - The parent graph of the node.
         * @returns {void}
         */
        this.onNodeSelected = function(node, parentGraph)
        {
            if (!this.monitoring)
            {
                return;
            }
    
            if (this.debug) {
                this.debugMessage('Monitor> Node selected: ', this.getPath(node, parentGraph));
            }
        }

        /**
         * Callback for when a node is deselected in the graph.
         * 
         * @param {Node} node - The node that was deselected.
         * @param {string} parentGraph - The parent graph of the node.
         * @returns {void}
         */
        this.onNodeDeselected = function(node, parentGraph)
        {
            if (!this.monitoring)
            {
                return;
            }

            if (this.debug) {
                //this.debugMessage('-> Node unselected at path: ', this.getPath(node, parentGraph));
            }
        }

        /** 
         * Callback for when a property changes on a node in the graph.
         * 
         * @param {string} nodeName - The name of the node.
         * @param {string} propertyName - The name of the property that changed.
         * @param {string} newValue - The new value of the property.
         * @param {string} previousValue - The previous value of the property.
         * @param {Node} node - The node where the property changed.
         * @returns {void}
         */
        this.onPropertyChanged = function (nodeName, propertyName, newValue, previousValue, node)
        {
            if (!this.monitoring)
            {
                return;
            }
    
            let path = this.getParentPath(node) + nodeName;
            if (this.debug) {
                console.log('Monitor> Property changed:', path, '. Property: ' + propertyName + 
                '. Value: ' + newValue + '. Previous Value: ' + previousValue, '. Category:', node.nodedef_node);
            }
        }

        /** 
         * Callback for when a property info changes on a node in the graph.
         * 
         * @param {string} nodeName - The name of the node.
         * @param {string} propertyName - The name of the property that changed.
         * @param {string} propertyInfoName - The name of the property info that changed.
         * @param {string} newValue - The new value of the property info.
         * @param {string} previousValue - The previous value of the property info.
         * @param {Node} node - The node where the property info changed.
         * @returns {void}
         */
        this.onPropertyInfoChanged = function(nodeName, propertyName, propertyInfoName, newValue, previousValue, node)
        {
            if (!this.monitoring)
            {
                return;
            }
    
            let path = this.getParentPath(node) + nodeName;
            if (this.debug) {
                console.log('Monitor> Property Info changed:', path, '. Property: ' + propertyName + 
                    '. Property Info: ' + propertyInfoName +
                '. Value: ' + newValue + '. Previous Value: ' + previousValue, '. Category:', node.nodedef_node);
            }    
        }
    }

    /** 
     * Get the name of the monitor.
     * 
     * @returns {string} The name of the monitor.
     */
    getName()
    {
        return this.name;
    }

    /**
     * Set the renderer for the monitor.
     * 
     * @param {Renderer} theRenderer - The renderer to set.
     * @returns {void}
     */
    setRenderer(theRenderer)
    {
        this.renderer = theRenderer
    }

    /**
     * Set the monitoring state of the monitor.
     * 
     * @param {boolean} monitor - The monitoring state to set.
     * @returns {void}
     */
    setMonitoring(monitor)
    {
        this.monitoring = monitor;
    }

    /** 
     * Get the monitoring state of the monitor.
     * 
     * @returns {boolean} The monitoring state of the monitor.
     */
    getMonitoring()
    {
        return this.monitoring;
    }

    /** 
     * Set connection change callback.
     * 
     * @param {function} callback - The callback to set.
     * @returns {void}
     */
    setOnConnectionChange(callback)
    {
        if (callback)
        {
            this.onConnectionChange = callback;
        }
    }

    /** 
     * Set node added callback.
     * 
     * @param {function} callback - The callback to set.
     * @returns {void}
     */
    setOnNodeAdded(callback)
    {
        if (callback)
        {
            this.onNodeAdded = callback;
        }
    }

    /** 
     * Set node removed callback.
     * 
     * @param {function} callback - The callback to set.
     * @returns {void}
     */
    setOnNodeRemoved(callback)
    {
        if (callback)
        {
            this.onNodeRemoved = callback;
        }
    }   
    
    /**
     * Set node renamed callback.
     * 
     * @param {function} callback - The callback to set.
     * @returns {void}
     */
    setOnNodeRenamed(callback)
    {
        if (callback)
        {
            this.onNodeRenamed = callback;
        }
    }

    /** 
     * Set node selected callback.
     * 
     * @param {function} callback - The callback to set.
     * @returns {void}
     */
    setOnNodeSelected(callback)
    {
        if (callback)
        {
            this.onNodeSelected = callback;
        }
    }

    /** 
     * Set node deselected callback.
     * 
     * @param {function} callback - The callback to set.
     * @returns {void}
     */
    setOnNodeDeselected(callback)
    {
        if (callback)
        {
            this.onNodeDeselected = callback;            
        }
    }

    /** 
     * Set property changed callback.
     * 
     * @param {function} callback - The callback to set.
     * @returns {void}
     */
    setOnPropertyChanged(callback)
    {
        if (callback)
        {
            this.onPropertyChanged = callback;            
        }    
    }

    /** 
     * Core monitoring of graph changes.
     * 
     * @param {LiteGraph} theGraph - The graph to monitor.
     * @param {boolean} monitor - The monitoring state.
     */
    monitorGraph(theGraph, monitor) 
    {
        // Update monitor state
        this.monitoring = monitor;
    
        if (!theGraph)
            return;

        theGraph.onConnectionChange = null;
        theGraph.onNodeAdded = null;
        theGraph.onNodeRemoved = null;

        if (monitor) {

            console.log('> Monitor graph: ', graph.title? graph.title : 'ROOT')

            var that = this;

            theGraph.onConnectionChange = function (node) {
                let parentGraph = '';
                var is_subgraph = node.graph._is_subgraph;
                if (is_subgraph)
                    parentGraph = graphcanvas.graph._subgraph_node.title;
                that.onConnectionChange(node, parentGraph);

                var selected = graphcanvas.selected_nodes;
                for (var s in selected) {
                    //console.log('update selected node:', selected[s].title);
                    MxShadingGraphEditor.theEditor.updatePropertyPanel(selected[s]);
                    break;
                }
            }

            theGraph.onNodeAdded = function (node) {
                let parentGraph = '';

                if (node.type == 'graph/subgraph') {
                    // Use MaterialX naming for subgraphs

                    // Scan the subgraph for any nodes which are not in the node inputs list.
                    var node_subgraph = node.subgraph;
                    var node_graph = node.graph;
                    if (node_subgraph) {
                        //console.log('** Scan subgraph: ', node_subgraph)
                        for (var i in node_subgraph._nodes) {
                            let theNode = node_subgraph._nodes[i];
                            if (!node_graph.findNodeByTitle(theNode.title)) {
                                if (theNode.nodedef_node == 'input') {
                                    node.addInput(theNode.title, theNode.nodedef_type);
                                    //console.log('--> Promote input node to subgraph node.', theNode.title);
                                }
                                else if (theNode.nodedef_node == 'output') {
                                    //console.log('--> Promote output node to subgraph node.', theNode.title);
                                    node.addOutput(theNode.title, theNode.nodedef_type);
                                }
                            }
                        }
                    }
                }

                node.title = MxShadingGraphEditor.theEditor.handler.createValidName(node.title)
                node.setSize(node.computeSize());
                //console.log('-> Node Added:', node, '. Type:', node.type, '. Graph:', node.graph._2458graph);

                // Expose node as an input or output on the subgraph
                var is_subgraph = node.graph._is_subgraph;
                if (is_subgraph) {
                    parentGraph = graphcanvas.graph._subgraph_node.title;

                    if (node.nodedef_node == 'input') {
                        //console.log('Adding input node to subgraph.', node.title, node.graph);
                        node.graph.addInput(node.title, node.nodedef_type);
                    }
                    else if (node.nodedef_node == 'output') {
                        //console.log('Adding output node to subgraph.');
                        node.graph.addOutput(node.title, node.nodedef_type);
                    }
                }

                if (node.type == 'graph/subgraph') {
                    that.monitorGraph(node.subgraph, monitor);
                }

                that.onNodeAdded(node, parentGraph);
            }

            //console.log('Monitor graph remove:', theGraph.title);
            theGraph.onNodeRemoved = function (node) {

                let parentGraph = '';
                /* This is too late the graph reference has already been removed */
                var is_subgraph = graphcanvas.graph._is_subgraph;
                if (is_subgraph) {
                    parentGraph = graphcanvas.graph._subgraph_node.title;
                    if (node.nodedef_node == 'input') {
                        //console.log('Removing input node from subgraph.', parentGraph);
                        graphcanvas.graph.removeInput(node.title);
                    }
                    else if (node.nodedef_node == 'output') {
                        //console.log('Removing output node from subgraph.', parentGraph);
                        graphcanvas.graph.removeOutput(node.title);
                    }
                }

                that.onNodeRemoved(node, parentGraph);
            }

            for (var i in theGraph._nodes) {
                var node = theGraph._nodes[i];
                if (node.type == 'graph/subgraph') {
                    console.log('> Monitor subgraph:', node.title);
                    that.monitorGraph(node.subgraph, monitor);
                    node.onConnectInput = MxShadingGraphEditor.theEditor.onConnectInput;
                }
            }
        }            
    }
}


/**
 * @class MxGraphHandler
 * 
 * Base class for graph handlers. 
 */
class MxGraphHandler 
{
    constructor(id, extension) {
        // Identifier
        this.id = id;
        // Extension of format that this handler is associated with
        // Generally the same as the file extension (e.g. mtlx for MaterialX)
        this.extension = extension;
        // Editor
        this.editor = null;

        // Keep track of global color space and distance unit
        this.DEFAULT_COLOR_SPACE = 'lin_rec709';
        this.DEFAULT_DISTANCE_UNIT = 'meter';
        this.sourceColorSpace = this.DEFAULT_COLOR_SPACE;
        this.targetDistanceUnit = this.DEFAULT_DISTANCE_UNIT;
        this.colorSpaces = [];
        this.units = [];

        // List of additional converters that can convert to the format
        // that this handler can handle
        this.converters = [];
        
        // Graph monitoring instance
        this.monitor = null;
    }

    /** 
     * Add a converter to the handler.
     * 
     * @param {Converter} converter - The converter to add.
     * @returns {void}
     */
    addConverter(converter) {
        // Add to front of list
        this.converters.unshift(converter);
        //this.converters.push(converter);
    }

    /** 
     * Set the monitor for the handler.
     * 
     * @param {MxGraphMonitor} monitor - The monitor to set.
     * @returns {void}
     */
    setMonitor(monitor)
    {
        this.monitor = monitor;
    }
    
    /** 
     * Return if the handler can export to the given extension / format.
     * Will test any additional converters that have been added to the handler.
     * 
     * @param {string} extension - The extension to check.
     * @returns {boolean} True if the handler can export to the extension, false otherwise.
     */
    canExport(extension)
    {
        if (extension == 'mtlx')
        {
            return true;
        }
        if (this.getExporter(extension))
        {
            return true;
        }
        return false; 
    }

    /** 
     * Find the first exporter that can export to the given extension / format.
     * 
     * @param {string} extension - The extension to check.
     * @returns {Converter} The first converter that can export to the extension, or null if none found.
     */
    getExporter(extension='') {
        for (let converter of this.converters) {
            if (converter.exportType() == extension) {
                return converter;
            }
        }
        return null;
    }

    /** 
     * Return if the handler can import the given extension / format.
     * 
     * @param {string} extension - The extension to check.
     * @returns {boolean} True if the handler can import the extension, false otherwise.
     */
    canImport(extension)
    {
        if (extension == 'mtlx')
        {
            return true;
        }
        if (this.getImporter(extension))
        {
            return true;
        }
        return false;
    }

    /**
     * Find the first importer that can import the given extension / format.
     * 
     * @param {string} extension - The extension to check.
     * @returns {Converter} The first converter that can import the extension, or null if none found.
     */
    getImporter(extension='') {
        for (let converter of this.converters) {
            if (converter.importType() == extension) {
                return converter;
            }
        }
        return null;
    }

    /**
     * Set the color spaces used by the handler.
     * 
     * @param {Array} colorSpaces - The color spaces to set.
     * @returns {void} 
     */
    setColorSpaces(colorSpaces) {
        this.colorSpaces = colorSpaces;
    }

    /**
     * Get the color spaces used by the handler.
     * 
     * @returns {Array} The color spaces used by the handler.
     */
    getColorSpaces() {
        return this.colorSpaces;
    }

    /**
     * Set the units used by the handler.
     * 
     * @param {Array} units - The units to set.
     * @returns {void}
     */
    setUnits(units) {
        this.units = units;
    }

    /** 
     * Get the units used by the handler.
     * 
     * @returns {Array} The units used by the handler.
     */
    getUnits() {
        return this.units;
    }

    /** 
     * Set the source color space for the handler.
     * 
     * @param {string} colorSpace - The source color space to set.
     * @returns {void}
     */
    setSourceColorSpace(colorSpace) {
        let newSpace = this.DEFAULT_COLOR_SPACE;
        if (colorSpace && colorSpace.length > 0)        
            newSpace = colorSpace;

        if (this.monitor)
        {
            this.monitor.onDocumentChange('colorspace', colorSpace, this.sourceColorSpace);
        }
        this.sourceColorSpace = newSpace;
    }

    /**
     * Set the target distance unit for the handler.
     * 
     * @param {string} unit - The target distance unit to set.
     * @returns {void}
     */
    setTargetDistanceUnit(unit) {
        let newUnit = this.DEFAULT_DISTANCE_UNIT;
        if (unit && unit.length > 0)
            newUnit = unit;

        if (this.monitor)
        {
            this.monitor.onDocumentChange('distanceunit', newUnit, this.targetDistanceUnit);
        }
        this.targetDistanceUnit = newUnit;
        //console.log('Handler SET target distance unit:', this.targetDistanceUnit);
    }

    /**
     * Get the source color space for the handler.
     * 
     * @returns {string} The source color space for the handler.
     */
    getSourceColorSpace() {
        //console.log('Handler GET source colorspace:', this.sourceColorSpace);
        return this.sourceColorSpace;
    }

    /**
     * Get the target distance unit for the handler.
     * 
     * @returns {string} The target distance unit for the handler.
     */
    getTargetDistanceUnit() {
        //console.log('Handler GET source distance unit:', this.targetDistanceUnit);
        return this.targetDistanceUnit;
    }

    /**
     * Get the extension /format for the handler.
     * 
     * @returns {string} The extension / format for the handler.
     */
    getExtension() {
        return this.extension;
    }    

    /**
     * Initialize the handler for the given editor. Default implementation just sets the editor instance.
     * 
     * @param {Editor} editor - The editor instance.
     * @returns {void}
     */
    initialize(editor) {
        this.editor = editor;
    }

    /**  
     * Create a valid name for the given name. Default implementation returns the name as is.
     * 
     * @param {string} name - The name to create a valid name for.
     * @returns {string} The valid name created.
     */      
    createValidName(name) {
        return name;
    }

    /**
     * Get default value as a string for the given value and type. If no value is specified
     * a default value will be returned based on the type.
     * 
     * @param {string} value - The value to get the default value for.
     * @param {string} _type - The type of the value.
     * @returns {string} The default value for the given value and type.
     */
    getDefaultValue(value, _type) {
        if (_type === 'string' || _type === 'filename') {
            value = "'" + value + "'";
        }
        else if (this.isArray(_type)) {
            if (value.length == 0) {
                if (_type === 'color3')
                    value = "[0.0, 0.0, 0.0]";
                else if (_type === 'color4')
                    value = "[0.0, 0.0, 0.0, 0.0]";
                else if (_type === 'vector2')
                    value = "[0.0, 0.0]";
                else if (_type === 'vector3')
                    value = "[0.0, 0.0, 0.0]";
                else if (_type === 'vector4')
                    value = "[0.0, 0.0, 0.0, 0.0]";
                else if (_type === 'matrix33')
                    value = "[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]";
                else if (_type === 'matrix44')
                    value = "[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]";
            }
            else {
                value = "[" + value + "]";
            }
        }
        else if (_type === 'integer') {
            if (value.length == 0) {
                value = 0;
            }
        }
        else if (_type === 'float') {
            if (value.length == 0) {
                value = 0.0;
            }
        }
        else if (_type === 'boolean') {
            if (value)
                value = 'true';
            else
                value = 'false';
        }

        if (value.length == 0) {
            //console.log('No value for input:', _name, 'type:', _type, 'value:', value);=
            value = "''";
        }
        return value;
    }
};

/**
 * @class MxMaterialXHandler
 * 
 * This class extends the MxGraphHandler class to provide MaterialX-specific functionality
 * for handling MaterialX graphs within the editor.
 */
class MxMaterialXHandler extends MxGraphHandler {

    /** 
     * Constructor for the MxMaterialXHandler class.
     * 
     * @param {string} id - The identifier for the handler.
     * @param {string} extension - The associated extension for the handler.
     */
    constructor(id, extension) {
        super(id, extension);
    }

    /**
     * Load in the MaterialX library.
     * Sets the global ne_mx variable to the MaterialX instance.
     * 
     * @returns {Promise} A promise that resolves when the MaterialX library is loaded.
     */
    loadMaterialX() {
        return new Promise((resolve, reject) => {
            MaterialX().then((ne_mtlx) => {
                // Save the MaterialX instance to the global variable
                ne_mx = ne_mtlx;
                resolve();
            }).catch((error) => {
                reject(error);
            });
        });
    }

    /**
     * Load the MaterialX document from library into the editor.
     * 
     * @param {Editor} editor - The editor instance.
     * @param {string} materialFilename - The filename of the library MaterialX document to graph.
     */
    loadLibraryDocument(editor, materialFilename) {

        function loadInitialText(filePath, handler) {
            try {
                fetch(filePath)
                    .then(response => response.blob())
                    .then(blob => {
                        const reader = new FileReader();
                        reader.onload = function (e) {
                            console.log('Loaded document:', filePath);
                            editor.loadGraphFromString('mtlx', e.target.result, filePath, 80);
                        }
                        reader.readAsText(blob);
                    })
            } catch (error) {
                console.error('Error loading file %s:' % filePath, error);
            }
        }

        loadInitialText(materialFilename, this);
    }

    /** 
        Initialize the MaterialX handler for the given editor.
        
        Initializes MaterialX and sets up the MaterialX document and standard libraries.
        If a default MaterialX document is provided, it will be loaded into the editor.
        The standard libraries are scanned for colorspaces and units, which are cached for later usage.

        @param {Editor} editor - The editor instance
        @param {string} materialFilename - The filename of the default MaterialX document to graph   
     */
    initialize(editor, materialFilename) {
        super.initialize(editor);

        if (!ne_mx) {

            this.loadMaterialX().then(() => {

                // Additional logic after MaterialX is loaded
                editor.debugOutput("Loaded MaterialX version:" + ne_mx.getVersionString(), 0, true);
                doc = ne_mx.createDocument();

                var generator = new ne_mx.EsslShaderGenerator();
                var genContext = new ne_mx.GenContext(generator);
                stdlib = ne_mx.loadStandardLibraries(genContext);
                editor.debugOutput('Loaded standard libraries definitions:' + stdlib.getNodeDefs().length, 0, false);

                // Find units, unittype pairs available. Keep in unique list.
                let units = new Map();
                for (let ud of stdlib.getUnitDefs()) {
                    let unittype = ud.getAttribute('unittype')
                    for (let unit of ud.getChildren()) {
                        units.set(unit.getName(), unittype);
                    }
                }
                // Sort units
                this.setUnits(Array.from(units).sort());
                console.log('> Setup real-world units: ', this.getUnits());

                // Find the colorspaces available. Keep in unique list. Hack as there
                // is no way to find a list of colorspaces.
                let colorSpaces = new Set();
                let docNodeDefs = stdlib.getNodeDefs();
                for (let i = 0; i < docNodeDefs.length; i++) {
                    let cmnode = docNodeDefs[i];
                    if (cmnode.getNodeGroup() === 'colortransform') {
                        let name = cmnode.getName();
                        name = name.replace('ND_', '');
                        let namesplit = name.split('_to_');
                        let type = 'color3';
                        if (namesplit[1].includes('color4')) {
                            namesplit[1] = namesplit[1].replace('_color4', '');
                            type = 'color4';
                        } else {
                            namesplit[1] = namesplit[1].replace('_color3', '');
                        }
                        colorSpaces.add(namesplit[0]);
                        colorSpaces.add(namesplit[1]);
                    }
                }
                // Sort the colorspaces
                this.setColorSpaces(Array.from(colorSpaces).sort())
                console.log('Set up colorspaces: ', this.getColorSpaces());

                var definitionsList = [];
                var result = this.createLiteGraphDefinitions(stdlib, false, true, definitionsList, 'mtlx', MxShadingGraphEditor.theEditor);
                var definitionsDisplayUpdater = editor.ui.definitionsDisplayUpdater;
                if (definitionsDisplayUpdater) {
                    definitionsDisplayUpdater(result);
                }

                editor.clearNodeTypes();
                try {
                    eval(result);
                } catch (e) {
                    editor.debugOutput('Error evaluating source: ' + e, 2, false);
                }

                var nodeTypes = LiteGraph.registered_node_types;
                var i = 0;
                for (var typeName in nodeTypes) {
                    i++;
                }
                editor.debugOutput("Registered node types:" + definitionsList.length, 0, false);

                editor.displayNodeTypes();

                if (materialFilename.length > 0) {
                    this.loadLibraryDocument(editor, materialFilename);
                }

                editor.updatePropertyPanel(null);

            }).catch((error) => {
                editor.debugOutput("Error on initialization:" + error, 2);
            });
        }
    }

    /** 
     * Find all MaterialX renderable items in a graph.
     * 
     * @param {LiteGraph} graph - The graph to scan.
     * @returns {Array} An array of MaterialX renderable items found in the graph.
     */
    findRenderableItems(graph) {

        let graphWriteOptions = { writeCustomLibs : false, saveNodePositions: false, writeOutputs : true };
        let mdoc = this.saveGraphToDocument(graph, graphWriteOptions);
        if (!mdoc) {
            console.log('Failed to save graph to document');
            return;
        }
        return this.findRenderableItemsInDoc(mdoc);
    }

    /** 
     * Find all renderable items in the MaterialX document.
     * 
     * @param {Document} mdoc - The MaterialX document to scan.
     * @returns {Array} An array of renderable items found in the document.
     */
    findRenderableItemsInDoc(mdoc) {

        const materialNodes = mdoc.getMaterialNodes();
        let shaderList = [];
        let renderableItems = [];

        for (let i = 0; i < materialNodes.length; ++i) {
            let materialNode = materialNodes[i];
            if (materialNode) {
                //console.log('Scan material: ', materialNode.getNamePath());
                let shaderNodes = ne_mx.getShaderNodes(materialNode)
                if (shaderNodes.length > 0) {
                    let shaderNodePath = shaderNodes[0].getNamePath()
                    if (!shaderList.includes(shaderNodePath)) {
                        //console.log('-- add shader: ', shaderNodePath);
                        shaderList.push(shaderNodePath);
                        renderableItems.push(shaderNodePath);
                    }
                }
            }
        }
        const nodeGraphs = mdoc.getNodeGraphs();
        for (let i = 0; i < nodeGraphs.length; ++i) {
            let nodeGraph = nodeGraphs[i];
            if (nodeGraph) {
                if (nodeGraph.hasAttribute('nodedef') || nodeGraph.hasSourceUri()) {
                    continue;
                }
                // Skip any nodegraph that is connected to something downstream
                if (nodeGraph.getDownstreamPorts().length > 0) {
                    continue
                }
                let outputs = nodeGraph.getOutputs();
                for (let j = 0; j < outputs.length; ++j) {
                    let output = outputs[j];
                    {
                        renderableItems.push(output.getNamePath());
                    }
                }
            }
        }
        const outputs = mdoc.getOutputs();
        for (let i = 0; i < outputs.length; ++i) {
            let output = outputs[i];
            if (output) {
                renderableItems.push(output.getNamePath());
            }
        }

        return renderableItems;
    }

    /**
     * Builds and returns metadata for a node based on the provided parameters.
     * This metadata can be used to enhance the node's representation and interaction
     * within the UI, specifying details like color space, unit, and UI properties.
     *
     * @param {string} colorSpace - The color space of the node (e.g., 'sRGB', 'linear').
     * @param {string} unit - The unit of measurement for the node's value (e.g., 'meters', 'seconds').
     * @param {string} unitType - The type of unit measurement (e.g., 'distance', 'time').
     * @param {string} uiname - The name to display in the UI for this node.
     * @param {number} uimin - The minimum value allowed for this node in the UI.
     * @param {number} uimax - The maximum value allowed for this node in the UI.
     * @param {string} uifolder - The folder/group in the UI where this node should be placed.
     * @param {string} _type - The data type of the node (e.g., 'float', 'vector3').
     * @returns {Object} An object containing the constructed metadata based on the input parameters.
     */
    buildMetaData(colorSpace, unit, unitType, uiname, uimin, uimax, uifolder, _type) {
        // Create a struct with the metadata names as key and value
        var metaData = {};
        metaData['colorspace'] = colorSpace;
        metaData['unit'] = unit;
        metaData['unittype'] = unitType;
        metaData['uiname'] = uiname;
        if (_type == 'vector2' || _type == 'vector3' || _type == 'vector4' || _type == 'matrix33' || _type == 'matrix44') {
            if (uimin) {
                uimin = uimin.split(',').map(Number);
            }
            if (uimax) {
                uimax = uimax.split(',').map(Number);
            }
        }
        metaData['uimin'] = uimin;
        metaData['uimax'] = uimax;
        metaData['uifolder'] = uifolder;

        // Return struct in an array
        return metaData;
    }

    /**
     * Creates LiteGraph node definitions based on the MaterialX document.
     * This function parses the MaterialX document to extract node definitions
     * and generates Javascript code for corresponding LiteGraph nodes that can be used within the editor.
     * 
     * @param {Document} doc - The MaterialX document to parse.
     * @param {boolean} debug - Flag to enable debug logging.
     * @param {boolean} addInputOutputs - Flag to determine whether to add inputs and outputs to the LiteGraph nodes.
     * @param {Array} definitionsList - List to store the generated LiteGraph node definitions.
     * @param {string} libraryPrefix - Prefix to use for the LiteGraph nodes, default is 'mtlx'.
     * @param {Editor} editor - The instance of the editor where the nodes will be used.
     * @param {string} icon - Icon to use for the LiteGraph nodes, default is an empty string.
     * @returns {void}
     */
    createLiteGraphDefinitions(doc, debug, addInputOutputs, definitionsList, libraryPrefix = 'mtlx',
        editor, icon = '')         
    {
        var definition_code = ""

        console.log('Creating LiteGraph definitions from MaterialX document:', doc);

        // Get the node definitions from the MaterialX document
        var nodeDefs = doc.getNodeDefs();

        if (debug)
            definition_code += "console.log('Loading MaterialX Definitions...');\n";

        definition_code += "// MaterialX LiteGraph Functional Definitions\n"
        definition_code += "//\n";
        definition_code += "// MaterialX Version: " + ne_mx.getVersionString() + "\n";
        const date = new Date();
        definition_code += "// Generated on: " + date.toString() + "\n"; 
        definition_code += "//\n";

        var TMAP = {}
        TMAP['float'] = 'float';
        TMAP['color3'] = 'color3';
        TMAP['color4'] = 'color4';
        TMAP['vector2'] = 'vector2';
        TMAP['vector3'] = 'vector3';
        TMAP['vector4'] = 'vector4';
        TMAP['matrix33'] = 'matrix33';
        TMAP['matrix44'] = 'matrix44';
        TMAP['integer'] = 'integer';
        TMAP['string'] = 'string';
        TMAP['boolean'] = 'boolean';
        TMAP['filename'] = 'filename';
        TMAP['BSDF'] = 'BSDF';
        TMAP['EDF'] = 'EDF';
        TMAP['VDF'] = 'VDF';
        TMAP['surfaceshader'] = 'surfaceshader';
        TMAP['volumeshader'] = 'volumeshader';
        TMAP['displacementshader'] = 'displacementshader';
        TMAP['lightshader'] = 'lightshader';
        TMAP['material'] = 'material';
        TMAP['vector2array'] = 'vector2array';

        var CMAP = {}
        CMAP['integer'] = "#A32";
        CMAP['float'] = "#161";
        CMAP['vector2'] = "#265";
        CMAP['vector3'] = "#465";
        CMAP['vector4'] = "#275";
        CMAP['color3'] = "#37A";
        CMAP['color4'] = "#69A";
        CMAP['matrix33'] = "#333";
        CMAP['matrix44'] = "#444";
        CMAP['string'] = "#395";
        CMAP['filename'] = "#888";
        CMAP['boolean'] = "#060";

        var inputTypes = ['float', 'color3', 'color4', 'vector2', 'vector3', 'vector4', 'matrix33', 'matrix44', 'integer', 'string', 'boolean', 'filename', 'BSDF', 'EDF', 'VDF', 'surfaceshader', 'volumeshader', 'displacementshader', 'lightshader', 'material', 'vector2array'];
        var outputTypes = ['float', 'color3', 'color4', 'vector2', 'vector3', 'vector4', 'matrix33', 'matrix44', 'integer', 'string', 'boolean', 'filename', 'BSDF', 'EDF', 'VDF', 'surfaceshader', 'volumeshader', 'displacementshader', 'lightshader', 'material', 'vector2array'];

        // TODO: Support tokens
        var supporTokens = false;
        if (supporTokens) {
            inputTypes.push('token');
            TMAP['token'] = 'string';
        }

        const INPUT_ND = 'ND_input_';
        const OUTPUT_ND = 'ND_output_';
        const INPUT_NODE_STRING = 'input';
        const OUTPUT_NODE_STRING = 'output';
        const LIBRARY_ICON = '';

        // Register inputs (which have no nodedef)
        if (addInputOutputs) {
            for (var _type of inputTypes) {
                var id = libraryPrefix + '/input/input_' + _type;
                var functionName = ne_mx.createValidName(id);
                var titleName = 'input_' + _type;
                definition_code += "\n/**\n"; 
                definition_code += "  * @function "+ functionName + "\n";
                definition_code += "  * @description Library: " + libraryPrefix + ". Category: input. Type: " + _type + "\n";
                definition_code += "  *   LiteGraph id: " + id + "\n"; 
                definition_code += "  */\n";
                definition_code += "function " + functionName + "() {\n";
                {
                    definition_code += "  this.nodedef_icon = '" + LIBRARY_ICON + "';\n";
                    definition_code += "  this.nodedef_name = '" + INPUT_ND + _type + "';\n";
                    definition_code += "  this.nodedef_node = '" + INPUT_NODE_STRING + "';\n";
                    definition_code += "  this.nodedef_type = '" + _type + "';\n";
                    definition_code += "  this.nodedef_group = '" + INPUT_NODE_STRING + "';\n";
                    if (_type == 'token')
                        _type = 'string';
                    definition_code += "  this.addInput('in', '" + TMAP[_type] + "');\n";
                    var value = this.getDefaultValue('', _type);
                    var metaData = this.buildMetaData('', '', '', '', null, null, '', null);
                    metaData = JSON.stringify(metaData);

                    // TODO: It's not possible to add a default colorspace since you 
                    // don't know what node type it will feed into. i.e. the specification
                    // is underdefined at this time (1.39)
                    if (_type == 'filename')
                    {
                        ; // Nothing for now.
                    }

                    definition_code += "  this.addProperty('in', " + value + ", '" + _type + "'," + metaData + ");\n";
                    definition_code += "  this.addOutput('out', '" + TMAP[_type] + "');\n";

                    definition_code += "  this.title = '" + titleName + "';\n"
                    var desc = '"MaterialX:' + id + '"';
                    definition_code += "  this.desc = " + desc + ";\n";

                    var onNodeCreated = "function() {\n";
                    onNodeCreated += "    //console.log('Node created:', this);\n";
                    onNodeCreated += "  }";
                    definition_code += "  this.onNodeCreated = " + onNodeCreated + "\n";
                    var onRemoved = "function() {\n";
                    onRemoved += "    //console.log('Node removed:', this);\n";
                    onRemoved += "  }";
                    definition_code += "  this.onRemoved = " + onRemoved + "\n";

                    // Property changed callback
                    let monitor = editor.monitor;
                    var onPropertyChanged = "function(name, value, prev_value) {\n";
                    if (monitor)
                    {
                        onPropertyChanged += " MxShadingGraphEditor.theEditor.monitor.onPropertyChanged(this.title, name, value, prev_value, this);\n";
                    }
                    else
                    {
                        onPropertyChanged += "    console.log('+ Internal property changed:', this.title, name, value, prev_value, this);\n";
                    }
                    onPropertyChanged += "  }";
                    definition_code += "  this.onPropertyChanged = " + onPropertyChanged + "\n";

                    // Property info / attribute changed callback
                    var onPropertyInfoChanged = "function(name, info, value, prev_value) {\n";
                    if (monitor)
                    {
                        onPropertyInfoChanged += " MxShadingGraphEditor.theEditor.monitor.onPropertyInfoChanged(this.title, name, info, value, prev_value, this);\n";
                    }
                    else
                    {
                        onPropertyInfoChanged += "    console.log('+ Internal property info changed:', this.title, name, info, value, prev_value, this);\n";
                    }
                    onPropertyInfoChanged += "  }"                    
                    definition_code += "  this.onPropertyInfoChanged = " + onPropertyInfoChanged + "\n";

                    // Output connection callback 
                    var onConnectOutput = "function(slot, input_type, input, target_node, target_slot) {\n";
                    if (monitor)
                    {
                        onConnectOutput += " MxShadingGraphEditor.theEditor.monitor.onConnectOutput(slot, input_type, input, target_node, target_slot, this);\n";
                    }
                    else
                    {
                        onConnectOutput += "    console.log('+ Output connection changed:', this.title, slot, input_type, input, target_node, target_slot);\n";
                    }
                    onConnectOutput += "  }"                    
                    definition_code += "  this.onConnectOutput = " + onConnectOutput + "\n";    
    
                    // Input connection callback 
                    var onConnectInput = "function(target_slot, output_type, output, source, slot) {\n";
                    if (monitor)
                    {
                        onConnectInput += " MxShadingGraphEditor.theEditor.monitor.onConnectInput(target_slot, output_type, output, source, slot, this);\n";
                    }
                    else
                    {
                        onConnectInput += "    console.log('+ Input connection changed:', this.title, target_slot, output_type, output, source, slot);\n";
                    }
                    onConnectInput += "  }"                    
                    definition_code += "  this.onConnectInput = " + onConnectInput + "\n";

                    definition_code += "  this.color = '#004C94';\n";
                    definition_code += "  this.bgcolor = '#000';\n";
                    if (_type in CMAP) {
                        definition_code += "  this.boxcolor = '" + CMAP[_type] + "';\n";
                    }
                    definition_code += "  this.shape = LiteGraph.ROUND_SHAPE;\n";

                    definition_code += "  this.onExecute = function() {\n";
                    definition_code += "    console.log('Executing node: ', this);\n";
                    definition_code += "  }\n";
                }
                definition_code += "}\n"
                definition_code += "LiteGraph.registerNodeType('" + id + "', " + functionName + ");\n";
            }

            // Register outputs (which have no nodedef)
            for (var _type of outputTypes) {
                var id = libraryPrefix + '/output/output_' + _type;
                var functionName = ne_mx.createValidName(id);
                var titleName = 'output_' + _type;

                definition_code += "\n/**\n"; 
                definition_code += "  * @function "+ functionName + "\n";
                definition_code += "  * @description Library: " + libraryPrefix + ". Category: output. Type: " + _type + "\n";
                definition_code += "  *   LiteGraph id: " + id + "\n"; 
                definition_code += "  */\n";

                definition_code += "function " + functionName + "() {\n";
                {
                    definition_code += "  this.title = '" + titleName + "';\n"
                    var desc = '"MaterialX Node :' + id + '"';
                    definition_code += "  this.desc = " + desc + ";\n";

                    definition_code += "  this.nodedef_icon = '" + LIBRARY_ICON + "';\n";
                    definition_code += "  this.nodedef_name = '" + OUTPUT_ND + + _type + "';\n";
                    definition_code += "  this.nodedef_node = '" + OUTPUT_NODE_STRING + "';\n";
                    definition_code += "  this.nodedef_type = '" + _type + "';\n";
                    definition_code += "  this.nodedef_group = '" + OUTPUT_NODE_STRING + "';\n";
                    definition_code += "  this.addInput('in', '" + TMAP[_type] + "');\n";
                    var value = this.getDefaultValue('', _type);
                    definition_code += "  this.addProperty('in', " + value + ", '" + _type + "');\n";
                    definition_code += "  this.addOutput('out', '" + TMAP[_type] + "');\n";

                    var onNodeCreated = "function() {\n";
                    onNodeCreated += "  //console.log('Node created:', this);\n";
                    onNodeCreated += "  }";
                    definition_code += "  this.onNodeCreated = " + onNodeCreated + "\n";
                    var onRemoved = "function() {\n";
                    onRemoved += "  //console.log('Node removed:', this);\n";
                    onRemoved += "  }";
                    definition_code += "  this.onRemoved = " + onRemoved + "\n";

                    let monitor = editor.monitor;
                    var onPropertyChanged = "function(name, value, prev_value) {\n";
                    if (monitor)
                    {
                        onPropertyChanged += " MxShadingGraphEditor.theEditor.monitor.onPropertyChanged(this.title, name, value, prev_value, this);\n";
                    }
                    else
                    {
                        onPropertyChanged += "    console.log('+ Internal property changed:', this.title, name, value, prev_value, this);\n";
                    }
                    onPropertyChanged += "  }";
                    definition_code += "  this.onPropertyChanged = " + onPropertyChanged + "\n";    

                    var onPropertyInfoChanged = "function(name, info, value, prev_value) {\n";
                    if (monitor)
                    {
                        onPropertyInfoChanged += " MxShadingGraphEditor.theEditor.monitor.onPropertyInfoChanged(this.title, name, info, value, prev_value, this);\n";
                    }
                    else
                    {
                        onPropertyInfoChanged += "    console.log('+ Internal property info changed:', this.title, name, info, value, prev_value, this);\n";
                    }
                    onPropertyInfoChanged += "  }"                    
                    definition_code += "  this.onPropertyInfoChanged = " + onPropertyInfoChanged + "\n";


                    // Output connection callback 
                    var onConnectOutput = "function(slot, input_type, input, target_node, target_slot) {\n";
                    if (monitor)
                    {
                        onConnectOutput += " MxShadingGraphEditor.theEditor.monitor.onConnectOutput(slot, input_type, input, target_node, target_slot, this);\n";
                    }
                    else
                    {
                        onConnectOutput += "    console.log('+ Output connection changed:', this.title, slot, input_type, input, target_node, target_slot);\n";
                    }
                    onConnectOutput += "  }"                    
                    definition_code += "  this.onConnectOutput = " + onConnectOutput + "\n";    
    
                    // Input connection callback 
                    var onConnectInput = "function(target_slot, output_type, output, source, slot) {\n";
                    if (monitor)
                    {
                        onConnectInput += " MxShadingGraphEditor.theEditor.monitor.onConnectInput(target_slot, output_type, output, source, slot, this);\n";
                    }
                    else
                    {
                        onConnectInput += "    console.log('+ Input connection changed:', this.title, target_slot, output_type, output, source, slot);\n";
                    }
                    onConnectInput += "  }"                    
                    definition_code += "  this.onConnectInput = " + onConnectInput + "\n";

                    definition_code += "  this.color = '#004C94';\n";
                    definition_code += "  this.bgcolor = '#000';\n";
                    if (_type in CMAP) {
                        definition_code += "  this.boxcolor = '" + CMAP[_type] + "';\n";
                    }
                    definition_code += "  this.shape = LiteGraph.ROUND_SHAPE;\n";

                    definition_code += "  this.onExecute = function() {\n";
                    definition_code += "  console.log('Executing node:', this);\n";
                    definition_code += "  }\n";
                }
                definition_code += "}\n"
                definition_code += "LiteGraph.registerNodeType('" + id + "', " + functionName + ");\n";
                definitionsList.push(id);
            }
        }

        // Iterate over all node definitions
        for (var nodeDef of nodeDefs) {

            var nodeDefName = nodeDef.getName();
            var id = libraryPrefix + '/' + nodeDef.getNodeGroup() + '/' + nodeDefName;
            id = id.replace('ND_', '');
            var functionName = ne_mx.createValidName(id);
            var nodeType = nodeDef.getType();
            var titleName = nodeDef.getNodeString() + "_" + nodeType;
            var swatchLocation = 'https://kwokcb.github.io/MaterialX_Learn/resources/mtlx/nodedef_materials/';
            var outputs = nodeDef.getActiveOutputs();
            var outputName = outputs[0].getName(); // TODO: Handle swatch for multiple outputs
            var swatchId = swatchLocation + 'material_' + nodeDefName + '_' + outputName + '_genglsl.png';
            swatchId = swatchId.replace('ND_', '');
            if (debug)
                console.log('\n--- Registering node type:', id, '----');


            definition_code += "\n/**\n"; 
            definition_code += "  * @function "+ functionName + "\n";
            definition_code += "  * @description Library: " + libraryPrefix + ". Category: " + nodeString + ". Type: " + nodeType + "\n";
            definition_code += "  *   LiteGraph id: " + id + "\n"; 
            definition_code += "  */\n";

            definition_code += "function " + functionName + "() {\n";
            {
                var nodeGroup = nodeDef.getNodeGroup();
                var nodeString = nodeDef.getNodeString();
                var theIcon = icon;
                if (theIcon.length == 0) {
                    for (var key in editor.ui.icon_map) {
                        if (nodeString.toLowerCase().startsWith(key.toLowerCase())) {
                            if (key in editor.ui.icon_map)
                                theIcon = editor.ui.icon_map[key];
                            //console.log('set icon:', theIcon, 'for:', key, nodeString);
                            break;
                        }
                        else if (nodeGroup.toLowerCase().startsWith(key.toLowerCase())) {
                            if (key in editor.ui.icon_map)
                                theIcon = editor.ui.icon_map[key];
                            //console.log('set icon:', theIcon, 'for:', key, nodeGroup);
                            break;
                        }
                    }
                }

                definition_code += "  this.nodedef_icon = '" + theIcon + "';\n";
                definition_code += "  this.nodedef_name = '" + nodeDefName + "';\n";
                definition_code += "  this.nodedef_type = '" + nodeType + "';\n";
                definition_code += "  this.nodedef_node = '" + nodeString + "';\n";
                definition_code += "  this.nodedef_href = 'https://kwokcb.github.io/MaterialX_Learn/documents/definitions/" + nodeString + ".html';\n";
                definition_code += "  this.nodedef_swatch = '" + swatchId + "';\n";
                definition_code += "  this.nodedef_group = '" + nodeGroup + "';\n";

                for (var input of nodeDef.getActiveInputs()) {
                    var _name = input.getName();
                    var _type = input.getType();
                    if (_type in TMAP)
                        _type = TMAP[_type];
                    else
                        console.log('Unmappable type:', _type)
                    definition_code += "  this.addInput('" + _name + "','" + _type + "');\n";

                    let value = input.getValueString();
                    value = this.getDefaultValue(value, _type);
                    let uiname = input.getAttribute('uiname');

                    let uimin = input.getAttribute('uimin');
                    if (uimin.length == 0) {
                        uimin = null;
                    }
                    let uimax = input.getAttribute('uimax');
                    if (uimax.length == 0) {
                        uimax = null;
                    }
                    let uisoftmin = input.getAttribute('uisoftmin');
                    if (uisoftmin.length > 0) {
                        uimin = uisoftmin;
                    }
                    let uisoftmax = input.getAttribute('uisoftmax');
                    if (uisoftmax.length > 0) {
                        uimax = uisoftmax;
                    }
                    var uifolder = input.getAttribute('uifolder');
                    var metaData = this.buildMetaData('', '', '', uiname, uimin, uimax, uifolder, _type);

                    // Add colorspace on nodedefs
                    let colorspace = input.getAttribute('colorspace');     
                    let nodeDefType = nodeDef.getType();               
                    if (_type == 'filename' && (nodeDefType == 'color3' || nodeDefType == 'color4'))
                    {
                        if (colorspace.length == 0)
                        {
                            colorspace = 'none';
                        }
                    }
                    if (colorspace.length > 0)
                        metaData['colorspace'] = colorspace;

                    // TODO: Add units, unitype on nodedefs. There is no
                    // default unittype or units.
                    let unitAttributes = ['unit', 'unittype'];
                    for (let unitAttribute of unitAttributes)
                    {
                        let value = input.getAttribute(unitAttribute);
                        if (value.length > 0)
                        {
                            metaData[unitAttribute] = value;
                        }
                    }

                    // Add in defaultgeomprop to denote geometric inputs.
                    let defaultgeomprop = input.getAttribute('defaultgeomprop')
                    metaData['defaultgeomprop'] = defaultgeomprop;

                    // Add enumerations
                    let enums = input.getAttribute('enum');
                    if (enums.length > 0)
                    {                        
                        metaData['enum'] = enums.split(',');
                        metaData['enum'].map(function(x) { return x.trim(); });                
                    }
                    let enumvalues = input.getAttribute('enumvalues');
                    if (enumvalues.length > 0)
                    {                        
                        metaData['enumvalues'] = enumvalues.split(',');
                        metaData['enumvalues'].map(function(x) { return x.trim(); });                
                    }

                    metaData = JSON.stringify(metaData);
                    definition_code += "  this.addProperty('" + _name + "', " + value + ", '" + _type + "'," + metaData + ");\n";
                }
                for (var output of nodeDef.getActiveOutputs()) {
                    var _name = output.getName();
                    var _type = output.getType();
                    if (_type in TMAP)
                        _type = TMAP[_type];
                    else
                        console.log('Unmappable type:', _type)
                    //if(_type && _type.constructor === String)
                    //   _type = '"'+_type+'"';
                    definition_code += "  this.addOutput('" + _name + "','" + _type + "');\n";
                }

                definition_code += "  this.title = '" + titleName + "';\n"
                var desc = '"MaterialX:' + id + '"';
                definition_code += "  this.desc = " + desc + ";\n";

                //definition_code += "  /**\n";
                //definition_code += "   * @function " + "onNodeCreated" + "\n"; 
                //definition_code += "   */";

                var onNodeCreated = "function() {\n";
                onNodeCreated += "  //console.log('Node created:', this);\n";
                onNodeCreated += "}";
                definition_code += "  this.onNodeCreated = " + onNodeCreated + "\n";
                var onRemoved = "function() {\n";
                onRemoved += "  //console.log('Node removed:', this);\n";
                onRemoved += "  }";
                definition_code += "  this.onRemoved = " + onRemoved + "\n";

                let monitor = editor.monitor;
                var onPropertyChanged = "function(name, value, prev_value) {\n";
                if (monitor)
                {
                    onPropertyChanged += " MxShadingGraphEditor.theEditor.monitor.onPropertyChanged(this.title, name, value, prev_value, this);\n";
                }
                else
                {
                    onPropertyChanged += "    console.log('+ Internal property changed:', this.title, name, value, prev_value, this);\n";
                }
                onPropertyChanged += "  }";
                definition_code += "  this.onPropertyChanged = " + onPropertyChanged + "\n";

                var onPropertyInfoChanged = "function(name, info, value, prev_value) {\n";
                if (monitor)
                {
                    onPropertyInfoChanged += " MxShadingGraphEditor.theEditor.monitor.onPropertyInfoChanged(this.title, name, info, value, prev_value, this);\n";
                }
                else
                {
                    onPropertyInfoChanged += "    console.log('+ Internal property info changed:', this.title, name, info, value, prev_value, this);\n";
                }
                onPropertyInfoChanged += "  }"                    
                definition_code += "  this.onPropertyInfoChanged = " + onPropertyInfoChanged + "\n";

                // Output connection callback 
                var onConnectOutput = "function(slot, input_type, input, target_node, target_slot) {\n";
                if (monitor)
                {
                    onConnectOutput += " MxShadingGraphEditor.theEditor.monitor.onConnectOutput(slot, input_type, input, target_node, target_slot, this);\n";
                }
                else
                {
                    onConnectOutput += "    console.log('+ Output connection changed:', this.title, slot, input_type, input, target_node, target_slot);\n";
                }
                onConnectOutput += "  }"                    
                definition_code += "  this.onConnectOutput = " + onConnectOutput + "\n";    

                // Input connection callback 
                var onConnectInput = "function(target_slot, output_type, output, source, slot) {\n";
                if (monitor)
                {
                    onConnectInput += " MxShadingGraphEditor.theEditor.monitor.onConnectInput(target_slot, output_type, output, source, slot, this);\n";
                }
                else
                {
                    onConnectInput += "    console.log('+ Input connection changed:', this.title, target_slot, output_type, output, source, slot);\n";
                }
                onConnectInput += "  }"                    
                definition_code += "  this.onConnectInput = " + onConnectInput + "\n";

                // Set the background color to slate grey
                definition_code += "  this.bgcolor = '#111';\n";
                //console.log('Node group:', nodeGroup, nodeDefName);
                if (nodeGroup == 'conditional') {
                    //console.log('Cond Node group:', nodeGroup)
                    definition_code += "  this.color = '#532200';\n";
                    definition_code += "  this.title_text_color = '#000';\n";
                    definition_code += "  this.shape = LiteGraph.CARD_SHAPE;\n";
                }

                else if (nodeString != 'convert' &&
                    (nodeGroup == 'shader' || nodeType == 'surfaceshader' || nodeType == 'volumshader' || nodeType == 'displacementshader')) {
                    definition_code += "  this.color = '#232';\n";
                    definition_code += "  this.shape = LiteGraph.ROUND_SHAPE;\n";
                }
                else if (nodeGroup == 'material') {
                    definition_code += "  this.color = '#151';\n";
                    definition_code += "  this.shape = LiteGraph.BOX_SHAPE;\n";
                }
                else {
                    definition_code += "  this.color = '#222';\n";
                    definition_code += "  this.shape = LiteGraph.ROUND_SHAPE;\n";
                }
                if (nodeType in CMAP) {
                    definition_code += "  this.boxcolor = '" + CMAP[nodeType] + "';\n";
                }
            }
            definition_code += "}\n"

            // Register the node type
            definition_code += functionName + ".nodedef_name = '" + nodeDefName + "';\n";
            definition_code += functionName + ".nodedef_node = '" + nodeString + "';\n";
            definition_code += functionName + ".nodedef_href = 'https://kwokcb.github.io/MaterialX_Learn/documents/definitions/" + nodeString + ".html';\n";

            definition_code += "LiteGraph.registerNodeType(" + "'" + id + "'," + functionName + ");\n";
            definitionsList.push(id);
            if (debug)
                definition_code += "console.log('Registered node type:', '" + id + "');\n";
        }

        //definition_code += "}\n";
        return definition_code;
    }

    /**
     * Validates the provided MaterialX document.
     * 
     * @param {Document} doc - The MaterialX document to validate.
     * @returns {boolean} True if the document is valid, false otherwise.
     */
    validateDocument(doc) 
    {
        if (!doc || !stdlib)
        {
            return true;
        }

        // Need to create a dummy "validation" doc
        let validationDocument = ne_mx.createDocument();
        validationDocument.copyContentFrom(doc);
        validationDocument.importLibrary(stdlib);

        var errors = {};
        var valid = validationDocument.validate(errors);
        if (!valid) {
            this.editor.debugOutput('Failed to validate document:\n' + errors.message, 2);
        }
    }

    /**
     * Saves the graph to a MaterialX document.
     * 
     * @param {Graph} graph - The graph to save.
     * @param {Object} graphWriteOptions - Options to use when writing the graph.
     * @returns {Document} The MaterialX document containing the graph.
     */
    saveGraphToDocument(graph, graphWriteOptions) {

        if (!ne_mx) {
            this.editor.debugOutput("MaterialX is not initialized", 2);
            return;
        }
        
        let writeCustomLibs = graphWriteOptions.writeCustomLibs;
        if (writeCustomLibs == undefined)
        {
            console.error('Graph output option: writeCustomLibs is undefined.')
            writeCustomLibs = true;
        }

        var outputDoc = ne_mx.createDocument();

        if (!stdlib) {
            var generator = new ne_mx.EsslShaderGenerator();
            var genContext = new ne_mx.GenContext(generator);
            stdlib = ne_mx.loadStandardLibraries(genContext);
        }

        // Handle top level
        this.writeGraphToDocument(outputDoc, graph, graphWriteOptions);

        if (writeCustomLibs) {
            console.log('Write custom libraries:', customlibs.length);
            for (var customlib of customlibs) {
                outputDoc.importLibrary(customlib[1]);
            }
            console.log('Write document custom definitions:', customDocLibs.length);
            for (var customDocLib of customDocLibs) {
                outputDoc.importLibrary(customDocLib[1]);
            }
        }

        // TODO: Add in other globals
        outputDoc.setColorSpace(this.getSourceColorSpace());
        outputDoc.removeAttribute('fileprefix');

        this.validateDocument(outputDoc);

        return outputDoc;
    }

    /**
     * Saves the graph to a string in the specified format.
     * 
     * @param {string} extension - The file extension to save the graph as.
     * @param {Graph} graph - The graph to save.
     * @param {Object} graphWriteOptions - Options to use when writing the graph.
     * @returns {Array} An array containing the data string and any error messages.
     */
    saveGraphToString(extension, graph, graphWriteOptions) {

        if (!ne_mx) {
            this.editor.debugOutput("MaterialX is not initialized", 2);
            return ['', 'MaterialX is not initialized'];
        }

        var outputDoc = this.saveGraphToDocument(graph, graphWriteOptions);
        if (!outputDoc) {
            this.editor.debugOutput("Failed to save graph to document", 2);
            return ['', 'Failed to save graph to document'];
        }

        if (extension == 'mtlx')
        {
            const writeOptions = new ne_mx.XmlWriteOptions();
            writeOptions.writeXIncludeEnable = false;
            var data = '';
            try {
                data = ne_mx.writeToXmlString(outputDoc, writeOptions);
            } catch (e) {
                this.editor.debugOutput("Failed to write graph:" + e, 2);
            }
            return [data, ''];                
        }

        // Look for a registered exporter
        else
        {            
            let exporter = this.getExporter(extension);
            if (!exporter) {
                this.editor.debugOutput('Failed to find ' + extension + ' exporter', 2);
            }
            else { 
                let exportDoc = ne_mx.createDocument();
                exportDoc.copyContentFrom(outputDoc);
                exportDoc.importLibrary(stdlib);

                let result = exporter.export(ne_mx, exportDoc);
                return result;
            }
        }
        return ['', 'Failed to export graph to ' + extension];
    }

    /** 
     * Saves the graph to a file with the specified extension.
     *
     * @param {string} extension - The file extension to save the graph as.
     * @param {Graph} graph - The graph to save.
     * @param {Object} graphWriteOptions - Options to use when writing the graph.
     * @returns {void} 
    */
    saveGraphToFile(extension, graph, graphWriteOptions) 
    {
        var data = this.saveGraphToString(extension, graph, graphWriteOptions);
        if (!data[0]) {
            return;
        }

        var blob = new Blob([data[0]], { type: "text/plain" });
        var url = URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = "output_graph.mtlx";
        a.click();
    }

    /** 
     * Writes the graph to the specified MaterialX document.
     * 
     * @param {Document} mltxgraph - The MaterialX document to write the graph to.
     * @param {Graph} graph - The graph to write.
     * @param {Object} graphWriteOptions - Options to use when writing the graph.
     * @returns {void}
     */
    writeGraphToDocument(mltxgraph, graph, graphWriteOptions) {

        var debug = false;

        if (debug)
            console.log('***** START Scan Graph:', graph.title);
        for (var node of graph._nodes) {
            if (node.type == 'graph/subgraph') {
                var subgraph = node.subgraph;
                //var subgraphNode = mltxgraph.addNodeGraph(node.title);
                var subgraphNode = mltxgraph.addChildOfCategory('nodegraph', node.title);
                if (debug)
                    console.log('---->>> Scan NodeGraph:', node.title);
                this.writeGraphToDocument(subgraphNode, subgraph, graphWriteOptions);
                continue;
            }

            if (debug)
                console.log('---->>> Scan Node:', node.title);

            var nodeDefName = node.nodedef_name;
            /* if (!nodeDefName)
            {
                this.editor.debugOutput('Failed to find nodeDef for:' + node.title, 1);
                continue;
            } */

            //var nodeTypes = LiteGraph.registered_node_types;
            //var nodeType = nodeTypes[node.type];
            var nodedefName = node.nodedef_name;
            var nodedef = null;
            var nodeElement = null;
            //if (nodeType) {
            //    nodedefName = nodeType.nodedef_name;
            //    nodedef = stdlib.getNodeDef(nodedefName);
            //}

            //if (nodedef) {
            //    nodeElement = mltxgraph.addNodeInstance(nodedef, name)
            //    nodeElement.setName(node.title);
            //}
            //else 
            {
                if (nodedefName) {
                    nodeElement = mltxgraph.addChildOfCategory(node.nodedef_node, node.nodedef_type);
                    nodeElement.setType(node.nodedef_type);                               

                    if (graphWriteOptions.saveNodePositions) {
                        // TODO: Get properly remapping for xpos, ypos.
                        nodeElement.setAttribute('xpos', JSON.stringify(node.pos[0]));
                        nodeElement.setAttribute('ypos', JSON.stringify(node.pos[1]));
                    }
                    if (debug)
                        console.log('** Create node:', nodeElement.getNamePath(), nodeElement.getType());
                    nodeElement.setName(node.title);
                }
            }

            if (nodeElement) {
                if (debug)
                    console.log('-> Write Node:', graph.title + '/' + node.title, ' --> ', nodeElement.getNamePath());
            }
            else {
                console.log('Skip writing :', node.title);
                //this.editor.debugOutput('No nodedef for:' + node.title + 'Nodetype: ' + node.type, 0);
                continue;
            }

            var properties = node.properties;

            var node_inputs = node.inputs;
            var isInputNode = false;
            var isOutputNode = false;
            if (nodeElement.getCategory() == 'input') {
                isInputNode = true;
                node_inputs = [node];
            }
            else if (nodeElement.getCategory() == 'output') {
                isOutputNode = true;
                node_inputs = [node];
            }

            // Add all outputs if the type is multioutput, or user option set
            if (!isInputNode && !isOutputNode)
            {
                if (node.nodedef_type == "multioutput")
                {                        
                    console.log('Write outputs for:', node, '. type: ', node.nodedef_type);
                    for (var output of node.outputs) {
                        var outputName = output.name;
                        var outputType = output.type;
                        var outputElement = nodeElement.addOutput(outputName, outputType);
                        if (debug) {
                            console.log('> Read: node.nodedef_type: ', node.nodedef_type);
                            console.log('> Write: output:', outputElement.getNamePath(), outputElement.getType());
                        }
                    }
                }                     
            }

            // Add inputs
            if (node_inputs) {

                var inputs = node_inputs;
                for (var i in inputs) {
                    let input = inputs[i];
                    if (debug)
                        console.log('---- Write port:', input);

                    let inputName = input.name;
                    let inputType = input.type;
                    if (nodeElement.getCategory() == 'input' ||
                        nodeElement.getCategory() == 'output') {
                        inputName = 'in';
                        inputType = node.nodedef_type;
                    }

                    //var inputType = input.type;
                    var inputElement = null;
                    var nodeToCheck = node;
                    var inputNode = null;
                    var inputLink = null;
                    if (isInputNode && node.graph._subgraph_node) {
                        nodeToCheck = node.graph._subgraph_node;
                        for (var i = 0; i < nodeToCheck.inputs.length; i++) {
                            var nci = nodeToCheck.inputs[i];
                            if (nci.name == node.title) {
                                inputNode = nodeToCheck.getInputNode(i);
                                inputLink = nodeToCheck.getInputLink(i);
                                //console.log('--- Found parent input:', nci.name, 'inputNode:', inputNode, 'inputLink:', inputLink);
                                break;
                            }
                        }
                    }
                    else {
                        inputNode = node.getInputNode(i);
                        inputLink = node.getInputLink(i);
                    }
                    var inputLinkOutput = '';
                    var numInputOutputs = 0;
                    if (inputLink) {
                        numInputOutputs = inputNode.outputs.length;
                        inputLinkOutput = inputNode.outputs[inputLink.origin_slot];
                    }
                    if (inputNode) {
                        //console.log('inputNode', inputNode, 'inputLink:', inputLink, '. --- upsteream Output:', inputLinkOutput);
                        if (nodeElement.getCategory() != 'input' &&
                            nodeElement.getCategory() != 'output') {
                            inputElement = nodeElement.getInput(inputName);
                            //console.log('Call add input on elem', nodeElement, inputName);
                            inputElement = nodeElement.addInput(inputName, inputType);
                        }
                        else {
                            inputElement = nodeElement;
                        }

                        if (debug) {
                            console.log('Write connection');
                            console.log('  - TO:', inputElement.getName() + "." + inputName);
                            console.log('  - FROM link:', inputNode.id + "." + inputLinkOutput.name);
                        }
                        if (inputNode.type == 'graph/subgraph') {
                            inputElement.setNodeGraphString(inputNode.title);
                            // Set output string if there was an output link.
                            if (numInputOutputs > 1 && inputLinkOutput) {
                                inputElement.setOutputString(inputLinkOutput.name);
                            }
                        }
                        else {
                            //var upstream_nodeType = nodeTypes[inputNode.type];
                            //if (upstream_nodeType) 
                            //console.log('Write connection: ', inputNode.title)
                            {
                                if (inputNode.nodedef_node == 'input') {
                                    inputElement.setInterfaceName(inputNode.title);
                                }
                                else {
                                    inputElement.setNodeName(inputNode.title);
                                    // Need to check that upstream has > 1 output.
                                    // TODO: Log issue that this is annoying to disallow an explicit output in validation. 
                                    if (numInputOutputs > 1 && inputNode.nodedef_node != 'output') {
                                        // Set output string if there was an output link.
                                        if (inputLinkOutput) {
                                            inputElement.setOutputString(inputLinkOutput.name);
                                        }
                                    }
                                }
                            }
                        }
                    }
                    else {

                        var inputValue = node.properties[inputName];
                        if (inputValue == null) {
                            console.log('Cannot find property value for input:', inputName);
                        }
                        else {


                            var origValue = inputValue;
                            //var inputType = propInfo.type;                            
                            if (inputType in ['float', 'integer', 'vector2', 'vector3', 'vector4',
                                'matrix33', 'matrix44', 'color3', 'color4']) {
                                inputValue = '"' + parseFloat(inputValue) + '"';
                            }
                            else if (inputType === 'boolean') {
                                if (inputValue === 'true')
                                    inputValue = 'true';
                                else
                                    inputValue = 'false';
                            }
                            else {
                                inputValue = inputValue.toString();
                            }
                            //console.log('Write input:', inputElement, node, inputName, origValue, inputValue, inputType);
                            
                            if (nodeElement.getCategory() != 'input' &&
                                nodeElement.getCategory() != 'output') {
                                inputElement = nodeElement.getInput(inputName);
                                if (!inputElement)
                                    inputElement = nodeElement.addInput(inputName, inputType);
                                else {
                                    // TODO: LiteGraph seems that copy+paste adds same input > once.
                                    console.log('Error> Trying add input more than once:', inputName, ' to node: ', nodeElement.getNamePath());
                                }
                            }
                            else {
                                inputElement = nodeElement;
                            }

                            try {
                                inputElement.setValueString(inputValue, inputType);
                            }
                            catch (e) {
                                console.warn("Set value error: ", e);
                            }
                        }
                    }

                    if (inputElement) {
                        var propInfo = null;
                        var skip_attributes = [];
                        if (isInputNode || isOutputNode) {
                            if (input.properties_info) {
                                skip_attributes = ['name', 'type', 'value', 'default_value'];
                                propInfo = input.properties_info[0];
                            }
                        }
                        else {
                            if (node.properties_info) {
                                skip_attributes = ['name', 'type', 'value', 'default_value', 'uimin', 'uimax', 'uiname', 'uifolder'];
                                propInfo = node.properties_info[i];
                            }
                        }
                        if (propInfo) {
                            //console.log('Scan propinfo:', propInfo, 'for input:', inputElement.getNamePath(), 'prop_info:', propInfo);

                            // Write node_properties metadata to input
                            skip_attributes = skip_attributes.concat(['defaultgeomprop', 'enum', 'enumvalues']);
                            //console.log('SKIP ATTRIBUTES:', skip_attributes);
                            for (var propAttribute in propInfo) {
                                if (skip_attributes.includes(propAttribute))
                                    continue;

                                //console.log('-- scan attrib:', propAttribute);
                                var propAttributeValue = propInfo[propAttribute];
                                if (propAttributeValue && propAttributeValue.length > 0) {
                                    inputElement.setAttribute(propAttribute, propAttributeValue);
                                }
                            }
                        }
                    }
                }

                if (debug)
                    console.log('---- END Write inputs:', node.inputs);
            }

            if (debug)
                console.log('---> End write node', node.title);
        }

        if (debug)
            console.log('***** END Scan Graph:', graph.title);
    }

    /**
     * Determines if the specified type is an array type.
     * 
     * @param {string} _type - The type to check.
     * @returns {boolean} True if the type is an array type, false otherwise.
     */
    isArray(_type) {
        var ARRAY_TYPES = ['color3', 'color4', 'vector2', 'vector3', 'vector4', 'matrix33', 'matrix44'];
        if (ARRAY_TYPES.includes(_type)) {
            return true;
        }
        return false;
    }

    /** 
     * Builds the connections between MaterialX nodes.
     * 
     * @param {} editor - The graph editor.
     * @param {Node} node - The MaterialXnode to build connections for.
     * @param {Node} lg_node - The LiteGraph node
     * @param {Array} explicitInputs - The explicit inputs to the node.
     * @param {LiteGraph} graph - The LiteGraph parent.
     * @param {NodeGraph} parentGraph - The parent MaterialX graph.
     */
    buildConnections(editor, node, lg_node, explicitInputs, graph, parentGraph) {

        var nodeInputs = [];
        var isOutput = (node.getCategory() == 'output');
        var isInput = (node.getCategory() == 'input');
        if (isOutput || isInput) {
            nodeInputs = [node];
        }
        else {
            nodeInputs = node.getInputs();
        }
        for (var input of nodeInputs) {

            var _name = ''

            if (!isOutput && !isInput) {
                _name = input.getName();
                explicitInputs.push(_name);
            }

            var nodeName = input.getNodeName();
            var nodeGraphName = input.getNodeGraphString();
            var inputInterfaceName = input.getInterfaceName();
            var outputName = input.getOutputString();

            if (nodeName.length ||
                nodeGraphName.length ||
                inputInterfaceName.length ||
                outputName.length) {

                //console.log('Test connection on input:', input.getNamePath(), 'nodeName:[ ', nodeName, 
                //    '] nodeGraphName:[', nodeGraphName, 
                //    '] inputInterfaceName:[', inputInterfaceName, 
                //    ']outputName:[', outputName, ']');

                var target_node = lg_node;
                var target_slot = null;
                if (!isOutput && !isInput)
                    target_slot = target_node.findInputSlot(_name);
                else
                    target_slot = 0;
                var source_node = null;
                var source_slot = 0;
                var source_name = nodeName;
                if (nodeGraphName.length) {
                    source_name = nodeGraphName;
                }
                if (inputInterfaceName.length) {
                    source_name = inputInterfaceName;
                }

                var graphToCheck = graph;
                if (isInput && graph._subgraph_node) {
                    target_node = graph._subgraph_node;
                    target_slot = target_node.findInputSlot(lg_node.title);
                    // Go up to parent graph
                    graphToCheck = parentGraph;
                    //console.log(' go up to parent graph:', graphToCheck,
                    //    'from:', graph, 'subgraph:', graph._subgraph_node,
                    //'target_node:', target_node.title, 'target_slot:', target_slot);
                }
                source_node = graphToCheck.findNodeByTitle(source_name);
                if (source_node) {
                    if (outputName) {
                        var outputSlot = source_node.findOutputSlot(outputName);
                        if (outputSlot >= 0) {
                            source_slot = outputSlot;
                        }
                        else {
                            editor.debugOutput('Failed to find output slot:' + outputName, 1);
                        }
                        var linkInfo = source_node.connect(source_slot, target_node, target_slot);
                        if (!linkInfo) {
                            editor.debugOutput('Failed to connect:' + source_node.title + '.' + outputName, '->', target_node.title + '.' + _name), 1, false;
                        }
                    }
                    //console.log('CONNECT START: source[', source_node.title, '.', source_slot,
                    //    '] --> target[:', target_node.title, ".", target_slot);
                    var linkInfo = null;
                    if (source_slot == null || target_slot == null || target_node == null) {
                        console.warning('Cannot connect!')
                    }
                    else {
                        linkInfo = source_node.connect(source_slot, target_node, target_slot);
                    }
                    if (!linkInfo) {
                        editor.debugOutput('Failed to connect:' + source_node.title + '.' + outputName, '->', target_node.title + '.' + _name, 1);
                    }
                    //console.log('CONNECT END: source[', source_node.title, '.', source_slot,
                    //    '] --> target[:', target_node.title, ".", target_slot);
                }
                else {
                    console.log('Failed to find node ', source_name, 'in graph:', graphToCheck);
                    this.editor.debugOutput('Failed to find source node: ' + source_node + "." +
                        source_name, '->', lg_node.title + "." + _name, 2);
                }
            }
            else {
                var _value = input.getResolvedValueString(); // input.getValueString();
                if (_value.length > 0) {
                    if (this.isArray(input.getType())) {
                        // split by commas or spaces
                        let valueArray = _value.split(/[\s,]+/);
                        _value = valueArray;
                    }

                    //console.log('-- Value Input:', 
                    //lg_node.title + "." + _name, 'value:', _value);
                    lg_node.setProperty(_name, _value);
                }
            }

            var property_info = lg_node.getPropertyInfo(_name);
            this.loadInputMetaData(node, input, property_info);
        }
    }

    /**
     * Set the meta-data for the specified input based on LiteGraph node property info
     * 
     * @param {Node} node - The MaterialX node parent of the input. If parent is a nodegraph then null is passed in.
     * @param {Input} input - The input to load the meta-data for.
     * @param {Object} property_info - The property info object to load the meta-data into.
     * @returns {void}
     */
    loadInputMetaData(node, input, property_info) {
        if (input && property_info) {

            // Load in basic meta-data
            var colorspace = input.getColorSpace();
            if (colorspace.length > 0)
                property_info['colorspace'] = colorspace;

            var unit = input.getUnit();
            if (unit.length > 0)
                property_info['unit'] = unit;

            var uiname = input.getAttribute('uiname');
            if (uiname.length > 0)
                property_info['uiname'] = uiname;

            var uimin = input.getAttribute('uimin');
            if (uimin.length > 0)
                property_info['uimin'] = uimin;

            var uimax = input.getAttribute('uimax');
            if (uimax.length > 0)
                property_info['uimax'] = uimax;
            var uisoftmin = input.getAttribute('uisoftmin');
            if (uisoftmin.length > 0)
                property_info['uimin'] = uisoftmin;

            var uisoftmax = input.getAttribute('uisoftmax');
            if (uisoftmax.length > 0)
                property_info['uimax'] = uisoftmax;

            var uifolder = input.getAttribute('uifolder');
            if (uifolder.length > 0)
                property_info['uifolder'] = uifolder;

            var basicMetaData = ['colorspace', 'unit', 'uiname', 'uimin', 'uimax', 'uifolder', 'name', 'type', 'output', 'nodename', 'nodegraph'];
            for (var attrName of input.getAttributeNames()) {
                if (!basicMetaData.includes(attrName)) {
                    property_info[attrName] = input.getAttribute(attrName);
                }
            }
            
            if (node && input.getType() == 'filename') 
            {
                let nodeType = node.getType();
                let colorTypes = ['color3', 'color4'];
                //console.log('Load input metadata for:', input.getName(), input.getType(), property_info, nodeType);
                if (colorTypes.includes(nodeType))
                {
                    if (!property_info['colorspace']) {
                        console.log('Auto create "none" colorspace for input:', input.getName());
                        let doc = node.getDocument();
                        let defaultColorSpace = 'none';
                        // For now don't use the document color space as 'none' is more flexible.
                        //let docColorSpace = doc.getAttribute('colorspace');
                        //if (docColorSpace.length > 0)
                        //    defaultColorSpace = docColorSpace;
                        property_info['colorspace'] = defaultColorSpace;
                    }
                }
            } 

            //console.log('load input metadata for:', input.getNamePath(), property_info);
        }
    }

    /** 
     * Builds the LiteGraph graph from the specified MaterialX document.
     * 
     * @param {Document} doc - The MaterialX document to build the graph from.
     * @param {GraphEditor} editor - The graph editor.
     * @param {boolean} auto_arrange - True to auto-arrange the graph, false otherwise.
     * @returns {void}
     */
    buildGraphFromDoc(doc, editor, auto_arrange) {
        let debug = false;
        let loadNodePositions = false; // TODO: Some issues with UI update when setting xpos, ypos. To address.

        //console.log('Build graph from doc. auto_arrange: ', auto_arrange);
        if (!ne_mx) {
            editor.debugOutput("MaterialX is not initialized", 2);
            return;
        }

        editor.clearGraph();

        // Don't try and update the graph while building it
        editor.monitor.monitorGraph(graph, false);

        // Index here is index into litegraph nodes
        var mtlxNodes = [];
        var mtlxNodeDefs = [];

        for (var interfaceInput of doc.getInputs()) {
            var _type = interfaceInput.getType();
            var id = 'mtlx/input/input_' + _type;

            var lg_node = LiteGraph.createNode(id);
            if (lg_node) {
                lg_node.title = interfaceInput.getName();
                if (debug)
                    console.log('Add top level input:', lg_node.title, 'to graph', graph);

                var _value = interfaceInput.getValueString();
                if (_value && _value.length > 0) {
                    if (this.isArray(interfaceInput.getType())) {
                        _value = "[" + _value + "]"
                        _value = JSON.parse(_value);
                    }
                    lg_node.setProperty('in', _value);
                }

                if (loadNodePositions) {
                    var xpos = interfaceInput.getAttribute('xpos');
                    var ypos = interfaceInput.getAttribute('ypos');
                    if (xpos.length > 0 && ypos.length > 0) {
                        lg_node.pos[0] = xpos;
                        lg_node.pos[1] = ypos;
                        //lg_node.flags.collapsed = false;
                    }
                }

                // Make sure size is updated
                lg_node.setSize(lg_node.computeSize());

                graph.add(lg_node);

                //mtlxNodes.push([interfaceInput, lg_node, graph]);                        
            }
        }

        for (var interfaceOutput of doc.getOutputs()) {
            var _type = interfaceOutput.getType()
            var id = 'mtlx/output/output_' + _type;

            var lg_node = LiteGraph.createNode(id);
            if (lg_node) {
                lg_node.title = interfaceOutput.getName();
                graph.add(lg_node);
                if (debug) {
                    console.log('Add graph output:', lg_node.title);
                }

                // Make sure size is updated
                lg_node.setSize(lg_node.computeSize());

                if (loadNodePositions) {
                    var xpos = interfaceOutput.getAttribute('xpos');
                    var ypos = interfaceOutput.getAttribute('ypos');
                    if (xpos.length > 0 && ypos.length > 0)
                        lg_node.pos = [xpos, ypos];
                }

                mtlxNodes.push([interfaceOutput, lg_node, graph]);
            }
        }

        for (var node of doc.getNodes()) {
            var nodeDef = node.getNodeDef();
            if (!nodeDef) {
                editor.debugOutput('Skip node w/o nodedef:' + node.getName(), 1)
                continue;
            }

            // mtlx/pbr/gltf_pbr_surfaceshader                    
            var id = 'mtlx/' + nodeDef.getNodeGroup() + '/' + nodeDef.getName();
            id = id.replace('ND_', '');
            if (debug)
                console.log('Load node:', node.getName(), ' -> ', id);

            var lg_node = LiteGraph.createNode(id);
            if (lg_node) {
                //console.log('LiteGraph node:', lg_node);
                lg_node.title = node.getName();

                graph.add(lg_node);

                // Make sure size is updated
                lg_node.setSize(lg_node.computeSize());

                if (loadNodePositions) {
                    var xpos = node.getAttribute('xpos');
                    var ypos = node.getAttribute('ypos');
                    if (xpos.length > 0 && ypos.length > 0)
                        lg_node.pos = [xpos, ypos];
                }

                mtlxNodes.push([node, lg_node, graph]);
                mtlxNodeDefs.push(nodeDef);
            }
            else {
                editor.debugOutput('Failed to create node:' + node.getName(), 2);
            }
        }

        for (var nodegraph of doc.getNodeGraphs()) {
            if (nodegraph.hasSourceUri()) {
                continue;
            }
            var nodedefAttrib = nodegraph.getAttribute('nodedef');
            if (nodedefAttrib && nodedefAttrib.length > 0) {
                console.log('Skip loading in functional graph:', nodegraph.getName(), 'nodedef:', nodedefAttrib);
                continue;
            }
            if (debug)
                console.log('Create nodegraph:', nodegraph.getName());

            var title = nodegraph.getName();
            var subgraphNode = LiteGraph.createNode("graph/subgraph", title);
            //var subgraph = new LiteGraph.LGraph();
            //subgraphNode._subgraph_node = subgraph;
            //subgraphNode.bgcolor = "#112";
            subgraphNode.bgImageUrl = "./Icons/nodegraph.png";

            var mtlxSubGraphNodes = [];
            for (var interfaceInput of nodegraph.getInputs()) {
                var _type = interfaceInput.getType();
                var id = 'mtlx/input/input_' + _type;

                var lg_node = LiteGraph.createNode(id);
                if (lg_node) {
                    lg_node.title = interfaceInput.getName();
                    this.loadInputMetaData(null, interfaceInput, lg_node.properties_info[0]);
                    subgraphNode.subgraph.add(lg_node);

                    if (debug)
                        console.log('-------- Add subgraph input:', lg_node.title, lg_node);

                    subgraphNode.addInput(interfaceInput.getName(), _type);
                    subgraphNode.subgraph.addInput(interfaceInput.getName(), _type);

                    var _value = interfaceInput.getValueString();
                    if (_value && _value.length > 0) {
                        if (this.isArray(interfaceInput.getType())) {
                            _value = "[" + _value + "]"
                            _value = JSON.parse(_value);
                        }
                        lg_node.setProperty('in', _value);
                    }

                    // Make sure size is updated
                    lg_node.setSize(lg_node.computeSize());

                    if (loadNodePositions) {
                        var xpos = nodegraph.getAttribute('xpos');
                        var ypos = nodegraph.getAttribute('ypos');
                        if (xpos.length > 0 && ypos.length > 0)
                            lg_node.pos = [xpos, ypos];
                    }

                    mtlxSubGraphNodes.push([interfaceInput, lg_node, graph]);
                }
            }

            for (var interfaceOutput of nodegraph.getOutputs()) {
                var _type = interfaceOutput.getType()
                var id = 'mtlx/output/output_' + _type;

                var lg_node = LiteGraph.createNode(id);
                if (lg_node) {
                    lg_node.title = interfaceOutput.getName();
                    subgraphNode.subgraph.add(lg_node);
                    if (debug)
                        console.log('Add subgraph output:', lg_node.title);

                    subgraphNode.addOutput(interfaceOutput.getName(), _type);
                    subgraphNode.subgraph.addOutput(interfaceOutput.getName(), _type);

                    // Make sure size is updated
                    lg_node.setSize(lg_node.computeSize());

                    if (loadNodePositions) {
                        var xpos = interfaceOutput.getAttribute('xpos');
                        var ypos = interfaceOutput.getAttribute('ypos');
                        if (xpos.length > 0 && ypos.length > 0)
                            lg_node.pos = [xpos, ypos];
                    }

                    mtlxSubGraphNodes.push([interfaceOutput, lg_node, graph]);
                }
            }


            for (var node of nodegraph.getNodes()) {
                var nodeDef = node.getNodeDef();
                if (!nodeDef) {
                    editor.debugOutput('Skip node w/o nodedef:' + node.getName(), 1)
                    continue;
                }

                // mtlx/pbr/gltf_pbr_surfaceshader                    
                var id = 'mtlx/' + nodeDef.getNodeGroup() + '/' + nodeDef.getName();
                id = id.replace('ND_', '');

                var lg_node = LiteGraph.createNode(id);
                lg_node.title = node.getName();
                subgraphNode.subgraph.add(lg_node);
                if (debug)
                    console.log('Add subgraph node:', lg_node.title);

                // Make sure size is updated
                lg_node.setSize(lg_node.computeSize());

                if (loadNodePositions) {
                    var xpos = node.getAttribute('xpos');
                    var ypos = node.getAttribute('ypos');
                    if (xpos.length > 0 && ypos.length > 0)
                        lg_node.pos = [xpos, ypos];
                }

                mtlxSubGraphNodes.push([node, lg_node, graph]);
            }

            for (var item of mtlxSubGraphNodes) {
                var node = item[0];
                var lg_node = item[1];
                var parentGraph = item[2];
                var explicitInputs = [];

                // Make sure size is updated
                lg_node.setSize(lg_node.computeSize());

                //console.log('Build connections for subgraog node:', lg_node.title);
                this.buildConnections(editor, node, lg_node, explicitInputs, subgraphNode.subgraph, parentGraph);
            }

            if (debug)
                console.log('Add subgraph:', subgraphNode.title);

            if (auto_arrange > 0) {
                subgraphNode.subgraph.arrange(auto_arrange);
            }

            graph.add(subgraphNode);

        }

        // Build top level connections last after top level nodes
        // and nodegraph have been added.
        var itemCount = 0;
        for (var item of mtlxNodes) {
            var node = item[0];
            var lg_node = item[1];

            // Keep track of explicit inputs
            var explicitInputs = [];
            //console.log('Build connections for:', lg_node.title);
            this.buildConnections(editor, node, lg_node, explicitInputs, graph, null);

            if (lg_node.nodedef_node == 'input' || lg_node.nodedef_node == 'output') {
                continue;
            }

            /* 
            var removeInputs = [];
            var nodeDef = mtlxNodeDefs[itemCount];
            if (nodeDef) {
                for (var nodeDefInput of nodeDef.getActiveInputs()) {
                    var _name = nodeDefInput.getName();
                    if (!explicitInputs.includes(_name)) {
                        removeInputs.push(_name);
                    }
                }
                for (var _name of removeInputs) {
                    var slot = lg_node.findInputSlot(_name);
                    lg_node.inputs[slot].hidden = true; 
                    console.log('Hide input:', _name, '. ', slot, ' on: ', lg_node);
                    //lg_node.removeInput(slot);
                }

                // Make sure size is updated
                lg_node.setSize(lg_node.computeSize());
            }
            */
            itemCount++;
        }

        editor.monitor.monitorGraph(graph, true);

        if (auto_arrange > 0) {
            graph.arrange(auto_arrange);
        }

        graph.setDirtyCanvas(true, true);
        graphcanvas.setDirty(true, true);
    }

    /**
     * Load MaterialX document containing node definitions from a file.
     * 
     * @returns {void}
     */
    loadDefinitionsFromFile() {
        var that = this;

        // Load mtlx document from disk
        var input = document.createElement("input");
        input.style = this.fontSizeStyle;
        input.type = "file";
        input.accept = ".mtlx";
        input.onchange = function (e) {
            var file = e.target.files[0];
            console.log('Loading definitions from file: ' + file.name);

            if (ne_mx) {
                // Load the content from the specified file (replace this with actual loading logic)

                const reader = new FileReader();
                reader.readAsText(file, 'UTF-8');

                reader.onload = function (e) {
                    // Display the contents of the file in the output div
                    let fileContents = e.target.result;
                    //console.log(fileContents);

                    (async () => {
                        try {
                            const readOptions = new ne_mx.XmlReadOptions();
                            readOptions.readXIncludes = false;
                            var customLib = ne_mx.createDocument();

                            await ne_mx.readFromXmlString(customLib, fileContents, '', readOptions);

                            // Create JS from custom library
                            try {
                                console.log('Create custom library definitions')
                                var iconName = '';
                                var scanForIcon = false;
                                if (scanForIcon) {
                                    // Icon name is filename with webp as extension 
                                    var iconName = file.name.replace(/\.[^/.]+$/, ".webp");
                                    // Check if iconName file exists
                                    var iconExists = await that.editor.uriExists(iconName);
                                    if (!iconExists) {
                                        iconName = '';
                                    }
                                }
                                var definitionsList = [];
                                var result = that.createLiteGraphDefinitions(customLib, false, false, definitionsList, 'mtlx', that.editor, iconName);
                                if (result) {
                                    eval(result);
                                    var definitionsListString = definitionsList.join(', ');
                                    that.editor.debugOutput("Registered custom node types: [" + definitionsListString + "]", 0, false);
                                    that.editor.displayNodeTypes();
                                }
                            } catch (e) {
                                console.log('Error evaluating source:', e);
                            }


                            // Keep track of libraries loaded by filename.
                            customlibs.push([file.name, customLib]);

                        } catch (error) {
                            that.editor.debugOutput('Error reading definitions:' + error, 2, false);
                        }
                    })();

                };

            } else {
                that.editor.debugOutput("MaterialX is not initialized", 2);
            }

            //customlibs
        };
        input.click();
    }

    /** 
     * Load graph editor from a string
     * 
     * @param {string} extension - The extension indicating the format of the string.
     * @param {string} fileContents - The document string.  
     * @param {string} fileName - The identifier for the source file, or a arbitrary name.
     * @param {boolean} auto_arrange - True to auto-arrange the graph, false otherwise.
     * @returns {void}
     */
    loadFromString(extension, fileContents, fileName, auto_arrange) {
        if (!ne_mx) {
            console.log('MaterialX is not initialized');
            return;
        }

        // Check if we need to pre-convert from extension type to mtlx
        if (extension != 'mtlx')
        {
            let converter = this.getImporter(extension);
            if (converter) {
                let result = converter.import(ne_mx, fileContents, stdlib);
                if (result) {
                    fileContents = result[0];
                } 
                else {
                    console.log('Failed to convert from:', extension, 'to mtlx. Errors:', result[1]);
                    return;
                }
            }    
            else
            {
                console.log('Failed to find converter from:', extension, 'to mtlx.');
                return;
            }
        }    

        (async () => {
            try {
                const readOptions = new ne_mx.XmlReadOptions();
                readOptions.readXIncludes = false;

                doc.clearContent();

                doc.importLibrary(stdlib);
                for (var item of customlibs) {
                    console.log('Import custom library:', item[0]);
                    doc.importLibrary(item[1]);
                }
                var loadDoc = ne_mx.createDocument();
                await ne_mx.readFromXmlString(loadDoc, fileContents, '', readOptions);

                // Check if nodedef is not in existingDefs
                //
                var customLib = ne_mx.createDocument();
                customLib.copyContentFrom(loadDoc);
                var keepChildren = [];
                var existingDefs = []
                var saveCustomLib = false;
                doc.getNodeDefs().forEach(def => { existingDefs.push(def.getName()); });
                for (var nodedef of loadDoc.getNodeDefs()) {
                    var nodedefName = nodedef.getName();
                    if (!existingDefs.includes(nodedefName)) {
                        keepChildren.push(nodedef.getName());
                        saveCustomLib = true;
                    }
                }
                for (var ng of loadDoc.getNodeGraphs()) {
                    if (ng.getAttribute('nodedef') && ng.getAttribute('nodedef').length > 0) {
                        saveCustomLib = true;
                        keepChildren.push(ng.getName());
                    }
                }

                if (saveCustomLib) {

                    for (var child of customLib.getChildren()) {
                        if (!keepChildren.includes(child.getName())) {
                            //console.log('Remove child:', child.getName());
                            customLib.removeChild(child.getName());
                        }
                    }

                    var additionDefs = [];
                    var result = this.createLiteGraphDefinitions(customLib, true, false, additionDefs, 'mtlx', MxShadingGraphEditor.theEditor);
                    try {
                        eval(result);
                        console.log('Loaded local definitions: ', additionDefs);
                    } catch (e) {
                        console.log('Error evaluating source:', e);
                    }
                }

                doc.copyContentFrom(loadDoc);

                this.validateDocument(doc);
                
                this.buildGraphFromDoc(doc, MxShadingGraphEditor.theEditor, auto_arrange);

                // Must do this after build as build will clear customDocLibs array
                if (saveCustomLib) {
                    customDocLibs.push([fileName, customLib]);
                }

                // Get the document's colorspace and set it as the active colorspace
                var documentColorSpace = doc.getColorSpace();
                this.setSourceColorSpace(documentColorSpace);
                documentColorSpace = this.getSourceColorSpace();
                MxShadingGraphEditor.theEditor.updatePropertyPanel(null);

                // Cleanup document, and get up-to-date contents after any possible upgrade.
                loadDoc.removeAttribute('fileprefix');
                fileContents = ne_mx.writeToXmlString(loadDoc);

                this.validateDocument(loadDoc);

                MxShadingGraphEditor.theEditor.debugOutput('Loaded document: "' + fileName + '"', 0, false);

                // Update mtlx text area
                let documentDisplayUpdater = MxShadingGraphEditor.theEditor.ui.documentDisplayUpdater;
                if (documentDisplayUpdater) {
                    documentDisplayUpdater(fileContents);
                }
                else {
                    console.log('No docDisplayUpdater!!!');
                }

                // Update render items in UI
                let renderableItemUpdater = MxShadingGraphEditor.theEditor.ui.renderableItemUpdater;
                if (renderableItemUpdater) {
                    let renderableItems = this.findRenderableItemsInDoc(doc);
                    if (!renderableItems || renderableItems.length == 0) {
                        MxShadingGraphEditor.theEditor.debugOutput('No renderable items found in graph: ' + fileName, 1, false);
                    }
                    renderableItemUpdater(renderableItems);
                }

            } catch (error) {
                MxShadingGraphEditor.theEditor.debugOutput('Error reading document: ' + fileName + '. Error: ' + error, 2, false);
            }
        })();
    }

    /** 
     * Load graph editor from a file
     * 
     * @param {string} extension - The extension indicating the format of the file.
     * @param {File} file - The file to load the graph from.
     * @param {string} fileName - The identifier for the source file, or a arbitrary name.
     * @param {GraphEditor} editor - The graph editor.
     * @param {boolean} auto_arrange - True to auto-arrange the graph, false otherwise.
     * @returns {void}
     */
    loadFromFile(extension, file, fileName, editor, auto_arrange) {
        var debug = false;

        if (ne_mx) {
            if (!this.loadMaterialXLibraries(stdlib))
                return;

            // Load the content from the specified file (replace this with actual loading logic)

            const reader = new FileReader();
            reader.readAsText(file, 'UTF-8');
            reader.accept = '.mtlx';

            var that = this;
            console.log('loadFromFile:', file, fileName);
            try {
                reader.onload = function (e) {
                    // Display the contents of the file in the output div
                    let fileContents = e.target.result;
                    console.log("read file: ", file.name, " with extension: ", extension, " and length: ", fileContents.length);

                    that.loadFromString(extension, fileContents, fileName, auto_arrange);
                };
            } catch (error) {
                MxShadingGraphEditor.theEditor.debugOutput('Error reading document: ' + fileName + '. Error: ' + error, 2, false);
            }

        } else {
            editor.debugOutput("MaterialX is not initialized", 2, false);
        }
    }

    /** 
     * Load MaterialX definition libraries.
     * 
     * @returns {Document} The MaterialX document containing the standard libraries.
     */
    loadMaterialXLibraries(stdlib) 
    {
        if (stdlib)
            return stdlib;

        if (!ne_mx) {
            MxShadingGraphEditor.theEditor.debugOutput("MaterialX is not initialized", 2);
            return null;
        }

        var generator = new ne_mx.EsslShaderGenerator();
        var genContext = new ne_mx.GenContext(generator);
        {
            stdlib = ne_mx.loadStandardLibraries(genContext);
            console.log('Loaded standard libraries:', stdlib.getNodeDefs().length);
        }

        return stdlib;
    }

    /** 
     * Create a valid MaterialX name within the context of the current graph.
     * 
     * @param {string} name - The name to validate.
     * @param {string} msg - The message to display if the name is invalid.
     * @returns {string} The valid name.
    */
    createValidName(name, msg = null) {
        if (name.length == 0) {
            if (msg) {
                msg = 'Setting empty name as "blank"';
            }
            name = "blank";
        }

        // Get list of all names in graph.
        var graph = graphcanvas.graph;
        var nodes = graph._nodes;
        var nodenames = [];
        for (var node of nodes) {
            nodenames.push(node.title);
        }
        //console.log('Current graph nodes:', nodenames);

        name = ne_mx.createValidName(name);

        if (!nodenames.includes(name)) {
            return name;
        }

        // Get starting number and root name
        var rootName = name;
        var i = 1;
        var number = name.match(/\d+$/);
        if (number) {
            i = (parseInt(number) + 1)
            rootName = name.slice(0, -number[0].length);
        }

        var valid_name = rootName + i.toString();
        while (nodenames.includes(valid_name)) {
            i++;
            valid_name = rootName + i.toString();
        }
        return valid_name;
    }
};

/**
 * @class MxShadingGraphEditor
 * 
 * This class is a wrapper around the LiteGraph library to provide a MaterialX node editor.
 * It is designed to work with the MaterialX JavaScript API.
 */
class MxShadingGraphEditor 
{
    /** 
     * Default constructor. Initializes the handler along with any converters
     */
    constructor() {
        if (!MxShadingGraphEditor.theEditor) {
            MxShadingGraphEditor.theEditor = this;

            this.ui = null;
            this.fontSizeStyle = 'font-size: 11px;';

            this.handler = new MxMaterialXHandler('MaterialX Handler', 'mtlx');
            let gltfConverter = new glTFMaterialX();
            this.handler.addConverter(gltfConverter);
            
            console.log('Create new editor with exporter for:', gltfConverter.exportType());            
            
        }
        return MxShadingGraphEditor.theEditor;
    }

    /**
     * Set the UI callbacks for the editor.
     * 
     * @param {Object} ui - The UI object containing the callbacks.
     * @returns {void}
     */
    setUI(ui) {
        this.ui = ui;
    }

    /**
     * Notify the editor to update it's graph
     */
    setDirty() {
        if (graph)
            graph.setDirtyCanvas(true, true);
        if (graphcanvas) {
            graphcanvas.setDirty(true, true);
            graphcanvas.resize();
        }
    }

    /**
     * Output debug information to the console or the UI console logger.
     * 
     * @param {string} text - The text to output.
     * @param {number} severity - The severity of the message.
     * @param {boolean} clear - True to clear the console, false otherwise.
     * @returns {void}
     */
    debugOutput(text, severity, clear = null) {
        var consoleLog = MxShadingGraphEditor.theEditor.ui.consoleLogger;
        if (consoleLog) {
            consoleLog(text, severity, clear);
        }
        else {
            console.log('> ', text, ' severity:', severity);
        }
    }

    /**
     * Set global color space for the editor.
     * 
     * @param {string} colorSpace - The color space to set.
     * @returns {void}
     */
    setSourceColorSpace(colorSpace) {
        if (this.handler) {
            this.handler.setSourceColorSpace(colorSpace);
        }
    }

    /**
     * Set the global distance unit for the editor.
     * 
     * @param {string} unit - The distance unit to set.
     * @returns {void}
     */
    setTargetDistanceUnit(unit) {
        if (this.handler) {
            this.handler.setTargetDistanceUnit(unit);
        }
    }

    /**
     * Get the global color space for the editor.
     * 
     * @returns {string} The color space.
     */
    getSourceColorSpace() {
        if (this.handler) {
            return this.handler.getSourceColorSpace();
        }
        return 'lin_rec709';
    }

    /**
     * Get the global distance unit for the editor.
     * 
     * @returns {string} The distance unit.
     */
    getTargetDistanceUnit() {
        if (this.handler) {
            return this.handler.getTargetDistanceUnit();
        }
        return 'meter';
    }

    /**
     * Auto layout the nodes in the graph.
     * 
     * @param {number} spacing - The spacing between nodes.
     * @returns {void}
     */
    arrangeGraph(spacing = 80) {
        // This does not track the current subgraph.
        if (graphcanvas) {
            graphcanvas.graph.arrange(spacing);
        }
    }

    /**
     * Open the subgraph for the selected node. The first node selected is used.
     */
    openSubgraph() {
        var selected = graphcanvas.selected_nodes;
        for (var s in selected) {
            var node = selected[s];
            if (node.type == 'graph/subgraph') {
                graphcanvas.openSubgraph(node.subgraph);
                break;
            }
        }
    }

    /**
     * Close the current subgraph open, if any.
     */
    closeSubgraph() {
        if (graphcanvas) {
            graphcanvas.closeSubgraph();
        }
    }

    /**
     * Reset the view of the graph.
     */
    resetView() {
        if (graphcanvas) {
            graphcanvas.ds.reset();
            graphcanvas.setDirty(true, true);
        }
    }

    /**
     * Reset the graph editor. Will also reset the global color space and distance unit
     * to their default values.
     */
    clearGraph() {

        this.handler.sourceColorSpace = this.handler.DEFAULT_COLOR_SPACE;
        this.handler.targetDistanceUnits = this.handler.DEFAULT_DISTANCE_UNITS;
        MxShadingGraphEditor.theEditor.updatePropertyPanel(null);
        this.updatePropertyPanel(null);
        if (graphcanvas) {
            // Set back to top graph
            graphcanvas.setGraph(graph);
            graphcanvas.graph.clear();
            graphcanvas.ds.reset();
            graphcanvas.setDirty(true, true);
        }
        customDocLibs = [];
    }

    /**
     * Use built-in serialization to save the graph to file.
     */
    saveSerialization() {
        var data = JSON.stringify(graph.serialize(), null, 2);
        var blob = new Blob([data], { type: "text/plain" });
        var url = URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = "serialized_graph.json";
        a.click();
    }

    /**
     * Use built-in serialization to load the graph from file.
     */
    loadSerialization() {
        MxShadingGraphEditor.theEditor.clearGraph();

        var input = document.createElement("input");
        input.style = this.fontSizeStyle;
        input.type = "file";
        input.accept = ".json";
        input.onchange = function (e) {
            var file = e.target.files[0];
            var reader = new FileReader();
            reader.onload = function (event) {
                var data = JSON.parse(event.target.result);
                graph.configure(data);
            };
            reader.readAsText(file);
        };
        input.click();
    }

    /** 
     * Save the graph to a file with the specified extension.
     * 
     * @param {string} extension - The extension to save the graph to.
     * @param {Object} graphWriteOptions - The options for writing the graph.
     * @returns {void}
     */
    saveGraphToFile(extension, graphWriteOptions) {
        if (this.handler.canExport(extension)) {
            this.handler.saveGraphToFile(extension, graph, graphWriteOptions);
        }
        else
        {
            this.debugOutput('Unsupported extension for saving graph:' + extension, 2, false);
        }
    }

    /** 
     * Save the graph to a string with the specified extension.
     * 
     * @param {string} extension - The extension to save the graph to.
     * @param {Object} graphWriteOptions - The options for writing the graph.
     */
    saveGraphToString(extension, graphWriteOptions) {
        if (this.handler.canExport(extension)) {
            return this.handler.saveGraphToString(extension, graph, graphWriteOptions);
        }
        else
        {
            this.debugOutput('Unsupported extension for saving graph: ' + extension, 2, false);
            return '';
        }
    }

    /** 
     * Load the graph from a file with the specified extension.
     * Currently only definitions specified using MaterialX are supported.
     * 
     * @param {string} extension - The extension to load the graph from.
     */
    loadDefinitionsFromFile(extension) {
        if (extension == 'mtlx') {
            this.handler.loadDefinitionsFromFile();
        }
        else
        {
            this.debugOutput('Unsupported extension for loading definitions: ' + extension, 2, false);
        }
    }

    /**
     * Load the graph from a file with the specified extension.
     * 
     * @param {string} extension - The extension to load the graph from.
     * @param {boolean} auto_arrange - True to auto-arrange the graph, false otherwise.
     * @returns {void}
     */
    loadGraphFromFile(extension, auto_arrange) {

        if (!this.handler.canImport(extension)) {
            this.debugOutput('Unsupported extension for loading graph: ' + extension, 2, false);
            return;
        }

        // Load document from disk.
        var input = document.createElement("input");
        input.style = this.fontSizeStyle;
        input.type = "file";
        input.accept = "." + this.handler.getExtension();
        input.onchange = function (e) {
            var file = e.target.files[0];
            console.log('Loading file: ' + file.name);
            MxShadingGraphEditor.theEditor.handler.loadFromFile(extension, file, file.name, MxShadingGraphEditor.theEditor, auto_arrange);
        };
        input.click();
    }

    /** 
     * Find all renderable elements in the graph using the handler.
     * 
     * @returns {Array} The list of renderable items.
     */
    findRenderableItems() {
        return this.handler.findRenderableItems(graph);
    }

    /** 
     * Load the graph from a string with the specified extension.
     * 
     * @param {string} extension - The extension to load the graph from.
     * @param {string} content - The content of the graph.
     * @param {string} fileName - The identifier for the source file, or a arbitrary name.
     * @param {boolean} auto_arrange - True to auto-arrange the graph, false otherwise.
     * @returns {void}
     */
    loadGraphFromString(extension, content, fileName, auto_arrange) {
        if (!this.handler.canImport(extension)) {
            this.debugOutput('Unsupported extension for loading graph: ' + extension, 2, false);
            return;
        }

        if (content.length > 0)
            this.handler.loadFromString(extension, content, fileName, auto_arrange);
        else
            MxShadingGraphEditor.theEditor.debugOutput('No content to load', 2, false);
    }

    /**
     * Utility to convert a color from RGB to hex.
     * 
     * @param {Array} rgb - The RGB color to convert.
     * @returns {string} The hex color.
     */
    rgbToHex(rgb) {
        if (!rgb) {
            console.log('rgbToHex empty !', rgb);
            return "#000000";
        }
        return '#' + rgb.map(x => {
            var hex = Math.round(x * 255).toString(16);
            return hex.length === 1 ? '0' + hex : hex;
        }).join('');
    }

    /**
     * Create a DOM button with an image and text.
     * 
     * @param {string} imageSrc - The source of the image.
     * @param {string} text - The text to display.
     * @param {string} id - The identifier for the button.
     * @returns {Element} The button element.
     */
    createButtonWithImageAndText(imageSrc, text, id) {
        // Create image element
        var img = document.createElement("img");
        img.id = id + "_img";
        img.src = imageSrc;
        img.classList.add("img-fluid");

        // Create text element
        var span = document.createElement("span");
        span.id = id + "_text";
        span.textContent = " " + text;

        // Create button element
        var button = document.createElement("button");
        button.id = id;
        button.classList.add("btn", "btn-sm", "btn-outline-secondary", "form-control", "form-control-sm");
        button.style = this.fontSizeStyle;
        button.appendChild(img);
        button.appendChild(span);

        return button;
    }

    /** 
     * Open a dialog to select a image file to load.
     * 
     * @param {Node} theNode - The node to update.
     * @param {string} updateProp - The property to update.
     * @param {boolean} wantURI - True to get the URI, false to get the file.
     */
    openImageDialog(theNode, updateProp, wantURI) {

        // Dynamically create a file input element
        var fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.accept = 'image/*'; // Accept any image file
        fileInput.style.display = 'none';
        document.body.appendChild(fileInput);

        fileInput.click();

        // TODO : Cache the fileURI on the node so can display without loading...
        fileInput.addEventListener('change', function () {
            var fileURI = fileInput.value.split('\\').pop(); // Get the filename without the full path
            var file = fileInput.files[0];
            //if (wantURI)
            fileURI = URL.createObjectURL(file);

            var updateElementId = '__pp:' + updateProp;
            var textInput = document.getElementById(updateElementId);
            //console.log('New filename:', fileURI, 'updateElementId:', updateElementId, 'updateProp:', updateProp);
            textInput.value = fileURI;
            theNode.setProperty(updateProp, fileURI);

            var propertypanel_preview = document.getElementById('propertypanel_preview');
            if (propertypanel_preview) {
                propertypanel_preview.src = URL.createObjectURL(file);
                propertypanel_preview.style.display = "block";
            }

            var previewImage = false;
            if (previewImage) {
                if (propertypanel_preview) {
                    var reader = new FileReader();
                    reader.onload = function (event) {
                        propertypanel_preview.src = event.target.result;
                    };

                    // Read the file as a data URL (base64 encoded string)
                    reader.readAsDataURL(file);
                    propertypanel_preview.style.display = "block";
                }
            }

            document.body.removeChild(fileInput);
        });
    }

    /**
     * Check if a URI exists.
     * 
     * @param {string} uri - The URI to check.
     * @returns {boolean} true if the URI exists, false otherwise.
     */
    uriExists(uri) {
        return fetch(uri)
            .then(response => {
                if (response.ok) {
                    return Promise.resolve(true);
                } else {
                    return Promise.resolve(false);
                }
            })
            .catch(error => {
                console.log('Error checking URI:', error);
                return Promise.resolve(false);
            });
    }

    /**
     * Create a color space input element.
     * 
     * @param {Array} colorSpaces - The list of color spaces.
     * @param {string} activeItem - The selected color space.
     * @returns {Element} The color space input element.
     */
    createColorSpaceInput(colorSpaces, activeItem) {
        var select = document.createElement("select");
        select.className = "form-control form-control-sm";
        select.style = this.fontSizeStyle;
        select.id = "propertypanel_colorspace";
        for (var i = 0; i < colorSpaces.length; i++) {
            var option = document.createElement("option");
            option.value = colorSpaces[i];
            option.text = colorSpaces[i];
            select.add(option);
        }
        // Add "none" option
        var option = document.createElement("option");
        option.value = "none";
        option.text = "none";
        select.add(option);
        
        select.value = activeItem;
        return select;
    }

    /**
     * Create a units input element.
     * 
     * @param {Array} units - The list of units.
     * @param {string} unittype - The type of unit.
     * @param {string} activeItem - The selected unit.
     * @returns {Element} The units input element.
     */
    createUnitsInput(units, unittype, activeItem) {
        var select = document.createElement("select");
        select.className = "form-control form-control-sm";
        select.style = this.fontSizeStyle;
        select.id = "propertypanel_units";
        for (var i = 0; i < units.length; i++) {
            var option = document.createElement("option");
            var unit_pair = units[i];
            if (unit_pair[1] == unittype) {
                option.value = unit_pair[0];
                option.text = unit_pair[0];
                select.add(option);
            }
        }
        select.value = activeItem;
        return select;
    }

    /** 
     * Update the image preview in the property panel.
     * 
     * @param {string} curImage - The image to preview.
     * @returns {void}
     */
    updateImagePreview(curImage) {
        var propertypanel_preview = document.getElementById('propertypanel_preview');
        if (curImage && propertypanel_preview) {
            this.uriExists(curImage)
                .then(exists => {
                    if (exists) {
                        propertypanel_preview.src = curImage;
                        propertypanel_preview.style.display = "block";
                    } else {
                        //propertypanel_preview.style.display = "none";
                        propertypanel_preview.src = "./Icons/no_image.png";
                        propertypanel_preview.style.display = "block";
                        MxShadingGraphEditor.theEditor.debugOutput('Image does not exist: ' + curImage, 1);
                    }
                });
        }
    }

    /** 
     * This method is called when a node is selected in the graph.
     * - It will update the property panel with the properties of the selected node.
     * - If a subgraph is selected, it updates the property panel with the subgraph properties.
     * - If the parent graph is the root and node node is selected, it updates the property panel with the document properties.
     * - If the parent graph is a subgraph and no node is selected, it updates the property panel with the subgraph properties.
     * 
     * @param {Node} node - The selected node in the graph.
     * @returns {void}
    */
    updatePropertyPanel(node) {
        //console.log('Update Panel For:', node);
        var propertypanelcontent = MxShadingGraphEditor.theEditor.ui.propertypanel_content;
        if (!propertypanelcontent) {
            console.error('No property panel content widget found!');
            return;
        }
        // Delete all children
        while (propertypanelcontent.firstChild) {
            propertypanelcontent.removeChild(propertypanelcontent.firstChild);
        }

        // Update icon
        var panelIcon = MxShadingGraphEditor.theEditor.ui.propertypanel_icon;
        if (node && node.nodedef_icon) {
            panelIcon.src = node.nodedef_icon;
        }
        else if (this.ui.icon_map) {
            if (!node)
                panelIcon.src = this.ui.icon_map['_default_graph_'];
            else
                panelIcon.src = this.ui.icon_map['_default_'];
        }

        propertypanelcontent.innerHTML = "";

        let colorSpaces = this.handler.getColorSpaces();
        let targetUnits = this.handler.getUnits();

        if (!node && graphcanvas.graph._subgraph_node) {
            node = graphcanvas.graph._subgraph_node;
            //console.log('In subgraph but no node selected. Select subgraph node', node)
        }
        else if (!node && !graphcanvas.graph._is_subgraph) {
            var docInfo = [['Colorspace', this.getSourceColorSpace()],
            ['Distance', this.getTargetDistanceUnit()]];

            for (let item of docInfo) {

                let elem = document.createElement("div");
                elem.className = "row px-1 py-0";
                let label = document.createElement("div");
                label.className = "col py-0 col-form-label-sm text-left";
                label.style = this.fontSizeStyle;
                label.innerHTML = "<b>" + item[0] + "</b>";
                elem.appendChild(label);

                if (item[0] == 'Colorspace' && colorSpaces.length > 0) {
                    // Create colorspace drop down
                    var inputCol = document.createElement("div");
                    inputCol.className = "col text-left";
                    var select = this.createColorSpaceInput(colorSpaces, item[1]);
                    select.onchange = function (e) {
                        MxShadingGraphEditor.theEditor.setSourceColorSpace(e.target.value);
                    }
                    inputCol.appendChild(select);
                    elem.appendChild(inputCol);
                }
                else if (item[0] == 'Distance' && targetUnits.length > 0) {
                    // Create units drop down
                    var inputCol = document.createElement("div");
                    inputCol.className = "col text-left";
                    var select = this.createUnitsInput(targetUnits, 'distance', item[1]);
                    select.onchange = function (e) {
                        MxShadingGraphEditor.theEditor.setTargetDistanceUnit(e.target.value);
                    }
                    inputCol.appendChild(select);
                    elem.appendChild(inputCol);
                }
                /*                        var inputCol = document.createElement("div");
                    inputCol.className = "col text-left";
                    var nameInput = document.createElement("input");
                    nameInput.type = "text";
                    nameInput.value = item[1];
                    nameInput.className = "form-control form-control-sm";
                    nameInput.disabled = true;
                    elem.appendChild(inputCol);
                    inputCol.appendChild(nameInput);
                }
                */
                propertypanelcontent.appendChild(elem);
            }
            return;
        }

        var _category = node.nodedef_node;
        var _type = node.nodedef_type;

        var isNodeGraph = node.type == 'graph/subgraph';
        if (isNodeGraph) {
            _category = 'nodegraph';
            if (node.outputs) {
                if (node.outputs.length > 1) {
                    _type = 'multi';
                }
                else if (node.outputs.length > 0) {
                    _type = node.outputs[0].type;
                }
            }
            else {
                _type = '';
            }
        }
        else {
            if (_category == 'surfacematerial') {
                _type = '';
            }
        }

        // Identification row
        var elem = document.createElement("div");
        elem.className = "row px-1 py-1";

        // Node category and output type
        var label = document.createElement("div");
        label.className = "col-4 px-1 py-0 col-form-label-sm text-end";
        label.style = this.fontSizeStyle;
        label.innerHTML = "<b>" + _category;
        if (_type.length > 0) {
            label.innerHTML += '<br>' + _type;
        }
        label.innerHTML += "</b>";
        elem.appendChild(label);

        // Node name / title
        var inputCol = document.createElement("div");
        inputCol.className = "col py-0";
        var nameInput = document.createElement("input");
        nameInput.style = this.fontSizeStyle;
        nameInput.type = "text";
        nameInput.value = node.title;
        nameInput.className = "form-control form-control-sm";
        let that = this;
        nameInput.onchange = function (e) {
            var oldTitle = node.title;
            var newTitle = MxShadingGraphEditor.theEditor.handler.createValidName(e.target.value);
            if (newTitle != oldTitle)
            {
                that.monitor.onNodeRenamed(node, newTitle);
                node.title = newTitle;
            } 
            e.target.value = node.title;
            //console.log('node.graph._is_subgraph:', node)
            if (node.graph._is_subgraph) {
                if (node.nodedef_node == 'input') {
                    //console.log('Rename subgraph input:');
                    node.graph.renameInput(oldTitle, node.title);
                }
                else if (node.nodedef_node == 'output') {
                    //console.log('Rename subgraph output:');
                    node.graph.renameOutput(oldTitle, node.title);
                }
            }

            // Note: there is a custom size fo subgraphs.
            node.setSize(node.computeSize());
            node.setDirtyCanvas(true, true);
        }
        inputCol.appendChild(nameInput);

        // TODO: Generate swatches on the fly
        if (node.nodedef_node != 'input' && node.nodedef_node != 'output'
            && node.type != 'graph/subgraph') {
            var imagePreview = document.createElement("img");
            imagePreview.src = "./Icons/no_image.png";
            var previewSet = false;
            //console.log('Check for preview:', node.nodedef_swatch, 'category:', _category)
            imagePreview.style.display = "none";
            imagePreview.src = "./Icons/no_image.png";
            /* if (node.nodedef_swatch && 
                (_type == 'BSDF' || _type == 'EDF' || _type == 'surfaceshader'))
            {
                this.uriExists(node.nodedef_swatch)
                .then(exists => {
                    if (exists) {
                        previewSet = true;
                        imagePreview.style.display = "block";
                        imagePreview.src = node.nodedef_swatch;    
                    } 
                });                
            } */
            imagePreview.id = "propertypanel_preview";
            imagePreview.className = "img-fluid form-control form-control-sm";
            inputCol.appendChild(imagePreview);
        }

        elem.appendChild(label);
        elem.appendChild(inputCol);
        
        // Toggle show/hide of inputs with default values         
        if (!isNodeGraph)
        {
            var filterCol = document.createElement("div");
            filterCol.className = "col-2 py-0";
            filterCol.width = 16;
            var filterIcon = document.createElement("button");
            if (node.showDefaultValueInputs == null)
            {
                node.showDefaultValueInputs = true;
            }
            var img = document.createElement("img");
            if (node.showDefaultValueInputs)
            {
                img.src = "./Icons/funnel_white.svg";
                filterIcon.className = "btn btn-sm btn-outline-secondary";
            }
            else
            {
                img.src = "./Icons/funnel-fill_white.svg";
                filterIcon.className = "btn btn-sm btn-outline-warning";
            }
            filterIcon.appendChild(img);
            filterIcon.onclick = function (e) {
                node.showDefaultValueInputs = !node.showDefaultValueInputs;
                MxShadingGraphEditor.theEditor.updatePropertyPanel(node);
            }
            filterCol.appendChild(filterIcon);
            elem.appendChild(filterCol); 
        }
        
        propertypanelcontent.appendChild(elem);

        var hr = document.createElement("hr");
        hr.classList.add("my-1");
        propertypanelcontent.appendChild(hr);

        var current_details = null;
        var first_details = true;
        var nodeInputs = node.inputs

        let targetNodes = [];
        for (var i in nodeInputs) {
            let nodeInput = nodeInputs[i];

            let inputName = nodeInput.name;
            let nodeInputLink = nodeInput.link;
            let uiName = inputName;
            // remove "_" from uiName
            uiName = uiName.replace(/_/g, ' ');
            let uimin = null;
            let uimax = null;
            let colorspace = '';
            let units = '';
            let defaultgeomprop = '';

            //console.log('Scan input:', inputName, ' on node: ', node.graph);

            let property_info = node.getPropertyInfo(inputName);
            //console.log('1. get property info for i: ', inputName, 'info: ', property_info)

            var skipInterorConnectedInput = false;
            if (node.graph._is_subgraph) {
                // Find input on subgraph node
                //console.log('Check subgraph for link:', node.graph)
                var sg_node = node.graph._subgraph_node;
                if (sg_node) {
                    //console.log('Check for input on sg node', sg_node, node.title);
                    var slot = sg_node.findInputSlot(node.title);
                    if (slot != null) {
                        if (sg_node.inputs) {
                            //property_info = sg_node.properties_info[slot];
                            var slotInput = sg_node.inputs[slot];
                            //console.log('check slot: ', slotInput.link);
                            if (slotInput != null && slotInput.link != null) {
                                skipInterorConnectedInput = true;
                            }
                        }
                        else {
                            //console.log('Error: no subgraph node inputs for subgraph input!', sg_node, node.title);
                        }
                    }
                }
            }

            if (skipInterorConnectedInput) {
                console.log('Skip interior connected input: ', nodeInput);
                continue;
            }

            //console.log('Property info:', property_info, ' for input:', inputName);
            if (property_info) {
                if (property_info.defaultgeomprop)
                {
                    defaultgeomprop = property_info.defaultgeomprop;
                }
                if (property_info.colorspace) {
                    colorspace = property_info.colorspace;
                }
                if (property_info.unit) {
                    units = property_info.unit;
                }
                if (property_info.uiname) {
                    uiName = property_info.uiname;
                }
                if (property_info.uimin) {
                    uimin = property_info.uimin;
                }
                if (property_info.uimax) {
                    uimax = property_info.uimax;
                }
                if (property_info.uifolder && property_info.uifolder.length > 0) {
                    // Create a details element
                    if (current_details == null || current_details.id != property_info.uifolder) {
                        //console.log('Create new details:', property_info.uifolder);
                        current_details = document.createElement("details");
                        current_details.id = property_info.uifolder;
                        current_details.open = first_details;
                        current_details.classList.add('w-100', 'p-1', 'border', 'border-secondary', 'rounded', 'my-1');
                        first_details = false;
                        var summary = document.createElement('summary')
                        summary.style = this.fontSizeStyle;
                        summary.innerHTML = "<b>" + property_info.uifolder + "</b>"
                        //summary.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'btn-block');
                        current_details.appendChild(summary);

                    }
                    else {
                        //current_details = null;
                    }
                }
                else {
                    current_details = null;
                }
                //console.log('2. uiName:', uiName, 'uimin:', uimin, 'uimax:', uimax, 'uiFolder:', property_info.uifolder);
            }
            else {
                current_details = null;
            }

            var elem = null;

            // Check if there is a link
            if (nodeInputLink) {
                let upstreamLink = null;

                let nodegraph = node.graph;
                let link = nodegraph.links[nodeInputLink];
                //console.log('link:', link);
                let linkId = link && link.origin_id;
                let linkNode = linkId && nodegraph.getNodeById(linkId);
                if (linkNode) {


                    //console.log('linkNode:', linkNode);`
                    let linkSlot = link.origin_slot;
                    //console.log('linkSlot:', linkSlot);
                    let linkOutput = linkNode.outputs[linkSlot];
                    //console.log('linkOutput:', linkOutput);
                    upstreamLink = linkNode.title + '.' + linkOutput.name;
                    //console.log('upstreamLink:', upstreamLink);

                    let id = "__pp:" + inputName;
                    let buttonText = upstreamLink;
                    // Truncate long names
                    if (buttonText.length > 15) {
                        buttonText = buttonText.substring(0, 15) + "...";
                    }
                    let input = this.createButtonWithImageAndText("./Icons/arrow_up_white.svg", buttonText, id);

                    input.onclick = function (e) {

                        var inputName = e.target.id;
                        inputName = inputName.replace('__pp:', '');
                        inputName = inputName.replace('_text', '');
                        inputName = inputName.replace('_img', '');
                        console.log('Clicked traversal button:', inputName);

                        console.log('Jump to node:', linkNode.title);
                        graphcanvas.selectNodes([linkNode]);
                        MxShadingGraphEditor.theEditor.updatePropertyPanel(linkNode);
                        node.setDirtyCanvas(true, true);
                    }

                    // Add new row
                    elem = document.createElement("div");
                    elem.className = "row px-1 py-0";

                    input.id = "__pp:" + inputName;

                    var label = document.createElement("div");
                    // invert-button
                    label.className = "col-4 px-1 py-0 col-form-label-sm text-end";
                    label.style = this.fontSizeStyle;
                    label.innerHTML = uiName;
                    label.for = input.id;
                    elem.appendChild(label);

                    // form-control
                    if (useFormControl) {
                        input.classList.add("form-control");
                    }
                    input.classList.add("form-control-sm");
                    // Disable if don't want interaction.
                    if (!graphcanvas.allow_interaction)
                        input.disabled = true;

                    var propvalue = document.createElement("div");
                    propvalue.className = "col p-1";
                    propvalue.appendChild(input);

                    elem.appendChild(propvalue);
                }
            }

            else {  
        
                targetNodes[i] = node;
                let targetNode = targetNodes[i];
                let propertyKey = inputName;

                var property = targetNode.properties[inputName];
                if (property == null) {
                    if (isNodeGraph) {
                        var subgraph = targetNode.subgraph;
                        if (subgraph) {
                            //console.log('Find node by title', inputName, ' in subgraph', subgraph._nodes);
                            var subNode = subgraph.findNodeByTitle(inputName);
                            if (subNode) {
                                targetNodes[i] = subNode;
                                propertyKey = 'in';
                                property = targetNodes[i].properties['in'];
                                //console.log('Route to subgraph target node:', targetNode, targetNode.title, '. ', inputName, ' = ', JSON.stringify(property), 'propkey=', propertyKey);
                            }
                        }
                    }
                    if (property == null) {
                        console.log('Update: Cannot find property value for input:', inputName);
                        continue;
                    }
                }

                // Check if there is a default property value. If so skip showing it
                if (defaultgeomprop)
                {
                    //console.log('Skip input with defaultgeomprop: ' + inputName);
                    continue;
                }

                // Check if property value is same as property info default value
                if (!node.showDefaultValueInputs && !isNodeGraph)
                {
                    let isDefault = node.isDefaultValue(inputName);
                    if (isDefault)
                    {
                        continue;
                    }                
                }

                // Add new row
                elem = document.createElement("div");
                elem.className = "row px-1 py-0";

                var input = null;
                var input_btn = null;
                let input_slider = null;
                var colorspace_unit_btn = null;
                var useFormControl = true;

                // Add colorspace drop-down if specified.
                if (colorspace.length > 0) {
                    // Create drop-down menu to choose colorspace from list stored
                    // in the handler class getColorSpaces() method.
                    //
                    colorspace_unit_btn = this.createColorSpaceInput(colorSpaces, colorspace);
                    let theNode = targetNodes[i];
                    colorspace_unit_btn.onchange = function (e) {

                        theNode.setPropertyInfo(inputName, 'colorspace', e.target.value);
                    }
                }
                else if (units.length > 0 && property_info.unittype) {
                    // Add units drop-down if specified.
                    colorspace_unit_btn = this.createUnitsInput(targetUnits, property_info.unittype, units);
                    let theNode = targetNodes[i];
                    colorspace_unit_btn.onchange = function (e) {
                        theNode.setPropertyInfo(inputName, 'unit', e.target.value);
                    }
                }

                var proptype = nodeInput.type;
                if (proptype == 'float' || proptype == 'integer') {
                    var isFloat = proptype == 'float';

                    input = document.createElement("input");
                    input.id = propertyKey + '_box';
                    input.style = this.fontSizeStyle;
                    input.type = 'number';
                    input.classList.add("form-control", "form-control-sm", "ps-0");
                    input.setAttribute('propertyKey', propertyKey);

                    input_slider = document.createElement("input");
                    input_slider.id = propertyKey + '_slider';
                    //input_slider.style = this.fontSizeStyle;
                    input_slider.type = 'range';
                    input_slider.classList.add('form-range', 'custom-slider', 'pe-0');
                    input_slider.setAttribute('propertyKey', propertyKey);

                    if (uimin) {
                        input.min = uimin;
                    }
                    else {
                        input.min = Math.min(property, 0);
                    }
                    if (uimax) {
                        input.max = uimax;
                    }
                    else {
                        if (isFloat) 
                        {
                            input.max = Math.max(property*3, 10.0);
                        }
                        else {
                            input.max = Math.max(property*3, 100);
                        }
                    }


                    input_slider.min = input.min;
                    input_slider.max = input.max;
                    if (isFloat) {
                        input.step = (input.max - input.min) / 100.0;
                        input_slider.step = input.step;
                    }
                    else {
                        input_slider.step = 1;
                        input.step = 1;
                    }

                    input.value = input_slider.value = property;

                    /* console.log('> ' + propertyKey + ' - Set up slider: min, max, value',
                        input_slider.min, input_slider.max, input_slider.value
                    );
                    console.log('> ' + propertyKey + ' - Set up box: min, max, value',
                        input.min, input.max, input.value
                    ); */

                    let theBox = input;
                    let theSlider = input_slider;
                    let theNode = targetNodes[i];
                    input_slider.onchange = function (e) {
                        var pi = e.target.getAttribute('propertyKey');
                        var val = parseFloat(e.target.value);
                        theNode.setProperty(pi, val);
                        //console.log('Update scalar property:', pi, parseFloat(e.target.value), theNode.title, theNode.properties)
                    }
                    input_slider.oninput = function(e) {
                        var pi = e.target.getAttribute('propertyKey');
                        var val = parseFloat(e.target.value);
                        theNode.setProperty(pi, val);
                        theBox.value = e.target.value;
                    }

                    input.onchange = function (e) {
                        var pi = e.target.getAttribute('propertyKey');
                        var val = parseFloat(e.target.value);
                        theNode.setProperty(pi, val);
                        //console.log('Update scalar property:', pi, parseFloat(e.target.value), theNode.title, theNode.properties)
                    }
                    input.oninput = function(e) {
                        var pi = e.target.getAttribute('propertyKey');
                        var val = parseFloat(e.target.value);
                        theNode.setProperty(pi, val);
                        theSlider.value = e.target.value;
                    }
                }
                else if (proptype == 'string' || proptype == 'filename') {
                    input = document.createElement("input");
                    input.style = this.fontSizeStyle;
                    input.type = "text";
                    if (proptype == 'filename') {
                        var curImage = property;
                        this.updateImagePreview(curImage);

                        input_btn = document.createElement("button");
                        input_btn.classList.add("btn", "btn-sm", "btn-outline-secondary");
                        input_btn.innerHTML = "+";
                        input_btn.setAttribute('propertyKey', propertyKey);
                        var fileId = "__pp:" + inputName;
                        let theNode = targetNodes[i];
                        input_btn.onclick = function (e) {
                            var pi = e.target.getAttribute('propertyKey');
                            MxShadingGraphEditor.theEditor.openImageDialog(theNode, pi, false);
                        }
                    }

                    else 
                    {
                        // Check if there is a 'enm' property
                        console.log('------------------- handle enum property info:', property_info, '. property:', property);
                        if (property_info && property_info.enum) {
                            
                            console.log('----------------- found enum property info:', property_info.enum);

                            // Create drop-down menu to choose from list stored in the handler class.                            
                            input = document.createElement("select");
                            input.style = this.fontSizeStyle;
                            input.classList.add("form-control", "form-control-sm");

                            input.setAttribute('propertyKey', propertyKey);
                            let theNode = targetNodes[i];
                            let enums = property_info.enum;
                            for (let j = 0; j < enums.length; j++) {
                                let option = document.createElement("option");
                                option.value = enums[j];
                                option.text = enums[j];
                                input.add(option);
                            }
                            input.value = property;
                            input.setAttribute('propertyKey', propertyKey);
                            input.onchange = function (e) {
                                var pi = e.target.getAttribute('propertyKey');
                                theNode.setProperty(pi, e.target.value);
                                //console.log('Update string property:', pi, theNode.properties[pi])
                            }
                        }
                    }

                    if (property_info && !property_info.enm) {
                        input.value = property;
                        input.setAttribute('propertyKey', propertyKey);
                        let theNode = targetNodes[i];
                        let isFilename = proptype == 'filename';
                        let that = this;
                        input.onchange = function (e) {
                            var pi = e.target.getAttribute('propertyKey');
                            //theNode.properties[pi] = e.target.value;
                            theNode.setProperty(pi, e.target.value);
                            if (isFilename) {
                                //console.log('Update filename property:', pi, theNode.properties[pi])
                                that.updateImagePreview(e.target.value);
                            }
                            else {
                                //console.log('Update string property:', pi, theNode.properties[pi])
                            }
                        }
                    }
                }
                else if (proptype == 'boolean') {
                    //console.log('Add Boolean property:', property);
                    input = document.createElement("input");
                    input.style = this.fontSizeStyle;
                    input.type = "checkbox";
                    input.classList = "form-check-input";
                    useFormControl = false;
                    input.checked = property;
                    input.setAttribute('propertyKey', propertyKey);
                    let theNode = targetNodes[i];
                    input.onchange = function (e) {
                        var pi = e.target.getAttribute('propertyKey');
                        //theNode.properties[pi] = e.target.checked;
                        theNode.setProperty(pi, e.target.checked);
                        //console.log('Update boolean property:', pi, theNode.properties[pi]);
                    }
                }

                else if (proptype == 'vector2' || proptype == 'vector3' || proptype == 'vector4') 
                {
                    // Find index of proptype in ['vector2', 'vector3', 'vector4' ]
                    var vector_size = ['vector2', 'vector3', 'vector4'].indexOf(proptype) + 2;
                    input = document.createElement("div");
                    useFormControl = false;

                    input.className = "row py-1 ps-4 pe-0";

                    for (let v=0; v<vector_size; v++) 
                    {
                        //console.log('Vector property:[', 0, '] = ', property[0], proptype)
                        let subinput = document.createElement("input");
                        subinput.style = this.fontSizeStyle;
                        subinput.type = 'number';
                        subinput.classList.add("form-control");
                        subinput.classList.add("form-control-sm");
                        subinput.setAttribute('propertyKey', propertyKey);

                        let subinput_slider = document.createElement("input");
                        subinput_slider.id = propertyKey + '_slider';
                        subinput_slider.type = 'range';
                        subinput_slider.classList.add('form-range', 'custom-slider', 'pe-0');
                        subinput_slider.setAttribute('propertyKey', propertyKey);

                        if (uimin) {
                            subinput.min = uimin[v];
                        }
                        else {
                            subinput.min = Math.min(property[v]*3, 0);
                        }
                        if (uimax) {
                            subinput.max = uimax[v];
                        }
                        else {
                            subinput.max = Math.max(property[v]*3, 10.0);
                        }
    
                        subinput_slider.min = subinput.min;
                        subinput_slider.max = subinput.max;
                        subinput.step = (subinput.max - subinput.min) / 100.0;
                        subinput_slider.step = subinput.step;

                        subinput.value = subinput_slider.value = property[v];

                        let theNode = targetNodes[i];
                        let vector_index = v;
                        let theBox = subinput;
                        let theSlider = subinput_slider;
                        theBox.onchange = function (e) {
                            let pi = e.target.getAttribute('propertyKey');
                            let value = parseFloat(e.target.value);
                            let newValue = theNode.properties[pi].map(item => item);
                            newValue[vector_index] = value; 
                            theNode.setProperty(pi, newValue);
                            //theNode.properties[pi][0] = value;
                            //console.log('Update Vector property:"', pi, '"', 0, parseFloat(e.target.value), theNode.properties[pi])
                        }
                        theBox.oninput = function(e) {
                            let pi = e.target.getAttribute('propertyKey');
                            let value = parseFloat(e.target.value);
                            let newValue = theNode.properties[pi].map(item => item);
                            newValue[vector_index] = value; 
                            theNode.setProperty(pi, newValue);
                            theSlider.value = e.target.value;
                        }                        

                        theSlider.onchange = function (e) {
                            let pi = e.target.getAttribute('propertyKey');
                            let value = parseFloat(e.target.value);
                            let newValue = theNode.properties[pi].map(item => item);
                            newValue[vector_index] = value; 
                            theNode.setProperty(pi, newValue);
                            //console.log('Update scalar property:', pi, parseFloat(e.target.value), theNode.title, theNode.properties)
                        }
                        theSlider.oninput = function(e) {
                            let pi = e.target.getAttribute('propertyKey');
                            let value = parseFloat(e.target.value);
                            let newValue = theNode.properties[pi].map(item => item);
                            newValue[vector_index] = value; 
                            theNode.setProperty(pi, newValue);
                            theBox.value = e.target.value;
                        }
    

                        let propvalue_slider = document.createElement("div");
                        propvalue_slider.className = "col p-0";
                        propvalue_slider.appendChild(subinput_slider);

                        let propvalue_box = document.createElement("div");
                        propvalue_box.className = "col p-0";
                        propvalue_box.appendChild(subinput);                                                

                        let input_row = document.createElement("div");
                        input_row.className = "row p-0";
                        input_row.appendChild(propvalue_slider);                        
                        input_row.appendChild(propvalue_box);
    
                        input.appendChild(input_row);
                    }
                }
                else if (proptype == 'color3' || proptype == 'color4') {
                    input = document.createElement("input");
                    input.type = "color";
                    //console.log('set color property:', rgbToHex(property));
                    input.value = this.rgbToHex(property);
                    input.setAttribute('propertyKey', propertyKey);
                    let theNode = targetNodes[i];
                    input.onchange = function (e) {
                        // Convert hex to rgb in 0..1 range
                        var hex = e.target.value;
                        var rgb = [0, 0, 0];
                        rgb[0] = parseInt(hex.substring(1, 3), 16) / 255.0;
                        rgb[1] = parseInt(hex.substring(3, 5), 16) / 255.0;
                        rgb[2] = parseInt(hex.substring(5, 7), 16) / 255.0;

                        var pi = e.target.getAttribute('propertyKey');
                        theNode.setProperty(pi, rgb);
                    }
                    let func = function (e) {
                        // Convert hex to rgb in 0..1 range
                        var hex = e.target.value;
                        var rgb = [0, 0, 0];
                        rgb[0] = parseInt(hex.substring(1, 3), 16) / 255.0;
                        rgb[1] = parseInt(hex.substring(3, 5), 16) / 255.0;
                        rgb[2] = parseInt(hex.substring(5, 7), 16) / 255.0;

                        var pi = e.target.getAttribute('propertyKey');
                        theNode.setProperty(pi, rgb);
                    }
                    input.onchange = func;
                    input.oninput = func;
                }
                else {
                    input = document.createElement("input");
                    input.style = this.fontSizeStyle;
                    input.type = "text";
                    input.value = property;
                    let propertyKey = inputName;
                    let theNode = targetNodes[i];
                    input.onchange = function (e) {
                        theNode.setProperty(propertyKey, e.target.value);
                        //theNode.properties[propertyKey] = e.target.value;
                    }
                }

                if (input) {
                    input.id = "__pp:" + inputName;
                    //console.log('> Add input:', input.id);

                    var label = document.createElement("div");
                    label.className = "col-4 p-0 col-form-label-sm text-end";
                    label.style = this.fontSizeStyle;
                    label.innerHTML = uiName;
                    label.for = input.id;
                    elem.appendChild(label);

                    // form-control
                    if (useFormControl) {
                        input.classList.add("form-control");
                    }
                    input.classList.add("form-control-sm");
                    // Disable if don't want interaction.
                    if (!graphcanvas.allow_interaction)
                        input.disabled = true;

                    var propvalue = document.createElement("div");
                    propvalue.className = "col py-0";
                    if (input_slider)
                    {
                        propvalue.classList.add('ps-1');
                    }
                    propvalue.appendChild(input);

                    if (input_btn) {
                        var propbutton = document.createElement("div");
                        propbutton.className = "col-2 py-0";
                        //console.log('Add input button:', input_btn);
                        propbutton.appendChild(input_btn);
                        elem.appendChild(propbutton);
                    }
                    if (colorspace_unit_btn) {
                        //console.log('Add cs / unit button:', input_btn);
                        var propbutton = document.createElement("div");
                        propbutton.className = "col col-form-label-sm";
                        var details = document.createElement("details");
                        var summary = document.createElement('summary')
                        summary.style = this.fontSizeStyle;
                        if (colorspace.length > 0)
                            summary.innerHTML = "Colorspace";
                        else if (targetUnits.length > 0)
                            summary.innerHTML = "Units";
                        details.appendChild(summary);
                        details.appendChild(colorspace_unit_btn);
                        propbutton.appendChild(details);
                        propvalue.appendChild(propbutton);
                    }

                    if (input_slider)
                    {
                        var propvalue_slider = document.createElement("div");
                        propvalue_slider.className = "col py-0 pe-0";
                        propvalue_slider.appendChild(input_slider);
                        elem.appendChild(propvalue_slider);
                    }    

                    elem.appendChild(propvalue);
                }
            }
            //elem.innerHTML = "<em>" + i  + "</em> : " + property;
            if (elem) {
                if (current_details) {
                    //console.log('3a. append child to details:', current_details.id, elem, inputName);
                    current_details.appendChild(elem);
                    // It current_details not already in the propertypanelcontent, add it.
                    if (current_details.parentElement == null) {
                        propertypanelcontent.appendChild(current_details);
                    }
                }
                else {
                    propertypanelcontent.appendChild(elem);
                    //console.log('3b. append child to parent content:', elem, inputName);
                }
            }
        }

    }


    /**
     * Initialize the LiteGraph graph editor for a given canvas element.
     * 
     * @param {HTMLCanvasElement} canvas The canvas element to use for the graph editor.
     * @returns {void}
     */
    initializeLiteGraph(canvas, readOnly = false) {
        // Initialize LiteGraph
        graph = new LiteGraph.LGraph();
        graphcanvas = new LiteGraph.LGraphCanvas(canvas, graph);

        if (readOnly)
        {
            // Put red border around canvas as an indicator
            //canvas.style.border = "2px solid #ffc107";
            canvas.style.border = "1px solid #ff1107";
        }

        //
        // Set up graph overrides
        //

        // Set up connection colors (off = not connected, on = connected)
        // TODO: Move this to application site and expose settings to user.
        graphcanvas.default_connection_color_byTypeOff = {
            integer: "#A32",
            float: "#161",
            vector2: "#265",
            vector3: "#465",
            vector4: "#275",
            color3: "#37A",
            color4: "#69A",
            matrix33: "#555",
            matrix44: "#666",
            string: "#395",
            filename: "#888",
            boolean: "#060",
        };

        graphcanvas.default_connection_color_byType = {
            integer: "#D52",
            float: "#1D1",
            vector2: "#4D4",
            vector3: "#7D7",
            vector4: "#9D9",
            color3: "#4AF",
            color4: "#6CF",
            matrix33: "#AAA",
            matrix44: "#BBB",
            string: "#3F4",
            filename: "#FFF",
            boolean: "#0F0",
        };

        // Making this a no-op as will not use the default panel
        graphcanvas.onShowNodePanel = function (node) {
            ;  
        }

        // Override to handle node selection
        graphcanvas.onNodeSelected = function (node) {
            if (MxShadingGraphEditor.theEditor.monitor)
            {
                let parentGraph = '';
                var is_subgraph = graphcanvas.graph._is_subgraph;
                if (is_subgraph) 
                    parentGraph = graphcanvas.graph._subgraph_node.title;
                MxShadingGraphEditor.theEditor.monitor.onNodeSelected(node, parentGraph);
            }
            MxShadingGraphEditor.theEditor.updatePropertyPanel(node);
        }

        // Override to handle node deselection
        graphcanvas.onNodeDeselected = function (node) {
            if (MxShadingGraphEditor.theEditor.monitor)
            {
                let parentGraph = '';
                var is_subgraph = graphcanvas.graph._is_subgraph;
                if (is_subgraph) 
                    parentGraph = graphcanvas.graph._subgraph_node.title;
                MxShadingGraphEditor.theEditor.monitor.onNodeDeselected(node, parentGraph);
            }
            MxShadingGraphEditor.theEditor.updatePropertyPanel(null);
        }

        // Add monitoring method for property info changes.
        // This API does not currently exist in LiteGraph, only getPropertyInfo() does.
        LGraphNode.prototype.setPropertyInfo = function(property, propertyInfo, value)
        {
            var info = null;
    
            if (this.properties_info) {
                for (var i = 0; i < this.properties_info.length; ++i) {
                    if (this.properties_info[i].name == property) {
                        info = this.properties_info[i];
                        break;
                    }
                }
            }    
            
            if (info && info[propertyInfo])
            {    
                if (this.onPropertyInfoChanged)
                {
                    this.onPropertyInfoChanged(property, propertyInfo, value, info[propertyInfo]);
                } 
                info[propertyInfo] = value;
            }
            else
            {
                console.warning('Failed to set property: ', property, '. info: ', propertyInfo, '. Value: ', value, '. Infos: ', this.properties_info);
            }
        }

        // Add in a method to check if an input / property is the default value
        LGraphNode.prototype.isDefaultValue = function(property)
        {
            let info = null;

            // Check if the property exists
            if (this.properties[property] == null)
            {
                console.warn('> Property value does not exist:', property);
                return false;
            }
            // Check if the property is linked
            if (this.getInputLink(property))
            {
                return false;
            }
    
            if (this.properties_info != null) 
            {
                for (let i = 0; i < this.properties_info.length; ++i) {
                    if (this.properties_info[i].name == property) {
                        info = this.properties_info[i];
                        break;
                    }
                }
            }    
            
            if (info != null && info.default_value != null)
            {
                let property_string = this.properties[property];
                let default_value_string = info.default_value;
                let isDefault = false;
                if (Array.isArray(default_value_string)) {
                    default_value_string = default_value_string.map(String); // or .map(element => String(element))
                    property_string = property_string.map(String); // or .map(element => String(element))
                    isDefault = (JSON.stringify(default_value_string) == JSON.stringify(property_string));                                 
                }
                else
                {
                    isDefault = (default_value_string == property_string);
                }
                return isDefault;
            }
            else 
            {
                console.warn('> Default value does not exist for:', property);
            }
            return false;
        }

        //
        // Set up graph
        //
        graphcanvas.resize();
        this.monitor.monitorGraph(graph, true);
        graph.arrange(80);

        // Run the graph. TODO: Add execution control.
        //graph.runStep();

        // Override global options
        //graphcanvas.hide_unconnected = false;
        console.log('> Read only mode: ', readOnly);
        graphcanvas.read_only = readOnly;
        graphcanvas.allow_interaction = !readOnly;      // Allow user interaction. TODO: Add option to turn this off
        graphcanvas.allow_dragnodes = !readOnly;        // Allow dragging nodes
        graphcanvas.allow_searchbox = !readOnly;        // Allow search box
        graphcanvas.render_connections_arrows = true;   // Render connection arrows
        graphcanvas.clear_background_color = "#222223"; // Set background color
        graphcanvas.max_zoom = 0.15;                    // Set maximum zoom level
        graphcanvas.connections_width = 2;              // Set connection width
        graphcanvas.render_canvas_border = false;       //  Set canvas border
        graphcanvas.align_to_grid = false;              // Align to grid
        graphcanvas.render_connection_arrows = false;   // Render connection arrows
        graphcanvas.render_curved_connections = true;   // Render curved connections
        //graphcanvas.background_image = null;          // Set background image
        graphcanvas.show_info = false;                  // Turn off HUD
        graph.ctrl_shift_v_paste_connect_unselected_outputs = true;

        //
        // Event handler overrides. TODO: Add more shortcuts
        //
        // Ad event handler to call centerOnNode with f key press within the canvas area
        canvas.addEventListener("keydown", function (e) {
            if (e.key === "f") {
                MxShadingGraphEditor.theEditor.centerNode();
            }
        });

        // Ad event handler to call array with l  key press within the canvas area
        canvas.addEventListener("keydown", function (e) {
            if (e.key === "l") {
                MxShadingGraphEditor.theEditor.arrangeGraph();
            }
        });


        var isIdle = true;
        var context = canvas.getContext('2d');

        function drawstart(event) {
            //context.beginPath();
            //context.moveTo(event.pageX - canvas.offsetLeft, event.pageY - canvas.offsetTop);
            console.log('>>>>>>>>>>> draw start');
            isIdle = false;
        }

        function drawmove(event) {
            if (isIdle) return;
            //context.lineTo(event.pageX - canvas.offsetLeft, event.pageY - canvas.offsetTop);
            //context.stroke();
            console.log('>>>>>>>>>>> draw move');
        }

        function drawend(event) {
            if (isIdle) return;
            drawmove(event);
            console.log('>>>>>>>>>>> draw move');
            isIdle = true;
        }

        function touchstart(event) {
            drawstart(event.touches[0]);
        }

        function touchmove(event) {
            drawmove(event.touches[0]);
            //event.preventDefault();
        }

        function touchend(event) {
            drawend(event.changedTouches[0]);
        }

        //canvas.addEventListener('touchstart', touchstart, false);
        //canvas.addEventListener('touchmove', touchmove, false);
        //canvas.addEventListener('touchend', touchend, false);

        //canvas.addEventListener('mousedown', drawstart, false);
        //canvas.addEventListener('mousemove', drawmove, false);
        //canvas.addEventListener('mouseup', drawend, false);        

    }

    /**
     * Center the graph on a selected node.
     */
    centerNode() {
        var selected = graphcanvas.selected_nodes;
        for (var s in selected) {
            //console.log('Focus on', selected[s]);
            graphcanvas.centerOnNode(selected[s]);
            break;
        }
    }

    /**
     * Remove built in node types, except for subgraph
     */
    clearNodeTypes() {
        LiteGraph.searchbox_extras = [];
        var nodeTypes = LiteGraph.registered_node_types;
        for (var typeName in nodeTypes) {
            if (typeName !== "graph/subgraph") {
                console.log('Removing node type:', LiteGraph.getNodeType(typeName));
                LiteGraph.unregisterNodeType(typeName);
            }
        }
    }

    /**
     * Collapse or expand a node.
     */
    collapseNode(node, collapse) {
        if (node.constructor.collapsable === false) {
            return false;
        }
        if (node.flags.collapsed != collapse) {
            node.flags.collapsed = collapse;
            return true;
        }
        return false;
    }

    /** 
     * Collapse or expand selected nodes.
     */
    collapseExpandNodes(collapse) {
        var curGraph = graphcanvas.graph;

        var selected_nodes = graphcanvas.selected_nodes;
        //console.log('Selected nodes:', selected_nodes);
        var modified = false;
        if (selected_nodes) {
            for (var i in selected_nodes) {
                var node = selected_nodes[i];
                //console.log('Collapse/Expand:', node.title, collapse);
                if (this.collapseNode(node, collapse))
                    modified = true;
            }
        }
        if (!modified) {
            var nodes = curGraph._nodes;
            for (var i in nodes) {
                var node = nodes[i];
                if (this.collapseNode(node, collapse))
                    modified = true;
            }
        }

        if (modified) {
            graph._version++;
            graph.setDirtyCanvas(true, true);
        }
    }

    /**
     * Copy selected nodes to the clipboard.
     */
    copyToClipboard() {
        graphcanvas.copyToClipboard();
    }

    /**
     * Paste nodes from the clipboard.
     */
    pasteFromClipboard() {
        graphcanvas.pasteFromClipboard(true);
    }

    /**
     * Extract the nodes in a subgraph to the main graph.
     */
    extractNodeGraph() {
        var selected = graphcanvas.selected_nodes;
        if (selected.length == 0) {
            console.log('No nodes selected.');
            return;
        }

        var subgraphsSelected = []
        for (var i in selected) {
            var node = selected[i];
            if (node.type == 'graph/subgraph') {
                subgraphsSelected.push(node);
            }
        }
        if (subgraphsSelected.length == 0) {
            console.log('No subgraphs selected.');
            return;
        }

        // Select subgraph nodes
        var subGraph = subgraphsSelected[0];
        var subGraphNodes = subGraph.subgraph._nodes;
        for (var i in subGraphNodes) {
            var node = subGraphNodes[i];
            //console.log('Select subgraph node:', node.title);
        }

        graphcanvas.openSubgraph(subGraph.subgraph);
        graphcanvas.selectNodes(subGraphNodes);
        // Copy the selected nodes to the clipboard
        graphcanvas.copyToClipboard();

        // Paste the copied nodes into the graph
        graphcanvas.closeSubgraph();
        graphcanvas.pasteFromClipboard();
    }

    /**
     * Create a new node subgraph from selected.
     * TODO: Handle connections between new graph and parent graph.
     */
    createNodeGraph() {
        // Disallow testing for now.
        if (graphcanvas.graph._is_subgraph) {
            this.debugOutput('Cannot create nest subgraphs.', 1);
            return;
        }

        // Check for selected nodes
        var selected = graphcanvas.selected_nodes;
        if (selected.length == 0) {
            console.log('No nodes selected.');
            return;
        }

        // Copy the selected nodes to the clipboard
        graphcanvas.copyToClipboard();

        // Create a new graph/subgraph node
        var node = LiteGraph.createNode('graph/subgraph');
        graph.add(node);
        node.title = MxShadingGraphEditor.theEditor.handler.createValidName('group');
        // Open subgraph
        graphcanvas.openSubgraph(node.subgraph);
        // Paste the copied nodes into the subgraph
        graphcanvas.pasteFromClipboard();

        node.subgraph.arrange(80);
        graphcanvas.ds.reset();
        graphcanvas.setDirty(true, true);
    }

    /**
     * Display the available node types in the UI if a UI updater is set.
     */
    displayNodeTypes() {
        // Get the node list display updater
        var nodeTypesListUpdater = this.ui.nodeTypesListUpdater;
        if (!nodeTypesListUpdater) {
            return;
        }

        // Get the list of available node types
        var nodeTypes = LiteGraph.registered_node_types;
        nodeTypesListUpdater(nodeTypes);
    }

    /**
     * Initialize the editor
     * @param {HTMLCanvasElement} canvas The canvas element to use for the graph editor.
     * @param {Object} ui The UI updater object to use for the editor.
     * @param {Object} monitor The monitor object to use for the editor.
     * @param {string} materialFilename The optional filename of the material to load.
     * @param {boolean} readOnly Set to true to make the editor read only.
     * @returns {void}
     */
    initialize(canvas, ui, monitor, materialFilename, readOnly = false) {

        this.setUI(ui);
        if (monitor) {
            console.log('Set custom monitor:', monitor.getName());
        }
        this.monitor = monitor;         
        this.initializeLiteGraph(canvas, readOnly);
        this.handler.initialize(MxShadingGraphEditor.theEditor, materialFilename);
        this.handler.setMonitor(this.monitor);
    }
}
