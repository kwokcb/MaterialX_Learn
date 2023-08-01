# %% [markdown]
# # Rendering
# 
# This book will examine how to set up for rendering with MaterialX. It is not about how to write a renderer.
# 
# The topics covered include:
# 
# 1. What is `renderable` and how to find `renderable`
# 2. Setting up graphs which are renderable.
# 2. Semantic differences between `roots` and handling "transparency".
# 3. Accessing inputs and binding resources.
# 
# This book is **WIP**.

# %% [markdown]
# ## Setup
# 
# The following code will be used to perform basic setup, which includes creating a working document 
# and loading in standard libraries.

# %%
import MaterialX as mx
import MaterialX.PyMaterialXGenShader as mx_gen_shader
import MaterialX.PyMaterialXGenGlsl as mx_gen_glsl
import MaterialX.PyMaterialXRender as mx_render
import MaterialX.PyMaterialXRenderGlsl as mx_render_glsl
import os, inspect, sys

from mtlxutils import mxshadergen

stdlib = mx.createDocument()
searchPath = mx.getDefaultDataSearchPath()
#searchPath.append(os.path.dirname(inputFilename))        
libraryFolders = mx.getDefaultDataLibraryFolders()
try:
    libFiles = mx.loadLibraries(libraryFolders, searchPath, stdlib)
except mx.Exception as err:
    print('Failed to load standard library definitions: "', err, '"')

if libFiles:
    doc = mx.createDocument()
    doc.importLibrary(stdlib)
    print('Loaded %s standard library definitions' % len(doc.getNodeDefs()))

# %%

#inputFilename = './data/standard_surface_marble_solid.mtlx'
inputFilename = './data/unlit_marble_solid.mtlx'
#inputFilename = './data/unlit_image.mtlx'
try:
    mx.readFromXmlFile(doc, inputFilename)        
    valid, msg = doc.validate()
    if not valid:
        raise mx.Exception('Document is invalid')

    print('Read in valid file "'"%s"'" for rendering.' % inputFilename)

except mx.ExceptionFileMissing as err:
    print('File %s could not be loaded: "' % inputFilename, err, '"')
except mx.Exception as err:
    print('File %s fail to load properly: "' % inputFilename, err, '"')

# %%
#import PIL 
#help(Image)

def imageLoaderTest():
    return False
    #if imageLoader:
    #    print('created image loader')
    #    newImage = imageLoader.loadImage('./images/Houdini_Node_Editor.png')
    #    print('load image:', newImage.getWidth(), ',', newImage.getHeight(), ',', newImage.getChannelCount())
    #    print('- bt:', newImage.getBaseType(), '. bs', newImage.getBaseStride() )
    #    imageLoader.saveImage('./test.png', newImage, False)

    #self.image = mx_render.Image.create(512, 512, 4, mx_render.BaseType.UINT8 )
    #if self.image:
    #    self.image.createResourceBuffer()
    #    color = mx.Color4(1, 1, 0, 1)
    #    self.image.setUniformColor(color)

class GlslRenderer():
    
    def __init__(self):
        # Renderer      
        self.renderer = None

        # Code Generator
        self.mxgen = None 
        self.activeShader = None
        self.activeShaderErrors = ''
        self.sourceCode = {}

        # Image capture
        self.capturedImage = None

        # Geometry loading
        self.haveCGLTFLoader = False
        for className, classObject in inspect.getmembers(sys.modules['MaterialX.PyMaterialXRender']):
            if className == 'CgltfLoader' and inspect.isclass(classObject):
                self.haveCGLTFLoader = True
                break

        # Light setup
        self.lightHandler = None

    def getRenderer(self):
        return self.renderer
    
    def getCodeGenerator(self):
        return self.mxgen
    
    def getActiveShader(self):
        return self.activeShader

    def getActiveShaderErrors(self):
        return self.activeShaderErrors
    
    def getSourceCode(self):
        return self.sourceCode
    
    def haveGLTFLoader(self):
        return self.haveCGLTFLoader
    
    def getLightHandler(self):
        return self.lightHandler

    def initialize(self, w=512, h=512, bufferFormat=mx_render.BaseType.UINT8):
        self.renderer = mx_render_glsl.GlslRenderer.create(w, h, bufferFormat)
        if self.renderer:
            self.renderer.initialize()
            self.initializeImageHandler()
            self.initializeGeometryHandler()

    def resize(self, w, h):
        if not self.renderer:
            return False
        
        self.renderer.setSize(w, h)
        self.capturedImage = None

    def initializeImageHandler(self):        
        imageLoader = mx_render.StbImageLoader.create()
        imageHandler = mx_render_glsl.GLTextureHandler.create(imageLoader)    
        # Missing fom the Python API !
        #imageHandler = renderer.createImageHandler()
        if imageHandler:
            imageHandler.setSearchPath(searchPath)
            print('Initialize image handler on renderer')
            self.renderer.setImageHandler(imageHandler)

    def initializeGeometryHandler(self):
        # renderer has a geometry handler created by
        # default so not need to call: mx_render.GeometryHandler.create()
        geometryHandler = self.renderer.getGeometryHandler()
        # TODO: Currently missing gltf loader from Python API
        if self.haveCGLTFLoader:
            gltfLoader = mx_render.CgltfLoader.create()
            geometryHandler.addLoader(gltfLoader)

    def loadGeometry(self, fileName):
        geometryHandler = self.renderer.getGeometryHandler()
        if geometryHandler:
            texcoordVerticalFlip = True
            if not geometryHandler.hasGeometry(fileName):
                geometryHandler.loadGeometry(fileName, texcoordVerticalFlip)

    def getGeometyHandler(self):
        return self.renderer.getGeometryHandler()

    def initializeLights(self, doc, enableDirectLighting, radianceIBLPath, irradianceIBLPath, enableReferenceQuality):
        self.lightHandler = mx_render.LightHandler.create()

        # Scan for lights
        if enableDirectLighting:
            lights = []
            self.lightHandler.findLights(doc, lights)
            mxcontext = self.mxgen.getContext()
            self.lightHandler.registerLights(doc, lights, mxcontext)

            # Set the list of lights on the with the generator
            self.lightHandler.setLightSources(lights)

        # Load environment lights.
        imageHandler = self.renderer.getImageHandler()
        envRadiance = imageHandler.acquireImage(radianceIBLPath)
        envIrradiance = imageHandler.acquireImage(irradianceIBLPath)

        # Apply light settings for render tests.
        self.lightHandler.setEnvRadianceMap(envRadiance)
        self.lightHandler.setEnvIrradianceMap(envIrradiance)
        self.lightHandler.setEnvSampleCount(4096 if enableReferenceQuality else 1024)
        # TODO: Python API missing
        #self.lightHandler.setRefractionTwoSided(True)

    def captureImage(self):

        self.capturedImage = self.renderer.captureImage(self.capturedImage)

    def saveCapture(self, filePath, verticalFlip=True): 
        if not self.capturedImage:
            self.captureImage()
        
        imageHandler = self.renderer.getImageHandler()
        if imageHandler:
            imageHandler.saveImage(filePath, self.capturedImage, verticalFlip)            

    def getImageHandler(self):
        return self.renderer.getImageHandler()

    def getCapturedImage(self):
        return self.capturedImage

    def setupGenerator(self, doc, stdlib, searchPath):
        # Setup generation
        self.mxgen = mxshadergen.MtlxShaderGen(doc, stdlib)
        self.mxgen.setup()

        # Set generator and generator options
        mxcontext = self.mxgen.setGeneratorForTarget('genglsl')
        mxgenerator = mxcontext.getShaderGenerator()

        # Set source code path
        self.mxgen.registerSourceCodeSearchPath(searchPath)

    def findRenderableElements(self, doc):
        # Generate shader for a given node
        self.nodes = self.mxgen.findRenderableElements(doc)
        return self.nodes

    def generateShader(self, node):
        self.activeShader = None
        if not node:
            return None
        
        # Set up generation options.
        # Detect requirement for shading and transparency.
        mxcontext = self.mxgen.getContext()
        mxoptions = mxcontext.getOptions()
        mxgenerator = mxcontext.getShaderGenerator()
        if not mx_gen_shader.elementRequiresShading(node):
            mxoptions.hwMaxActiveLightSources = 0
        else:
            mxoptions.hwMaxActiveLightSources = 0
        mxoptions.hwTransparency = mx_gen_shader.isTransparentSurface(node, mxgenerator.getTarget())
        mxoptions.targetColorSpaceOverride = 'lin_rec709'

        self.activeShader, self.activeShaderErrors = self.mxgen.generateShader(node)        
        if self.activeShader:
            self.sourceCode[mx_gen_shader.VERTEX_STAGE] = self.activeShader.getSourceCode(mx_gen_shader.VERTEX_STAGE)
            self.sourceCode[mx_gen_shader.PIXEL_STAGE] = self.activeShader.getSourceCode(mx_gen_shader.PIXEL_STAGE)

        return self.activeShader

    def createProgram(self):
        if not self.activeShader:
            return False
        
        #psStage = shader.getStage('pixel') #mx_gen_shader.Stage.PIXEL
        #block = psStage.getUniformBlock('PublicUniforms') #mx_gen_shader.HW.PUBLIC_UNIFORMS)
        # getVariableOrder() is not defined in the Python API
        #for uniform in block: #.getVariableOrder():
        #    uniformVariable = uniform.getVariable()
        #    print(uniformVariable)

        self.renderer.setLightHandler(self.lightHandler)
        self.renderer.createProgram(self.activeShader)
        #self.renderer.validateInputs()

        program = self.renderer.getProgram()
        if program:
            return True
        else:
            return False

    def getProgram(self):
        if self.renderer:
            return self.renderer.getProgram() 

    def render(self):
        if not self.renderer:
            return False, 'No renderer'
        
        # Render
        try:
            print('Render')
            self.renderer.render()
            print('Render done')
        except LookupError as err:
            return False, err
        
        return True, ''

# %% [markdown]
# ## Rendering Setup

# %%
glslRenderer = GlslRenderer()
glslRenderer.initialize(512, 512, mx_render.BaseType.UINT8)
# This is not exposed
#clearColor = mx.Color3(1.0, 1.0, 1.0)
#glslRenderer.setScreenColor(clearColor)

glslRenderer.initializeLights(doc, False, 
                              './data/lights/san_giuseppe_bridge.hdr', 
                              './data/lights/irradiance/san_giuseppe_bridge.hdr',
                              False)
lightHandler = glslRenderer.getLightHandler()
if lightHandler:
    print('Setup lighting:')
    radMap = lightHandler.getEnvRadianceMap()
    irradMap = lightHandler.getEnvIrradianceMap()
    print('- Loaded radiance map: %d x %d' % (radMap.getWidth(), radMap.getHeight()))
    print('- Loaded irradiance map: %d x %d' % (irradMap.getWidth(), irradMap.getHeight()))

geometryFile = './data/sphere.obj'
#if glslRenderer.haveGLTFLoader():
#    geometryFile = './data/shaderball.glb'

glslRenderer.loadGeometry(geometryFile)
geometryHandler = glslRenderer.getGeometyHandler() 
if geometryHandler:
    print('Setup geometry:')
    for mesh in geometryHandler.getMeshes():
        print('- Initialze geometry mesh: "%s"' % mesh.getName())

glslRenderer.setupGenerator(doc, stdlib, searchPath)
context = glslRenderer.getCodeGenerator().getContext()
if context:
    generator = context.getShaderGenerator()
    if generator:
        print('- Iniitialize generator for target:', generator.getTarget())

# %%
# Set up additional options for generation
context = glslRenderer.getCodeGenerator().getContext()
genOptions = context.getOptions()
# TODO: This has not been exposed in Python
#genOptions.addUpstreamDependencies = True

# Find a renderable and generate the shader for it
nodes = glslRenderer.findRenderableElements(doc)
shader = None
printSource = True
if nodes:
    shader = glslRenderer.generateShader(nodes[0])
    if shader:
        print('Generate shader for node: %s' % nodes[0].getNamePath())

# %% [markdown]
# ## Shader Stages / Uniform Blocks / Shader Ports
# 
# * For languages like OSL and MSL there is only one shader which is the `pixel` shader -- and thus one stage.
# * For hardware shading languages like GLSL, MSL, Vulkan there can be more than 1 stage. Currently the
# defaults code generators only emit a `vertex` and `pixel` stage.
# * Within each stage the list of uniforms can be extracted. These are organized into "blocks". User facing uniforms will be organiz "public" blocks, and internal ones in "private" blocks. 
# * Lighting uniforms are exposed as a "lighting" block. For example environment lighting can be bound there.
# * Within each block the each uniform is represented as a <a href="" target="_blank">ShaderPort</a>
# 
# ### Shader Ports
# * shader ports will provide the exact name of the uniform in the shader via `getVariable()` interface
# * they will also provide the value after all "resolves" have been performed. Note that this can differ
# from the original value stored on a node Input. For example tokens may be resolved on geometric attribute and
# filenames. 
# * It is possible to "pre-resolve" values as needed. For example MDL has a special resolver to handle file names.
# It makes use of the <a href="" target="_blank">flattenFilenames()</a> utility before performing additional resolves
# for `Omniverse` compatibility
# 
# * To find correspondence back to the original MaterialX input the path may be found using `getPath()`, and then
# calling `Document.getDescendent()` with the path as the interface argument. An `Input` will be returned if found.
#   * Note that an input to an graph's interior node may be returned as the port path. In this case,
#     the interface input should be found to provide the correct upstream corresponding path. The method
#     `getPortPath()` shows this logic.
#   * Note that a Shader may be generated at a given time, and if the MaterialX graph changes then the Shader paths
#     may reference inputs which may no longer exist. It is up the integration to regenerate shaders on any "topological"
#     changes.
# 
# In the sample funciton `debugStages()`, each stage is iterated over. For each stage the list of uniform blocks is extracted.
# Then for each block the list of shader ports is printed out. Note that "private" vertex stage uniforms involve things like model / view transforms, there are private and pixel stage uniforms as well as "light data" uniforms for environment map binding.

# %%
def getPortPath(inputPath, doc):
    '''
    Find any upstream interface input which maps to a given path
    '''
    if not inputPath:
        return inputPath, None
    
    input = doc.getDescendant(inputPath)
    if input:
        # Redirect to interface input if it exists.
        # TODO: This should be done during shader generation !
        interfaceInput = input.getInterfaceInput()
        if interfaceInput:
            input = interfaceInput
            return input.getNamePath(), interfaceInput

    return inputPath, None

def debugStages(shader, doc, filter='Public'):
    '''
    Scan through each stage of a shader and get the uniform blocks for each stage.
    For each block, print out list of assocaited ports.
    '''
    if not shader:
        return

    for i in range(0, shader.numStages()):
        stage = shader.getStage(i)
        if stage:
            print('Stage name: "%s"' % stage.getName())
            print('-' * 30)
            if stage.getName():
                for blockName in stage.getUniformBlocks():
                    block = stage.getUniformBlock(blockName)
                    if filter:
                        if filter not in block.getName():
                            continue                        
                    print('- Block: ', block.getName())  

                    for shaderPort in block:
                        variable = shaderPort.getVariable()
                        value = shaderPort.getValue().getValueString() if shaderPort.getValue() else '<NONE>'
                        origPath = shaderPort.getPath()
                        path, interfaceInput = getPortPath(shaderPort.getPath(), doc)                                                
                        if not path:
                            path = '<NONE>'
                        else:
                            if path != origPath:
                                path = origPath + ' --> ' + path
                        type = shaderPort.getType().getName()
                        print('  - Variable: %s. Value: (%s). Type: %s, Path: "%s"' % (variable, value, type, path))

                        unit = shaderPort.getUnit()
                        if interfaceInput:
                            colorspace = interfaceInput.getColorSpace()
                        else:
                            colorspace = shaderPort.getColorSpace() 
                        if unit or colorspace:                            
                            print('   - Unit:%s, ColorSpace:%s' % (unit,colorspace))
                        
if shader:
    # Examine public uniforms first
    debugStages(shader, doc, 'Public')

# %% [markdown]
# <img src='./data/unlit_image_graph.png' width='80%'>
# <img src='./data/unlit_image_top_level.png' width='80%'>
# 

# %% [markdown]
# 
# In the output, you will note that:
# * the shader variable `multiply_color3_in1` corresponds to an input: `nodegraph1/multiply_color3/in1` maps to the interface input `nodegraph1/color3_port`. 
# * the shader variable `image_color3_file` corresponds to an interior input: `nodegraph1/image_color3/file` is maps to the interface input `nodegraph1/filename_port`. 
# 
# Then updating the interface ports, the appropriate shader uniform needs ot be used.
# 
# The file image input 'nodegraph1/filename_port' is an interface input which has a `colorspace` transform specified.

# %% [markdown]
# ### Building UI
# 
# MaterialXRender has the utility `createUIPropertyGroups()` which performs parsing on a block to build
# UI for the MaterialX Viewer and Graph Editor.
# 
# It goes through the interface mapping step as well as extracting desired information from the MaterialX `Inputs` and `ShaderPort` inputs.

# %% [markdown]
# ### Source Code
# 
# The uniform information can be compared against the produced source code.
# In the sample code below we scan the source for "uniforms" and prints them out.

# %%
if printSource:
    sourceCode = glslRenderer.getSourceCode()
    for stage in sourceCode:
        print('-' * 80)
        print('- "%s" Stage Code:' % stage)
        lines = sourceCode[stage].split('\n')
        for l in lines:
            if l.startswith('uniform'):
                print('  ', l)


# %% [markdown]
# 
# ## Note on Topological Changes
# * In previous version there was a dirty/notification system which could be hooked into when a document changed. As this no longer exists, it is up the integration to keep track of relevant changes.
# * Value changes can require rebinding of resources such as geometry and images as well as scalar values.
# * Topological changes can include:
#   * changes between node port connections, 
#   * changes in value on conditional nodes, 
#   * changes to attributes which extract channels from a tuple, 
#   * changes to values which affect transparency
#   * changes which affect "uniform blocks", if the blocks organization / layout changes. (e.g. `Vulkan` creates uniform blocks) 
#   For this it would be **very useful if there was a way to specify a hint that a value change means a topological change.**
# * Value changes only require rebinding to an existing shader while topological changes require a shader to be rebuilt.
# 
# 

# %% [markdown]
# ## Binding Inputs
# 
# **WIP**

# %%
createdProgram = False
if shader:
    print('Generated shader for node: %s' % nodes[0].getNamePath())
    createdProgram = glslRenderer.createProgram()

printAttribs = False
if createdProgram:
    print('Create renderer program from shader')

    program = glslRenderer.getProgram()
    if program:
        if printAttribs:
            attribs = program.getAttributesList()
            print('%d geometry attribs in program' % len(attribs))   
            for attrib in attribs:
                print('- attribute: %s' % attrib)
                input = attribs[attrib] 
            
            uniforms = program.getUniformsList()
            print('%d uniforms' % len(uniforms))
            for uniform in uniforms:
                print('- Uniform:', uniform)
                port = uniforms[uniform]
                print('  - Port type:', port.gltype)   



# %% [markdown]
# ## Rendering and Capturing Images

# %%

runRender = True
if createdProgram and runRender:
    rendered, renderErrors = glslRenderer.render()
    if not rendered:
        print('Failed to render, Errors:', renderErrors)
    else:
        print('Rendered frame.')

glslRenderer.captureImage()
capturedImage = glslRenderer.getCapturedImage()
if capturedImage:
    flipImage = True
    fileName = './data/render_notebook_capture.png'
    print('Saved rendering to: %s' % fileName)
    glslRenderer.saveCapture(fileName, flipImage) 

# %% [markdown]
# Rendering Images
# 
# <img src="data/render_notebook_capture.png" style="border:5px outset silver"> 


