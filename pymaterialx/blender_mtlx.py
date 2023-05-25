import sys, os, argparse

# Import blender package
import bpy
import MaterialX as mx

# MX Utilities
import mtlxutils.mxbase as mxb
import mtlxutils.mxfile as mxf
import mtlxutils.mxnodegraph as mxg
import mtlxutils.mxtraversal as mxt

# To silent Blender output
import io
from contextlib import redirect_stdout, redirect_stderr

class BlenderToMtlx:

    def __init__(self):
        self.writeSingleMaterialFile = True
        self.writeSingleGeomFile = False
        self.exportMeshMaterials = True
        self.outputPath = mx.FilePath()
        self.outputFileName = mx.FilePath()

    def setWriteSingleMaterialFile(self, val):
        "Set whether to write single MaterialX file. Default is True"
        self.writeSingleMaterialFile = val

    def setWriteSingleGeomFile(self, val):
        "Set whether to write single geometry file. Default is False"
        self.writeSingleGeomFile = val

    def setExportMeshMaterials(self, val):
        self.exportMeshMaterials = val

    def setOutputPath(self, val):
        self.outputPath = val

    def setOutputFileName(self, val):
        self.outputFileName = val

    def floatToStr(self, val):
        """ 
        Emit formatted float value to string
        """
        return f"{val:.4g}"

    def createMtlxInput(self, portName, blenderVal, node, nodedef):
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
        valueLen['float'] = 1

        portType = nodedefInput.getType()

        # Check Python type to get string values
        # * Use nodedef port type to clamp vector inputs. For example
        # * Blender colors can be 4 float (rgba) in length, but the MaterialX port is only 3 float (rgb).
        # * Blender float can map to a MaterialX vector. The float is replicated as needed
        valueString = ''
        valueLength = valueLen[portType]
        if isinstance(blenderVal, float):
            if valueLength == 1:
                valueString = self.floatToStr(blenderVal)  
            else:
                blenderValString = []
                for i in range(0,valueLength):
                    blenderValString.append(self.floatToStr(blenderVal))
                valueString = ','.join(blenderValString)
        elif isinstance(blenderVal, int):
            valueString = str(blenderVal)
        elif isinstance(blenderVal, str):
            valueString = str(blenderVal)
        else:
            if len(blenderVal) in (2,3,4):
                blenderValString = []
                for i, c in enumerate(blenderVal):
                    if i < valueLength:                                 
                        blenderValString.append(self.floatToStr(blenderVal[i]))
                valueString = ','.join(blenderValString)

        if len(valueString):        
            newInput = node.addInput(portName, portType)
            if newInput:
                newInput.setValueString(valueString) 
        
        return newInput

    def init_node_dictionary(self, targetBSDF):

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

    def createMtlxShaderNode(self, doc, name, shaderNodeDefinition, isMaterial):

        mtlxShadername = name + ('_' + 'Shader' if isMaterial else '')
        mtlxShaderNode = mxg.MtlxNodeGraph.addNode(doc, shaderNodeDefinition, mtlxShadername)
        if not mtlxShaderNode:
            return None

        # Create MaterialX material and shader for each Blender material
        if isMaterial:
            mtlxMaterialNode = mxg.MtlxNodeGraph.addNode(doc, 'ND_surfacematerial', name)
            if mtlxMaterialNode:
                # Connect the material node to the output of the graph
                mxg.MtlxNodeGraph.connectNodeToNode(mtlxMaterialNode, 'surfaceshader', mtlxShaderNode, '')          

        return mtlxShaderNode

    def connectImageNode(self, doc, SHADER_NODE_map, mtlxInput, blenderNode):
        nodeDefinition = SHADER_NODE_map['TEX_IMAGE']
        nodeDefinition = nodeDefinition + mtlxInput.getType() 
        mtxImageNode = self.createMtlxShaderNode(doc, blenderNode.label, nodeDefinition, False)

        # Connect input to new node
        if mtxImageNode:
            imagePath = ''
            if blenderNode.image:
                imagePath = blenderNode.image.filepath_from_user() 
            fileInput = mtxImageNode.addInput('file', 'filename')
            fileInput.setValueString(imagePath)
            mxg.MtlxNodeGraph.connectNodeToNode(mtlxInput.getParent(), mtlxInput.getName(), mtxImageNode, '')
        
        return mtxImageNode

    def connectNormalMapNode(self, doc, SHADER_NODE_map, mtlxInput, blenderNode):
        """ 
        Create a MaterialX normal map node from a Blender node
        Connected the new node to an downstream input 
        """
        nodeDefinition = SHADER_NODE_map['NORMAL_MAP']
        mtxNormalMap = self.createMtlxShaderNode(doc, blenderNode.label, nodeDefinition, False) 
        mxg.MtlxNodeGraph.connectNodeToNode(mtlxInput.getParent(), mtlxInput.getName(), mtxNormalMap, '')                               
        return mtxNormalMap

    def getUpstreamNode(self, blenderInput):
        if not blenderInput:
            return None
        link = blenderInput.links[0] if blenderInput.links else None
        if link and link.is_valid:
            return link.from_node
        return None

    def loadLibraries(self, librarySearchPath): 
        stdlib = mx.createDocument()
        if mxb.haveVersion(1, 38, 7):
            searchPath = mx.getDefaultDataSearchPath()
            libFiles = mx.loadLibraries(mx.getDefaultDataLibraryFolders(), searchPath, stdlib)
        else:
            libraryPath = mx.FilePath('libraries')
            searchPath = mx.FileSearchPath()
            searchPath.append(librarySearchPath)
            libFiles = mx.loadLibraries([ libraryPath ], searchPath, stdlib)
        print('Loaded %d library files' % len(libFiles))
        return stdlib

    def createWorkingDocument(self, stdlib):
        doc = mx.createDocument()
        doc.importLibrary(stdlib)
        return doc

    def exportMaterials(self, shaderNodeMappings, materialFilter, librarySearchPath):
        """
        Simple Export of a few Blender nodes to MaterialX material nodes + shaders
        """
        docs = dict()

        stdlib = self.loadLibraries(librarySearchPath)
        if len(stdlib.getNodeDefs()) == 0:
            print('Failed to load MaterialX libraries')
            return docs            

        doc = None
        if self.writeSingleMaterialFile:
            doc = self.createWorkingDocument(stdlib)
            docs[self.outputFileName.asString()] = doc

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
                #print('Compare: ', m.name, 'with',  materialFilter)
                if materialFilter and m.name not in materialFilter:
                    print('Skip material: ', m.name)
                    continue

                # Creat a corresponding MaterialX material / shader node
                shaderNodeDefinition = SHADER_NODE_map[shaderType]
                if not shaderNodeDefinition:
                    print('Skip handling of node', materialNode.name)
                    continue

                if not self.writeSingleMaterialFile:
                    doc = self.createWorkingDocument(stdlib)

                mtlxShaderNode = self.createMtlxShaderNode(doc, m.name, shaderNodeDefinition, shaderType == 'BSDF_PRINCIPLED')
                if not mtlxShaderNode:
                    continue

                if not self.writeSingleMaterialFile:
                    docs[mtlxShaderNode.getName()] = doc

                mtlxShaderNodeDef = mtlxShaderNode.getNodeDef()

                # Nothing to do with outputs for now
                #for noutput in materialNode.outputs:
                #    print("  - Visit output: ", noutput.name)

                #print('Add inputs to node: ', mtlxShaderNode.getNamePath())
                PBSDF_USDPS_map = SHADER_NODE_INPUTS_map[shaderType]
                for ninput in materialNode.inputs:
                    if not ninput.name in PBSDF_USDPS_map:
                        #print('-- Skip translating input: ', ninput.name)
                        continue                   

                    # Add in inputs
                    val = ninput.default_value
                    portName  = PBSDF_USDPS_map[ninput.name]
                    newInput = None
                    if portName:
                        newInput = self.createMtlxInput(portName, val, mtlxShaderNode, mtlxShaderNodeDef)                         
                        if portName == 'normal':
                            newInput.setValueString('0,0,1') 

                    # Check for upstream connections
                    if not newInput:
                        continue

                    connectedNode = self.getUpstreamNode(ninput)
                    if connectedNode:
                        mtxNormalMap = None
                        # Add a MaterialX normal map node for each Blender normal map node
                        if connectedNode.type == 'NORMAL_MAP':                                
                            colorInput = connectedNode.inputs['Color']
                            connectedNodeUp = None
                            if colorInput:
                                connectedNodeUp = self.getUpstreamNode(colorInput)
                            if connectedNodeUp:
                                mtxNormalMap = self.connectNormalMapNode(doc, SHADER_NODE_map, newInput, connectedNode)
                                # Traverse upstream
                                connectedNode = connectedNodeUp 

                        # Add an MaterialX image node for each Blender texture image node
                        mtxImageNode = None
                        if connectedNode and connectedNode.type == 'TEX_IMAGE':                                
                            mtxImageNode = self.connectImageNode(doc, SHADER_NODE_map, newInput, connectedNode)

                        # Connect normal map and image node if both found
                        if mtxNormalMap and mtxImageNode:
                            mxg.MtlxNodeGraph.connectNodeToNode(mtxNormalMap, 'normal', mtxImageNode, '')  
        return docs

    def writeMaterialXFile(self, doc, filePath):
        """
        Simple utility to write a document to a Markdown section
        and or a to disk.
        """
        if not filePath:
            return

        writeOptions = mx.XmlWriteOptions()
        major, minor, patch = mx.getVersionIntegers()
        # Write predicate does not work prior to 1.38.7
        if major >= 1 and minor >= 38 and patch >= 7:
            writeOptions.writeXIncludeEnable = False
            writeOptions.elementPredicate = mxf.MtlxFile.skipLibraryElement
        else:
            for elem in doc.getChildren():
                    if elem.hasSourceUri():
                        doc.removeChild(elem.getName())

        mx.writeToXmlFile(doc, filePath, writeOptions)

    def writeMaterialXFiles(self, docs):
        filesWritten = []

        for filename in docs:
            doc = docs[filename]
            mtlxFilePath = self.outputPath / filename
            mtlxFilePath.removeExtension()
            mtlxFilePath.addExtension('mtlx')
            self.writeMaterialXFile(doc, mtlxFilePath)
            filesWritten.append(mtlxFilePath.asString())
        
        return filesWritten

    def getMeshesAndMaterials(self, renderableOnly=True, activeOnly=False):
        meshes = []
        materials = []
        scene = bpy.context.scene
        for obj in scene.objects:
            if obj.type == 'MESH' and obj.visible_get():
                if renderableOnly and obj.hide_render == True:
                    continue
                if activeOnly and not obj.select_get():
                    continue
                mat = obj.active_material
                #print('- Translate mesh: ', obj.name, '. mat: ', mat.name)
                materials.append(mat.name)
                meshes.append(obj)    
            obj.select_set(False)
        return meshes, materials    

    def writeGLTFMesh(self, mesh, outputPath, export_settings):
        """
        Write a Blender mesh out to GLTF format
        """
        exportMaterials = export_settings['write_mesh_material']
        exportNormals = export_settings['export_normals']
        exportColors = export_settings['export_vertex_color']
        exportUv = export_settings['export_uv']
        exportTangent = export_settings['export_tangents']
        exportAnim = export_settings['export_animation']
        outputFormat = export_settings['geometry_format']         

        # Output selected
        outMeshName = outputPath / mx.createValidName(mesh.name) 
        outMeshName.addExtension('gltf')
        if outputFormat == 'GLB':
            outMeshName.addExtension('glb')
        bpy.ops.export_scene.gltf(filepath=outMeshName.asString(),
                                use_visible=True,
                                use_selection=True,
                                export_format=outputFormat,
                                #use_triangles=True,
                                export_cameras=False, 
                                export_lights=False,
                                export_materials=exportMaterials,
                                export_normals=exportNormals,
                                export_texcoords=exportUv,
                                export_colors=exportColors,
                                export_tangents=exportTangent,
                                export_animations=exportAnim,
                                )

        return outMeshName.asString()        

    def writeGLTFMeshes(self, meshes, outputPath, export_settings):
        exportMaterials = export_settings['write_mesh_material']
        exportNormals = export_settings['export_normals']
        exportColors = export_settings['export_vertex_color']
        exportUv = export_settings['export_uv']
        exportTangent = export_settings['export_tangents']
        exportAnim = export_settings['export_animation']
        outputFormat = export_settings['geometry_format'] 

        filesWritten = []

        if self.writeSingleGeomFile:
            for mesh in meshes:
                mesh.select_set(True)

            outMeshName = outputPath / self.outputFileName
            outMeshName.removeExtension()
            outMeshName.addExtension('glb')
            filesWritten.append(outMeshName.asString())
            bpy.ops.export_scene.gltf(filepath=outMeshName.asString(),
                                use_visible=True,
                                use_selection=True,
                                export_format=outputFormat,
                                #use_triangles=True,
                                export_cameras=False, 
                                export_lights=False,
                                export_materials=exportMaterials,
                                export_normals=exportNormals,
                                export_texcoords=exportUv,
                                export_colors=exportColors,
                                export_tangents=exportTangent,
                                export_animations=exportAnim,
                                )
        else:
            for mesh in meshes:
                mesh.select_set(True)
                filesWritten.append( self.writeGLTFMesh(mesh, outputPath, export_settings))
                mesh.select_set(False)    

        return filesWritten

    def execute(self, export_settings):    
        """
        Perform export.
        """
        selected_objects = export_settings['selected_objects']
        separateMtlxFile = export_settings['seperate_materials']

        outputFileName = mx.FilePath(export_settings['file_path'])
        outputFilePath = outputFileName.getParentPath()
        outputFileName = mx.FilePath(outputFileName.getBaseName())

        self.setOutputPath(outputFilePath)
        self.setOutputFileName(outputFileName)

        shaderNodeMap = self.init_node_dictionary('ND_UsdPreviewSurface_surfaceshader')
        self.setWriteSingleMaterialFile(not separateMtlxFile)
        major, minor, patch = mx.getVersionIntegers()
        # Write predicate does not work prior to 1.38.7
        if major >= 1 and minor >= 38 and patch >= 7:
            librarySearchPath = mx.FileSearchPath()
        else:
            librarySearchPath = export_settings['library_search_path']

        meshes, materials = self.getMeshesAndMaterials(True, selected_objects)
        if materials:
            docs  = self.exportMaterials(shaderNodeMap, materials, librarySearchPath)
            if docs:
                filesWritten = self.writeMaterialXFiles(docs)
                for f in filesWritten:
                    print('Write MaterialX material file:', f)
            else:
                print('Failed to export materials')

            writeMtlxGraph =  export_settings['diagram']
            if writeMtlxGraph:
                for fileName in docs:
                    # Load in document and create a Mermaid graph
                    doc = docs[fileName]
                    roots = doc.getMaterialNodes()
                    graph = mxt.MtlxMermaid.generateMermaidGraph(roots, 'LR')
                    graphFileName = outputFilePath / mx.FilePath(fileName)
                    graphFileName.addExtension('md')
                    print('Write Mermaid graph file:', graphFileName.asString())
                    graphFile = open(graphFileName.asString(), 'w')
                    if graphFile:                
                        graphFile.write('```mermaid\n')
                        for line in graph:
                            if line:
                                graphFile.write(line + '\n')
                        #graphFile.writelines(graph)
                        graphFile.write('```\n')
                        graphFile.close() 

        # Export meshes as separate pieces
        if meshes:
            separateGeomFile = export_settings['seperate_files']
            if export_settings['write_geometry']:
                filesWritten = []
                output = io.StringIO()
                with redirect_stdout(output), redirect_stderr(output):        
                    self.setWriteSingleGeomFile(not separateGeomFile)
                    filesWritten = self.writeGLTFMeshes(meshes, outputFilePath, export_settings)
                for fileWritten in filesWritten:
                    print('Write GLTF to file:', fileWritten)


def main():

    parser = argparse.ArgumentParser(description='Extract MaterialX materials from a Blender file. Optionally export meshes as GLTF files')
    parser.add_argument(dest='inputFileName', help='Root name of image files to examine.')
    parser.add_argument('--writeGeom', dest='writeGeom', default=False, type=bool, help='Set to True to export meshes in GLTF format. Default is False.')
    parser.add_argument('--writeGeomMaterials', dest='writeGeomMaterials', default=False, type=bool, help='Set to True to write materials as part of mesh export. Default is False.')
    parser.add_argument('--separateGeomFile', dest='separateGeomFile', default=False, type=bool, help='Set to True to write meshes to separate GLTF files. Default is False.')
    parser.add_argument('--separateMtlxFile', dest='separateMtlxFile', default=False, type=bool, help='Set to True to write each material to a separate MaterialX file. Default is False.')
    parser.add_argument('--writeMtlxGraph', dest='writeMtlxGraph', default=False, type=bool, help='Set to True to export Mermaid graph for materials. Default is False.')
    parser.add_argument('--outputPath', dest='outputPath', default="./", help='File path to output shaders to. If not specified, is the location of the input document is used.')
    opts = parser.parse_args()

    haveVersion1387 = mxb.haveVersion(1,38,7)
    if not haveVersion1387:
        print("** Warning: Recommended version is 1.38.7 for tutorials. Have version: ", mx.__version__)

    inputFileName = opts.inputFileName  
    if not os.path.exists(inputFileName):
        print('Input file does not exist. Exiting')
        exit(-1)
    bpy.ops.wm.open_mainfile(filepath=inputFileName)

    outputFileName = mx.FilePath(inputFileName)
    outputFileName.removeExtension()
    outputFileName.addExtension('mtlx')
    outputFileName = outputFileName.getBaseName()
    outputFilePath = mx.FilePath(opts.outputPath)
    pathExists = os.path.exists(outputFilePath.asString())
    if not pathExists:
        print('Created folder: ', outputFilePath.asString())
        os.makedirs(outputFilePath.asString())
    outputFilePath = outputFilePath / outputFileName

    export_settings = dict()
    export_settings['file_path'] = outputFilePath.asString() 
    export_settings['selected_objects'] = False

    export_settings['write_geometry'] = opts.writeGeom
    export_settings['geometry_format'] = 'GLB'
    export_settings['seperate_files'] = opts.separateGeomFile
    print('opts.writeGeomMaterials', opts.writeGeomMaterials)
    export_settings['write_mesh_material'] = 'EXPORT' if opts.writeGeomMaterials else 'NONE' 
    export_settings['export_vertex_color'] = False
    export_settings['export_tangents'] = True
    export_settings['export_normals'] = True
    export_settings['export_uv'] = True
    export_settings['export_animation'] = False
    
    export_settings['seperate_materials'] = opts.separateMtlxFile
    export_settings['diagram'] = opts.writeMtlxGraph

    converter = BlenderToMtlx()
    return converter.execute(export_settings)

if __name__ == '__main__':
    main()

