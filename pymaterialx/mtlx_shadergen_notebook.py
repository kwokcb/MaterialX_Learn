# %% [markdown]
# # Shader Generation
# 
# This book will examine how to set up MaterialX for code generation. This book covers the 
# <a href="https://github.com/AcademySoftwareFoundation/MaterialX/blob/main/python/Scripts/generateshader.py" target="_blank">
# generateshader.py</a> 
# script provided as part of the core distribution.
# 
# Topics covered:
# 1. Submodules per code generator
# 2. Context and options for generation
# 3. Real world unit and color management transform. 
# 4. Finding "renderable" items
# 5. Per `target` (shading language) generators.
# 5. Introspection and source code extraction.
# 
# Not covered are the details behind code generation and the pros and cons of different generation options.
# Code Generation is covered 
# <a href="https://github.com/AcademySoftwareFoundation/MaterialX/blob/main/documents/DeveloperGuide/ShaderGeneration.md"
# target ="_blank">here.</a>

# %% [markdown]
# ## Code Generation Submodules
# 
# For the Python distribution, each code generator has created to be a submodule under the MaterialX module. 
# 
# The name of each submodule is of the form:
# ```
#    PyMaterialXGen<target>
# ``` 
# where target is the code generation target written in camel-case. 
# 
# All target names start with `gen` and then the shading language name:
# ```
#    gen<target>
# ``` 
# 
# For example the target for the OSL shading language is `genosl`, with the submodule's target string being `GenOsl`.
# The variants for GLSL include: `genglsl` and `genessl`, with single submodule with target string `GenGlsl`.
# 
# Each sub-module is roughly equivalent to a library (dynamic or static) for the C++ distribution which has the name:
# ```
#    MaterialXGen<target>
# ```
# That is with the `Py` prefix
# 
# The submodule `PyMaterialxShader` contains the base support for all code generators.
# 
# In the code below the submodule is imported in addition to  all generators which are part of the core distribution of MaterialX.

# %%
import sys, os, subprocess
import MaterialX as mx
import MaterialX.PyMaterialXGenShader as mx_gen_shader
import MaterialX.PyMaterialXGenGlsl as mx_gen_glsl
import MaterialX.PyMaterialXGenOsl as mx_gen_osl
import MaterialX.PyMaterialXGenMdl as mx_gen_mdl


# %% [markdown]
# ## Setup
# 
# The basic setup requires that a document is created, the standard libraries are loaded, and the document containing the elements to generate code for to be present.
# 
# Additional modules can be imported to support such as shader validation.
# 
# ### Code Validation
# 
# For `GLSL`, `ESSL`, and `Vulkan` languages <a href="https://github.com/KhronosGroup/glslang" target="_blank">glslangValidator</a> 
# can be used for syntax and compilation validation. It is installed using `vcpkg` and run as part of the CI process. For OSL and MDL: `olsc` and `mdlc` are used respectively.
# 
# The `generateshader.py` script supports passing in a external program argument which can be executed against the produced source code. 
# It runs the program with the source code as input and returns whether the program is 'valid'.
# 
# The utility function from that script has been extracted out and is included below.

# %%

def validateCode(sourceCodeFile, codevalidator, codevalidatorArgs):
    if codevalidator:
        cmd = codevalidator + ' ' + sourceCodeFile 
        if codevalidatorArgs:
            cmd += ' ' + codevalidatorArgs
        print('----- Run Validator: '+ cmd)
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            result = output.decode(encoding='utf-8')
        except subprocess.CalledProcessError as out:                                                                                                   
            return (out.output.decode(encoding='utf-8'))
    return ""


# %% [markdown]
# ### Exception Handling
# 
# In the following code, a MaterialX file which defines a "marble" material is loaded.
# As mentioned a document is created and the file loaded in.
# 
# MaterialX throws exceptions when encountering errors instead of keeping track of status code.
# There are some specific exceptions which provide additional information beyond the regular exception information.
# 
# This includes custom exceptions for file I/O,  code generation and rendering. 
# It is always prudent to catch exceptions and especially so for these usage areas.
# In this example a "file missing" exception may be returned if the file cannot be read.
# See the possible `Exception` types as defined <a href="https://materialx.org/docs/api/class_exception.html" target="_blank">in the API
# documentation</a>. In Python, the exception name is the same as the C++ class name.

# %%
# Read in MaterialX file
#
inputFilename = 'standard_surface_marble_solid.mtlx'
doc = mx.createDocument()
try:
    mx.readFromXmlFile(doc, inputFilename)    
    
    valid, msg = doc.validate()
    if not valid:
        raise mx.Exception('Document is invalid')

    print('Read in valid file "'"%s"'" for code generation.' % inputFilename)

except mx.ExceptionMissing as err:
    print('File %s could not be loaded: "' % inputFilename, err, '"')
except mx.Exception as err:
    print('File %s fail to load properly: "' % inputFilename, err, '"')


# %% [markdown]
# ### Implementations
# 
# The standard library includes both definitions as well as implementations for each shading language. 
# The `stdlib`, `stdlib`, and 'bxdf' folders contain definitions and any corresponding node graph implementations.
# These are shading language agnostic. The sub-folders starting with `gen` contain source code implementations.
# <pre>
# ├───bxdf
# │   ├───lama
# │   └───translation
# ├───lights
# │   └───genglsl
# ├───pbrlib
# │   ├───genglsl  <-- e.g. target 'genglsl's implementations can be found here
# │   ├───genmdl
# │   └───genosl
# ├───stdlib
# │   ├───genglsl
# │   ├───genmdl
# │   └───genosl
# └───targets
# </pre>
# 
# Without these, no code generation can occur, thus the `libraries` folder found at the root of the
# MaterialX distribution (or within the search path) must always be read in. Additional libraries can be loaded as required.
# 
# Implementations are of the type <a href="https://materialx.org/docs/api/class_implementation.html" target="_blank">`Implementation`</a>.

# %%
# Load in standard libraries
stdlib = mx.createDocument()
searchPath = mx.FileSearchPath(os.path.dirname(inputFilename))
libraryFolders = []
libraryFolders.append("libraries")
try:
    mx.loadLibraries(libraryFolders, searchPath, stdlib)
    doc.importLibrary(stdlib)
    print('Standard library definitions and implementations loaded.')
except err:
    print('Standard library definitions and implementation failed to load: "', err, '"')
    sys.exit(-1)


# %% [markdown]
# 
# There are many implementations as code for all supported shading languages implementations is read in. 
# 
# The `getImplementations()` API is used to get a list of `Implementation` references.

# %%
implmentations = doc.getImplementations()
if implmentations:
    print('Read in %d implementations' % len(implmentations))    

# %% [markdown]
# ## Implementation "Targets"
# 
# Every non-nodegraph implementation must specify a `target` that it supports. 
# 
# A `target` name is used to identify shading languages and their variants. The naming convention is:
# ```
#   gen<language name>
# ```
# These are represented as a <a href="https://materialx.org/docs/api/class_target_def.html" target="_blank">`TargetDef`</a>. 
# The target identifiers are loaded in as part of the standard library, and these can be queried by
# looking for elements of category `targetdef`. For convenience, a list of available targets can be retrieved from a 
# document using the `getTargetDefs()` API.
# 
# However, at time of writing, this is missing from the Python API. Thus a simple utility function is provided here.

# %%
# The targetdef type and support API does not currently exist so cannot be used.
#doc.getTargetDefs()
#doc.getChildOfType(mx.TargetDef)

# Utility that basically does what doc.getTargetDefs() does.
# Matching the category can be used in lieu to testing for the class type.
def getTargetDefs(doc):
    targets = []
    for element in doc.getChildren():
        if element.getCategory() == 'targetdef':
            targets.append(element.getName())
    return targets

foundTargets = getTargetDefs(doc)
for target in foundTargets:
    print('Found target identifier:', target)

# %% [markdown]
# ## Code Generators
# 
# ### Generator Creation
# 
# Every code generator must have a `target` identifier to indicate which shading langauge / variant it supports.
# A language version can be used to distinguish a variant if appropriate (e.g. ESSL is distinguishable this way)
# 
# It is recommended that any new generators be unique. 
# 
# Currently there is no "registry" for generators by target so the user must know before hand which generators exist and
# go through all generators to find one with the appropriate `target` to use.
# 
# Targets themselves can be "inherited" which is reflected in the inheritance hierarcht for generators.
# For example the `essl` (ESSL) target inherits from the `genglsl` (GLSL) target as does the corresponding generators. 
# Inheritance is generally used to specialize code generation to handle shading language variations. 
# 
# For a list of generators and their derivations see documentation for the base class <a href="https://materialx.org/docs/api/class_shader_generator.html" target="_blank">ShaderGenerator<a>
# 
# <img src="../documents/images/ShaderGenerator_inheritance.png" style="width:50%"></img>

# %% [markdown]
# Note that Vulkan has the same target as `genglsl`, but has it's own generator.
# 
# Integrations are free to create custom generators. Some notable existing generators include those used to support USD HDStorm, VEX, and Arnold OSL.
# 
# Any such generator can be instantiated and use the same generation process as described here.
# 
# For this example, we will show how all the the generators can be created, but will choose to only produce GLSL code via an `GlslShaderGenerator` generator. This can be found in the `PyMaterialXGenGlsl` Python submodule and corresponding `MaterialXGenGlsl` library in C++.  

# %%

# Create all generators
generators = []
generators.append(mx_gen_osl.OslShaderGenerator.create())
generators.append(mx_gen_mdl.MdlShaderGenerator.create())
generators.append(mx_gen_glsl.EsslShaderGenerator.create())
generators.append(mx_gen_glsl.VkShaderGenerator.create())

# Create a dictionary based on target identifier
generatordict = {}
for gen in generators:
    generatordict[gen.getTarget()] = gen

# Choose generator to use based on target identifier
language = 'glsl'
target = 'genglsl'
if language == 'osl':
    target = 'genosl'
elif language == 'mdl':
    target = 'genmdl'
elif language == 'essl':
    target = 'essl'
elif language in ['essl', 'glsl', 'vulkan']:
    target = 'genglsl'

test_language = 'essl'
test_shadergen = generatordict[test_language]
print('Find code generator for target:', test_shadergen.getTarget(), ' for language: ', test_language, ". Version: ", test_shadergen.getVersion())

shadergen = generatordict[target]
print('Use code generator for target:', shadergen.getTarget(), ' for language: ', language)

# %% [markdown]
# ### Generator Contexts
# 
# All generators require a "context"to be provided. This is represented bya 
# <a href="https://materialx.org/docs/api/class_gen_context.html" target="_blank">`GenContext`</a> structure. 
# 
# At a minimum a path to where the source code implementations must be provided as part of the context.
# Any number of paths can be added using the `registerSourceCodeSearchPath()` function. Searching will occur in first to last added order.
# Here the path to the `libraries` folder can be used so that source code for standard libraries can be found.

# %%
        
# Create a context for a generator
context = mx_gen_shader.GenContext(shadergen)

# Register a path to where implmentations can be found.
context.registerSourceCodeSearchPath(searchPath)


# %% [markdown]
# ### Color Management
# 
# Color management is used to ensure that input colors are interpreted properly.
# When specified additional logic will be emitted into the shader source code via a "color management system".
# 
# For color management it is necessary t0 indicate for which shading language
# `target` the color management system. Naturally specifying a non-matching target will inject incompatible code.
# 
# The basic steps are to:
# 1. Create the system. In this case the "default" system is created with the `target` being specified at creation time.
# A color management system is derived from the base API interface <a href="https://materialx.org/docs/api/class_color_management_system.html" target="_blank">`ColorManagementSystem`</a>). 
# 2. Setting where the library of definitions exists for the system. In this case the main document is specified.
# 3. Setting the color management system on the generator. If it is not set or cleared then no color management will occur.

# %%
cms = mx_gen_shader.DefaultColorManagementSystem.create(shadergen.getTarget())  
cms.loadLibrary(doc)
shadergen.setColorManagementSystem(cms)

cms = shadergen.getColorManagementSystem()
if cms:
    print('Set up CMS:', cms.getName())


# %% [markdown]
# ### Real World Units
# 
# To handle real-world unit specifiers a "unit system" should be instantiated and associated with the generator.
# The API interface is a <a href="https://materialx.org/docs/api/class_unit_system.html" target="_blank">UnitSystem</a> which definitions. 
# 
# By default a unit system does not know how to perform any conversions. This is provided by a 
# <a href="https://materialx.org/docs/api/class_unit_converter_registry.html" target="_blank">`UnitConverterRegistry`</a> which
# contains a list of convertor. Currently MaterialX supports convertors for converting linear units: distance, and angle.
# The corresponding API interface is <a href="https://materialx.org/docs/api/class_linear_unit_converter.html" target="_blank">`LinearUnitConverter`</a>.
# 

# %%

registry = mx.UnitConverterRegistry.create()
if registry:
    distanceTypeDef = doc.getUnitTypeDef('distance')
    if distanceTypeDef:
        registry.addUnitConverter(distanceTypeDef, mx.LinearUnitConverter.create(distanceTypeDef))
    angleTypeDef = doc.getUnitTypeDef('angle')
    if angleTypeDef:
        registry.addUnitConverter(angleTypeDef, mx.LinearUnitConverter.create(angleTypeDef))
    print('Created unit converter registry')

# %% [markdown]
# As with a color management system the implementations need to be set in addition to setting the registry. 
# The unit system can then be set on the generator.

# %%
unitsystem = mx_gen_shader.UnitSystem.create(shadergen.getTarget())
unitsystem.loadLibrary(stdlib)
unitsystem.setUnitConverterRegistry(registry)

if unitsystem:
    print('Set unit system on code')
    shadergen.setUnitSystem(unitsystem)


# %% [markdown]
# This sets up how to perform unit conversions, but does not specify to which unit the values should convert to.
# For this access is needed to the "options" for the context which are stored in a <a href="https://materialx.org/docs/api/class_gen_options.html"  target="_blank">GenOptions</a> structure on the context.

# %%
# Set the target unit to be meter.
genoptions = context.getOptions()
genoptions.targetDistanceUnit = 'meter'

# %% [markdown]
# ## Finding Elements to Render
# 
# There are a few utilities which are included to find elements which are "renderable":
# 
# 1. The <a href="https://materialx.org/docs/api/_material_x_gen_shader_2_util_8h.html" target="_blank">findRenderableElement()</a> utility can be used in general to find these. 
# 2. Another possible utility is to find only material nodes using `getMaterialNodes()` or 
# 2. Shader nodes by looking for nodes of type `SURFACE_SHADER_TYPE_STRING` in a document.
# 
# For this example, the first "renderable" found is used.
# 
# 

# %%

# Look for renderable nodes
nodes = mx_gen_shader.findRenderableElements(doc, False)
print('Found: %d renderables' % len(nodes))
if not nodes:
    nodes = doc.getMaterialNodes()
    if not nodes:
        nodes = doc.getNodesOfType(mx.SURFACE_SHADER_TYPE_STRING)

node = None 
if nodes:
    node = nodes[0]
    print('Found node to render: ', node.getName())


# %% [markdown]
# ## Generating Code
# 
# After all of this setup, code can be generated.
# 1. First a valid name is generated using `createValidName` to ensure that the shader name produced is valid. 
# 2. Then the generator's <a href="https://materialx.org/docs/api/class_shader_generator.html" target="_blank">generate()</a> interface is called with this name, the node, and the generation context. Note that derived classes will override this interface to perform custom generation.
# 
# Upon success a new <a href="https://materialx.org/docs/api/class_shader.html", target="_blank">Shader</a> instance is created. Note that this is a special interface used to keep track of an entire shader. This instance can be inspected to extract information required for rendering.

# %%
shader = None
nodeName = node.getName() if node else ''
if nodeName:
    shaderName = mx.createValidName(nodeName)
    try:
        shader = shadergen.generate(shaderName, node, context)
    except err:
        print('Shader generation errors:', err)

if shader:
    print('Succeeded in generating code for shader "%s" code from node "%s"' % (shaderName, nodeName)) 
else:
    print('Failed to generate code for shader "%s" code from node "%s"' % (shaderName, nodeName)) 

# %% [markdown]
# ### Generated Code
# 
# For hardware languages like GLSL, currently vertex, and pixel shader code is generated.
# To complete this example the pixel shader code generated is examined.
# 
# All code is available via the <a href="https://materialx.org/docs/api/class_shader.html" target="_blank">getSourceCode()</a>
# with a argument as to which code to return. This code can be directly compiled and used for a renderer.
# 
# It is at this point in the `generateshader.py` that validation is performed. 

# %%
        

pixelSource = ''
vertexSource = ''
if shader:
    errors = ''

    # Use extension of .vert and .frag as it's type is
    # recognized by glslangValidator
    if language in ['glsl', 'essl', 'vulkan']:
        vertexSource = shader.getSourceCode(mx_gen_shader.VERTEX_STAGE)
        f = open('vertexSource.' + target, 'w')        
        print(vertexSource, file=f)
        f.close()

    pixelSource = shader.getSourceCode(mx_gen_shader.PIXEL_STAGE)
    f = open('pixelSource.' + target, 'w')        
    print(pixelSource, file=f)
    f.close()


# %% [markdown]
# **Pixel Source Code**
# <iframe src="pixelSource.genglsl" title="ShaderGen Notebook" width="80%" height="800"></iframe>
# 


