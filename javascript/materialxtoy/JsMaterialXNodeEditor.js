
// Globals
var mx = null;
var doc = null;
var stdlib = null;
var customlibs = [];
var customDocLibs = [];
var graph = null;
var graphcanvas = null;

// Base Class for Graph Handler
class MxGraphHandler
{
    constructor(id, extension)
    {
        // Identifier
        this.id = id;
        // Extension
        this.extension = extension;
        // Editor
        this.editor = null;

        this.DEFAULT_COLOR_SPACE = 'lin_rec709';
        this.DEFAULT_UNIT = 'meter';
        this.activeColorSpace = this.DEFAULT_COLOR_SPACE;
        this.activeUnit = this.DEFAULT_UNIT;
    }

    setActiveColorSpace(colorSpace)
    {
        if (colorSpace && colorSpace.length > 0)
            this.activeColorSpace = colorSpace;
        else
            this.activeColorSpace = this.DEFAULT_COLOR_SPACE;
    }

    setActiveUnit(unit)
    {
        if (unit && unit.length > 0)
            this.activeUnit = unit;
        else
            this.activeUnit = this.DEFAULT_UNIT;
    }

    getActiveColorSpace()
    {
        return this.activeColorSpace;
    }

    getActiveUnit()
    {
        return this.activeUnit;
    }

    getExtension()
    {
        return this.extension;
    }

    initialize(editor)
    {
        this.editor = editor;
    }

    createValidName(name)
    {
        return name;
    }

    getDefaultValue(value, _type) 
    {
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

    /*
    getDefaultValueRaw(value, _type) {
        if (_type === 'integer' || _type === 'float') {
            if (value.length == 0) {
                value = 0;
            }
        }
        else if (_type === 'string' || _type === 'filename') {
            //value = value + "'";
        }
        else if (isArray(_type)) {
            if (value.length == 0) {
                if (_type === 'color3')
                    value = [0.0, 0.0, 0.0];
                else if (_type === 'color4')
                    value = [0.0, 0.0, 0.0, 0.0];
                else if (_type === 'vector2')
                    value = [0.0, 0.0];
                else if (_type === 'vector3')
                    value = [0.0, 0.0, 0.0];
                else if (_type === 'vector4')
                    value = [0.0, 0.0, 0.0, 0.0];
                else if (_type === 'matrix33')
                    value = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0];
                else if (_type === 'matrix44')
                    value = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0];
            }
            else {
                value = [value];
            }
        }

        if (value.length == 0) {
            //console.log('No value for input:', _name, 'type:', _type, 'value:', value);
            value = "";
        }
        return value;
    }
    */    
};

class MxMaterialXHandler extends MxGraphHandler {
    constructor(id, extension)
    {
        super(id, extension);
    }

    loadMaterialX() {
        return new Promise((resolve, reject) => {
            MaterialX().then((mtlx) => {
                // Save the MaterialX instance to the global variable
                mx = mtlx;
                resolve();
            }).catch((error) => {
                reject(error);
            });
        });
    }

    // Initialize the MaterialX handler for the given editor
    initialize(editor)
    {
        super.initialize(editor);

        if (!mx) {

            this.loadMaterialX().then(() => {

                // Additional logic after MaterialX is loaded
                editor.debugOutput("Loaded MaterialX version:" + mx.getVersionString(), 0, true);
                doc = mx.createDocument();

                var generator = new mx.EsslShaderGenerator();
                var genContext = new mx.GenContext(generator);
                stdlib = mx.loadStandardLibraries(genContext);
                editor.debugOutput('Loaded standard libraries definitions:' + stdlib.getNodeDefs().length, 0, false);

                var definitionsList = [];
                var result = this.createLiteGraphDefinitions(stdlib, false, true, definitionsList, 'mtlx', MxShadingGraphEditor.theEditor);
                var textarea = editor.ui.mtlxlib;
                if (textarea)
                {
                    //console.log('set value', result);
                    textarea.setValue(result);
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

                editor.updatePropertyPanel(null);

            }).catch((error) => {
                editor.debugOutput("Error on initialization:" + error, 2);
            });
        }    
    }

    buildMetaData(colorSpace, unit, unitType, uiname, uimin, uimax, uifolder, _type)
    {
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
            if (uimax)
            {
                uimax = uimax.split(',').map(Number);
            }
        }
        metaData['uimin'] = uimin;
        metaData['uimax'] = uimax;
        metaData['uifolder'] = uifolder;

        // Return struct in an array
        return metaData;
    }

    createLiteGraphDefinitions(doc, debug, addInputOutputs, definitionsList, libraryPrefix='mtlx',
        editor, icon='')
    {
        //var ctor_code = "function loadMaterialXDefinitions(){\n";

        var ctor_code = ""

        console.log('Creating LiteGraph definitions from MaterialX document:', doc);

        // Get the node definitions from the MaterialX document
        var nodeDefs = doc.getNodeDefs();

        if (debug)
            ctor_code += "console.log('Loading MaterialX Definitions...');\n";

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
        /*
        CMAP['float'] = "#753";
        CMAP['color3'] = "#679";
        CMAP['color4'] = "#899";
        CMAP['vector2'] = "#A32";
        CMAP['vector3'] = "#A76";
        CMAP['vector4'] = "#A98";
        CMAP['matrix33'] = "#333";
        CMAP['matrix44'] = "#444";
        CMAP['integer'] = "#A32";
        CMAP['string'] = "#888";
        CMAP['boolean'] = "#48A";
        CMAP['filename'] = "#58E";
        */
        /*
        float: "#753",
        vector2: "#A32",
        vector3: "#A76",
        vector4: "#A98",
        color3: "#679",
        color4: "#899",
        matrix33: "#333",
        matrix44: "#444",
        string: "#888",
        filename: "#58E",
        boolean: "#48A", */

        var inputTypes = ['float', 'color3', 'color4', 'vector2', 'vector3', 'vector4', 'matrix33', 'matrix44', 'integer', 'string', 'boolean', 'filename', 'BSDF', 'EDF', 'VDF', 'surfaceshader', 'volumeshader', 'displacementshader', 'lightshader', 'material', 'vector2array'];
        var outputTypes = ['float', 'color3', 'color4', 'vector2', 'vector3', 'vector4', 'matrix33', 'matrix44', 'integer', 'string', 'boolean', 'filename', 'BSDF', 'EDF', 'VDF', 'surfaceshader', 'volumeshader', 'displacementshader', 'lightshader', 'material', 'vector2array'];

        // TODO: Support tokens
        var supporTokens = false;
        if (supporTokens)
        {
            inputTypes.push('token');
            TMAP['token'] = 'string';
        }

        const INPUT_ND = 'ND_input_';
        const OUTPUT_ND = 'ND_output_';
        const INPUT_NODE_STRING = 'input';
        const OUTPUT_NODE_STRING = 'output';
        const LIBRARY_ICON = editor.ui.icon_map['_default_'];

        // Register inputs (which have no nodedef)
        if (addInputOutputs)
        {
            for (var _type of inputTypes) {
                var id = libraryPrefix + '/input/input_' + _type;
                var functionName = mx.createValidName(id);
                var titleName = 'input_' + _type;
                ctor_code += "\n// MaterialX node type: " + id + "\n//\n";
                ctor_code += "function " + functionName + "() {\n";
                {
                    ctor_code += "  this.nodedef_icon = '" + LIBRARY_ICON + "';\n";
                    ctor_code += "  this.nodedef_name = '" + INPUT_ND + _type + "';\n";
                    ctor_code += "  this.nodedef_node = '" + INPUT_NODE_STRING + "';\n";
                    ctor_code += "  this.nodedef_type = '" + _type + "';\n";
                    ctor_code += "  this.nodedef_group = '" + INPUT_NODE_STRING + "';\n";
                    if (_type == 'token')
                        _type = 'string';
                    ctor_code += "  this.addInput('in', '" + TMAP[_type] + "');\n";
                    var value = this.getDefaultValue('', _type);
                    var metaData = this.buildMetaData('', '', '', '', null, null, '', null);
                    metaData = JSON.stringify(metaData);
                    ctor_code += "  this.addProperty('in', " + value + ", '" + _type + "'," + metaData + ");\n";
                    ctor_code += "  this.addOutput('out', '" + TMAP[_type] + "');\n";

                    ctor_code += "  this.title = '" + titleName + "';\n"
                    var desc = '"MaterialX:' + id + '"';
                    ctor_code += "  this.desc = " + desc + ";\n";

                    var onNodeCreated = "function() {\n";
                    onNodeCreated += "    //console.log('Node created:', this);\n";
                    onNodeCreated += "  }";
                    ctor_code += "  this.onNodeCreated = " + onNodeCreated + "\n";
                    var onRemoved = "function() {\n";
                    onRemoved += "    //console.log('Node removed:', this);\n";
                    onRemoved += "  }";
                    ctor_code += "  this.onRemoved = " + onRemoved + "\n";

                    ctor_code += "  this.color = '#004C94';\n";
                    ctor_code += "  this.bgcolor = '#000';\n";
                    if (_type in CMAP)
                    {
                        ctor_code += "  this.boxcolor = '" + CMAP[_type] + "';\n";
                    }    
                    ctor_code += "  this.shape = LiteGraph.ROUND_SHAPE;\n";

                    ctor_code += "  this.onExecute = function() {\n";
                    ctor_code += "    console.log('Executing node: ', this);\n";
                    ctor_code += "  }\n";
                }
                ctor_code += "}\n"
                ctor_code += "LiteGraph.registerNodeType('" + id + "', " + functionName + ");\n";                
            }

            // Register outputs (which have no nodedef)
            for (var _type of outputTypes) {
                var id = libraryPrefix + '/output/output_' + _type;
                var functionName = mx.createValidName(id);
                var titleName = 'output_' + _type;
                ctor_code += "\n// MaterialX node type: " + id + "\n//\n";
                ctor_code += "function " + functionName + "() {\n";
                {
                    ctor_code += "  this.title = '" + titleName + "';\n"
                    var desc = '"MaterialX Node :' + id + '"';
                    ctor_code += "  this.desc = " + desc + ";\n";

                    ctor_code += "  this.nodedef_icon = '" + LIBRARY_ICON + "';\n";
                    ctor_code += "  this.nodedef_name = '" + OUTPUT_ND + + _type + "';\n";
                    ctor_code += "  this.nodedef_node = '" + OUTPUT_NODE_STRING + "';\n";
                    ctor_code += "  this.nodedef_type = '" + _type + "';\n";
                    ctor_code += "  this.nodedef_group = '" + OUTPUT_NODE_STRING + "';\n";
                    ctor_code += "  this.addInput('in', '" + TMAP[_type] + "');\n";
                    var value = this.getDefaultValue('', _type);
                    ctor_code += "  this.addProperty('in', " + value + ", '" + _type + "');\n";
                    ctor_code += "  this.addOutput('out', '" + TMAP[_type] + "');\n";

                    var onNodeCreated = "function() {\n";
                    onNodeCreated += "  //console.log('Node created:', this);\n";
                    onNodeCreated += "  }";
                    ctor_code += "  this.onNodeCreated = " + onNodeCreated + "\n";
                    var onRemoved = "function() {\n";
                    onRemoved += "  //console.log('Node removed:', this);\n";
                    onRemoved += "  }";
                    ctor_code += "  this.onRemoved = " + onRemoved + "\n";

                    ctor_code += "  this.color = '#004C94';\n";
                    ctor_code += "  this.bgcolor = '#000';\n";
                    if (_type in CMAP)
                    {
                        ctor_code += "  this.boxcolor = '" + CMAP[_type] + "';\n";
                    }    
                    ctor_code += "  this.shape = LiteGraph.ROUND_SHAPE;\n";
                    
                    ctor_code += "  this.onExecute = function() {\n";
                    ctor_code += "  console.log('Executing node:', this);\n";
                    ctor_code += "  }\n";
                }
                ctor_code += "}\n"
                ctor_code += "LiteGraph.registerNodeType('" + id + "', " + functionName + ");\n";
                definitionsList.push(id);
            }
        }

        // Iterate over all node definitions
        for (var nodeDef of nodeDefs) {

            var nodeDefName = nodeDef.getName();
            var id = libraryPrefix + '/' + nodeDef.getNodeGroup() + '/' + nodeDefName;
            id = id.replace('ND_', '');
            var functionName = mx.createValidName(id);
            var nodeType = nodeDef.getType();
            var titleName = nodeDef.getNodeString() + "_" + nodeType;
            var swatchLocation = 'https://materialx.nanmucreative.com/resources/mtlx/nodedef_materials/';
            var outputs = nodeDef.getActiveOutputs();
            var outputName = outputs[0].getName(); // TODO: Handle swatch for multiple outputs
            var swatchId =  swatchLocation + 'material_' + nodeDefName + '_' + outputName + '_genglsl.png';
            swatchId = swatchId.replace('ND_', '');
            if (debug)
                console.log('\n--- Registering node type:', id, '----');                

            ctor_code += "\n// MaterialX node type: " + id + "\n//\n";
            ctor_code += "function " + functionName + "() {\n";
            {
                var nodeGroup = nodeDef.getNodeGroup();
                var nodeString = nodeDef.getNodeString();
                var theIcon = icon;
                if (theIcon.length == 0)
                {
                    for (var key in editor.ui.icon_map)
                    {
                        if (nodeString.toLowerCase().startsWith(key.toLowerCase()))
                        {
                            theIcon = editor.ui.icon_map[key];
                            //console.log('set icon:', theIcon, 'for:', key, nodeString);
                            break;
                        }
                        else if (nodeGroup.toLowerCase().startsWith(key.toLowerCase()))
                        {
                            theIcon = editor.ui.icon_map[key];
                            //console.log('set icon:', theIcon, 'for:', key, nodeGroup);
                            break;
                        }
                    }
                }

                ctor_code += "  this.nodedef_icon = '" + theIcon + "';\n";
                ctor_code += "  this.nodedef_name = '" + nodeDefName + "';\n";
                ctor_code += "  this.nodedef_type = '" + nodeType + "';\n";
                ctor_code += "  this.nodedef_node = '" + nodeString + "';\n";
                ctor_code += "  this.nodedef_href = 'https://materialx.nanmucreative.com/documents/definitions/" + nodeString + ".html';\n";
                ctor_code += "  this.nodedef_swatch = '" + swatchId + "';\n";
                ctor_code += "  this.nodedef_group = '" + nodeGroup + "';\n";

                for (var input of nodeDef.getActiveInputs()) {
                    var _name = input.getName();
                    var _type = input.getType();
                    if (_type in TMAP)
                        _type = TMAP[_type];
                    else
                        console.log('Unmappable type:', _type)
                    ctor_code += "  this.addInput('" + _name + "','" + _type + "');\n";

                    var value = input.getValueString();
                    value = this.getDefaultValue(value, _type);
                    var uiname = input.getAttribute('uiname');
                    var uimin = input.getAttribute('uimin');
                    if (uimin.length == 0)
                    {
                        uimin = null;
                    }
                    var uimax = input.getAttribute('uimax');
                    if (uimax.length == 0)
                    {
                        uimax = null;
                    }
                    var uifolder = input.getAttribute('uifolder');
                    var metaData = this.buildMetaData('', '', '', uiname, uimin, uimax, uifolder, _type);
                    metaData = JSON.stringify(metaData);
                    ctor_code += "  this.addProperty('" + _name + "', " + value + ", '" + _type + "'," + metaData + ");\n";
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
                    ctor_code += "  this.addOutput('" + _name + "','" + _type + "');\n";
                }

                ctor_code += "  this.title = '" + titleName + "';\n"
                var desc = '"MaterialX:' + id + '"';
                ctor_code += "  this.desc = " + desc + ";\n";

                var onNodeCreated = "function() {\n";
                onNodeCreated += "  //console.log('Node created:', this);\n";
                onNodeCreated += "}";
                ctor_code += "  this.onNodeCreated = " + onNodeCreated + "\n";
                var onRemoved = "function() {\n";
                onRemoved += "  //console.log('Node removed:', this);\n";
                onRemoved += "  }";
                ctor_code += "  this.onRemoved = " + onRemoved + "\n";

                // Set the background color to slate grey
                ctor_code += "  this.bgcolor = '#111';\n";
                //console.log('Node group:', nodeGroup, nodeDefName);
                if (nodeGroup == 'conditional')
                {
                    //console.log('Cond Node group:', nodeGroup)
                    ctor_code += "  this.color = '#532200';\n";     
                    ctor_code += "  this.title_text_color = '#000';\n";               
                    ctor_code += "  this.shape = LiteGraph.CARD_SHAPE;\n";
                }
 
                else if (nodeString != 'convert' && 
                        (nodeGroup == 'shader' || nodeType == 'surfaceshader' || nodeType == 'volumshader' || nodeType == 'displacementshader'))
                {
                    ctor_code += "  this.color = '#232';\n";                        
                    ctor_code += "  this.shape = LiteGraph.ROUND_SHAPE;\n";
                }
                else if (nodeGroup == 'material')
                {
                    ctor_code += "  this.color = '#151';\n";                        
                    ctor_code += "  this.shape = LiteGraph.BOX_SHAPE;\n";                    
                }
                else 
                {
                    ctor_code += "  this.color = '#222';\n";
                    ctor_code += "  this.shape = LiteGraph.ROUND_SHAPE;\n";
                }
                if (nodeType in CMAP)
                {
                    ctor_code += "  this.boxcolor = '" + CMAP[nodeType] + "';\n";
                }
            }
            ctor_code += "}\n"

            // Register the node type
            ctor_code += functionName + ".nodedef_name = '" + nodeDefName + "';\n";
            ctor_code += functionName + ".nodedef_node = '" + nodeString + "';\n";
            ctor_code += functionName + ".nodedef_href = 'https://materialx.nanmucreative.com/documents/definitions/" + nodeString + ".html';\n";

            ctor_code += "LiteGraph.registerNodeType(" + "'" + id + "'," + functionName + ");\n";
            definitionsList.push(id);
            if (debug)
                ctor_code += "console.log('Registered node type:', '" + id + "');\n";
        }

        //ctor_code += "}\n";
        return ctor_code;
    }

    validateDocument(doc)
    {
        var errors = {};
        var valid = doc.validate(errors);
        if (!valid) {
            this.editor.debugOutput('Failed to validate document:\n' + errors.message, 2);
        }
    }

    writeGraphToString(graph, writeCustomLibs = true, saveNodePositions = false) 
    {
        if (!mx) {
            this.editor.debugOutput("MaterialX is not initialized", 2);
            return;
        }

        var outputDoc = mx.createDocument();
        
        if (!stdlib) {
            var generator = new mx.EsslShaderGenerator();
            var genContext = new mx.GenContext(generator);
            stdlib = mx.loadStandardLibraries(genContext);
        }

        // Handle top level
        this.writeGraphToDocument(outputDoc, graph, saveNodePositions);

        if (writeCustomLibs)
        {
            console.log('Write custom libraries:', customlibs.length);
            for (var customlib of customlibs)
            { 
                outputDoc.importLibrary(customlib[1]);
            }
            console.log('Write document custom definitions:', customDocLibs.length);
            for (var customDocLib of customDocLibs)
            {
                outputDoc.importLibrary(customDocLib[1]);
            }
        }

        // TODO: Add in another other globals
        outputDoc.setColorSpace(this.getActiveColorSpace());
        outputDoc.removeAttribute('fileprefix');

        this.validateDocument(outputDoc);

        const writeOptions = new mx.XmlWriteOptions();
        writeOptions.writeXIncludeEnable = false;
        var result = false;
        try {
            var result = mx.writeToXmlString(outputDoc, writeOptions);
        } catch (e) {
            this.editor.debugOutput("Failed to write graph:" + e, 2);
        }
        return result;
    }

    saveGraphToString(graph, writeCustomLibs = true, saveNodePositions = false) {
        if (!mx) {
            this.editor.debugOutput("MaterialX is not initialized", 2);
            return;
        }

        var data = this.writeGraphToString(graph, writeCustomLibs, saveNodePositions);

        return data;
    }

    saveGraphToFile(graph, saveCustomLibs = true, saveNodePositions = false) {
        var data = this.saveGraphToString(graph, saveCustomLibs, saveNodePositions);
        if (!data) {
            return;
        }

        var blob = new Blob([data], { type: "text/plain" });
        var url = URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = "output_graph.mtlx";
        a.click();
    }

    writeGraphToDocument(mltxgraph, graph, saveNodePositions = false) {

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
                this.writeGraphToDocument(subgraphNode, subgraph, saveNodePositions);
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
                    if (saveNodePositions)
                    {
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

            // Add inputs
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
            if (node_inputs) {

                var inputs = node_inputs;
                for (var i in inputs) {
                    var input = inputs[i];
                    if (debug)
                        console.log('---- Write port:', input);
    
                    var inputName = input.name;
                    var inputType = input.type;
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
                    if (isInputNode && node.graph._subgraph_node)
                    {
                        nodeToCheck = node.graph._subgraph_node;
                        for (var i=0; i<nodeToCheck.inputs.length; i++)
                        {
                            var nci = nodeToCheck.inputs[i];
                            if (nci.name == node.title) {
                                inputNode = nodeToCheck.getInputNode(i);
                                inputLink = nodeToCheck.getInputLink(i);
                                //console.log('--- Found parent input:', nci.name, 'inputNode:', inputNode, 'inputLink:', inputLink);
                                break;
                            }
                        }
                    }
                    else
                    {
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
                            {
                                if (inputNode.nodedef_node == 'input') {
                                    inputElement.setInterfaceName(inputNode.title);
                                }
                                else {
                                    inputElement.setNodeName(inputNode.title);
                                    // TODO: Need to check that upstream has > 1 output.
                                    // Put up an issue that this is really annoying to
                                    // disallow an explicit output in validation !!! 
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
                                    // TODO: Seems that c+paste adds same input > once ???
                                    console.log('Error> Trying add input more than once:', inputName, ' to node: ', nodeElement.getNamePath());
                                }
                            }
                            else {
                                inputElement = nodeElement;
                            }
                            inputElement.setValueString(inputValue, inputType);
                        }
                    }

                    if (inputElement)
                    {
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
                        if (propInfo)
                        {
                            //console.log('Scan propinfo:', propInfo, 'for input:', inputElement.getNamePath(), 'prop_info:', propInfo);

                            // Write node_properties metadata to input
                            for (var propAttribute in propInfo)
                            {
                                if (skip_attributes.includes(propAttribute))
                                    continue;
                                
                                //console.log('-- scan attrib:', propAttribute);
                                var propAttributeValue = propInfo[propAttribute];
                                if (propAttributeValue && propAttributeValue.length > 0)
                                {
                                    //console.log('---- save attribute:', propAttribute, propAttributeValue, 'on input:', inputElement.getNamePath());
                                    inputElement.setAttribute(propAttribute, propAttributeValue);
                                }                                                
                            }                     
                        }       
                    }
                }

                if (debug)
                    console.log('---- END Write inputs:', node.inputs);
            }

            // Add outputs
            if (node.outputs) {
                /*
                var outputs = node.outputs;
                for (var i in outputs)
                {
                    var output = outputs[i];
                    var outputName = output.name;
                    var outputType = output.type;
                    var outputElement = nodeElement.addOutput(outputName, outputType);
                }
                */
            }

            if (debug)
                console.log('---> End write node', node.title);
        }

        if (debug)
            console.log('***** END Scan Graph:', graph.title);
    }

    isArray(_type) {
        var ARRAY_TYPES = ['color3', 'color4', 'vector2', 'vector3', 'vector4', 'matrix33', 'matrix44'];
        if (ARRAY_TYPES.includes(_type)) {
            return true;
        }
        return false;
    }

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
                if (isInput && graph._subgraph_node)
                {
                    target_node = graph._subgraph_node;
                    target_slot = target_node.findInputSlot(lg_node.title);
                    // Go up to parent graph
                    graphToCheck = parentGraph;
                    //console.log(' go up to parent graph:', graphToCheck,
                    //    'from:', graph, 'subgraph:', graph._subgraph_node,
                    //'target_node:', target_node.title, 'target_slot:', target_slot);

                    // Need to scan parent graph here if interfacename and input
                    /* for (var p = 0; p < parentGraph._nodes.length; ++p) {
                        console.log('local check graph node title', parentGraph._nodes[p].title, source_name);
                        if (parentGraph._nodes[p].title == source_name) {
                            source_node = parentGraph._nodes[p];
                            break;
                        }
                    } */
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
                        if (!linkInfo)
                        {
                            editor.debugOutput('Failed to connect:' + source_node.title + '.' + outputName, '->', target_node.title + '.' + _name), 1, false;
                        }
                    }
                    //console.log('CONNECT START: source[', source_node.title, '.', source_slot,
                    //    '] --> target[:', target_node.title, ".", target_slot);
                    var linkInfo = null;
                    if (source_slot == null || target_slot == null || target_node == null)
                    {
                        console.warning('Cannot connect!')
                    } 
                    else 
                    {
                        linkInfo = source_node.connect(source_slot, target_node, target_slot);
                    }
                    if (!linkInfo) 
                    {
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
                        _value = "[" + _value + "]"
                        _value = JSON.parse(_value);
                    }
                    
                    //console.log('-- Value Input:', 
                    //lg_node.title + "." + _name, 'value:', _value);
                    lg_node.setProperty(_name, _value);
                }
            }

            var property_info = lg_node.getPropertyInfo(_name);
            this.loadInputMetaData(input, property_info);
        }
    }

    loadInputMetaData(input, property_info)
    {
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
            
            var uifolder = input.getAttribute('uifolder');
            if (uifolder.length > 0)
                property_info['uifolder'] = uifolder;  

            var basicMetaData = ['colorspace', 'unit', 'uiname', 'uimin', 'uimax', 'uifolder', 'name', 'type', 'output', 'nodename', 'nodegraph'];
            for (var attrName of input.getAttributeNames())
            {
                if (!basicMetaData.includes(attrName)) {
                    property_info[attrName] = input.getAttribute(attrName);
                }
            }

            //console.log('load input metadata for:', input.getNamePath(), property_info);
        }
    }

    buildGraphFromDoc(doc, editor, auto_arrange) {
        var debug = false;

        //console.log('Build graph from doc. auto_arrange: ', auto_arrange);
        if (!mx) {
            editor.debugOutput("MaterialX is not initialized", 2);
            return;
        }

        editor.clearGraph();

        // Don't try and update the graph while building it
        editor.monitorGraph(graph, false);
      
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

                var xpos = interfaceInput.getAttribute('xpos');
                var ypos = interfaceInput.getAttribute('ypos');
                if (xpos.length > 0 && ypos.length > 0)
                {
                    ;//lg_node.pos[0] = xpos;
                    ;//lg_node.pos[1] = ypos;
                }
                //lg_node.flags.collapsed = false;

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
                if (debug)
                {
                    console.log('Add graph output:', lg_node.title);
                }

                // Make sure size is updated
                lg_node.setSize(lg_node.computeSize());

                var xpos = interfaceOutput.getAttribute('xpos');
                var ypos = interfaceOutput.getAttribute('ypos');
                if (xpos.length > 0 && ypos.length > 0)
                    ;//lg_node.pos = [xpos, ypos];

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

                var xpos = node.getAttribute('xpos');
                var ypos = node.getAttribute('ypos');
                if (xpos.length > 0 && ypos.length > 0)
                    ;//lg_node.pos = [xpos, ypos];

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
            if (nodedefAttrib && nodedefAttrib.length > 0)
            {
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
            subgraphNode.bgImageUrl = "./Images/nodegraph.png";

            var mtlxSubGraphNodes = [];
            for (var interfaceInput of nodegraph.getInputs()) {
                var _type = interfaceInput.getType();
                var id = 'mtlx/input/input_' + _type;

                var lg_node = LiteGraph.createNode(id);
                if (lg_node) {
                    lg_node.title = interfaceInput.getName();
                    this.loadInputMetaData(interfaceInput, lg_node.properties_info[0]);       
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
                    
                    var xpos = nodegraph.getAttribute('xpos');
                    var ypos = nodegraph.getAttribute('ypos');
                    if (xpos.length > 0 && ypos.length > 0)
                        ; // lg_node.pos = [xpos, ypos];

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

                    var xpos = interfaceOutput.getAttribute('xpos');
                    var ypos = interfaceOutput.getAttribute('ypos');
                    if (xpos.length > 0 && ypos.length > 0)
                        ; // lg_node.pos = [xpos, ypos];

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

                var xpos = node.getAttribute('xpos');
                var ypos = node.getAttribute('ypos');
                if (xpos.length > 0 && ypos.length > 0)
                    ; // lg_node.pos = [xpos, ypos];

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

            if (auto_arrange > 0)
            {
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

            if (lg_node.nodedef_node == 'input' || lg_node.nodedef_node == 'output') 
            {
                continue;
            }

            var removeInputs = [];
            var nodeDef = mtlxNodeDefs[itemCount];
            if (nodeDef)
            {
                for (var nodeDefInput of nodeDef.getActiveInputs()) {
                    var _name = nodeDefInput.getName();
                    if (!explicitInputs.includes(_name)) {
                        removeInputs.push(_name);
                    }
                }
                for (var _name of removeInputs) {
                    var slot = lg_node.findInputSlot(_name);
                    //console.log('Remove input:', _name, ' on: ', lg_node);
                    lg_node.removeInput(slot);
                }

                // Make sure size is updated
                lg_node.setSize(lg_node.computeSize());
            }
            itemCount++;
        }

        editor.monitorGraph(graph, true);

        if (auto_arrange > 0)
        {
            graph.arrange(auto_arrange);
        }

        graph.setDirtyCanvas(true, true);
        graphcanvas.setDirty(true, true);
    }

    loadDefinitionsFromFile()
    {
        var that = this;

        // Load mtlx document from disk
        var input = document.createElement("input");
        input.type = "file";
        input.accept = ".mtlx";
        input.onchange = function (e) {
            var file = e.target.files[0];
            console.log('Loading definitions from file: ' + file.name);
            
            if (mx) {
                // Load the content from the specified file (replace this with actual loading logic)
    
                const reader = new FileReader();
                reader.readAsText(file, 'UTF-8');
    
                reader.onload = function (e) {
                    // Display the contents of the file in the output div
                    let fileContents = e.target.result;
                    //console.log(fileContents);
    
                    (async () => {
                        try {
                            const readOptions = new mx.XmlReadOptions();
                            readOptions.readXIncludes = false;
                            var customLib = mx.createDocument();
    
                            await mx.readFromXmlString(customLib, fileContents, '', readOptions);

                            // Create JS from custom library
                            try {
                                console.log('Create custom library definitions')
                                var iconName = '';
                                var scanForIcon = false;
                                if (scanForIcon)
                                {
                                    // Icon name is filename with webp as extension 
                                    var iconName = file.name.replace(/\.[^/.]+$/, ".webp");
                                    // Check if iconName file exists
                                    var iconExists = await that.editor.uriExists(iconName);
                                    if (!iconExists) {
                                        iconName = '';
                                    } 
                                }
                                var definitionsList = [];
                                var result = that.createLiteGraphDefinitions(customLib, false, false, definitionsList , 'mtlx', that.editor, iconName);
                                if (result)
                                {
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

    loadFromString(fileContents, fileName, auto_arrange) 
    {
        (async () => {
            try {
                const readOptions = new mx.XmlReadOptions();
                readOptions.readXIncludes = false;
                
                doc.clearContent();

                doc.importLibrary(stdlib);
                for (var item of customlibs) {
                    console.log('Import custom library:', item[0]);
                    doc.importLibrary(item[1]);
                }
                var loadDoc = mx.createDocument();
                await mx.readFromXmlString(loadDoc, fileContents, '', readOptions);          

                // Check if nodedef is not in existingDefs
                //
                var customLib = mx.createDocument();
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
                            console.log('Remove child:', child.getName());
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

                var documentColorSace = doc.getColorSpace();
                this.setActiveColorSpace(documentColorSace);
                documentColorSace = this.getActiveColorSpace();
                //console.log('Document colorspace:', documentColorSace);
                var csArea = MxShadingGraphEditor.theEditor.ui.mtlxdoc_colorspace;
                if (csArea)
                    csArea.innerHTML = documentColorSace;
                MxShadingGraphEditor.theEditor.updatePropertyPanel(null);

                // Cleanup document, and get up-to-date contents after any possible upgrade.
                loadDoc.removeAttribute('fileprefix');
                fileContents = mx.writeToXmlString(loadDoc);

                this.validateDocument(loadDoc);

                MxShadingGraphEditor.theEditor.debugOutput('Loaded document: "' + fileName + '"', 0, false);

                // Update mtlx text area
                let textArea = MxShadingGraphEditor.theEditor.ui.mtlxdoc;
                if (!textArea) {
                    MxShadingGraphEditor.theEditor.debugOutput('Failed to find text area for mtlxdoc', 2, false);
                }
                else {
                    textArea.setValue(fileContents);
                }        
            } catch (error) {
                MxShadingGraphEditor.theEditor.debugOutput('Error reading document:' + error, 2, false);
            }
        })();
    }

    loadFromFile(file, fileName, editor, auto_arrange) {
        var debug = false;

        if (mx) 
        {
            if (!this.loadMaterialXLibraries())
                return;    

            // Load the content from the specified file (replace this with actual loading logic)

            const reader = new FileReader();
            reader.readAsText(file, 'UTF-8');
            reader.accept = '.mtlx';

            var that = this;
            reader.onload = function (e) {
                // Display the contents of the file in the output div
                let fileContents = e.target.result;

                that.loadFromString(fileContents, fileName, auto_arrange);
            };

        } else {
            editor.debugOutput("MaterialX is not initialized", 2, false);
        }
    }    

    loadMaterialXLibraries() {
        if (stdlib)
            return stdlib;

        if (!mx) {
            MxShadingGraphEditor.theEditor.debugOutput("MaterialX is not initialized", 2);
            return null;
        }

        var generator = new mx.EsslShaderGenerator();
        var genContext = new mx.GenContext(generator);
        {
            stdlib = mx.loadStandardLibraries(genContext);
            console.log('Loaded standard libraries:', stdlib.getNodeDefs().length);
        }

        return stdlib;
    }

    // Create a valid MaterialX name
    createValidName(name, msg=null)
    {
        if (name.length == 0) {
            if (msg)
            {
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

        name = mx.createValidName(name);

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

class MxShadingGraphEditor {
    //
    // This class is a wrapper around the LiteGraph library to provide a MaterialX node editor.
    // It is designed to work with the MaterialX JavaScript API.
    //
    // List of methods:
    // - constructor
    // - setUI
    // - setDirty
    // - debugOutput
    // - arrangeGraph
    // - resetView
    // - clearGraph
    // - saveSerialization
    // - loadSerialization
    // - saveGraph
    // - saveGraphToString
    // - ladDefinitions
    // - loadGraph
    // - loadGraphFromString
    // - rgbToHex
    // - createButtonWithImageAndText
    // - openImageDialog
    // - updatePropertyPanel     
    //
    constructor() {
        if (!MxShadingGraphEditor.theEditor)
        {
            MxShadingGraphEditor.theEditor = this;
            this.handler = new MxMaterialXHandler('MaterialX Handler', 'mtlx');
            console.log('Create new editor', MxShadingGraphEditor.theEditor, ' and handler: ', this.handler);
        }
        return MxShadingGraphEditor.theEditor;
    }

    setUI(ui) {
        this.ui = ui;
    }

    setDirty()
    {
        if (graphcanvas)
        {
            graphcanvas.setDirty(true, true);
            //graphcanvas.resize();
        }
    }

    debugOutput(text, severity, clear = null) {
        var console_area = MxShadingGraphEditor.theEditor.ui.console_area;
        if (!console_area) {
            console.error('No console area found!');
            return;
        }
        if (severity === 2) {
            text = '> Error: ' + text
        }
        else if (severity === 1) {
            text = '> Warning: ' + text
        }
        else {
            if (text.length)
                text = '> ' + text;
        }

        //if (clear) {
        //    console_area.value = text + '\n';
        //}
        //else 
        {
            console_area.value = console_area.value + text + '\n';
        }
        // Scroll to latest entry.
        console_area.scrollTop = console_area.scrollHeight;
    }

    arrangeGraph() {
        // This does not track the current subgraph.
        if (graphcanvas) {
            graphcanvas.graph.arrange(80);
        }
    }

    openSubgraph()
    {
        var selected = graphcanvas.selected_nodes;
        for (var s in selected) {
            var node = selected[s];
            if (node.type == 'graph/subgraph') {
                console.log('Open subgraph', node.title );
                graphcanvas.openSubgraph(node.subgraph);
                break;
            }
        }
    }

    closeSubgraph()
    {
        if (graphcanvas) {
            graphcanvas.closeSubgraph();
        }
    }

    resetView() {
        if (graphcanvas) {
            graphcanvas.ds.reset();
            graphcanvas.setDirty(true, true);
        }
    }

    clearGraph() {
        //localStorage.setItem(
        //    "litegrapheditor_clipboard", ""
        //);

        this.handler.activeColorSpace = this.handler.DEFAULT_COLOR_SPACE;
        this.handler.activeUnits = this.handler.DEFAULT_UNITS;
        MxShadingGraphEditor.theEditor.updatePropertyPanel(null);
        MxShadingGraphEditor.theEditor.debugOutput('', 0, false);
        this.updatePropertyPanel(null);
        if (graphcanvas) {
            // Set back to top graph
            graphcanvas.setGraph(graph);
            graphcanvas.graph.clear();
            graphcanvas.ds.reset();
            graphcanvas.setDirty(true, true);
        }
        //console.log('Clear graph', customDocLibs);
        customDocLibs = [];
    }

    saveSerialization() {
        var data = JSON.stringify(graph.serialize(), null, 2);
        var blob = new Blob([data], { type: "text/plain" });
        var url = URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = "my_lite_graph.json";
        a.click();
    }

    loadSerialization() {
        MxShadingGraphEditor.theEditor.clearGraph();

        var input = document.createElement("input");
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

    saveGraphToFile(extension, saveCustomLibs, saveNodePositions)
    {
        if (extension == 'mtlx')
            this.handler.saveGraphToFile(graph, saveCustomLibs, saveNodePositions);
    }    

    saveGraphToString(extension, saveCustomLibs, saveNodePositions)
    {
        if (extension == 'mtlx')
            return this.handler.saveGraphToString(graph, saveCustomLibs, saveNodePositions);
        return '';
    }
        
    loadDefinitionsFromFile(extension)
    {
        if (extension == 'mtlx')
        {
            this.handler.loadDefinitionsFromFile();
        }
    }

    loadGraphFromFile(extension, auto_arrange) {

        if (extension != this.handler.getExtension())
        {
            this.debugOutput('Unsupported extension for loading graph', 2, false);
            return;
        }

        // Load document from disk. TODO: handle other extensions
        var input = document.createElement("input");
        input.type = "file";
        input.accept = "." + this.handler.getExtension();
        console.log('Accept:', input.accept);
        input.onchange = function (e) {
            var file = e.target.files[0];
            console.log('Loading file: ' + file.name);
            MxShadingGraphEditor.theEditor.handler.loadFromFile(file, file.name, MxShadingGraphEditor.theEditor, auto_arrange);
        };
        input.click();
    }

    loadGraphFromString(extension, content, fileName, auto_arrange)
    {
        if (extension != this.handler.getExtension())
        {
            this.debugOutput('Unsupported extension for loading graph', 2, false);
            return;
        }
    
        // TODO: handle other extensions
        if (content.length > 0)
            this.handler.loadFromString(content, fileName, auto_arrange);
        else
            MxShadingGraphEditor.theEditor.debugOutput('No content to load', 2, false);
    }

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

    createButtonWithImageAndText(imageSrc, text, id) {
        // Create image element
        var img = document.createElement("img");
        img.id = id + "_img";
        img.src = imageSrc;
        img.classList.add("img-fluid"); // Bootstrap class for responsive images

        // Create text element
        var span = document.createElement("span");
        span.id = id + "_text";
        span.textContent = " " + text;

        // Create button element
        var button = document.createElement("button");
        button.id = id;
        button.classList.add("btn", "btn-sm", "btn-outline-secondary", "form-control", "form-control-sm"); // Bootstrap button classes
        button.appendChild(img); // Append image to button
        button.appendChild(span); // Append text to button

        return button;
    }


    openImageDialog(theNode, updateProp, wantURI) {
        //console.log('updateImageDialog', theNode, updateProp, wantURI);

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
            theNode.properties[updateProp] = fileURI;

            var propertypanel_preview = document.getElementById('propertypanel_preview');
            propertypanel_preview.src = URL.createObjectURL(file);
            propertypanel_preview.style.display = "block";

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

    uriExists(uri) {
        // Add try / catch block to handle network errors        
        return fetch(uri)
            .then(response => {
                if (response.ok) {
                    return true; 
                } else {
                    return false;
                }
            })
            .catch(error => {
                console.log('Error checking URI:', error);
                return false;
            });
    }

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
            //if (panelIcon.src != node.nodedef_icon)
                panelIcon.src = node.nodedef_icon;
        }
        else {
            if (!node)
                panelIcon.src = this.ui.icon_map['_default_graph_'];
            else
            panelIcon.src = this.ui.icon_map['_default_'];
        }

        propertypanelcontent.innerHTML = "";

        if (!node && graphcanvas.graph._subgraph_node)
        {
            node = graphcanvas.graph._subgraph_node;
            console.log('In subgraph but no node deleted. Select subgram node', node)
        }
        else if (!node && !graphcanvas.graph._is_subgraph) {
            var docInfo = [ ['Colorspace', this.handler.activeColorSpace],
                            ['Units', this.handler.activeUnit ]];

            for (var item of docInfo) {
                
                var elem = document.createElement("div");
                elem.className = "row px-1 py-0";
                var label = document.createElement("div");
                label.className = "col py-0 col-form-label-sm text-left";
                label.innerHTML = "<b>" + item[0] + "</b>";                
                elem.appendChild(label);
                
                var inputCol = document.createElement("div");
                inputCol.className = "col text-left";
                var nameInput = document.createElement("input");
                nameInput.type = "text";
                nameInput.value = item[1];
                nameInput.className = "form-control form-control-sm";
                nameInput.disabled = true;
                elem.appendChild(inputCol);
                inputCol.appendChild(nameInput);

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

        var elem = document.createElement("div");
        elem.className = "row px-1 py-0";
        var label = document.createElement("div");
        label.className = "col-4 py-0 col-form-label-sm text-left";
        label.innerHTML = "<b>" + _category;
        if (_type.length > 0) {
            label.innerHTML += '<br>' + _type;
        }
        label.innerHTML += "</b>";

        var inputCol = document.createElement("div");
        inputCol.className = "col text-left";
        var nameInput = document.createElement("input");
        nameInput.type = "text";
        nameInput.value = node.title;
        nameInput.className = "form-control form-control-sm";
        nameInput.onchange = function (e) {
            var oldTitle = node.title;
            node.title = MxShadingGraphEditor.theEditor.handler.createValidName(e.target.value);
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

        // TODO: Preview image
        if (node.nodedef_node != 'input' && node.nodedef_node != 'output'
            && node.type != 'graph/subgraph') {
            var imagePreview = document.createElement("img");
            imagePreview.src = "./Images/no_image.png";
            var previewSet = false;
            //console.log('Check for preview:', node.nodedef_swatch, 'category:', _category)
            imagePreview.style.display = "none";
            imagePreview.src = "./Images/no_image.png";
            if (node.nodedef_swatch && 
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
            }
            imagePreview.id = "propertypanel_preview";
            imagePreview.className = "img-fluid form-control form-control-sm";
            inputCol.appendChild(imagePreview);
        }

        elem.appendChild(label);
        elem.appendChild(inputCol);
        propertypanelcontent.appendChild(elem);

        // TODO: Add toggle for showing/hiding all inputs
        var addShow = false;
        if (addShow) {
            var elem = document.createElement("div");
            elem.className = "row px-1 py-0";

            var label = document.createElement("div");
            label.className = "col-12 col-form-label-sm";
            label.innerHTML = "All Inputs: ";
            elem.appendChild(label);
            var input = document.createElement("input");
            input.type = "checkbox";
            label.appendChild(input);

            var showAll = false;
            if (node.showAllInputs) {
                showAll = node.showAllInputs;
            }
            input.checked = showAll;
            input.onclick = function (e) {
                var show = e.target.checked;
                node.showAllInputs = show;

                // Need to keep all old + new inputs in order. Easiest
                // is to keep a list of all inputs, remove old and add new.
                for (var index in node.properties_info) {
                    var propInfo = node.properties_info[index];
                    var found = false;
                    for (var i = 0; i < node.inputs.length; ++i) {
                        if (node.inputs[i].name == propInfo.name) {
                            found = true;
                            break;
                        }
                    }                    
                    if (!found) {
                        console.log('Add missing input:', propInfo.name, propInfo.default_value, propInfo.type);
                        //node.addInput(propInfo.name, propInfo.type);
                        //node.addProperty(propInfo.name, propInfo.value, propInfo.type);
                    }
                }
            }

            if (current_details)
                current_details.appendChild(elem);
            else
                propertypanelcontent.appendChild(elem);
        }

        var hr = document.createElement("hr");
        hr.classList.add("my-1");
        propertypanelcontent.appendChild(hr);

        var current_details = null;
        var first_details = true;
        var nodeInputs = node.inputs

        var targetNodes = [];
        for (var i in nodeInputs) {
            var nodeInput = nodeInputs[i];
            var inputName = nodeInput.name;
            var nodeInputLink = nodeInput.link; 
            var uiName = inputName;
            var uimin = null;
            var uimax = null;
            var colorspace = '';
            var units = '';

            //console.log('Scan input:', inputName, ' on node: ', node.graph);

            var property_info = node.properties_info[i];

            var skipInterorConnectedInput = false;
            if (node.graph._is_subgraph)
            {
                // Find input on subgraph node
                //console.log('Check subgraph for link:', node.graph)
                var sg_node = node.graph._subgraph_node;
                if (sg_node)
                {
                    //console.log('Check for input on sg node', sg_node, node.title);
                    var slot = sg_node.findInputSlot(node.title);
                    if (slot != null)
                    {
                        if (sg_node.inputs)
                        {
                            //property_info = sg_node.properties_info[slot];
                            var slotInput = sg_node.inputs[slot];
                            //console.log('check slot: ', slotInput.link);
                            if (slotInput != null && slotInput.link != null)
                            {
                                skipInterorConnectedInput = true;
                            }
                        }
                        else
                        {
                            console.log('Error: no subgraph node inputs for subgraph input!', sg_node, node.title);
                        }
                    }
                } 
            }        

            if (skipInterorConnectedInput)
            {
                console.log('Skip interior connected input: ', nodeInput);  
                continue;
            }

            //console.log('Property info:', property_info, ' for input:', inputName);
            if (property_info)
            {
                if (property_info.colorspace)
                {
                    colorspace = property_info.colorspace;
                }
                if (property_info.unit)
                {
                    units = property_info.unit;
                }
                if (property_info.uiname)
                {
                    uiName = property_info.uiname;
                }
                if (property_info.uimin)
                {
                    uimin = property_info.uimin;
                }
                if (property_info.uimax)
                {
                    uimax = property_info.uimax;
                }
                if (property_info.uifolder && property_info.uifolder.length > 0)
                {
                    // Create a details element
                    if (current_details == null || current_details.id != property_info.uifolder)
                    {
                        //console.log('Create new details:', property_info.uifolder);
                        current_details = document.createElement("details");
                        current_details.id = property_info.uifolder;
                        current_details.open = first_details;
                        current_details.classList.add('w-100', 'p-1', 'border', 'border-secondary', 'rounded', 'my-1');
                        first_details = false;
                        var summary = document.createElement('summary')
                        summary.innerHTML = property_info.uifolder;
                        //summary.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'btn-block');
                        current_details.appendChild(summary);                    
                        
                        propertypanelcontent.appendChild(current_details);
                    }
                }
                else {
                    current_details = null;
                }
                //console.log('>>>>>>>>>>>> uiName:', uiName, 'uimin:', uimin, 'uimax:', uimax);
            }
            else {
                current_details = null;
            }

            var elem = null;

            // Check if there is a link
            if (nodeInputLink) {
                var upstreamLink = null;

                var nodegraph = node.graph;
                var link = nodegraph.links[nodeInputLink];
                //console.log('link:', link);
                var linkId = link && link.origin_id;
                var linkNode = linkId && nodegraph.getNodeById(linkId);
                if (linkNode) {

                   
                    //console.log('linkNode:', linkNode);
                    var linkSlot = link.origin_slot;
                    //console.log('linkSlot:', linkSlot);
                    var linkOutput = linkNode.outputs[linkSlot];
                    //console.log('linkOutput:', linkOutput);
                    upstreamLink = linkNode.title + '.' + linkOutput.name;
                    //console.log('upstreamLink:', upstreamLink);

                    var id = "__pp:" + inputName;
                    var input = this.createButtonWithImageAndText("./Images/arrow_up_white.svg", upstreamLink, id);

                    //var input = document.createElement("div");
                    //input.id = "__pp:" + inputName;
                    //input.type = "text";
                    //input.value = upstreamLink;
                    //input.disabled = true;
                    //input.className = "btn form-control form-control-sm";
                    //input.style = "background-color: #252";
                    input.onclick = function (e) {

                        var inputName = e.target.id;
                        inputName = inputName.replace('__pp:', '');
                        inputName = inputName.replace('_text', '');
                        inputName = inputName.replace('_img', '');
                        console.log('Clicked traversal button:', inputName);

                        console.log('Jump to node:', linkNode.title);
                        graphcanvas.selectNodes([linkNode]);
                        //node.setDirtyCanvas(true, true);
                        MxShadingGraphEditor.theEditor.updatePropertyPanel(linkNode);
                        node.setDirtyCanvas(true, true);
                    }

                    // Add new row
                    elem = document.createElement("div");
                    elem.className = "row px-1 py-0";

                    input.id = "__pp:" + inputName;

                    var label = document.createElement("div");
                    label.className = "col-4 p-0 col-form-label-sm text-end";
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
                var propertyKey = inputName;

                var property = targetNode.properties[inputName];
                if (property == null) {
                    if (isNodeGraph)
                    {
                        var subgraph = targetNode.subgraph;
                        if (subgraph)
                        {
                            //console.log('Find node by title', inputName, ' in subgraph', subgraph._nodes);
                            var subNode = subgraph.findNodeByTitle(inputName);
                            if (subNode)
                            {
                                targetNodes[i] = subNode;
                                propertyKey = 'in';
                                property = targetNodes[i].properties['in'];
                                console.log('Route to subgraph target node:', targetNode, targetNode.title, '. ', inputName, ' = ', JSON.stringify(property), 'propkey=', propertyKey);
                            }
                        }                        
                    }
                    if (property == null)
                    {
                        console.log('Update: Cannot find property value for input:', inputName);
                        continue;
                    }
                }
                else {
                    //console.log('handle propery value: ', property, 'for input', input);
                }

                // Add new row
                elem = document.createElement("div");
                elem.className = "row px-1 py-0";

                var input = null;
                var input_btn = null;
                var colorspace_unit_btn = null;
                var useFormControl = true;

                // TODO: Clean this up to be a drop-down and only apply to numbers / colors
                if (colorspace.length > 0) {
                    /* 
                    // Create drop-down menu
                    /* 
                    colorspace_unit_btn = document.createElement("div");
                    colorspace_unit_btn.classList.add("dropdown");
                    var dropdownButton = document.createElement("button");
                    dropdownButton.classList.add("btn", "btn-sm", "btn-outline-secondary", "dropdown-toggle");
                    dropdownButton.type = "button";
                    dropdownButton.id = "dropdownMenuButton";
                    dropdownButton.setAttribute("data-bs-toggle", "dropdown");
                    dropdownButton.setAttribute("aria-expanded", "false");                    
                    dropdownButton.innerHTML = "+";
                    var dropdownMenu = document.createElement("ul");
                    dropdownMenu.classList.add("dropdown-menu");
                    dropdownMenu.setAttribute("aria-labelledby", "dropdownMenuButton");
                    var dropdownItem = document.createElement("li");
                    dropdownItem.classList.add("dropdown-item");
                    dropdownItem.innerHTML = colorspace;
                    dropdownMenu.appendChild(dropdownItem);
                    colorspace_unit_btn.appendChild(dropdownMenu);
                    */
                    colorspace_unit_btn = document.createElement("button");
                    colorspace_unit_btn.classList.add("btn", "py-0", "btn-sm", "btn-outline-secondary");
                    colorspace_unit_btn.innerHTML = colorspace;
                    
                    console.log('Show MetaData Colorspace:', colorspace, ' for input:', inputName, ' on node:', node.title)
                }
                else if (units.length > 0) {
                    colorspace_unit_btn = document.createElement("button");
                    colorspace_unit_btn.classList.add("btn", "py-0", "btn-sm", "btn-outline-secondary");
                    colorspace_unit_btn.innerHTML = units;
                    console.log('Show MetaData Units:', units, ' for input:', inputName, ' on node:', node.title)
                }

                var proptype = nodeInput.type;
                if (proptype == 'float' || proptype == 'integer') {
                    var isFloat = proptype == 'float';
                    input = document.createElement("input");
                    input.type = 'number';
                    input.value = property;
                    if (uimin)
                    {
                        input.min = uimin;
                    }
                    if (uimax)
                    {
                        input.max = uimax;
                    }
                    if (input.min && input.max && isFloat)
                    {
                        input.step = uimax - uimin / 100.0;
                    }                    
                    input.setAttribute('propertyKey', propertyKey);
                    let theNode = targetNodes[i];
                    input.onchange = function (e) {
                        var pi = e.target.getAttribute('propertyKey');
                        var val = parseFloat(e.target.value);
                        if (uimin && val < uimin) {
                            val = uimin;
                            e.target.value = val;
                        }
                        if (uimax && val > uimax) {
                            val = uimax;
                            e.target.value = val;
                        }                        
                        theNode.properties[pi] = val;
                        console.log('Update scalar property:', pi, parseFloat(e.target.value), theNode.title, theNode.properties)
                    }
                }
                else if (proptype == 'string' || proptype == 'filename') {
                    input = document.createElement("input");
                    input.type = "text";
                    if (proptype == 'filename') {
                        var propertypanel_preview = document.getElementById('propertypanel_preview');
                        var curImage = property;
                        if (curImage) {
                            this.uriExists(curImage)
                                .then(exists => {
                                    if (exists) {
                                        propertypanel_preview.src = curImage;
                                        propertypanel_preview.style.display = "block";
                                    } else {
                                        //propertypanel_preview.style.display = "none";
                                        propertypanel_preview.src = "./Images/no_image.png";
                                        propertypanel_preview.style.display = "block";
                                        MxShadingGraphEditor.theEditor.debugOutput('Image does not exist: ' + curImage, 1);
                                    }
                                });
                        }

                        input_btn = document.createElement("button");
                        input_btn.classList.add("btn", "btn-sm", "btn-outline-secondary");
                        input_btn.innerHTML = "+";
                        input_btn.setAttribute('propertyKey', propertyKey);
                        var fileId = "__pp:" + inputName;
                        var theNode = targetNodes[i];
                        input_btn.onclick = function (e) {
                            var pi = e.target.getAttribute('propertyKey');
                            console.log('pi:', pi);
                            MxShadingGraphEditor.theEditor.openImageDialog(theNode, pi, false);
                        }
                    }
                    input.value = property;
                    input.setAttribute('propertyKey', propertyKey);
                    var theNode = targetNodes[i];
                    input.onchange = function (e) {
                        var pi = e.target.getAttribute('propertyKey');
                        theNode.properties[pi] = e.target.value;
                        //console.log('Update string property:', pi, theNode.properties[pi])
                    }
                }
                else if (proptype == 'boolean') {
                    //console.log('Add Boolean property:', property);
                    input = document.createElement("input");
                    input.type = "checkbox";
                    input.classList = "form-check-input";
                    //input.style.width = "10%";
                    //input.style.height = "50%";
                    useFormControl = false;
                    input.checked = property;
                    input.setAttribute('propertyKey', propertyKey);
                    var theNode = targetNodes[i];
                    input.onchange = function (e) {
                        var pi = e.target.getAttribute('propertyKey');
                        theNode.properties[pi] = e.target.checked;
                        //console.log('Update boolean property:', theNode.properties[pi]);
                    }
                }

                else if (proptype == 'vector2' || proptype == 'vector3' || proptype == 'vector4') {
                    // Find index of proptype in ['vector2', 'vector3', 'vector4' ]
                    var vector_size = ['vector2', 'vector3', 'vector4'].indexOf(proptype) + 2;
                    var input = document.createElement("div");
                    useFormControl = false;

                    input.className = "row py-1 ps-2";
                    {
                        //console.log('Vector property:[', 0, '] = ', property[0], proptype)
                        var subinput = document.createElement("input");
                        subinput.type = 'number';
                        subinput.classList.add("form-control");
                        subinput.classList.add("form-control-sm");
                        subinput.value = property[0];
                        if (uimin) {
                            subinput.min = uimin[0];                            
                        }
                        if (uimax) {
                            subinput.max = uimax[0];
                        }
                        if (uimin && uimax) {
                            subinput.step = (uimax[0] - uimin[0]) / 100.0;
                        }
                        subinput.setAttribute('propertyKey', propertyKey);
                        var theNode = targetNodes[i];
                        subinput.onchange = function (e) {
                            var pi = e.target.getAttribute('propertyKey');
                            var value = parseFloat(e.target.value);
                            if (uimin && value < uimin[0]) {
                                value = uimin[0];
                            }
                            if (uimax && value > uimax[0]) {
                                value = uimax[0];
                            }
                            e.target.value = value;
                            theNode.properties[pi][0] = value;
                        }
                        input.appendChild(subinput);
                    }
                    {
                        //console.log('Vector property:[', 1, '] = ', property[0], proptype)
                        var subinput = document.createElement("input");
                        subinput.type = 'number';
                        subinput.value = property[1];
                        if (uimin) {
                            subinput.min = uimin[1];                            
                        }
                        if (uimax) {
                            subinput.max = uimax[1];
                        }
                        if (uimin && uimax) {
                            subinput.step = (uimax[1] - uimin[1]) / 100.0;
                        }
                        subinput.setAttribute('propertyKey', propertyKey);
                        subinput.classList.add("form-control");
                        subinput.classList.add("form-control-sm");
                        var theNode = targetNodes[i];
                        subinput.onchange = function (e) {
                            var pi = e.target.getAttribute('propertyKey');
                            var value = parseFloat(e.target.value);
                            if (uimin && value < uimin[1]) {
                                value = uimin[1];
                            }
                            if (uimax && value > uimax[1]) {
                                value = uimax[1];
                            }
                            e.target.value = value;
                            theNode.properties[pi][1] = value;
                            //console.log('Update Vector property:"', pi, '"', 1, parseFloat(e.target.value), theNode.properties[pi])
                        }
                        input.appendChild(subinput);
                    }
                    if (vector_size > 2) {
                        //console.log('Vector property:[', 2, '] = ', property[0], proptype)
                        var subinput = document.createElement("input");
                        subinput.type = 'number';
                        if (uimin) {
                            subinput.min = uimin[2];                            
                        }
                        if (uimax) {
                            subinput.max = uimax[2];
                        }
                        if (uimin && uimax) {
                            subinput.step = (uimax[2] - uimin[2]) / 100.0;
                        }
                        subinput.value = property[2];
                        subinput.setAttribute('propertyKey', propertyKey);
                        subinput.classList.add("form-control");
                        subinput.classList.add("form-control-sm");
                        var theNode = targetNodes[i];
                        subinput.onchange = function (e) {
                            var pi = e.target.getAttribute('propertyKey');
                            //console.log('Update Vector property:"', pi, '"', 2, parseFloat(e.target.value), theNode.properties[pi])
                            var value = parseFloat(e.target.value);
                            if (uimin && value < uimin[2]) {
                                value = uimin[2];
                            }
                            if (uimax && value > uimax[2]) {
                                value = uimax[2];
                            }                    
                            e.target.value = value;        
                            theNode.properties[pi][2] = value;
                        }
                        input.appendChild(subinput);
                    }
                    if (vector_size > 3) {
                        //console.log('Vector property:[', 3, '] = ', property[0], proptype)
                        var subinput = document.createElement("input");
                        subinput.type = 'number';
                        if (uimin) {
                            subinput.min = uimin[3];                            
                        }
                        if (uimax) {
                            subinput.max = uimax[3];
                        }
                        if (uimin && uimax) {
                            subinput.step = (uimax[3] - uimin[3]) / 100.0;
                        }
                        subinput.value = property[3];
                        subinput.setAttribute('propertyKey', propertyKey);
                        subinput.classList.add("form-control");
                        subinput.classList.add("form-control-sm");
                        var theNode = targetNodes[i];
                        subinput.onchange = function (e) {
                            var pi = e.target.getAttribute('propertyKey');
                            //console.log('Update Vector property:"', pi, '"', 3, parseFloat(e.target.value), theNode.properties[pi])
                            var value = parseFloat(e.target.value);
                            if (uimin && value < uimin[3]) {
                                value = uimin[3];
                            }
                            if (uimax && value > uimax[3]) {
                                value = uimax[3];
                            }
                            e.target.value = value;
                            theNode.properties[pi][3] = value;
                        }
                        input.appendChild(subinput);
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
                        if (uimin)
                        {
                            if (rgb[0] < uimin) rgb[0] = uimin;
                            if (rgb[1] < uimin) rgb[1] = uimin;
                            if (rgb[2] < uimin) rgb[2] = uimin;                         
                        }
                        if (uimax)
                        {
                            if (rgb[0] > uimax) rgb[0] = uimax;
                            if (rgb[1] > uimax) rgb[1] = uimax;
                            if (rgb[2] > uimax) rgb[2] = uimax;
                        }
                        var pi = e.target.getAttribute('propertyKey');
                        theNode.properties[pi] = rgb;
                        console.log('set color property:', theNode.title, theNode.properties[propertyKey], 'key=', propertyKey, rgb);
                    }
                }
                else {
                    input = document.createElement("input");
                    input.type = "text";
                    input.value = property;
                    var propertyKey = inputName;
                    var theNode = targetNodes[i];
                    input.onchange = function (e) {
                        theNode.properties[propertyKey] = e.target.value;
                    }
                }
                /*
                TODO: Handle enumerations
                else if (proptype == 'enum') {
                    var input = document.createElement("select");
                    for (var j in nodes.inputs[i].values) {
                        var option = document.createElement("option");
                        option.value = j;
                        option.innerHTML = nodes.inputs[i].values[j];
                        input.appendChild(option);
                    }
                    input.value = property;
                    input.onchange = function (e) {
                        targetNode.properties[i] = e.target.value;
                    }
                } */

                if (input) {
                    input.id = "__pp:" + inputName;
                    //console.log('> Add input:', input.id);

                    var label = document.createElement("div");
                    label.className = "col-4 p-0 col-form-label-sm text-end font-small";
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
                    propvalue.appendChild(input);

                    if (input_btn) {
                        var propbutton = document.createElement("div");
                        propbutton.className = "col-1 py-0";
                        //console.log('Add input button:', input_btn);
                        propbutton.appendChild(input_btn);
                        elem.appendChild(propbutton);
                    }
                    if (colorspace_unit_btn) {                   
                        //console.log('Add cs / unit button:', input_btn);
                        var propbutton = document.createElement("div");
                        propbutton.className = "col col-form-label-sm font-small";
                        var details = document.createElement("details");     
                        var summary = document.createElement('summary')
                        if (colorspace.length > 0)
                            summary.innerHTML = "Colorspace";
                        else if (units.length > 0)
                            summary.innerHTML = "Units";
                        details.appendChild(summary);
                        details.appendChild(colorspace_unit_btn);
                        propbutton.appendChild(details);
                        propvalue.appendChild(propbutton);
                    }
                    elem.appendChild(propvalue);
                }
            }
            //elem.innerHTML = "<em>" + i  + "</em> : " + property;
            if (elem) {
                if (current_details)
                    current_details.appendChild(elem);
                else
                    propertypanelcontent.appendChild(elem);
            }
        }
    }

    onConnectOutput(slot, input_type, input, target_node, target_slot)
    {
        console.log('**** Connect output');
        console.log(' - slot:', slot);
        console.log(' - input type: ', input_type)
        console.log(' - input:', input);
        console.log(' - target_node', target_node); 
        console.log(' - target slot', target_slot);
    }

    onConnectInput(target_slot, output_type, output, source, slot)
    {
        console.log('**** Node connection changed');
        console.log(' - target_slot:', target_slot);
        console.log(' - output_type: ', output_type)
        console.log(' - output:', output);
        console.log(' - source', source); 
        console.log(' - source slot', slot);
    }

    monitorGraph(theGraph, monitor) {
        if (!theGraph)
            return;

        theGraph.onConnectionChange = null;
        theGraph.onNodeAdded = null;
        theGraph.onNodeRemoved = null;

        if (monitor) {

            var that = this;
            //console.log('Monitor connection change:', theGraph.title);
            theGraph.onConnectionChange = function (node) 
            {
                //console.log('On connection change:', node.title, node);
                var selected = graphcanvas.selected_nodes;
                for (var s in selected) {
                    console.log('update selected node:', selected[s].title);
                    that.updatePropertyPanel(selected[s]);
                    break;
                }
            }

            //console.log('Monitor graph add:', theGraph.title);
            theGraph.onNodeAdded = function (node) {

                node.onConnectOutput = MxShadingGraphEditor.theEditor.onConnectOutput;

                if (node.type == 'graph/subgraph') {
                    // Use MaterialX naming for subgraphs
                    //node.title = 'nodegraph';
                    //console.log('Monitor new subgraph node for connection change:', node.title, node);
                    node.onConnectInput = MxShadingGraphEditor.theEditor.onConnectInput;
                    //node.onConnectionChange = function (node) {
                    //    console.log('**** Subgraph connection changed');
                    //}

                    //MxShadingGraphEditor.theEditor.monitorGraph(node.subgraph, monitor);

                    // Scan the subgraph for any nodes which are not in the node inputs list.
                    var node_subgraph = node.subgraph;
                    var node_graph = node.graph;
                    if (node_subgraph)
                    {
                        //console.log('** Scan subgraph: ', node_subgraph)
                        for (var i in node_subgraph._nodes)
                        {
                            var theNode = node_subgraph._nodes[i];
                            //console.log('*** scan subgrapn node: ', theNode.title)
                            if (!node_graph.findNodeByTitle(theNode.title))
                            {
                                if (theNode.nodedef_node == 'input') {
                                    console.log('-0-0-0 add input', theNode.title)
                                    node.addInput(theNode.title, theNode.nodedef_type);
                                    console.log('--> Promote input node to subgraph node.', theNode.title);
                                }
                                else if (theNode.nodedef_node == 'output') {
                                    console.log('--> Promote output node to subgraph node.', theNode.title);
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
                var is_subgraph = node.graph._is_subgraph;;
                if (is_subgraph) {

                    if (node.nodedef_node == 'input') {
                        console.log('Adding input node to subgraph.', node.title, node.graph);
                        node.graph.addInput(node.title, node.nodedef_type);
                    }
                    else if (node.nodedef_node == 'output') {
                        console.log('Adding output node to subgraph.');
                        node.graph.addOutput(node.title, node.nodedef_type);
                    }
                }

                if (node.type == 'graph/subgraph') {
                    MxShadingGraphEditor.theEditor.monitorGraph(node.subgraph, monitor);
                }
            }

            //console.log('Monitor graph remove:', theGraph.title);
            theGraph.onNodeRemoved = function (node) {
                //console.log('-> Node Removed:', node, '. Type:', node.type, '. Graph:', graphcanvas.graph);
                /* This is too late the graph reference has already been removed */
                var is_subgraph = graphcanvas.graph._is_subgraph;
                if (is_subgraph) {
                    if (node.nodedef_node == 'input') {
                        console.log('Removing input node from subgraph.');
                        graphcanvas.graph.removeInput(node.title);
                    }
                    else if (node.nodedef_node == 'output') {
                        console.log('Removing output node from subgraph.');
                        graphcanvas.graph.removeOutput(node.title);
                    }
                }
            }
        }


        for (var i in theGraph._nodes) {
            var node = theGraph._nodes[i];
            if (node.type == 'graph/subgraph') {
                //console.log('Monitor node:', node.title);
                this.monitorGraph(node.subgraph, monitor);
                node.onConnectInput = MxShadingGraphEditor.theEditor.onConnectInput;
                //node.onConnectionChange = function (node) {
                //    console.log('**** Subgraph connection changed');
                //}
            }
        }
    }

    initializeLiteGraph(canvas) 
    {
        // Initialize Litegraph
        graph = new LiteGraph.LGraph();
        graphcanvas = new LiteGraph.LGraphCanvas(canvas, graph);
        graphcanvas.onShowNodePanel = function (node) {
            ;  // Making this a no-op as will not use the default panel
        }
        graphcanvas.onNodeSelected = function (node) {
            console.log('Selected node:', node.title, node);
            MxShadingGraphEditor.theEditor.updatePropertyPanel(node);
        }
        graphcanvas.onNodeDeselected = function (node) {
            //console.log('Node Deselected:', node);
            MxShadingGraphEditor.theEditor.updatePropertyPanel(null);
        }

        // Todo: Move this to application site and expose settings to use.
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
        /*    float: "#666",
            vector3: "#888",
            color3: "#89A",
            vector4: "#99B",
            color4: "#9AC",
            matrix33: "#9BD",
            matrix44: "#9CE",
            string: "#9DF",
            filename: "#9EF",
            boolean: "#AF0",
        }; */

        //console.log('Setup graph canvas:', graphcanvas);

        graphcanvas.resize();

        this.monitorGraph(graph, true);
        graph.arrange(80);

        // Run the graph
        //graph.runStep();

        // Enable interaction
        //graphcanvas.hide_unconnected = false;
        graphcanvas.allow_interaction = true;
        graphcanvas.allow_dragnodes = true;
        graphcanvas.allow_searchbox = true;
        graphcanvas.render_connections_arrows = true;
        graphcanvas.clear_background_color = "#222223";
        graphcanvas.max_zoom = 0.25;
        graphcanvas.connections_width = 2;
        graphcanvas.render_canvas_border = false;
        graphcanvas.align_to_grid = false;
        graphcanvas.render_connection_arrows = false;
        graphcanvas.render_curved_connections = true;
        //graphcanvas.background_image = null; 

        // Turn off HUD
        graphcanvas.show_info = false;

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

    }

    centerNode() {
        var selected = graphcanvas.selected_nodes;
        for (var s in selected) {
            console.log('Focus on', selected[s]);
            graphcanvas.centerOnNode(selected[s]);
            break;
        }
    }

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

    collapseExpandNodes(collapse) {
        var curGraph = graphcanvas.graph;

        var selected_nodes = graphcanvas.selected_nodes;
        console.log('Selected nodes:', selected_nodes);
        var modified = false;
        if (selected_nodes) {
            for (var i in selected_nodes) {
                var node = selected_nodes[i];
                console.log('Collapse/Expand:', node.title, collapse);
                if (this.collapseNode(node, collapse))
                    modified = true;
            }
        }
        if (!modified)
        {
            var nodes = curGraph._nodes;
            for (var i in nodes) {
                var node = nodes[i];
                if (this.collapseNode(node, collapse))
                    modified = true;
            }
        }

        if (modified)
        {
            graph._version++;
            graph.setDirtyCanvas(true, true);
        }
    }

    copyToClipboard() {
        graphcanvas.copyToClipboard();
    }

    pasteFromClipboard() {
        graphcanvas.pasteFromClipboard();
    }

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
            console.log('Select subgraph node:', node.title);
        }

        graphcanvas.openSubgraph(subGraph.subgraph);
        graphcanvas.selectNodes(subGraphNodes);
        // Copy the selected nodes to the clipboard
        graphcanvas.copyToClipboard();

        // Paste the copied nodes into the graph
        graphcanvas.closeSubgraph();
        graphcanvas.pasteFromClipboard();
    }

    createNodeGraph() {
        // Disallow testing for now.
        if (graphcanvas.graph._is_subgraph)
        {
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

    displayNodeTypes() {
        // Get the list of available node types
        var nodeTypes = LiteGraph.registered_node_types;

        // Get the list container
        var nodeList = this.ui.nodeTypesList;
        // Clear all children of nodeList
        while (nodeList.firstChild) {
            nodeList.removeChild(nodeList.firstChild);
        }

        // Iterate over the node types and add them to the list        
        for (var typeName in nodeTypes) {            

            var rowItem = document.createElement("tr");

            var cellItem = document.createElement("td");
            cellItem.textContent = typeName;
            rowItem.appendChild(cellItem);

            cellItem = document.createElement("td");
            var nodeDefString = '<None>';
            var nodeDefName = nodeTypes[typeName].nodedef_name;
            var nodeDefNode = nodeTypes[typeName].nodedef_node
            var nodeDefHref = nodeTypes[typeName].nodedef_href;
            if (nodeDefName) {
                if (nodeDefNode)
                {
                    var link = document.createElement("a");
                    link.target = "_blank";
                    link.href = nodeDefHref;
                    link.textContent = nodeDefNode + " ( " + nodeDefName + " )";
                    cellItem.appendChild(link);
                }
                else
                {
                    cellItem.textContent = nodeDefName;                
                }
            }
            else {
                cellItem.textContent = nodeDefString;
            }
            rowItem.appendChild(cellItem);

            nodeList.appendChild(rowItem);
        }
    }


    initialize(createMode, canvas, ui) {

        this.setUI(ui);
        this.initializeLiteGraph(canvas);
        this.handler.initialize(MxShadingGraphEditor.theEditor);
    }
}

/*
document.addEventListener('DOMContentLoaded', () {
    console.log('Setup property panel event handlers...')
    var panel1 = document.getElementById('propertypanelcontent');
    //var panel2 = document.getElementById('panel2');
    var isDraggingPanel1 = false;
    //var isDraggingPanel2 = false;
    var offsetX1, offsetY1, offsetX2, offsetY2;

    panel1.addEventListener('mousedown', (e) {
        console.log('mousedown:', e.target.id);
        isDraggingPanel1 = true;
        var rect = panel1.getBoundingClientRect();
        offsetX1 = e.clientX - rect.left;
        offsetY1 = e.clientY - rect.top;
        e.stopPropagation();
    });


    document.addEventListener('mousemove', (e) {
        if (isDraggingPanel1) {
            handleDragging(panel1, offsetX1, offsetY1, e);
        }
    });

    document.addEventListener('mouseup', () {
        isDraggingPanel1 = false;
        //isDraggingPanel2 = false;
    });

    handleDragging(panel, offsetX, offsetY, e) {
        var canvas = document.getElementById('graphcanvas');
        var canvasRect = canvas.getBoundingClientRect();
        var canvasLeft = canvasRect.left + window.pageXOffset;
        var canvasTop = canvasRect.top + window.pageYOffset;
        var canvasRight = canvasLeft + canvas.width;
        var canvasBottom = canvasTop + canvas.height;

        var x = e.clientX - offsetX;
        var y = e.clientY - offsetY;

        x = Math.min(Math.max(canvasLeft, x), canvasRight - panel.offsetWidth);
        y = Math.min(Math.max(canvasTop, y), canvasBottom - panel.offsetHeight);

        panel.style.left = x - canvasLeft + 'px';
        panel.style.top = y - canvasTop + 'px';
    }
}); */
