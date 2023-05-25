
# Blender and MaterialX
import bpy, bmesh
import MaterialX as mx

import sys, os, argparse, io, math
from contextlib import redirect_stdout, redirect_stderr

# MaterialX Utilities
#import mtlxutils.mxbase as mxb
import mtlxutils.mxfile as mxf
import mtlxutils.mxnodegraph as mxg
#import mtlxutils.mxtraversal as mxt
#from mtlxutils.mxfile import MtlxFile as mxf

class imageToMeshBuilder():
    """
    Utility class to convert image to a mesh.
    Uses Blender to create a mesh with the dimensions of an image
    Use MaterialX to create material with image as base color input. Option to choose the type
    of shader definition (lit or not). Default is to use a lit material (standard surface).
    """
   
    shaderNodeDefinition = 'ND_standard_surface_surfaceshader'
    imageFilePath = ''
    imageFilePathId = ''

    def setImageFilePath(self, val):
        self.imageFilePath = val
        path = mx.FilePath(val)
        path.removeExtension()
        path = path.getBaseName()
        self.imageFilePathId = mx.createValidName(path)

    def setUseUnlitMaterial(self, val):
        if val:
            self.shaderNodeDefinition = 'ND_surface_unlit'
        else:
            self.shaderNodeDefinition = 'ND_standard_surface_surfaceshader'

    def loadImage(self):

        yimage = ximage = -1        
        image_src = bpy.data.images.load(self.imageFilePath)
        if image_src:
            yimage = image_src.size[1]
            ximage = image_src.size[0]
        return image_src, yimage, ximage

    def createMaterial(self, obj, image_src, materialName):
        mat = obj.active_material
        if not mat:
            mat = bpy.data.materials.new(name=obj.name + '_Material')
            obj.active_material = mat
        
        mat.use_nodes = True
        
        #mat = ob.active_material
        # Get the nodes
        nodes = mat.node_tree.nodes
        nodes.clear()

        bsdfNode = nodes.new(type='ShaderNodeBsdfPrincipled')
        #bsdfNode.location = 0,0

        imageNode = nodes.new('ShaderNodeTexImage')
        imageNode.image = image_src 
        #node_tex.location = -400,0

        materialNode = nodes.new(type='ShaderNodeOutputMaterial')   
        #node_output.location = 400,0

        # Link all nodes
        links = mat.node_tree.links
        link = links.new(imageNode.outputs["Color"], bsdfNode.inputs["Base Color"])
        link = links.new(bsdfNode.outputs["BSDF"], materialNode.inputs["Surface"])    

    def floatToStr(self, val):
        """ 
        Emit formatted float value to string
        """
        return f"{val:.4g}"

    def inputColorName(self):
        if self.shaderNodeDefinition == 'ND_standard_surface_surfaceshader':
            return 'base_color'
        else:
            return 'emission_color'

    def createMtlxMaterial(self, doc, meshName, materialName):
        """
        Create a MaterialX material and shaders.
        """
        look = doc.getLook(materialName + '_look')
        if not look:
            look = doc.addLook(materialName + '_look')

        #meshName = mx.createValidName('Mesh_' + obj.name)

        mtlxShadername = materialName + ('_' + 'Shader')
        mtlxShaderNode = mxg.MtlxNodeGraph.addNode(doc, self.shaderNodeDefinition, mtlxShadername)
        if not mtlxShaderNode:
            return None

        mtlxMaterialNode = mxg.MtlxNodeGraph.addNode(doc, 'ND_surfacematerial', materialName + '_Material')
        if mtlxMaterialNode:
            # Connect the material node to the output of the graph
            mxg.MtlxNodeGraph.connectNodeToNode(mtlxMaterialNode, 'surfaceshader', mtlxShaderNode, '')          

        inputName = self.inputColorName()
        mtlxShaderNode.addInputFromNodeDef(inputName)

        # TODO: Add image node, connect to shader and set image name
        mtlxImageNode = mxg.MtlxNodeGraph.addNode(doc, 'ND_tiledimage_color3', materialName + '_Image')
        input = mtlxImageNode.addInputFromNodeDef('file')
        input.setValueString(self.imageFilePath)
        mxg.MtlxNodeGraph.connectNodeToNode(mtlxShaderNode, inputName, mtlxImageNode, '')

        newMaterialName = mtlxMaterialNode.getNamePath()
        #self.materialDict[materialName] = newMaterialName

        #print('-- Create MTLX material node:', newMaterialName)
        #print('---- Assign new material:', newMaterialName, ' to object: ', meshName)
        assign = look.addMaterialAssign(newMaterialName, newMaterialName)
        assign.setGeom(meshName)
        return mtlxMaterialNode

    def setMeshUvs(self, obj, sideTexel = [0.05, 0.05]):
        #obj = bpy.context.active_object
        bm = bmesh.from_edit_mesh(obj.data)

        uv_layer = bm.loops.layers.uv.verify()
        loop_uvs = [ [0,0], [1,0], [1,1], [0,1] ] 
        loop_uvs2 = [ sideTexel, sideTexel, sideTexel, sideTexel ] 
        facei = 0
        for f in bm.faces:
            index = 0;      
            for l in f.loops:
                if facei == 5 or facei == 4:
                    l[uv_layer].uv = (loop_uvs[index][0], loop_uvs[index][1])
                else:
                    l[uv_layer].uv = (loop_uvs2[index][0], loop_uvs2[index][1])
                index = index + 1
            facei = facei + 1

        bmesh.update_edit_mesh(obj.data)

    def deleteAllObjects(self):
        deleteListObjects = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'HAIR', 'POINTCLOUD', 'VOLUME', 'GPENCIL',
                         'ARMATURE', 'LATTICE', 'EMPTY', 'LIGHT', 'LIGHT_PROBE', 'CAMERA', 'SPEAKER']

        for o in bpy.context.scene.objects:
            for i in deleteListObjects:
                if o.type == i:
                    o.select_set(False)
                else:
                    o.select_set(True)
        bpy.ops.object.delete() 

    #bpy.ops.object.mode_set( mode = 'OBJECT' )

    def execute(self, width=1.0, height = 0.1, sideTexel = [0.05, 0.05]):
        # Clear the scene
        self.deleteAllObjects()

        # Load input image
        image_src, yimage, ximage = self.loadImage()
        if not image_src:
            return
        
        # Create a cube and size it to match the image x,y dimenesions but normalized so that x is length 1
        cubex = width
        cubey = width * (yimage / ximage)
        bpy.ops.mesh.primitive_cube_add(size=1.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(math.pi, 0.0, 0.0), scale=(cubex, cubey, height))
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        selected = [obj for obj in bpy.context.selected_objects]
        geom = selected[0]
        geom.name = self.imageFilePathId
        self.createMaterial(geom, image_src, 'material')

        #bpy.ops.screen.info_log_show()

        # Update texture coordinates
        bpy.ops.object.mode_set( mode = 'EDIT' )
        bpy.ops.mesh.select_mode( type = 'FACE' )
        bpy.ops.mesh.select_all( action = 'SELECT' ) 
        self.setMeshUvs(selected[0], sideTexel)
        bpy.ops.object.mode_set( mode = 'OBJECT' )

    def writeMaterialXFile(self, doc, filePath):
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


def getFiles(rootPath):
    filelist = []
    exts = ('.png', '.jpg' )
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            if file.lower().endswith(exts):
                filelist.append(os.path.join(subdir, file)) 
    return filelist

def main():
    parser = argparse.ArgumentParser(description='Reads Image file into Blender to produce a 3d mesh and material. Save meshes to GLTF, material as MaterialX, and Blender file')
    parser.add_argument(dest='inputFileName', help='Path containing Image file to convert.')
    parser.add_argument('--unlit', dest='unlit', default=False, type=bool, help="Create unlit materials.")
    parser.add_argument('--width', dest='width', default=1.0, type=float, help="Width of mesh to create. Default is 1.0")
    parser.add_argument('--height', dest='height', default=0.1, type=float, help="Height of mesh to create. Default is 0.1")
    parser.add_argument('--outputPath', dest='outputPath', default='', help='File path to output shaders to. If not specified, is the location of the input document is used.')
    parser.add_argument('--writeBlender', dest='writeBlender', default=False, type=bool, help='Write out scene as Blender file. Default is False.')

    opts = parser.parse_args()
    width = opts.width
    height = opts.height
    sideTexel = [0.05, 0.05]

    fileList = []
    if os.path.isdir(opts.inputFileName): 
        fileList = getFiles(opts.inputFileName)
    else:
        fileList.append(opts.inputFileName)

    outputFilePath = mx.FilePath(opts.outputPath)
    if outputFilePath:
        pathExists = os.path.exists(outputFilePath.asString())
        if not pathExists:
            print('Created folder: ', outputFilePath.asString())
            os.makedirs(outputFilePath.asString())

    for fileName in fileList:

        imageFilePath = mx.FilePath(fileName)

        builder = imageToMeshBuilder()
        if opts.unlit:
            builder.setUseUnlitMaterial(True)
        builder.setImageFilePath(imageFilePath.asString())
        builder.execute(width, height, sideTexel)

        doc, libFiles = mxf.MtlxFile.createWorkingDocument()
        builder.createMtlxMaterial(doc, builder.imageFilePathId, builder.imageFilePathId)

        # MaterialX output
        mtlxFilePath = imageFilePath
        if outputFilePath:
            baseName = imageFilePath.getBaseName()
            mtlxFilePath = outputFilePath / mx.FilePath(baseName)
        mtlxFilePath.removeExtension()
        mtlxFilePath = mx.FilePath(mtlxFilePath.asString() + "_to_mesh") 
        mtlxFilePath.addExtension('mtlx')
        print('Write MaterialX file:', mtlxFilePath.asString())  
        builder.writeMaterialXFile(doc, mtlxFilePath)

        # GLTF output
        gltfFilePath = imageFilePath
        if outputFilePath:
            baseName = imageFilePath.getBaseName()
            gltfFilePath = outputFilePath / mx.FilePath(baseName)
        gltfFilePath.removeExtension()
        gltfFilePath = mx.FilePath(gltfFilePath.asString() + "_to_mesh") 
        gltfFilePath.addExtension('glb')
        outputFormat = 'GLB'
        exportMeshMaterials = True
        exportMaterials = 'PLACEHOLDER'
        if exportMeshMaterials:
            exportMaterials = 'EXPORT'

        # Make sure to only export selected
        print('Write GLTF file:', gltfFilePath.asString())  
        output = io.StringIO()
        with redirect_stdout(output), redirect_stderr(output):        
            bpy.ops.export_scene.gltf(filepath=gltfFilePath.asString(),
                                    use_visible=True,
                                    use_selection=True,
                                    export_format=outputFormat,
                                    # use_triangles=True,
                                    export_cameras=False,
                                    export_lights=False,
                                    export_materials=exportMaterials
                                    )

        # Blender file output
        if opts.writeBlender:
            blenderFilePath = imageFilePath
            if outputFilePath:
                baseName = imageFilePath.getBaseName()
                blenderFilePath = outputFilePath / mx.FilePath(baseName)
            blenderFilePath.removeExtension()
            blenderFilePath = mx.FilePath(blenderFilePath.asString() + "_to_mesh") 
            blenderFilePath.addExtension('blend')
            print('Write Blender file:', blenderFilePath.asString())
            with redirect_stdout(output), redirect_stderr(output):        
                bpy.ops.wm.save_mainfile(filepath=os.path.abspath(blenderFilePath.asString()), check_existing=True)

if __name__ == "__main__":
    main()