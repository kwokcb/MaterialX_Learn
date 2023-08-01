import sys, os, argparse

# Import blender package
import bpy

# MaterialX Setup
# Import MaterialX package
import MaterialX as mx

def initializeMaterialX(materialXRoot):
    """
    Perform basic setup
    """
    libraryPath = mx.FilePath('libraries')
    stdlib = mx.createDocument()
    searchPath = mx.FileSearchPath()
    searchPath.append(materialXRoot)
    libFiles = mx.loadLibraries([ libraryPath ], searchPath, stdlib)

    doc = mx.createDocument()
    doc.importLibrary(stdlib)
    return doc

def skipLibraryElement(elem):
    """
    Write predicate. Only works for MaterialX 1.38.7+
    """
    return not elem.hasSourceUri()

def writeMaterialX(doc, filePath, markdown_title):
    """
    Simple utility to write a document to a Markdown section
    and or a to disk.
    """
    writeOptions = mx.XmlWriteOptions()
    major, minor, patch = mx.getVersionIntegers()
    # Write predicate does not work prior to 1.38.7
    if major >= 1 and minor >= 38 and patch >= 7:
        writeOptions.writeXIncludeEnable = False
        writeOptions.elementPredicate = skipLibraryElement

    if markdown_title:
        documentContents = mx.writeToXmlString(doc, writeOptions)
        print(markdown_title)
        print(documentContents)
    
    if filePath:
        mx.writeToXmlFile(doc, filePath, writeOptions)

# MaterialX Graphing Utilities
def createNode(doc, definitionName, parent, name):
    "Utility to create a node under a given parent using a definition name and desired instance name"
    nodeName = parent.createValidChildName(name)
    nodedef = doc.getNodeDef(definitionName)
    if nodedef:
        newNode = parent.addNodeInstance(nodedef, nodeName)
        if newNode:
            return newNode
    else:
        print('Cannot find nodedef:',  definitionName)
    return None

def connectNodeToNode(inputNode, inputName, outputNode, outputName):
    "Connect an input on one node to an output on another node. Existence and type checking are performed."
    "Returns input port with connection set if succesful. Otherwise None is returned."

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
    else:
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

# Blender to MaterialX Conversion Utilities 
# - Blender Value to MaterialX Node Input
def floatToStr(val):
    return f"{val:.4g}"

def blender_createMtlxInput(portName, blenderVal, node, nodedef):
    """ 
    Creat input on shader node based on blender value 
    """
    #print('------- add input: ', portName)
    nodedefInput = nodedef.getInput(portName)
    if not nodedefInput:
        return

    valueLen = dict()
    valueLen['color3'] = 3
    valueLen['color4'] = 4
    valueLen['vector2'] = 2
    valueLen['vector3'] = 3
    valueLen['vector4'] = 4

    portType = nodedefInput.getType()

    valueString = ''
    if isinstance(blenderVal, float):
        valueString = floatToStr(blenderVal)  
    elif isinstance(blenderVal, int):
        valueString = str(blenderVal)
    elif isinstance(blenderVal, str):
        valueString = str(blenderVal)
    else:
        if len(blenderVal) in (2,3,4):
            blenderValString = []
            valueLength = valueLen[portType]
            for i, c in enumerate(blenderVal):
                if i < valueLength:                                 
                    blenderValString.append(floatToStr(blenderVal[i]))
            valueString = ','.join(blenderValString)

    if len(valueString):        
        newInput = node.addInput(portName, portType)
        if newInput:
            newInput.setValueString(valueString) 
    
    return newInput

# - Mapping of Blender Nodes / Inputs to MaterialX
def blender_init_node_dictionary(targetBSDF):

    # Manual name mapping from Blender BSDF to USD Preview Surface
    PBSDF_USDPS_map = dict()
    PBSDF_USDPS_map['Base Color'] = 'diffuseColor'
    PBSDF_USDPS_map['Specular'] = 'specularColor'
    PBSDF_USDPS_map['IOR'] = 'ior'
    PBSDF_USDPS_map['Clearcoat'] = 'clearcoat'
    PBSDF_USDPS_map['Clearcoat Roughness'] = 'clearcoatRoughness'
    PBSDF_USDPS_map['Metallic'] = 'metallic'
    PBSDF_USDPS_map['Roughness'] = 'roughness'
    PBSDF_USDPS_map['Alpha'] = 'opacity'
    PBSDF_USDPS_map['Emission'] = 'emissiveColor'  
    PBSDF_USDPS_map['Normal'] = 'normal'  

    IMAGE_map = dict()
    NORMALMAP_map = dict()

    # Mapping from Blender nodes to MaterialX node definitions
    SHADER_NODE_map = dict()
    SHADER_NODE_map['BSDF_PRINCIPLED'] =  targetBSDF
    SHADER_NODE_map['TEX_IMAGE'] =  'ND_image_'
    SHADER_NODE_map['NORMAL_MAP'] =  'ND_normalmap'

    SHADER_NODE_INPUTS_map = dict()
    SHADER_NODE_INPUTS_map['BSDF_PRINCIPLED'] = PBSDF_USDPS_map
    SHADER_NODE_INPUTS_map['TEX_IMAGE'] = IMAGE_map
    SHADER_NODE_INPUTS_map['NORMAL_MAP'] = NORMALMAP_map

    return [ SHADER_NODE_map, SHADER_NODE_INPUTS_map ]

def blender_createMtlxShaderNode(doc, name, shaderNodeDefinition, isMaterial):

    mtlxShadername = doc.createValidChildName(name + ('_' + 'Shader' if isMaterial else ''))
    mtlxShaderNode = createNode(doc, shaderNodeDefinition, doc, mtlxShadername)
    if not mtlxShaderNode:
        return None

    # Create MaterialX material and shader for each Blender material
    if isMaterial:
        mtlxName = doc.createValidChildName(name)
        mtlxMaterialNode = createNode(doc, 'ND_surfacematerial', doc, name)
        if mtlxMaterialNode:
            # Connect the material node to the output of the graph
            connectNodeToNode(mtlxMaterialNode, 'surfaceshader', mtlxShaderNode, '')          

    return mtlxShaderNode

# - Main Blender to MaterialX Converter
def blender_materialx(doc, shaderNodeMappings):
    """
    Simple Export of a few Blender nodes to MaterialX material nodes + shaders
    """
    SHADER_NODE_map = shaderNodeMappings[0]
    SHADER_NODE_INPUTS_map = shaderNodeMappings[1]

    shaderType = 'BSDF_PRINCIPLED'
    for m in bpy.data.materials:
        if not m.node_tree:
            continue

        # Find the default material node type
        materialNode = None
        for node in m.node_tree.nodes:
            if node.type == shaderType:
                materialNode = node
                break

        if materialNode: 
            shaderNodeDefinition = SHADER_NODE_map[shaderType]
            if not shaderNodeDefinition:
                print('Skip handling of node', materialNode)
                continue

            mtlxShaderNode = blender_createMtlxShaderNode(doc, m.name, shaderNodeDefinition, shaderType == 'BSDF_PRINCIPLED')
            if not mtlxShaderNode:
                continue
            mtlxShaderNodeDef = mtlxShaderNode.getNodeDef()

            # Set to not use 'Specular Workflow`
            # `
            newInput = mtlxShaderNode.addInput('useSpecularWorkflow', 'integer')
            if newInput:
                newInput.setValueString('0')                    

            # Nothing to do with outputs for now
            #for noutput in materialNode.outputs:
            #    print("  - Visit output: ", noutput.name)
            #print('Add inputs to node: ', mtlxShaderNode.getNamePath())
            PBSDF_USDPS_map = SHADER_NODE_INPUTS_map[shaderType]
            for ninput in materialNode.inputs:
                if not ninput.name in PBSDF_USDPS_map:
                    #print('-- Skip translating input: ', ninput.name)
                    continue                   

                # This is not a robust way to perform conversion
                # For now this is only sample WIP code.
                val = ninput.default_value
                portName  = PBSDF_USDPS_map[ninput.name]
                newInput = None
                if portName:
                    if portName == 'specularColor':
                        valueString = floatToStr(val) + "," + floatToStr(val) + "," + floatToStr(val)
                        newInput = mtlxShaderNode.addInput('specularColor', 'color3')
                        if newInput:
                            newInput.setValueString(valueString)
                    else:
                        newInput = blender_createMtlxInput(portName, val, mtlxShaderNode, mtlxShaderNodeDef)  
                        if portName == 'normal':
                            newInput.setValueString('0,0,1') 


                if newInput and ninput.links:
                    link = ninput.links[0]
                    if link.is_valid:                    
                        connectedNode = link.from_node
                        if connectedNode:
                            mtxNormalMap = None
                            if connectedNode.type == 'NORMAL_MAP':                                
                                nodeDefinition = SHADER_NODE_map['NORMAL_MAP']
                                mtxNormalMap = blender_createMtlxShaderNode(doc, 
                                                                            connectedNode.label, nodeDefinition, False) 
                                connectNodeToNode(newInput.getParent(), newInput.getName(), mtxNormalMap, '')                               
                                colorInput = connectedNode.inputs['Color']
                                if colorInput:
                                    link = colorInput.links[0] if colorInput.links else None
                                    if link:
                                        connectedNode = link.from_node

                            mtxImageNode = None
                            if connectedNode.type == 'TEX_IMAGE':                                
                                nodeDefinition = SHADER_NODE_map['TEX_IMAGE']
                                nodeDefinition = nodeDefinition + newInput.getType() 
                                mtxImageNode = blender_createMtlxShaderNode(doc, 
                                                                            connectedNode.label, nodeDefinition, False)
                                # Connect input to new node
                                if mtxImageNode:
                                    imagePath = ''
                                    if connectedNode.image:
                                        imagePath = connectedNode.image.filepath_from_user() 
                                    fileInput = mtxImageNode.addInput('file', 'filename')
                                    fileInput.setValueString(imagePath)
                                    connectNodeToNode(newInput.getParent(), newInput.getName(), mtxImageNode, '')

                            if mtxNormalMap and mtxImageNode:
                                connectNodeToNode(mtxNormalMap, 'normal', mtxImageNode, '')


def removeReferencedElements(doc):
    """
    Remove any elements which are referenced in. That is has a source URI.
    """
    for elem in doc.getChildren():
        if elem.hasSourceUri():
            doc.removeChild(elem.getName())

def main():
    parser = argparse.ArgumentParser(description='Extract MaterialX materials from a Blender file. Optionally export meshes as GLTF files')
    parser.add_argument('--inputFileName', dest='inputFileName', default="", help='Blender file name.')
    parser.add_argument('--outputFileName', dest='outputFileName', default="", help='MaterialX file name.')
    opts = parser.parse_args()

    blenderFile = opts.inputFileName
    if blenderFile:
        if not os.path.exists(blenderFile):
            print('Blender file does not exist: ')
            exit(-1)    
    
    pythonRoot = mx.FilePath(sys.exec_prefix)
    materialXRoot = pythonRoot / mx.FilePath('lib/site-packages/MaterialX') 
    if not os.path.exists(materialXRoot.asString()):
        print('Cannot find MaterialX package at:', materialXRoot.asString())
    print('Use MaterialX package at location:', materialXRoot.asString())    
    
    if blenderFile:
        bpy.ops.wm.open_mainfile(filepath=blenderFile)
    doc = initializeMaterialX(materialXRoot)
    shaderNodeMap = blender_init_node_dictionary('ND_UsdPreviewSurface_surfaceshader')
    blender_materialx(doc, shaderNodeMap)
    
    if not blenderFile:          
        blenderFile = bpy.data.filepath
    materialXFile = opts.outputFileName
    if not materialXFile:
        materialXFile = mx.FilePath(blenderFile)
        materialXFile.removeExtension()
        materialXFile.addExtension("mtlx")
    else:
        materialXFile = mx.FilePath(materialXFile)
 
    # Delete library elements
    removeReferencedElements(doc)
    writeMaterialX(doc, materialXFile, '')
    print('Converted:', blenderFile, 'to MaterialX file:', materialXFile.asString()) 
    
if __name__ == "__main__":
    main()    


