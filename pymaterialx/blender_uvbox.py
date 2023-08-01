import bpy, bmesh

class imageToMeshBuilder():

    def loadImage(self, filePath):

        yimage = ximage = -1
        
        image_src = bpy.data.images.load(filePath)
        if image_src:
            print(image_src)
            yimage = image_src.size[1]
            ximage = image_src.size[0]
        return image_src, yimage, ximage

    def createMaterial(self, obj, image_src):
        mat = obj.active_material
        if not mat:
            mat = bpy.data.materials.new(name=obj.name + '_Material')
            obj.active_material = mat
        
        mat.use_nodes = True
        
        #mat = ob.active_material
        # Get the nodes
        nodes = mat.node_tree.nodes
        nodes.clear()

        # Add the Principled Shader node
        node_principled = nodes.new(type='ShaderNodeBsdfPrincipled')
        node_principled.location = 0,0

        # Add the Image Texture node
        node_tex = nodes.new('ShaderNodeTexImage')
        # Assign the image
        node_tex.image = image_src #bpy.data.images.load("//your_image.exr")
        node_tex.location = -400,0

        # Add the Output node
        node_output = nodes.new(type='ShaderNodeOutputMaterial')   
        node_output.location = 400,0

        # Link all nodes
        links = mat.node_tree.links
        link = links.new(node_tex.outputs["Color"], node_principled.inputs["Base Color"])
        link = links.new(node_principled.outputs["BSDF"], node_output.inputs["Surface"])    

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

    def execute(self, filePath, width=1.0, height = 0.1, sideTexel = [0.05, 0.05]):
        # Clear the scene
        self.deleteAllObjects()

        # Load input image
        image_src, yimage, ximage = self.loadImage(filePath)
        if not image_src:
            return
        
        # Create a cube and size it to match the image x,y dimenesions but normalized so that x is length 1
        cubex = width
        cubey = width * (yimage / ximage)
        bpy.ops.mesh.primitive_cube_add(size=1.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(cubex, cubey, height))
 
        selected = [obj for obj in bpy.context.selected_objects]
        geom = selected[0]
        self.createMaterial(geom, image_src)

        #bpy.ops.screen.info_log_show()

        # Update texture coordinates
        bpy.ops.object.mode_set( mode = 'EDIT' )
        bpy.ops.mesh.select_mode( type = 'FACE' )
        bpy.ops.mesh.select_all( action = 'SELECT' ) 
        self.setMeshUvs(selected[0], sideTexel)
        bpy.ops.object.mode_set( mode = 'OBJECT' )

width = 3.0
height = 0.1
sideTexel = [0.05, 0.05]
filePath = "D:/Work/HeathCarePrivate/Diabetes/images/ui/release button label.png"
builder = imageToMeshBuilder()
builder.execute(filePath, width, height, sideTexel)