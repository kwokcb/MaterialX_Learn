import sys, os, argparse
import bpy
import MaterialX as mx

import io
from contextlib import redirect_stdout, redirect_stderr

# MX Utilities
#import mtlxutils.mxbase as mxb
import mtlxutils.mxfile as mxf
import mtlxutils.mxnodegraph as mxg
#import mtlxutils.mxtraversal as mxt
#from mtlxutils.mxfile import MtlxFile as mxf

class svgBuilder():
    """
    Utility class to convert SVG to a mesh.
    Uses Blender to convert from SVG to mesh and export to GLTF
    Use MaterialX to create material from SVG color. Option to choose the type
    of shader definition (lit or not). Default is to use a lit material (standard surface).
    """
    
    svgFilePath = mx.FilePath()
    materialDict = dict()
    shaderNodeDefinition = 'ND_standard_surface_surfaceshader'
    extrudeValue = 0.001
    bevelValue = 0.0
    
    def setExtrudeValue(self, val):
        self.extrudeValue = val

    def setBevelValue(self, val):
        self.bevelValue = val

    def setUseUnlitMaterial(self, val):
        if val:
            self.shaderNodeDefinition = 'ND_surface_unlit'
        else:
            self.shaderNodeDefinition = 'ND_standard_surface_surfaceshader'

    def inputColorName(self):
        if self.shaderNodeDefinition == 'ND_standard_surface_surfaceshader':
            return 'base_color'
        else:
            return 'emission_color'

    def setSVGFilePath(self, svgFile):    
        self.svgFilePath = svgFile
        
    def load(self):
        if not os.path.exists(self.svgFilePath.asString()):
            return False
        try:
            bpy.ops.import_curve.svg(filepath=self.svgFilePath.asString())
        except RuntimeError as ex:
            error_report = "\n".join(ex.args)
            print("Error on SVG load:", error_report)
            return False

        return True
        
    def extrudeCurves(self):
        extruded = False
        for curve in bpy.data.curves[:]:
            curve.extrude = self.extrudeValue                    
            curve.bevel_depth = self.bevelValue
            extruded = True
        return extruded
            
    def createMaterial(self, obj):
        material = obj.active_material
        if not material:
            material = bpy.data.materials.new(name=obj.name + '_Material')
            obj.active_material = material
            print('  -- Create material for curve with no material:', material.name)
        if material.name in self.materialDict:
            return
        
        baseColor = material.diffuse_color
        material.use_nodes = True
        bsdfNode = material.node_tree.nodes['Principled BSDF']
        if bsdfNode:
            # Assign the color to the BSDF node
            bsdfNode.inputs[0].default_value = baseColor

    def floatToStr(self, val):
        """ 
        Emit formatted float value to string
        """
        return f"{val:.4g}"

    def createMtlxMaterial(self, doc, obj):
        """
        Create a MaterialX material and shaders.
        Will create a 'standard_surface' BSDF node 

        TODO: Hash unique shader based on material values (base_color etc) instead of name of material
        """
        look = doc.getLook('Default_Look')
        if not look:
            look = doc.addLook('Default_Look')

        blmaterial = obj.active_material
        meshName = mx.createValidName('Mesh_' + obj.name)
        if blmaterial.name in self.materialDict:
            print('---- Assign existing material:', self.materialDict[blmaterial.name], ' to object: ', )
            assign = look.getMaterialAssign(self.materialDict[blmaterial.name])
            if assign:
                curGeom = assign.getGeom()
                assign.setGeom(curGeom + ', ' + meshName)
            return

        mtlxShadername = blmaterial.name + ('_' + 'Shader')
        mtlxShaderNode = mxg.MtlxNodeGraph.addNode(doc, self.shaderNodeDefinition, mtlxShadername)
        if not mtlxShaderNode:
            return None

        # Create MaterialX material and shader for each Blender material
        mtlxMaterialNode = mxg.MtlxNodeGraph.addNode(doc, 'ND_surfacematerial', blmaterial.name + '_Material')
        if mtlxMaterialNode:
            # Connect the material node to the output of the graph
            mxg.MtlxNodeGraph.connectNodeToNode(mtlxMaterialNode, 'surfaceshader', mtlxShaderNode, '')          

        inputName = self.inputColorName()
        mtlxShaderNode.addInputFromNodeDef(inputName)
        if blmaterial:
            baseColor = blmaterial.diffuse_color
            base_color = mtlxShaderNode.getInput(inputName)
            print('    - Set base color = ', self.floatToStr(baseColor[0]), self.floatToStr(baseColor[1]), self.floatToStr(baseColor[2]))
            base_color.setValue(mx.Color3(baseColor[0], baseColor[1], baseColor[2]))

        newMaterialName = mtlxMaterialNode.getNamePath()
        self.materialDict[blmaterial.name] = newMaterialName

        print('-- Create MTLX material node:', newMaterialName)
        print('---- Assign new material:', newMaterialName, ' to object: ', meshName)
        assign = look.addMaterialAssign(newMaterialName, newMaterialName)
        assign.setGeom(meshName)
        return mtlxMaterialNode

    def createMeshFromCurve(self, context, curve):
        deg = context.evaluated_depsgraph_get()
        mesh = None
        try:
            mesh = bpy.data.meshes.new_from_object(curve.evaluated_get(deg), depsgraph=deg)
        except RuntimeError as ex:
            error_report = "\n".join(ex.args)
            print("Error on SVG load:", error_report)
            return None, None
        
        mesh.name = mx.createValidName('Mesh_' + curve.name + '_geom')

        new_obj = bpy.data.objects.new(mx.createValidName('Mesh_' + curve.name), mesh)
        context.collection.objects.link(new_obj)

        new_obj.matrix_world = curve.matrix_world
        
        # Center the object
        new_obj.select_set(True)
        context.view_layer.objects.active = new_obj
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
        new_obj.location[0] = 0.0
        new_obj.location[1] = 0.0
        new_obj.location[2] = 0.0
        return new_obj, mesh

    def convertToMesh(self, doc):
        newobjs = []
        context = bpy.context
        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.data.objects:
            if obj.type == 'MESH':
                obj.select_set(True)
                bpy.ops.object.delete()

        for obj in bpy.data.objects:
            #print('Examine object:', obj.name)
            if obj.type == 'CURVE':
                obj.select_set(True)
                #print('- Examine curve:', obj.name)
                newobj, mesh = self.createMeshFromCurve(context, obj)
                if newobj and mesh:
                    mesh.name = mx.createValidName(mesh.name)
                    print('-- Created mesh:', newobj.name, ',', mesh.name, 'for curve:', obj.name)
                    self.createMaterial(obj)
                    self.createMtlxMaterial(doc, obj)
                    newobjs.append(newobj)

        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.data.objects:
            if obj.type == 'CURVE':
                obj.select_set(True)
                bpy.ops.object.delete()

        return newobjs
    
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

def main():
    parser = argparse.ArgumentParser(description='Reads SVG file into Blender to produce 3d meshes. Save meshes as GLTF and SVG color as MaterialX material.')
    parser.add_argument(dest='inputFileName', help='Path containing SVG file to convert.')
    parser.add_argument('--unlit', dest='unlit', default=False, type=bool, help="Create unlit materials.")
    parser.add_argument('--extrude', dest='extrude', default=0.001, type=float, help="Amount to extrude.")
    parser.add_argument('--bevel', dest='bevel', default=0.000, type=float, help="Amount to bevel.")

    # Add curve options
    # Add curve->mesh options
    # Add gltf output options
    # Add mtlx options
    opts = parser.parse_args()

    #dataPath = mx.FilePath("/Users/bernardkwok/work/modelAssets/healthcare/diabetes_project/images")
    #svgFile = mx.FilePath('power.svg')
    svgFilePath = mx.FilePath(opts.inputFileName)

    builder = svgBuilder()
    builder.setSVGFilePath(svgFilePath)
    if opts.unlit:
        builder.setUseUnlitMaterial(True)
    builder.setExtrudeValue(opts.extrude)
    builder.setBevelValue(opts.bevel)

    if not builder.load():
        print('Failed to load SVG file: ', svgFilePath.asString())
        exit(-1)

    if not builder.extrudeCurves():
        print('Failed to extrude curves for file:', svgFilePath.asString())
    else:
        print('-- Set extrude:', opts.extrude, ", bevel: ", opts.bevel)

    doc, libFiles = mxf.MtlxFile.createWorkingDocument()

    newobjs = builder.convertToMesh(doc)
    if len(newobjs) == 0:
        print('Failed to create mesh from curve')
        exit(-1)

    # MaterialX output
    mtlxFilePath = svgFilePath
    mtlxFilePath.removeExtension()
    mtlxFilePath = mx.FilePath(mtlxFilePath.asString() + "_to_mesh") 
    mtlxFilePath.addExtension('mtlx')
    print('Write MaterialX file to:', mtlxFilePath.asString())  
    builder.writeMaterialXFile(doc, mtlxFilePath)

    # GLTF output
    blenderFilePath = svgFilePath
    blenderFilePath.removeExtension()
    blenderFilePath = mx.FilePath(blenderFilePath.asString() + "_to_mesh") 
    blenderFilePath.addExtension('glb')
    outputFormat = 'GLB'
    exportMeshMaterials = True
    exportMaterials = 'PLACEHOLDER'
    if exportMeshMaterials:
        exportMaterials = 'EXPORT'
    print('Write GLTF file to:', blenderFilePath.asString())  

    # Make sure to only export selected
    bpy.ops.object.select_all(action='DESELECT')
    for newobj in newobjs:
        newobj.select_set(True)
    output = io.StringIO()
    with redirect_stdout(output), redirect_stderr(output):        
        bpy.ops.export_scene.gltf(filepath=blenderFilePath.asString(),
                                use_visible=True,
                                use_selection=True,
                                export_format=outputFormat,
                                # use_triangles=True,
                                export_cameras=False,
                                export_lights=False,
                                export_materials=exportMaterials
                                )

    # Blender file output
    blenderFilePath = svgFilePath
    blenderFilePath.removeExtension()
    blenderFilePath = mx.FilePath(blenderFilePath.asString() + "_to_mesh") 
    blenderFilePath.addExtension('blend')
    print('Output new blender file: ', blenderFilePath.asString())
    with redirect_stdout(output), redirect_stderr(output):        
        bpy.ops.wm.save_mainfile(filepath=blenderFilePath.asString(), check_existing=True)

if __name__ == "__main__":
    main()