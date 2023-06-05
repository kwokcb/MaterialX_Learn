# %% [markdown]
# # Rendering
# 
# This book will examine how to set up for rendering with MaterialX. It is not about how to write a renderer.
# 
# The topics covered include:
# 
# 1. Setting up renderers and using rendering utilities for geometry, images, and lighting.
# 1. Using graphs which are have `renderable` items.
# 2. Semantic differences between `roots` and handling "transparency".
# 3. Accessing inputs and binding resources.
# 
# This book is **WIP**.
# 
# Some example results are shown below to show: lit vs unlit, texture resource usage. (more to come)
# <table border="0">
# <tr>
# <td><img src="./data/standard_surface_marble_solid.png" style="border:5px outset silver" > 
# <td><img src="./data/unlit_marble_solid.png" style="border:5px outset silver" >  
# <td><img src="./data/unlit_image.png" style="border:5px outset silver" > 
# </tr>
# </table>
# <sup>The above images are renders from different files. Left shows the sample Marble from the MaterialX distribution,
# the middle is a modified version which uses an `unlit surface` shader, and the last is a graph which uses an external image resources modulated by an input color. Both the image and input color have a input color space specified.
# 
# > Execution Note: The notebook can cause some loss to the current context for the renderer resulting in bad state. If this occurs then the notebook can be restarted, or the Python file can be run from the command line. In general, a renderer would not inject Python queries and Markdown code intermixed with rendering as is the case for this book.

# %% [markdown]
# ## 1. Setup
# 
# ### 1.1 Core Setup
# The following code will be used to perform basic setup, which includes creating a working document 
# and loading in standard libraries.

# %%
import MaterialX as mx

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

# %% [markdown]
# ### 1.2 Code Generation and Rendering Modules
# For code generation `MaterialxGenShader` and any per target generation modules are loaded.
# In this example we load in the GLSL code generator. Note that we use the `mtlxutils` utility
# logic found in `mxshadergen` to handle code generation so that the GLSL generation module
# is not directly used.
# 
# For rendering an example GLSL renderer (PyMaterialXRenderGlsl) is loaded. This is used for MaterialX Viewer and Node Editor 
# as well as render test suite unit testing. This makes use of the base rendering module (`MaterialXRender`) which provides access to utilities such as geometry and image loaders as well as higher level utilities such as texture baking.
# 
# Some additional utilities are added for display (`IPython`) and module discovery (`inspect`)

# %%
import MaterialX.PyMaterialXGenShader as mx_gen_shader
import MaterialX.PyMaterialXGenGlsl as mx_gen_glsl
import MaterialX.PyMaterialXRender as mx_render
import MaterialX.PyMaterialXRenderGlsl as mx_render_glsl
from mtlxutils import mxshadergen

import inspect, sys
from IPython.display import display_markdown

# %% [markdown]
# ## 2. Sample Renderer Logic
# 
# A class called `GlslRenderer` is added to encapsulate the logic required to set up the <a href="https://materialx.org/docs/api/class_glsl_renderer.html" target="_blank">GLSL example renderer</a>,
# set up resource handlers and a source code generator, create executable shader programs, and run the render pipeline.
# 
# > A "TODO" has been added as a comment for C++ apis which are missing Python API wrappers.
# 
# The main methods of interest are:
# 
# 1. `initialize()` which calls the GLSL example renderer to initialize a device and framebuffer. Image and geometry handlers are also initialized.
# 
# 2. `initializeImageHandler` which initialize <a href="https://materialx.org/docs/api/class_image_handler.html" target="_blank">image handlers</a> and 
# loaders such as the built in <a href="https://materialx.org/docs/api/class_stb_image_loader.html" target="_blank">STB image loader</a>. If built the `Open Image IO (OIIO)` loader (<a href="https://materialx.org/docs/api/class_oiio_image_loader.html" target="_blank">OiioImageLoader</a>) can also be instantiated and used. Note that as this is a hardware renderer a specific GLSL handler is instantiated which allows for hardware texture resource management. The handler used by the renderer is set using `setImageHandler()`.
# 
# 3. `initializeGeometryHandler` which uses a <a href="https://materialx.org/docs/api/class_geometry_handler.html" target="_blank">geometry handler</a> to setup geometry loaders. By default an <a href="https://materialx.org/docs/api/class_tiny_obj_loader.html" target="_blank">'obj' file loader</a> is created.
# A <a href="https://materialx.org/docs/api/class_cgltf_loader.html" target="_blank">GLTF loader</a> is available in C++, but at time of writing has no Python wrapper. The loader will be used to
# load in geometry for rendering. Note that the loaders will automatically create tangent and bitangents. This
# is important to note as all shading models (except for `unlit surface`) require these geometric streams.
# 
# `loadGeometry()` calls into actual geometry loaders to load geometry files. 
# 
# 4. `initializeLights` which is used to set up a <a href="https://materialx.org/docs/api/class_light_handler.html" target="_blank">light handler</a> which handles setting up directional lights specified in a MaterialX file as well as set up indirect lighting by specifying environment lighting files. These files are loaded in using the `ImageLoader.acquireImage()` interface. 
# 
# 5. `setupGenerator` which sets up the shader code generator for the desired target (`genglsl`). Note that the
# shader generation utility keeps <a href="https://materialx.org/docs/api/class_gen_context.html" target="_blank">GenContext</a> for reuse. It is important to "register" where source code stored in files can be found by calling <a href="https://materialx.org/docs/api/class_gen_context.html" target="_blank">registerSourceCodeSearchPath()</a> on the context. Generally this would be to the root of where
# the definition libraries are found but could also be elsewhere. The interface appends additional paths to search.
# 
# 6. `generateShader` sets up some basic <a href="" target="_blank">generation options</a> such as whether to use lighting or not and a hint if the shader is transparent. The utility methods: <a href="https://materialx.org/docs/api/_material_x_gen_shader_2_util_8h.html" target="_blank">elementRequiresShading()</a> and <a href="https://materialx.org/docs/api/_material_x_gen_shader_2_util_8h.html" target="_blank">isTransparentSurface()</a> perform this introspection respectively. They are both found as utilities within the `MaterialXGenShader` module.
# 
# > Note that an application integration should provide the following additional information for the renderer's working color space as as well as the geometry scene real-world units. This is because only an integration can provide this information.
# See the reference <a href="https://kwokcb.github.io/MaterialX_Learn/documents/definitions/library_glossary.html" target="_blank">Glossary</a> for units and color space transform information.
# 
# 7. `createProgram` is used to create a GLSL program from a <a href="https://materialx.org/docs/api/class_shader.html" target="_blank">Shader</a> which is created via code generation. This is just one example of source code usage.
# 
# 8. `render` is used to render a frame. As the example renderer's pipline is a limited one used for unit testing, it
# will perform all of the required program setup and input bindings based on inspecting the program itself, making
# used of the specified image, geometry and light handlers to (in this case) set up hardware resources for binding.

# %% [markdown]
# ### 2.1 Handling Real-World Units and Color Management
# 
# Thought not strictly necessary, it is useful to check for available unit and color management support.
# 
# 1. Units: The `buildUnitDict()` will scan for available unit types and unit identifiers. For example `distance` units are supported with unit identifiers such as `meter`, `inch`, and `foot` conversions being supported.
# 2. Color Transforms: The `buildColorTransformDict()` will scan for available `colorspace` transforms. Note that only transforms to a (target) linear color space (`lin_rec709`) is currently supported. 

# %%
def buildUnitDict(doc):
    '''
    Sample code to examine unit types and unit name information
    '''
    unitdict = {}

    for ud in doc.getUnitDefs():
        unittype = ud.getAttribute('unittype')
        unitinfo = {}
        for unit in ud.getChildren():
            unitinfo[unit.getName()] = unit.getAttribute('scale')

        unitdict[unittype] = unitinfo
    return unitdict

def buildColorTransformDict(doc):
    colordict = {}
    targetdict = {}
    for cmnode in doc.getNodeDefs():
        if cmnode.getNodeGroup() == 'colortransform':
            name = cmnode.getName()
            name = name.removeprefix('ND_')
            namesplit = name.split('_to_')
            type = 'color3'
            if 'color4' in namesplit[1]:
                continue
            else:
                namesplit[1] = namesplit[1].removesuffix('_color3')

            sourceSpace = namesplit[0]
            targetSpace = namesplit[1]

            if sourceSpace in colordict:
                sourceItem = colordict[sourceSpace]
                sourceItem.append(targetSpace)
            else:
                colordict[sourceSpace] = [targetSpace]

            if targetSpace in targetdict:
                taregetItem = targetdict[targetSpace]
                taregetItem.append(sourceSpace)
            else:
                targetdict[targetSpace] = [sourceSpace]

    
    return colordict, targetdict

# Build unit dictionary
unitdict = buildUnitDict(doc)
for unittype in unitdict:
    print('Unit Type: %s' % unittype)
    units = unitdict[unittype]
    for unit in units:
        print('  Unit: %s. Scale Factor: %s' % (unit, units[unit]))

print('')

# Build colorspace dictionary
stdict, tsdict = buildColorTransformDict(doc)
print('Supported Source to Target Transforms:')
for sourceSpace in stdict:
    print('  %s --> %s supported' % (sourceSpace, ', '.join(stdict[sourceSpace])))
print('Supported Target From Target Transforms:')
for targetSpace in tsdict:
    print('  %s <-- %s supported' % (targetSpace, ', '.join(tsdict[targetSpace])))    


# %%

class GlslRenderer():
    '''
    Wrapper for GLSL sample renderer.

    Handles setup of image, geometry and light handlers as well as GLSL code and 
    program generation. 

    Calls into sample renderer to render and capture images as desired.
    '''
    
    def __init__(self):
        # Renderer      
        self.renderSize = [512, 512]
        self.renderer = None

        # Code Generator
        self.mxgen = None 
        self.activeShader = None
        self.activeShaderErrors = ''
        self.sourceCode = {}

        # Image Handling
        self.capturedImage = None
        self.haveOIIOImageHandler = False
        mxrenderMembers = inspect.getmembers(sys.modules['MaterialX.PyMaterialXRender'])
        for className, classObject in mxrenderMembers:
            if className == 'OiioImageLoader' and inspect.isclass(classObject):
                self.haveOIIOImageHandler = True
                break

        # Geometry loading
        self.haveCGLTFLoader = False
        # Note: TODO: Test for existence of GLTF loader in Python module. This does not exist in a release currently.
        for className, classObject in mxrenderMembers:
            if className == 'CgltfLoader' and inspect.isclass(classObject):
                self.haveCGLTFLoader = True
                break

        # Light setup
        self.lightHandler = None

        # Units dictionary
        self.unitDict = None

        # Colorspace dictionaries
        self.sourceColorDict = None
        self.targetColorDict = None

    def getRenderer(self):
        return self.renderer
    
    def getDefaultRenderSize(self):
        return self.renderSize
    
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

    def haveOIIOLoader(self):
        return self.haveOIIOImageHandler
    
    def getLightHandler(self):
        return self.lightHandler

    def initialize(self, w=0, h=0, bufferFormat=mx_render.BaseType.UINT8):
        '''
        Setup sample renderer with a given frame buffer size.
        Initialize image and geometry handlers.
        '''
        if w == 0 and h == 0:
            w = self.renderSize[0]
            h = self.renderSize[1]
        if w < 4:
            w = 4
        if h < 4:
            h = 4
        self.renderer = mx_render_glsl.GlslRenderer.create(w, h, bufferFormat)
        if self.renderer:
            self.renderer.initialize()
            self.initializeImageHandler()
            self.initializeGeometryHandler()

    def resize(self, w, h):
        '''
        Resize frame buffer. 
        Clears any cached captured image.
        '''
        if not self.renderer:
            return False
        
        self.renderer.setSize(w, h)
        self.capturedImage = None

    def initializeImageHandler(self):   
        '''
        Initialize image handler. 
        ''' 
        if self.renderer.getImageHandler():
            return
            
        # TODO: Missing fom the Python API for createImageHandler() 
        #imageHandler = renderer.createImageHandler()
        imageLoader = mx_render.StbImageLoader.create()
        imageHandler = mx_render_glsl.GLTextureHandler.create(imageLoader)    
        # Add OIIO handler if it exists
        if self.haveOIIOImageHandler:
            imageHandler.addLoader(mx_render.OIIOHandler.create())

        if imageHandler:
            imageSearchPath = mx.FileSearchPath()
            imageSearchPath.append(mx.FilePath('./data'))            
            imageHandler.setSearchPath(imageSearchPath)
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
        if self.lightHandler:
            return
        
        # Ensure image handler is initialized
        self.initializeImageHandler()

        # Create a light handler
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
        '''
        Capture the framebuffer contents to an image
        '''
        self.capturedImage = self.renderer.captureImage(self.capturedImage)

    def clearCaptureImage(self):
        '''
        Clear out any captured image
        '''
        self.captureImage = None

    def saveCapture(self, filePath, verticalFlip=True): 
        '''
        Save captured image to a file.
        Vertical flip image as needed.
        '''
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
        '''
        Setup code generation. Returns the generator instantiated.
        Note: It is important to set up the source code path so that
        file implementations can be found.
        '''
        self.mxgen = mxshadergen.MtlxShaderGen(doc, stdlib)
        self.mxgen.setup()

        # Check generator and generator options
        mxgenerator = None
        mxcontext = self.mxgen.setGeneratorForTarget('genglsl')
        if mxcontext:
            mxgenerator = mxcontext.getShaderGenerator()

        # Set source code path
        self.mxgen.registerSourceCodeSearchPath(searchPath)

        return mxgenerator

    def findRenderableElements(self, doc):
        # Generate shader for a given node
        self.nodes = self.mxgen.findRenderableElements(doc)
        return self.nodes

    def buildUnitDict(self, doc):
        ''' 
        Create real-world units dictionary for target unit checking
        '''
        if self.unitDict:
            return

        self.unitDict = {}

        for ud in doc.getUnitDefs():
            unittype = ud.getAttribute('unittype')
            unitinfo = {}
            for unit in ud.getChildren():
                unitinfo[unit.getName()] = unit.getAttribute('scale')

            self.unitDict[unittype] = unitinfo
        return self.unitDict

    def buildColorTransformDict(self,doc):
        '''
        Build a pair of dictionaries to test for supported colorspace transforms. 
        One is from source color space to target, and the other is to a target from source.
        '''
        if self.sourceColorDict:
            return

        colordict = {}
        targetdict = {}
        for cmnode in doc.getNodeDefs():
            if cmnode.getNodeGroup() == 'colortransform':
                name = cmnode.getName()
                name = name.removeprefix('ND_')
                namesplit = name.split('_to_')
                type = 'color3'
                if 'color4' in namesplit[1]:
                    continue
                else:
                    namesplit[1] = namesplit[1].removesuffix('_color3')

                sourceSpace = namesplit[0]
                targetSpace = namesplit[1]

                if sourceSpace in colordict:
                    sourceItem = colordict[sourceSpace]
                    sourceItem.append(targetSpace)
                else:
                    colordict[sourceSpace] = [targetSpace]

                if targetSpace in targetdict:
                    taregetItem = targetdict[targetSpace]
                    taregetItem.append(sourceSpace)
                else:
                    targetdict[targetSpace] = [sourceSpace]
    
        self.sourceColorDict = colordict
        self.targetColorDict = targetdict
        return colordict, targetdict
    
    def getColorTransformDict(self):
        return self.sourceColorDict, self.targetColorDict

    def generateShader(self, node, targetColorSpaceOverride='lin_rec709', targetDistanceUnit='meter'):
        '''
        Generate new GLSL shader.
        - Inspects node to check if it requires lighting and / or is transparent.
        - Sets target colorspace and real-world units
        - Generates code and caches it
        - Caches the "active" Shader node
        '''
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

        # Check support of units and working color space
        doc = node.getDocument()
        if doc:
            self.buildUnitDict(doc)
            units = self.unitDict['distance']
            if targetDistanceUnit not in units:
                targetDistanceUnit = 'meter'

            sdict, tdict = self.buildColorTransformDict(doc)
            if tdict:
                if targetColorSpaceOverride not in tdict:
                    targetColorSpaceOverride = 'lin_rec709'
        else:
            targetDistanceUnit = 'meter'
            targetColorSpaceOverride = 'lin_rec709'

        mxoptions.targetDistanceUnit = targetDistanceUnit
        mxoptions.targetColorSpaceOverride = targetColorSpaceOverride

        self.activeShader, self.activeShaderErrors = self.mxgen.generateShader(node)        
        if self.activeShader:
            self.sourceCode[mx_gen_shader.VERTEX_STAGE] = self.activeShader.getSourceCode(mx_gen_shader.VERTEX_STAGE)
            self.sourceCode[mx_gen_shader.PIXEL_STAGE] = self.activeShader.getSourceCode(mx_gen_shader.PIXEL_STAGE)

        return self.activeShader

    def createProgram(self):
        '''
        Create a GLSL program from the active shader node and validates it's inputs.
        Note: A light handler **must** be set to for validation to work properly.
        '''
        if not self.activeShader:
            return False
        
        self.renderer.setLightHandler(self.lightHandler)
        self.renderer.createProgram(self.activeShader)
        self.renderer.validateInputs()

        program = self.renderer.getProgram()
        if program:
            return True
        else:
            return False

    def getProgram(self):
        if self.renderer:
            return self.renderer.getProgram() 

    def render(self):
        '''
        Render a frame.
        - Note: LookupError's are returned if any failure occurs.
        - Status and and any errors are returned. 
        '''
        if not self.renderer:
            return False, 'No renderer'
        
        # Render
        try:
            self.renderer.render()
        except LookupError as err:
            return False, err
        
        return True, ''

# %% [markdown]
# ## 3. Rendering Setup
# 
# This utility class can now be used for rendering with specified output frame parameters.
# 

# %%
glslRenderer = GlslRenderer()
renderSize = glslRenderer.getDefaultRenderSize()
glslRenderer.initialize(renderSize[0], renderSize[1], mx_render.BaseType.UINT8)
print('Initialized renderer')
print('- Have OIIO loader support: %s' % glslRenderer.haveOIIOLoader()) 
print('- Have GLTF loader support: %s' % glslRenderer.haveGLTFLoader()) 

# This is not exposed
#clearColor = mx.Color3(1.0, 1.0, 1.0)
#glslRenderer.setScreenColor(clearColor)

# %% [markdown]
# In the sample code we set up to:
# 
# 1. Use a sphere as the scene geometry 

# %%

geometryHandler = glslRenderer.getGeometyHandler()
if geometryHandler:
    print('- Initialized geometry loader:')

    desiredGeometry = 'sphere'
    geometryFile = './data/sphere.obj'
    if desiredGeometry == 'shaderball':
        if glslRenderer.haveGLTFLoader():
            geometryFile = './data/shaderball.glb'

    glslRenderer.loadGeometry(geometryFile)
    for mesh in geometryHandler.getMeshes():
        print(' - Loaded Mesh: "%s"' % mesh.getName())

# %% [markdown]
# 2. Set up the input file to render

# %%
inputFilename = './data/standard_surface_marble_solid.mtlx'
inputFilename = './data/unlit_marble_solid.mtlx'
inputFilename = './data/unlit_image.mtlx'
inputFilename = './data/stained_glass_material.mtlx'
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

# %% [markdown]
# 3. Set up the lighting. A document which specifies
# the lighting is required. This could be in the working document or a separately loaded in document.
# Here only indirect lighting is setup. 

# %%
glslRenderer.initializeLights(None, False, 
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


# %% [markdown]
# 4. Set up source code generation for `GLSL`. This requires a working document to initialize
# based on the working document and a definition document (which may be the same). Additionally
# a source code search path needs to specified. The default `libraries` path is used as the
# search path. If source code resides elsewhere then the search path can be extended as needed
# but at a minimum the `libraries` path must be included to use the standard definition library.

# %%
sourceCodeSearchPath = searchPath
glslRenderer.setupGenerator(doc, stdlib, sourceCodeSearchPath)
context = glslRenderer.getCodeGenerator().getContext()
if context:
    generator = context.getShaderGenerator()
    if generator:
        print('- Iniitialize generator for target: %s.\n - Source path: %s' % 
              (generator.getTarget(), sourceCodeSearchPath.asString()))

# %% [markdown]
# 5. Chose a node to render with and generate the `Shader`

# %%
# Set up additional options for generation
context = glslRenderer.getCodeGenerator().getContext()
genOptions = context.getOptions()
genOptions.emitColorTransforms = True # This is True by default
genOptions.fileTextureVerticalFlip = True
# TODO: This and a number of other options are not been exposed in the Python API
#genOptions.addUpstreamDependencies = True

# Find a renderable and generate the shader for it
nodes = glslRenderer.findRenderableElements(doc)
shader = None
printSource = True

# Set up overrides for color space and units. Color space may come from the document,
# but units are a property of the application.
targetColorSpaceOverride = 'lin_rec709'
docColorSpace = doc.getColorSpace()
targetDistanceUnit = 'centimeter'
if nodes:
    shader = glslRenderer.generateShader(nodes[0], targetColorSpaceOverride, targetDistanceUnit)
    if shader:
        print('Generate shader for node: "%s"\n- Is Transparent: %s. V-Flip textures: %d.\n- Emit Color Xforms: %d. Default input colorspace: "%s".\n- Target Color space: "%s". Scene Units: "%s"' %
                (nodes[0].getNamePath(),
                 genOptions.hwTransparency, 
                 genOptions.fileTextureVerticalFlip, 
                 genOptions.emitColorTransforms,
                 docColorSpace,
                 genOptions.targetColorSpaceOverride, 
                 genOptions.targetDistanceUnit))

# %% [markdown]
# ## 4. Shader Stages / Uniform Blocks / Shader Ports
# 
# * For languages like OSL and MSL there is only one shader which is the `pixel` shader -- and thus one stage.
# * For hardware shading languages like GLSL, MSL, Vulkan there can be more than 1 stage. Currently the
# defaults code generators only emit a `vertex` and `pixel` stage.
# * Within each stage the list of uniforms can be extracted. These are organized into "blocks". User facing uniforms will be organiz "public" blocks, and internal ones in "private" blocks. 
# * Lighting uniforms are exposed as a "lighting" block. For example environment lighting can be bound there.
# * Within each block the each uniform is represented as a <a href="" target="_blank">ShaderPort</a>
# 
# ### 4.1 Shader Ports
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
# In the sample function `debugStages()`, each stage is iterated over. For each stage the list of uniform blocks is extracted.
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
# ### 3.2 Building UI
# 
# MaterialXRender has the utility `createUIPropertyGroups()` which performs parsing on a block to build
# UI for the MaterialX Viewer and Graph Editor.
# 
# It goes through the interface mapping step as well as extracting desired information from the MaterialX `Inputs` and `ShaderPort` inputs.

# %% [markdown]
# ### 3.3 Examining Source Code
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
# ## 4. Rendering and Capturing Images

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
    fileName = mx.FilePath(inputFilename)
    fileName.removeExtension()
    fileName.addExtension('png')                             
    glslRenderer.saveCapture(fileName, flipImage) 

    imageMD = '### %s\n<img src="%s" style="border:5px outset silver">' % (fileName.asString(), fileName.asString())
    display_markdown(imageMD, raw=True)

# %% [markdown]
# ## 5. Binding Inputs
# 
# This section is *WIP* and will go over binding of scalars and images.
# 
# Note that currently we don't do the actual process of binding but just find the shader uniform, load in an image
# and then find the target shader variable to update.

# %%
imagesToBind = []
variablesToBind = []
nodePathsToBind = []

# Loading in images
imageHandler = glslRenderer.getImageHandler()

# Get the program
program = glslRenderer.getProgram()    

# Scan for input filenames, create the image and bind it to the program
stage = shader.getStage('pixel') if shader else None
if stage:
    block = stage.getUniformBlock('PublicUniforms')

    for shaderPort in block:
        value = shaderPort.getValue()
        if not value:
            continue

        type = shaderPort.getType().getName()
        if type != 'filename':
            continue

        variable = shaderPort.getVariable()
        value = shaderPort.getValue().getValueString() if shaderPort.getValue() else '<NONE>'

        origPath = shaderPort.getPath()
        path, interfaceInput = getPortPath(shaderPort.getPath(), doc)                                                

        unit = shaderPort.getUnit()
        if interfaceInput:
            colorspace = interfaceInput.getColorSpace()
        else:
            colorspace = shaderPort.getColorSpace() 

        imagesToBind.append(value)
        variablesToBind.append(variable)
        nodePathsToBind.append(path)

        newImage = imageHandler.acquireImage(value)
        if newImage:
            print('- Loaded image: "%s". Size: %d x %d. Channel count: %d' % 
                (value, newImage.getWidth(), newImage.getHeight(), newImage.getChannelCount()))
            print(' - Base Type:', newImage.getBaseType(), '. Base Stride:', newImage.getBaseStride() )
            if colorspace:
                print(' - Source color space: %s' % colorspace)
            elif unit:
                print(' - Source unit: %s' % unit)

        # Find the appropriate port on the program
        if program:
            uniforms = program.getUniformsList()
            if variable in uniforms:
                print('- Bind to program / shader port:', variable)


# %% [markdown]
# ## 6. Handling Topological Changes
# 
# In earlier versions of MaterialX there was a "dirty/notification" system which could be hooked into when a document changed. As this no longer exists, it is up the integration to keep track of relevant changes.
# 
# Value changes can require rebinding of resources such as geometry and images as well as scalar values.
# 
# Topological changes can occur due to:
#   * changes between node port connections, 
#   * changes in value on conditional nodes, 
#   * changes in enumerations which result in conditional branching,
#   * changes to attributes which extract channels from a tuple, 
#   * changes to values which affect transparency
#   * changes which affect "uniform blocks", if the blocks organization / layout changes. (e.g. `Vulkan` creates uniform blocks) 
#   For this it would be **very useful if there was a way to specify a hint that a value change means a topological change.**
# 
# Value changes only require rebinding to an existing shader while topological changes require a shader to be rebuilt.
# 
# This section is **WIP**.
# 
# 


