/** 
    jsMaterialXglTF 
    
    glTF procedural texturing extension utilities
*/
/** 
 * @const {string} MTLX_DEFAULT_MATERIAL_NAME
 * 
     * The default MaterialX material name for import if no name is provided. 
*/
let MTLX_DEFAULT_MATERIAL_NAME = 'MAT_0' 
/**
 * @const {string} MTLX_MATERIAL_PREFIX
 * 
     * The prefix for MaterialX material names.
*/
let MTLX_MATERIAL_PREFIX = 'MAT_'
/**
 * @const {string} MTLX_DEFAULT_SHADER_NAME
 * 
     * The default MaterialX shader name for import if no name is provided.
 * */
let MTLX_DEFAULT_SHADER_NAME = 'SHD_0'
/**
 * @const {string} MTLX_SHADER_PREFIX
 * 
     * The prefix for MaterialX shader names.
 */
let MTLX_SHADER_PREFIX = 'SHD_'

/**
 * @const {string} MTLX_INTERFACEINPUT_NAME_ATTRIBUTE
 * 
     * The name of the attribute used to indicate an interface connection on an input.
 */
let MTLX_INTERFACEINPUT_NAME_ATTRIBUTE = 'interfacename';
/** 
 * @const {string} MTLX_NODE_NAME_ATTRIBUTE
 * 
     * The name of the attribute used to indicate a node connection on an input.
 */
let MTLX_NODE_NAME_ATTRIBUTE = 'nodename';
/**
 * @const {string} MTLX_NODEGRAPH_NAME_ATTRIBUTE
 * 
     * The name of the attribute used to indicate a nodegraph connection on an input.
 */
let MTLX_NODEGRAPH_NAME_ATTRIBUTE = 'nodegraph';
/**
 * @const {string} MTLX_GLTF_PBR_CATEGORY
 * 
     * The name of the MaterialX category for a glTF PBR shader.
 */
let MTLX_GLTF_PBR_CATEGORY = 'gltf_pbr'
/**
 * @const {string} MTLX_UNLIT_CATEGORY_STRING
 * 
     * The name of the MaterialX category for an unlit shader.
 */
let MTLX_UNLIT_CATEGORY_STRING = 'surface_unlit'
/**
 * @const {string} MULTI_OUTPUT_TYPE_STRING
 * 
     * The name of the MaterialX type for a multi-output node.
 */
let MULTI_OUTPUT_TYPE_STRING = 'multioutput'

/**
 * 
     * Base class for MaterialX converters
 */
class MxConverter {
    /**
     * Export a MaterialX document to a glTF procedural graph. This method must be implemented by derived classes.
     * @param ne_mex - The MaterialX runtime.
     * @param doc - The MaterialX document
     */
    export(ne_mx, doc) {
        return (() => { throw new Error("Method not implemented. This is a required base class method."); })();
    }

    /** 
     * 
     * Get the type that the converter can export to. This method must be implemented by derived classes.
     * @return The type supported by the converter.
     */
    exportType() {
        return (() => { throw new Error("Method not implemented. This is a required base class method."); })();
    }

    /** 
     * 
     * Import a glTF procedural graph to a MaterialX document. This method must be implemented by derived classes.
     * @param ne_mx - The MaterialX runtime.
     * @param gltfDoc - The glTF document to convert.
     * @param stdlib - The MaterialX standard library.
     * @return The MaterialX document if successful, otherwise null.
     */
    import(ne_mx, gltfDoc, stdlib) {
        return (() => { throw new Error("Method not implemented. This is a required base class method."); })();
    }

    /** 
     * 
     * Get the type that the converter can import from. This method must be implemented by derived classes.
     * @return The type supported by the converter.
     */
    importType() {
        return (() => { throw new Error("Method not implemented. This is a required base class method."); })();
    }
}

/**
 * @class glTFMaterialX
 * 
 * Class for converting between glTF and MaterialX
 */
class glTFMaterialX extends MxConverter {
    constructor() {
        super();
    }

    /** 
     * 
     * Get the type that the converter can export to.
     * @return The type supported by the converter.
     */
    exportType() {
        return 'gltf';
    }


    /** 
     * 
     * Get the type that the converter can import from.
     * 
     * @return The type supported by the converter.
     */
    importType() {
        return 'gltf';
    }

    /**
     * 
     * Convert a scalar value to a string.
     * @param {any} value - The scalar value to convert.
     * @param {string} type - The type of the value.
     * @return {string|null} - The converted string value, or null if the type is unsupported.
     */
    scalarToString(value, type) {
        let returnvalue = null;

        const supportedTypes = ['string', 'integer', 'matrix33', 'matrix44', 'vector2', 'vector3', 'vector4', 'float', 'color3', 'color4'];
        const arrayTypes = ['matrix33', 'matrix44', 'vector2', 'vector3', 'vector4', 'color3', 'color4'];

        if (supportedTypes.includes(type)) {
            if (arrayTypes.includes(type)) {
                returnvalue = value.map(x => String(x)).join(', ');
            } else {
                returnvalue = String(value);
            }
        }

        return returnvalue;
    }

    /** 
    
     * Convert a string to a scalar value.
    @param value: The string value to convert.
    @param type: The type of the value.
    @return The converted scalar value if successful, otherwise the original string value.
    */
    stringToScalar(value, type) {
        let returnvalue = value;

        const scalarTypes = ['integer', 'matrix33', 'matrix44', 'vector2', 'vector3', 'vector4', 'float', 'color3', 'color4'];

        if (scalarTypes.includes(type)) {
            const splitvalue = value.split(',');

            if (splitvalue.length > 1) {
                returnvalue = splitvalue.map(x => parseFloat(x));
            } else {
                if (type === 'integer') {
                    returnvalue = parseInt(value, 10);
                } else {
                    returnvalue = parseFloat(value);
                }
            }
        }

        return returnvalue;
    }

    /** 
    
     * Initialize a new glTF image entry and texture entry which references
    the image entry.
 
    @param texture: The glTF texture entry to initialize.
    @param name: The name of the texture entry.
    @param uri: The URI of the image entry.
    @param images: The list of images to append the new image entry to.
    */
    initialize_gtlf_texture(texture, name, uri, images) {
        const image = {};
        image.name = name;

        // Assuming mx.FilePath and mx.FormatPosix equivalents exist in JavaScript context
        //const uriPath = ne_mx.createFilePath(uri);  // Assuming mx.FilePath is a class in the context
        //image.uri = uriPath.asString(ne_mx.FormatPosix);  // Assuming asString method and FormatPosix constant exist
        image.uri = uri;

        images.push(image);

        texture.name = name;
        texture.source = images.length - 1;
    }

    /**
     * 
     * Get the URI of a glTF texture.
     * @param {object} texture - The glTF texture.
     * @param {Array<object>} images - The set of glTF images.
     * @return {string} - The URI of the texture.
     */
    getGLTFTextureUri(texture, images) {
        let uri = '';
        if (texture && 'source' in texture) {
            const source = texture.source;
            if (source < images.length) {
                const image = images[source];
                if ('uri' in image) {
                    uri = image.uri;
                }
            }
        }
        return uri;
    }

    /**
     * 
     * Does the glTF document have the required extensions.
     * @param {object} glTFDoc - The glTF document to check.
     * @return {Array} - The result of the check in the form [boolean, string], where "boolean" is true if the extensions are present, 
     * and "string" is an error message if the extensions are not present.
     */
    haveExtensions(glTFDoc) {
        // check extensionsUsed for KHR_texture_procedurals
        let extensionsUsed = glTFDoc.extensionsUsed || null;
        if (extensionsUsed === null) {
            return [null, 'No extension used'];
        }
        let found = [false, false];
        for (let ext of extensionsUsed) {
            if (ext === 'KHR_texture_procedurals') {
                found[0] = true;
            }
            if (ext === 'EXT_texture_procedurals_mx_1_39') {
                found[1] = true;
            }
        }
        if (!found[0])
            return [null, 'Missing KHR_texture_procedurals extension'];
        if (!found[1])
            return [null, 'Missing EXT_texture_procedurals_mx_1_39 extension'];

        return [true, ''];
    }

    /** 
     * 
     * Add inputs to a node from a given MaterialX node definition.
     * @param {object} node - The MaterialX node to add inputs to.
     * @param {object} nodeDef - The MaterialX node definition to add inputs from.
     * @return {object} - The updated MaterialX node.
     */
    addInputsFromNodeDef(node, nodeDef) {
        if (nodeDef) {
            for (let nodeDefInput of nodeDef.getActiveInputs()) {
                let inputName = nodeDefInput.getName();
                let nodeInput = node.getInput(inputName);
                if (!nodeInput) {
                    //console.log('-------------> add input:', inputName);
                    nodeInput = node.addInput(inputName, nodeDefInput.getType());
                    if (nodeDefInput.hasValueString()) {
                        nodeInput.setValueString(nodeDefInput.getValueString(), nodeDefInput.getType());
                    }
                }
            }
        }
    }

    /** 
     * 
     * Convert a glTF procedural graph to a MaterialX document.
     * @param {object} ne_mx - The MaterialX runtime.
     * @param {string} glTFDocString - The glTF document to convert.
     * @param {object} stdlib - The MaterialX standard library.
     */
    import(ne_mx, glTFDocString, stdlib) {
        if (!ne_mx) {
            return [null, 'MaterialX runtime not passed in'];
        }
        let glTFDoc = JSON.parse(glTFDocString);

        let extensionCheck = this.haveExtensions(glTFDoc);
        if (extensionCheck[0] === null) {
            return extensionCheck;
        }

        let doc = ne_mx.createDocument();

        // Import the graph
        this.importGraphs(doc, glTFDoc);

        let global_extensions = glTFDoc.extensions || null;
        let procedurals = null;
        if (global_extensions && global_extensions.KHR_texture_procedurals) {
            procedurals = global_extensions.KHR_texture_procedurals.procedurals || null;
            console.log('Imported all procedurals:', procedurals);
        }

        // Import materials and connect to graphs as needed
        let shaderName = MTLX_DEFAULT_SHADER_NAME;
        let materialName = MTLX_DEFAULT_MATERIAL_NAME;
        let materialIndex = 1;
        let glTFmaterials = glTFDoc.materials || null;
        if (glTFmaterials) {

            // TODO iterator over all the mappings.
            let inputMaps = [];
            inputMaps[MTLX_GLTF_PBR_CATEGORY] = [
                ['base_color', 'baseColorTexture', 'pbrMetallicRoughness'],
                ['metallic', 'metallicRoughnessTexture', 'pbrMetallicRoughness'],
                ['roughness', 'metallicRoughnessTexture', 'pbrMetallicRoughness'],
                ['occlusion', 'occlusionTexture', ''],
                ['normal', 'normalTexture', ''],
                ['emissive', 'emissiveTexture', '']
            ];
            inputMaps[MTLX_UNLIT_CATEGORY_STRING] = [['emission_color', 'baseColorTexture', 'pbrMetallicRoughness']]

            for (let glTFmaterial of glTFmaterials) {

                //console.log('reading material:', glTFmaterial.name || 'no name');
                let mtlxShaderName = glTFmaterial.name;
                let mtlxMaterialName = '';
                if (mtlxShaderName.length == 0) {
                    mtlxShaderName = shaderName + String(materialIndex);
                    materialIndex++;
                    mtlxMaterialName = materialName + String(materialIndex);
                }
                else {
                    mtlxMaterialName = 'MAT_' + mtlxShaderName;
                }
                mtlxShaderName = doc.createValidChildName(mtlxShaderName);
                mtlxMaterialName = doc.createValidChildName(mtlxMaterialName);

                //console.log('create valid names:', mtlxShaderName, mtlxMaterialName);

                let use_unlit = false;
                let extensions = glTFmaterial.extensions || null;
                if (extensions) {
                    let KHR_materials_unlit = extensions.KHR_materials_unlit || null;
                    if (KHR_materials_unlit) {
                        use_unlit = true;
                    }
                }

                let shaderCategory = MTLX_GLTF_PBR_CATEGORY;
                let nodedefString = 'ND_gltf_pbr_surfaceshader';
                if (use_unlit) {
                    shaderCategory = MTLX_UNLIT_CATEGORY_STRING;
                    nodedefString = 'ND_surface_unlit';
                }
                let comment = doc.addChildOfCategory('comment')
                comment.setDocString(' Generated shader: ' + mtlxShaderName + ' ')
                let shaderNode = doc.addNode(shaderCategory, mtlxShaderName, ne_mx.SURFACE_SHADER_TYPE_STRING);
                //console.log(ne_mx.prettyPrint(shaderNode))
                shaderNode.setAttribute(ne_mx.InterfaceElement.NODE_DEF_ATTRIBUTE, nodedefString)
                if (stdlib) {
                    let nodedef = stdlib.getNodeDef(nodedefString);
                    if (nodedef)
                        this.addInputsFromNodeDef(shaderNode, nodedef);
                }

                // Connect inputs to nodegraph outputs. Ugly bespoke code...
                let defaultGraphName = 'nodegraph';
                if (procedurals) {
                    let currentMap = inputMaps[shaderCategory];
                    for (let map of currentMap) {
                        let destInput = map[0];
                        let sourceTexture = map[1];
                        let sourceParent = map[2];
                        if (sourceParent.length > 0) {
                            if (sourceParent == 'pbrMetallicRoughness') {
                                let newSource = glTFmaterial.pbrMetallicRoughness[sourceTexture];
                                //console.log('remap from  parent:', sourceParent, 'sourceTexture:', sourceTexture, 'to:', newSource);
                                sourceTexture = newSource;
                            }
                        }
                        else {
                            sourceTexture = glTFmaterial[sourceTexture];
                        }

                        let baseColorTexture = sourceTexture;

                        if (baseColorTexture) {
                            //console.log('-- sourceTexture:', sourceTexture);
                            if (baseColorTexture) {
                                let extensions = baseColorTexture.extensions || null;
                                if (extensions) {
                                    //console.log('----- extensions:', extensions);
                                    let KHR_texture_procedurals = extensions.KHR_texture_procedurals || null;
                                    if (KHR_texture_procedurals) {
                                        let pindex = KHR_texture_procedurals.index;
                                        let output = KHR_texture_procedurals.output;
                                        //console.log('----- proc index:', pindex, 'output:', output);
                                        if (pindex != null) {
                                            if (pindex < procedurals.length) {
                                                //console.log('------ connect to proc: ', procedurals[pindex]);
                                                let proc = procedurals[pindex];
                                                if (proc) {
                                                    let nodegraphName = defaultGraphName;
                                                    if (proc.name)
                                                        nodegraphName = proc.name;

                                                    let graphOutputs = proc.outputs || null;
                                                    if (graphOutputs && graphOutputs.length > 0) {
                                                        let proc_output = graphOutputs[0];
                                                        if (output != null) {
                                                            proc_output = graphOutputs[output];
                                                        }
                                                        if (proc_output) {
                                                            let input = shaderNode.getInput(destInput);
                                                            if (!input)
                                                                input = shaderNode.addInput(destInput, proc_output.type);
                                                            if (input) {
                                                                //console.log('------ connect to output:', proc_output.name, 'type:', proc_output.type);
                                                                input.setNodeGraphString(nodegraphName);
                                                                input.setAttribute('output', proc_output.name);
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

                comment = doc.addChildOfCategory('comment')
                comment.setDocString(' Generated material: ' + mtlxMaterialName + ' ')
                let materialNode = doc.addNode(ne_mx.SURFACE_MATERIAL_NODE_STRING, mtlxMaterialName, ne_mx.MATERIAL_TYPE_STRING)
                let shaderInput = materialNode.addInput(ne_mx.SURFACE_SHADER_TYPE_STRING, ne_mx.SURFACE_SHADER_TYPE_STRING)
                shaderInput.setAttribute(MTLX_NODE_NAME_ATTRIBUTE, mtlxShaderName)
                //console.log(ne_mx.prettyPrint(materialNode))

                console.log('>> Import material:', materialNode.getName(), 'Shader:', shaderNode.getName());
            }
        }

        // Import asset information
        let asset = glTFDoc.asset || null;
        let docDoc = ''
        if (asset) {
            //console.log('import asset info')
            let version = asset.version || null;
            if (version) {
                let comment = doc.addChildOfCategory('comment');
                docDoc += 'glTF version: ' + version + '. ';
                comment.setDocString('glTF version: ' + version);
            }
            let generator = asset.generator || null;
            if (generator) {
                let comment = doc.addChildOfCategory('comment');
                docDoc += 'glTF generator: ' + generator + '. ';
                comment.setDocString('glTF generator: ' + generator);
            }
            let copyRight = asset.copyright || null;
            if (copyRight) {
                let comment = doc.addChildOfCategory('comment');
                docDoc += 'Copyright: ' + copyRight + '. ';
                comment.setDocString('Copyright: ' + copyRight);
            }

            if (docDoc.length > 0) {
                doc.setAttribute('doc', docDoc);
            }
        }

        // Validate
        let errors = ''
        var valid = doc.validate(errors);

        let docString = ne_mx.writeToXmlString(doc);
        //console.log('*** gltF -> MaterialX document:', docString);
        return [docString, errors];
    }

    /**
     * 
     * Convert glTF document to a MaterialX document.
     * @param {object} doc - The MaterialX document to update.
     * @param {object} gltfDoc - The glTF document to read from.
     * @return {object|null} - The root MaterialX element if successful, otherwise null.
     */
    importGraphs(doc, gltfDoc) {
        let root_mtlx = null;

        // Look for the extension
        let extensions = gltfDoc.extensions || null;
        let procedurals = null;
        if (extensions) {
            procedurals = extensions.KHR_texture_procedurals.procedurals || null;
        }

        if (procedurals === null) {
            console.log('> Error - no procedurals array found');
            return null;
        }

        let graph_index = 0;

        // Use index to auto-generate dummy nodegraph names
        let procindex = 1;
        for (let proc of procedurals) {
            console.log(`> Scan procedural ${procindex} of ${procedurals.length} :`);
            if (!proc.nodetype) {
                console.log('>> Warning: No nodetype found in procedural. SKipping');
                continue;
            }

            if (proc.nodetype !== 'nodegraph') {
                console.log('>> Skip unsupported rocedural nodetype:', proc.nodetype);
                continue;
            }

            let graphname = 'graph_' + graph_index;
            if (proc.name) {
                graphname = proc.name;
            } else {
                graph_index++;
            }
            let mtlxgraph = doc.addNodeGraph(graphname);
            root_mtlx = mtlxgraph;

            let input_index = 0;
            let output_index = 0;
            let node_index = 0;

            let inputs = proc.inputs || [];
            let outputs = proc.outputs || [];
            let nodes = proc.nodes || [];

            // Scan for input interfaces in the nodegraph
            for (let input of inputs) {
                let inputname = input.name || 'input_' + input_index;
                if (!input.name) {
                    input_index++;
                }

                let inputtype = input.type || null;
                if (!inputtype) {
                    console.log('>> Error - Input type not found for graph input:', inputname);
                    continue;
                }

                let mtlxinput = mtlxgraph.addInput(inputname, inputtype);

                if (input.colorspace) {
                    mtlxinput.setAttribute('colorspace', input.colorspace);
                }

                if (inputtype === 'filename') {
                    let textureIndex = input.texture || null;
                    if (textureIndex !== null) {
                        let gltftextures = gltfDoc.textures || null;
                        let gltfimages = gltfDoc.images || null;
                        if (gltftextures && gltfimages) {
                            let gltftexture = gltftextures[textureIndex] || null;
                            if (gltftexture) {
                                let uri = this.getGLTFTextureUri(gltftexture, gltfimages);
                                mtlxinput.setValueString(uri, inputtype);
                            }
                        }
                    }
                }

                let inputvalue = input.value || null;
                if (inputvalue !== null) {
                    let mtlxvalue = this.scalarToString(inputvalue, inputtype);
                    if (mtlxvalue !== null) {
                        mtlxinput.setValueString(mtlxvalue, inputtype);
                    } else {
                        console.log('>> Error - Unsupported handle input type:', inputtype, '. Performing straight assignment.');
                        mtlxinput.setValueString(String(inputvalue, inputtype));
                    }
                } else {
                    console.log('>> Invalid usage of top level graph connections:', inputname);
                    if (input.procedural) {
                        //console.log('*** Connect input to procedural', proc.procedural);
                    }
                }
            }

            // Scan for output interfaces in the nodegraph
            for (let output of outputs) {
                let outputname = output.name || 'output_' + output_index;
                let outputtype = output.type || null;
                let mtlxgraph_output = mtlxgraph.addOutput(outputname, outputtype);

                let connectable = null;
                if (output.input !== undefined) {
                    connectable = inputs[output.input];
                    if (connectable)
                        mtlxgraph_output.setAttribute(MTLX_INTERFACEINPUT_NAME_ATTRIBUTE, connectable.name);
                    else
                        console.log('>> Error - Input not found:', output.input, inputs);
                }
                /* } else if (output.output !== undefined) {
                    connectable = outputs[output.output];
                    if (connectable)
                        mtlxgraph_output.setAttribute('output', connectable.name);
                    else
                        console.log('*** ERROR: Output not found:', output.output, outputs);
                } */
                else if (output.node !== undefined) {
                    connectable = nodes[output.node];
                    if (connectable) {
                        mtlxgraph_output.setAttribute(MTLX_NODE_NAME_ATTRIBUTE, connectable.name);
                        // Check for any output qualifier
                        if (output.output !== undefined) {
                            mtlxgraph_output.setAttribute('output', output.output);
                        }
                    }
                    else
                        console.log('>> Error - Output node not found:', output.node, nodes);
                }
            }

            // Scan for nodes in the nodegraph
            for (let node of nodes) {
                let nodename = node.name || 'node_' + node_index;
                let nodetype = node.nodetype || null;
                let outputType = node.type || null;
                let node_outputs = node.outputs || [];
                if (node_outputs.length > 1) {
                    outputType = MULTI_OUTPUT_TYPE_STRING;
                }
                let mtlxnode = mtlxgraph.addChildOfCategory(nodetype);
                mtlxnode.setName(nodename);
                if (outputType) {
                    mtlxnode.setType(outputType);
                } else {
                    console.log('>> Error - no output type for node:', nodename);
                }

                input_index = 0;
                let node_inputs = node.inputs || [];
                for (let input of node_inputs) {
                    let inputname = input.name || 'input_' + input_index;
                    let inputtype = input.type || null;
                    let mtlxinput = mtlxnode.addInput(inputname, inputtype);

                    if (input.colorspace) {
                        mtlxinput.setAttribute('colorspace', input.colorspace);
                    }

                    if (inputtype === 'filename') {
                        let textureIndex = input.texture || null;
                        if (textureIndex !== null) {
                            let gltftextures = gltfDoc.textures || null;
                            let gltfimages = gltfDoc.images || null;
                            if (gltftextures && gltfimages) {
                                let gltftexture = gltftextures[textureIndex] || null;
                                if (gltftexture) {
                                    let uri = this.getGLTFTextureUri(gltftexture, gltfimages);
                                    mtlxinput.setValueString(uri, inputtype);
                                }
                            }
                        }
                    }

                    let inputvalue = input.value || null;
                    if (inputvalue !== null) {
                        let mtlxvalue = this.scalarToString(inputvalue, inputtype);
                        if (mtlxvalue !== null) {
                            mtlxinput.setValueString(mtlxvalue, inputtype);
                        } else {
                            console.log('>> Error - Unsupported input type:', inputtype, '. Performing straight assignment.');
                            mtlxinput.setValueString(String(inputvalue), inputtype);
                        }
                    } else {
                        let connectable = null;
                        if (input.input !== undefined) {
                            connectable = inputs[input.input];
                            mtlxinput.setAttribute(MTLX_INTERFACEINPUT_NAME_ATTRIBUTE, connectable.name);
                        } else if (input.output !== undefined) {
                            if (input.node !== undefined) {
                                mtlxinput.setAttribute('output', input.output);
                            } else {
                                connectable = outputs[input.output];
                                mtlxinput.setAttribute('output', connectable.name);
                            }
                        }
                        if (input.node !== undefined) {
                            connectable = nodes[input.node];
                            mtlxinput.setAttribute(MTLX_NODE_NAME_ATTRIBUTE, connectable.name);
                        }
                    }
                }

                output_index = 0;
                for (let output of node_outputs) {
                    let outputname = output.name || 'output_' + output_index;
                    let outputtype = output.type || null;
                    let mtlxoutput = mtlxnode.addOutput(outputname, outputtype);

                    let connectable = null;
                    if (output.input !== undefined) {
                        connectable = inputs[output.input];
                        mtlxoutput.setAttribute(MTLX_INTERFACEINPUT_NAME_ATTRIBUTE, connectable.name);
                    } else if (output.output !== undefined) {
                        connectable = outputs[output.output];
                        mtlxoutput.setAttribute('output', connectable.name);
                    }
                    if (output.node !== undefined) {
                        connectable = nodes[output.node];
                        mtlxoutput.setAttribute(MTLX_NODE_NAME_ATTRIBUTE, connectable.name);
                    }
                }
            }

            procindex++;
        }

        return root_mtlx;
    }

    /** 
    
     * Convert a MaterialX graph to JSON.
    @param ne_mx: MaterialX runtime
    @param graph: The MaterialX graph to convert.
    @param json: The JSON object to add the converted graph to.
    */
    exportGraph(ne_mx, graph, json, materials) {
        let no_result = [null, null, null]

        if (!ne_mx) {
            console.log('MaterialX runtime not passed in')
            return no_result;
        }

        let graphOutputs = graph.getOutputs();
        if (graphOutputs.length == 0) {
            console.log('No graph outputs found on graph: ', graph.getNamePath())
            return no_result;
        }

        const debug = false;
        const usePaths = false;

        // Create fallback texture:
        const fallback = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQI12P4z/AfAAQAAf/zKSWvAAAAAElFTkSuQmCC';
        let fallbackIndex = -1;

        let imageArray = json['images'] || [];
        if (!json['images']) json['images'] = imageArray;

        for (let i = 0; i < imageArray.length; i++) {
            const image = imageArray[i];
            if (image['uri'] === fallback) {
                fallbackIndex = i;
                break;
            }
        }

        let fallbackTextureIndex = -1;
        if (fallbackIndex === -1) {
            const image = {
                'uri': fallback,
                'name': 'KHR_texture_procedural_fallback'
            };
            imageArray.push(image);
            fallbackIndex = imageArray.length - 1;
        }

        let textureArray = json['textures'] || [];
        if (!json['textures']) json['textures'] = textureArray;

        for (let i = 0; i < textureArray.length; i++) {
            const texture = textureArray[i];
            if (texture['source'] === fallbackIndex) {
                fallbackTextureIndex = i;
                break;
            }
        }

        if (fallbackTextureIndex === -1) {
            textureArray.push({ 'source': fallbackIndex });
            fallbackTextureIndex = textureArray.length - 1;
        }

        const skipAttr = ['uiname', 'xpos', 'ypos'];
        const procDictNodes = {};
        const procDictInputs = {};
        const procDictOutputs = {};

        let extensions = json['extensions'] || {};
        if (!json['extensions']) json['extensions'] = extensions;

        let KHR_texture_procedurals = extensions['KHR_texture_procedurals'] || {};
        if (!extensions['KHR_texture_procedurals']) extensions['KHR_texture_procedurals'] = KHR_texture_procedurals;

        if (!KHR_texture_procedurals['procedurals']) {
            KHR_texture_procedurals['procedurals'] = [];
        }

        const procs = KHR_texture_procedurals['procedurals'];
        const nodegraph = {
            'name': usePaths ? graph.getNamePath() : graph.getName(),
            'nodetype': graph.getCategory()
        };

        nodegraph['type'] = graphOutputs.length > 1 ? 'multioutput' : graphOutputs[0].getType();
        const nodegraphInputs = nodegraph['inputs'] = [];
        const nodegraphOutputs = nodegraph['outputs'] = [];
        const nodegraphNodes = nodegraph['nodes'] = [];
        procs.push(nodegraph);

        const metadata = ['colorspace', 'unit', 'unittype', 'uiname', 'uimin', 'uimax', 'uifolder', 'doc'];

        graph.getNodes().forEach((node) => {
            const jsonNode = {
                'name': usePaths ? node.getNamePath() : node.getName()
            };
            nodegraphNodes.push(jsonNode);
            procDictNodes[node.getNamePath()] = nodegraphNodes.length - 1;
        });

        graph.getInputs().forEach((input) => {
            const jsonNode = {
                'name': usePaths ? input.getNamePath() : input.getName(),
                'nodetype': input.getCategory()
            };

            metadata.forEach((meta) => {
                if (input.getAttribute(meta)) {
                    jsonNode[meta] = input.getAttribute(meta);
                }
            });

            if (input.getValue() !== null) {
                const inputType = input.getAttribute(ne_mx.TypedElement.TYPE_ATTRIBUTE);
                jsonNode['type'] = inputType;
                if (inputType === ne_mx.FILENAME_TYPE_STRING) {
                    const texture = {};
                    const filename = input.getResolvedValueString();
                    //console.log('initialize file texture: ', input.getNamePath(), filename, '. Skip image properties');
                    this.initialize_gtlf_texture(texture, input.getNamePath(), filename, imageArray);
                    textureArray.push(texture);
                    jsonNode['texture'] = textureArray.length - 1;
                } else {
                    let value = input.getValueString();
                    value = this.stringToScalar(value, inputType);
                    jsonNode['value'] = value;
                }
                nodegraphInputs.push(jsonNode);
                procDictInputs[input.getNamePath()] = nodegraphInputs.length - 1;
            } else {
                //if (input.getAttribute("interfacename") || input.getAttrbute("nodename") || 
                //    input.getAttribute("nodegraph"))
                //{
                //    console.error('Error: Graph input connections to upstream nodes are invalid. Input skipped:', input.getNamePath());
                //}
                //else
                {
                    console.error('Error: no value or invalid connection specified for input. Input skipped:', input.getNamePath());
                }
            }
        });

        graphOutputs.forEach((output) => {
            const jsonNode = {
                'name': usePaths ? output.getNamePath() : output.getName()
            };
            nodegraphOutputs.push(jsonNode);
            procDictOutputs[output.getNamePath()] = nodegraphOutputs.length - 1;

            jsonNode['nodetype'] = output.getCategory();
            jsonNode['type'] = output.getType();

            let connection = output.getAttribute(MTLX_INTERFACEINPUT_NAME_ATTRIBUTE);
            if (connection.length == 0)
                connection = output.getAttribute(MTLX_NODE_NAME_ATTRIBUTE);

            const connectionNode = graph.getChild(connection);
            if (connectionNode) {
                let connectionPath = connectionNode.getNamePath()
                if (debug)
                    jsonNode['debug_connection_path'] = connectionPath;

                if (procDictInputs[connectionPath] != null) {
                    jsonNode['input'] = procDictInputs[connectionPath];
                } else if (procDictNodes[connectionPath] != null) {
                    jsonNode['node'] = procDictNodes[connectionPath];
                } else {
                    console.error('Invalid output connection to:', connectionPath);
                }

                const outputString = output.getAttribute('output');
                if (outputString.length > 0) {
                    jsonNode['output'] = outputString;
                }
            }
        });

        graph.getNodes().forEach((node) => {
            let jsonNode = null;
            const index = procDictNodes[node.getNamePath()];
            jsonNode = nodegraphNodes[index];
            jsonNode['nodetype'] = node.getCategory();
            const nodedef = node.getNodeDef();

            if (debug && nodedef && nodedef.getNodeGroup().length) {
                jsonNode['nodegroup'] = nodedef.getNodeGroup();
            }

            node.getAttributeNames().forEach((attrName) => {
                if (!skipAttr.includes(attrName)) {
                    jsonNode[attrName] = node.getAttribute(attrName);
                }
            });

            const inputs = [];
            node.getInputs().forEach((input) => {
                const inputItem = {
                    'name': input.getName(),
                    'nodetype': 'input'
                };

                metadata.forEach((meta) => {
                    if (input.getAttribute(meta)) {
                        inputItem[meta] = input.getAttribute(meta);
                    }
                });

                const inputType = input.getAttribute(ne_mx.TypedElement.TYPE_ATTRIBUTE);
                inputItem['type'] = inputType;

                if (input.getValue() !== null) {
                    if (inputType === ne_mx.FILENAME_TYPE_STRING) {
                        const texture = {};
                        const filename = input.getResolvedValueString();
                        this.initialize_gtlf_texture(texture, input.getNamePath(), filename, imageArray);
                        textureArray.push(texture);
                        inputItem['texture'] = textureArray.length - 1;
                    } else {
                        let value = input.getValueString();
                        value = this.stringToScalar(value, inputType);
                        inputItem['value'] = value;
                    }
                } else {
                    let isInterface = true;
                    let connection = input.getAttribute(MTLX_INTERFACEINPUT_NAME_ATTRIBUTE);
                    if (!connection.length) {
                        isInterface = false;
                        connection = input.getAttribute(MTLX_NODE_NAME_ATTRIBUTE);
                    }

                    if (connection.length > 0) {
                        const connectionNode = graph.getChild(connection);
                        if (connectionNode) {
                            const inputType = input.getAttribute(ne_mx.TypedElement.TYPE_ATTRIBUTE);
                            inputItem['type'] = inputType;
                            let connectionPath = connectionNode.getNamePath();
                            if (debug) {
                                inputItem['debug_connection_path'] = connectionPath;
                            }

                            if (isInterface && procDictInputs[connectionPath] != null) {
                                inputItem['input'] = procDictInputs[connectionPath];
                            } else if (procDictNodes[connectionPath] != null) {
                                inputItem['node'] = procDictNodes[connectionPath];
                            }

                            const outputString = input.getAttribute('output');
                            if (outputString.length > 0) {
                                const connectedNodeOutputs = connectionNode.getOutputs();
                                for (let i = 0; i < connectedNodeOutputs.length; i++) {
                                    if (connectedNodeOutputs[i].getName() === outputString) {
                                        inputItem['output'] = i;
                                        break;
                                    }
                                }
                            }
                        } else {
                            console.error('Error: Invalid input connection to:', connection, ' from: input:', input.getNamePath(), ' node:', node.getNamePath());
                        }
                    }

                    if (input.getAttribute(MTLX_NODEGRAPH_NAME_ATTRIBUTE)) {
                        console.error('Error: Invalid input connection to:', connection, ' from: input:', input.getNamePath(), ' node:', node.getNamePath());
                    }
                }

                inputs.push(inputItem);
            });

            if (inputs.length > 0) {
                jsonNode['inputs'] = inputs;
            }

            const outputs = [];
            node.getOutputs().forEach((output) => {
                const outputItem = {
                    'nodetype': 'output',
                    'name': output.getName(),
                    'type': output.getType()
                };
                outputs.push(outputItem);
            });

            if (nodedef) {
                nodedef.getOutputs().forEach((output) => {
                    let exists = false;
                    outputs.forEach((outputItem) => {
                        if (outputItem['name'] === output.getName()) {
                            exists = true;
                        }
                    });

                    if (!exists) {
                        const outputItem = {
                            'nodetype': 'output',
                            'name': output.getName(),
                            'type': output.getType()
                        };
                        outputs.push(outputItem);
                    }
                });
            } else {
                console.error('Missing nodedef for node:', node.getNamePath());
            }

            if (outputs.length > 0) {
                jsonNode['outputs'] = outputs;
            }
        });

        return [procs, procDictOutputs, procDictNodes, fallbackTextureIndex];
    }

    /**
     * 
     * Convert a MaterialX document to a glTF procedural graph
     * @param {object} ne_mx - The MaterialX runtime.
     * @param {object} glTFDoc - The MaterialX document to convert.
     */
    export(ne_mx, glTFDoc) {

        if (!ne_mx) {
            status = 'MaterialX runtime not passed in'
            return [null, status];
        }

        let status = '';
        if (!glTFDoc) {
            status = 'Invalid document to convert';
            return [null, status];
        }

        let materials = [];
        let mxMaterials = glTFDoc.getMaterialNodes();
        if (mxMaterials.length == 0) {
            //status = 'No MaterialX materials found in document';            
            //return [null, status];
        }

        let json = {};
        let json_asset = {
            "version": "2.0",
            "generator": "MaterialX 1.39 to glTF 2.0 procedural textures converter",
            "copyright": "Copyright (c) 2024, Bernard Kwok"
        }

        let inputMaps = [];
        inputMaps[MTLX_GLTF_PBR_CATEGORY] = [
            ['base_color', 'baseColorTexture', 'pbrMetallicRoughness'],
            ['metallic', 'metallicRoughnessTexture', 'pbrMetallicRoughness'],
            ['roughness', 'metallicRoughnessTexture', 'pbrMetallicRoughness'],
            ['occlusion', 'occlusionTexture', ''],
            ['normal', 'normalTexture', ''],
            ['emissive', 'emissiveTexture', '']
        ];
        inputMaps[MTLX_UNLIT_CATEGORY_STRING] = [['emission_color', 'baseColorTexture', 'pbrMetallicRoughness']]

        let pbrNodes = [];
        let fallbackTextureIndex = -1;
        let procs = [];
        let exportGraphNames = [];

        for (let mxMaterial of mxMaterials) {
            let mxshaders = ne_mx.getShaderNodes(mxMaterial);
            for (let shaderNode of mxshaders) {
                let category = shaderNode.getCategory();
                let path = shaderNode.getNamePath()
                let isUnlit = (category == MTLX_UNLIT_CATEGORY_STRING);
                let isPBR = (category == MTLX_GLTF_PBR_CATEGORY);
                if ((isPBR || isUnlit) && pbrNodes[path] == null) {
                    console.log('> Convert shader to glTF:', shaderNode.getNamePath(), 'Category:', category);
                    // Add to pbrNodes if not exists
                    pbrNodes[path] = shaderNode;

                    let material = {};
                    {
                        let base_color_input = null;
                        let base_color_output = '';
                        let inputPairs = inputMaps[category];
                        for (let inputPair of inputPairs) {
                            //console.log('Input map:', inputPair[0], ' maps to', inputPair[1]);
                            base_color_input = shaderNode.getInput(inputPair[0]);
                            base_color_output = inputPair[1];

                            if (!base_color_input) {
                                continue;
                            }

                            let nodeGraphName = base_color_input.getNodeGraphString();
                            if (nodeGraphName.length == 0) {
                                continue;
                            }

                            let nodeGraphOutput = base_color_input.getOutputString();
                            material['name'] = path;

                            let parent = material;
                            if (inputPair[2].length > 0) {
                                if (!material[inputPair[2]]) {
                                    material[inputPair[2]] = {};
                                }
                                parent = material[inputPair[2]]
                            }

                            // Look for existing graph
                            let graphIndex = -1;
                            let outputIndex = -1;
                            if (procs) {
                                let i = 0;
                                for (let proc of procs) {
                                    if (proc['name'] == nodeGraphName) {
                                        graphIndex = i;
                                        if (nodeGraphOutput.length > 0) {
                                            let outputs = proc['outputs'];
                                            let j = 0;
                                            for (let output of outputs) {
                                                if (output['name'] == nodeGraphOutput) {
                                                    outputIndex = j;
                                                    break;
                                                }
                                                j++;
                                            }
                                        }
                                        break;
                                    }
                                    i++;
                                }
                            }

                            if (graphIndex >= 0) {
                                let baseColorTexture = parent[base_color_output] = {}
                                baseColorTexture['index'] = fallbackTextureIndex;
                                let ext = baseColorTexture['extensions'] = {}
                                {
                                    if (isUnlit) {
                                        ext['KHR_materials_unlit'] = {};
                                    }
                                    let lookup = ext['KHR_texture_procedurals'] = {}
                                    lookup['index'] = graphIndex;
                                    if (outputIndex >= 0) {
                                        lookup['output'] = outputIndex;
                                    }
                                }
                            }
                            else {
                                let graph = glTFDoc.getNodeGraph(nodeGraphName);
                                exportGraphNames.push(nodeGraphName);

                                let gltfInfo = this.exportGraph(ne_mx, graph, json, materials)
                                //console.log('gltfInfo:', gltfInfo);
                                procs = gltfInfo[0]
                                let outputNodes = gltfInfo[1];
                                let proceduralNodes = gltfInfo[2];
                                fallbackTextureIndex = gltfInfo[3];

                                //console.log('procs', procs, 'gltfInfo:', gltfInfo, 'fallbackTextureIndex:', fallbackTextureIndex)

                                //visitedGraphs.push([nodeGraphName, nodeGraphOutput]);

                                let baseColorTexture = parent[base_color_output] = {}
                                baseColorTexture['index'] = fallbackTextureIndex;
                                let ext = baseColorTexture['extensions'] = {}
                                {
                                    if (isUnlit) {
                                        ext['KHR_materials_unlit'] = {};
                                    }
                                    let lookup = ext['KHR_texture_procedurals'] = {}
                                    lookup['index'] = procs.length - 1;
                                    let outputIndex = -1;

                                    if (nodeGraphOutput.length > 0) {
                                        for (let outputNodeName in outputNodes) {
                                            let nodeGraphOutputPath = (nodeGraphName + '/' + nodeGraphOutput);
                                            if (outputNodeName == nodeGraphOutputPath) {
                                                outputIndex = outputNodes[outputNodeName];
                                                break;
                                            }
                                        }
                                        if (outputIndex == -1) {
                                            console.error('Failed to find output:', nodeGraphOutput, ' in:', outputNodes)
                                        }
                                        lookup['output'] = outputIndex;
                                    }
                                    // Default is first procedural output
                                    else {
                                        lookup['output'] = 0;
                                    }
                                }
                            }
                        }
                    }

                    if (material['name']) {
                        materials.push(material);
                    }
                }
            }
        }

        let unconnectedGraphs = [];
        for (let ng of glTFDoc.getNodeGraphs()) {
            let ng_name = ng.getName();
            if (ng.getAttribute('nodedef') || ng.hasSourceUri()) {
                //console.log('Skip nodegraph for nodedef', ng_name, ng.getAttribute('nodedef'));
                continue;
            }
            if (!exportGraphNames.includes(ng_name)) {
                unconnectedGraphs.push(ng_name);

                let gltfInfo = this.exportGraph(ne_mx, ng, json, materials)
                procs = gltfInfo[0]
                let outputNodes = gltfInfo[1];
                let proceduralNodes = gltfInfo[2];
                fallbackTextureIndex = gltfInfo[3];
            }
        }

        if (materials.length > 0) {
            json['materials'] = materials;
            if (unconnectedGraphs.length > 0) {
                status = 'Exported unconnected graphs: ' + unconnectedGraphs.join(', ');
            }
        }
        else {
            if (unconnectedGraphs.length > 0) {
                status = 'Exported unconnected graphs: ' + unconnectedGraphs.join(', ');
            }
            else {
                status = 'No appropriate glTF shader graphs found';
            }
        }

        //console.log('pbrNodes:', pbrNodes, 'unlitNodes:', unlitNodes, 'materials:', json['materials'])

        if (procs.length > 0) {
            json['asset'] = json_asset;
            json['extensionsUsed'] = [];
            json['extensionsUsed'].push('KHR_texture_procedurals');
            json['extensionsUsed'].push('EXT_texture_procedurals_mx_1_39');
        }

        // Convert JSON to string
        let jsonString = json ? JSON.stringify(json, null, 2) : '';
        if (jsonString == '{}') {
            jsonString = '';
        }

        return [jsonString, status];
    }
}
