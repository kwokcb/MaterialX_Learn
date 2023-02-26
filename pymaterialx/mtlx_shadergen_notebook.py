# %% [markdown]
# # Shader Generation
# 
# This book will examine how to set up MaterialX for code generation. This book covers the <a href="https://github.com/AcademySoftwareFoundation/MaterialX/blob/main/python/Scripts/generateshader.py" target="_blank">
# generateshader.py</a> script provided as part of the core distribution.
# 
# Topics covered:
# 1. Shading language 'target's
# 2. Module / library organization
# 3. Setting up generators and generation contexts 
# 5. Real world units and color management 
# 6. Discovering "renderable" items, and generating code
# 7. Extracting source code
# 
# Details behind code generation, generation options, introspection / reflection,
# and input binding is covered as part of rendering.  
# 
# Background on code generation can be found <a href="https://github.com/AcademySoftwareFoundation/MaterialX/blob/main/documents/DeveloperGuide/ShaderGeneration.md" target ="_blank">here.</a>

# %% [markdown]
# ## Code Generation Modules / Libraries
# 
# For the Python distribution, each code generator resides in a separate module in the MaterialX package. 
# 
# The name of each module is of the form:
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
# For example, the target for the OSL shading language is `genosl`, with the module's postfix string being `GenOsl`.
# The variants for GLSL include: `genglsl` and `genessl`, which reside in a single module with postfix string `GenGlsl`.
# 
# The C++ library equivalent to the module is named:
# ```
#    MaterialXGen<target>
# ```
# This is basically the same as the Python module but without the `Py` prefix.
# 
# The module `PyMaterialxShader` contains the base support for all code generators. In the code below this module as well as modules for all targets are imported.

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
# > For the purposes of showing formatted results we use the `IPython` package to be able to output `Markdown` from Python code.

# %%
from IPython.display import display_markdown

# %% [markdown]
# 
# 
# Additional modules can be imported to support functionality such as code validation.
# 
# ### Code Validation
# 
# For `GLSL`, `ESSL`, and `Vulkan` languages <a href="https://github.com/KhronosGroup/glslang" target="_blank">glslangValidator</a>  can be used for syntax and compilation validation. It is installed using `vcpkg` and is run as part of the CI process. For OSL and MDL: `olsc` and `mdlc` compilers are used respectively.
# 
# The `generateshader.py` script supports passing in a external program as an argument. The source code passed to this program for validation.
# 
# The utility function from that script has been extracted out and is included below as an example.

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
# In the following code, a document is first created and then a sample file which defines a "marble" material is read in.
# 
# Note that MaterialX throws exceptions when encountering errors instead of keeping track of status code.
# There are some specific exceptions which provide additional information beyond the regular exception information.
# 
# It is always prudent to catch exceptions including checking of custom exceptions 
# provided for file I/O, code generation and rendering.
# 
# In this example a "file missing" exception may be returned if the file cannot be read.
# 
#  The possible `Exception` types are defined in the <a href="https://materialx.org/docs/api/class_exception.html" target="_blank">API documentation</a>. In Python, the exception name is the same as the C++ class name.

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
# The `stdlib`, `stdlib`, and `bxdf` folders contain definitions and any corresponding node graph and
# source code implementations.
# 
# The sub-folders starting with `gen` contain per-target source code implementations.
# 
# <pre>
# ├───bxdf
# │   ├───lama
# │   └───translation
# ├───lights
# │   └───genglsl
# ├───pbrlib
# │   ├───genglsl  <-- e.g. target 'genglsl's implementations reside here
# │   ├───genmdl
# │   └───genosl
# ├───stdlib
# │   ├───genglsl
# │   ├───genmdl
# │   └───genosl
# └───targets
# </pre>
# 
# As this code is required for code generation to occur,  the standard `libraries` folder must be read in. 
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
# The `getImplementations()` API is used to get a list of `Implementation` references. Even though the total number
# of implementations seem large, only the source code for a specific generator are used at any given time.

# %%
# Get list of all implementations
implmentations = doc.getImplementations()
if implmentations:
    print('Read in %d implementations' % len(implmentations))

# %% [markdown]
# ## Implementation Targets
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
    implcount = 0
    # Find out how many implementations we have 
    for impl in implmentations:
        testtarget = target
        if target == 'essl':
            testtarget = 'genglsl'
        if impl.getTarget() == testtarget:
            implcount = implcount + 1
    print('Found target identifier:', target, 'with', implcount, 'source implementations.')      

# %% [markdown]
# ## Code Generators
# 
# ### Generator Creation
# 
# Every code generator must have a `target` identifier to indicate which shading langauge / variant it supports.
# A language version can be used to distinguish a variant if appropriate (e.g. ESSL is distinguishable this way)
# 
# It is recommended that all new generators have a unique target name. 
# 
# Currently there is no "registry" for generators by target so the user must know before hand which generators exist and
# go through all generators to find one with the appropriate `target` to use.
# 
# Targets themselves can be "inherited" which is reflected in the inheritance hierarchy for generators.
# For example the `essl` (ESSL) target inherits from the `genglsl` (GLSL) target as does the corresponding generators. 
# Inheritance is generally used to specialize code generation to handle shading language variations. 
# 
# For a list of generators and their derivations see documentation for the base class <a href="https://materialx.org/docs/api/class_shader_generator.html" target="_blank">ShaderGenerator</a>
# 
# <img src="https://kwokcb.github.io/MaterialX_Learn/documents/images/ShaderGenerator_inheritance.png" style="width:50%"></img>
# 
# Note that Vulkan has the same target as `genglsl`, but has it's own generator.
# 
# Integrations are free to create custom generators. Some notable existing generators include those used to support USD HDStorm, VEX, and Arnold OSL.
# 
# Any such generator can be instantiated and use the same generation process as described here.
# 
# For this example, we will show how all the the generators can be created, but will only produce OSL code via an `OslShaderGenerator` generator. This can be found in the `PyMaterialXGenOsl` Python submodule and corresponding `MaterialXGenOsl` library in C++.  

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
language = 'mdl'
target = 'genosl'
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
print('Find code generator for target:', test_shadergen.getTarget(), ' for language:', test_language, ". Version:", test_shadergen.getVersion())

shadergen = generatordict[target]
print('Use code generator for target:', shadergen.getTarget(), ' for language: ', language)

# %% [markdown]
# ### Generator Contexts
# 
# A "generation context" is required to be created for each generator instance. This is represented by a 
# <a href="https://materialx.org/docs/api/class_gen_context.html" target="_blank">`GenContext`</a> structure. 
# 
# This context provides a number of settings and options to be used for code generation. 
# 
# For simplicity, we will only point out the minimal requirements. This includes providing a search path to where source code implementations can be found. Any number of paths can be added using the `registerSourceCodeSearchPath()` function, on the context. The search order is first to last path added.
# 
# Adding the path to the `libraries` folder is sufficient to find the source code for standard library definitions found in sub-folders. If the user has custom definitions in other locations, the root of those locations should be added. 

# %%
 # Create a context for a generator
context = mx_gen_shader.GenContext(shadergen)

# Register a path to where implmentations can be found.
context.registerSourceCodeSearchPath(searchPath)


# %% [markdown]
# ### Color Management
# 
# Color management is used to ensure that input colors are interpreted properly via shader code.
# 
# A "color management system" cab be created and specified to be used by a shader generator. 
# During code generation, additional logic is emitted into the shader source code via the system.
# 
# Usage of such as system during code generation is optional, as some renderers perform color management on input values
# and images before binding them to shading code.
# 
# Color management systems need to be derived from the base API interface <a href="https://materialx.org/docs/api/class_color_management_system.html" target="_blank">`ColorManagementSystem`</a>). A "default" system is provided
# as part of the MaterialX distribution.
# 
# It is necessary to indicate which `target` shading language code when instantiating the color management system. Naturally specifying a non-matching target will inject incompatible code.
# 
# The setup steps are:
# 
# 1. Create the system. In this example the "default" system is created with the `target` being specified at creation time.
# 2. Setting where the library of definitions exists for the system. In this case the main document which contains the standard library is specified.
# 3. Setting the color management system on the generator. If it is not set or cleared then no color management will occur during code generation.

# %%
# Create default CMS
cms = mx_gen_shader.DefaultColorManagementSystem.create(shadergen.getTarget())  
# Indicate to the CMS where definitions can be found
cms.loadLibrary(doc)
# Indicate to the code generator to use this CMS
shadergen.setColorManagementSystem(cms)

cms = shadergen.getColorManagementSystem()
if cms:
    print('Set up CMS: %s for target: %s' 
          % (cms.getName(), shadergen.getTarget()))

# %% [markdown]
# ### Real World Units
# 
# To handle real-world unit specifiers a "unit system" should be instantiated and associated with the generator.
# The API interface is a <a href="https://materialx.org/docs/api/class_unit_system.html" target="_blank">UnitSystem</a> which definitions. 
# 
# By default a unit system does not know how to perform any conversions. This is provided by a 
# <a href="https://materialx.org/docs/api/class_unit_converter_registry.html" target="_blank">`UnitConverterRegistry`</a> which contains a list of convertors. 
# 
# Currently MaterialX supports convertors for converting linear units: distance, and angle.
# The corresponding API interface is <a href="https://materialx.org/docs/api/class_linear_unit_converter.html" target="_blank">`LinearUnitConverter`</a>.
# 

# %%
# Create unit registry
registry = mx.UnitConverterRegistry.create()
if registry:
    # Get distance and angle unit type definitions and create a linear converter for each
    distanceTypeDef = doc.getUnitTypeDef('distance')
    if distanceTypeDef:
        registry.addUnitConverter(distanceTypeDef, mx.LinearUnitConverter.create(distanceTypeDef))
    angleTypeDef = doc.getUnitTypeDef('angle')
    if angleTypeDef:
        registry.addUnitConverter(angleTypeDef, mx.LinearUnitConverter.create(angleTypeDef))
    print('Created unit converter registry')

# %% [markdown]
# As with a color management system the location of implementations and the registry need to be set on a unit system. 
# The unit system can then be set on the generator.

# %%
# Create unit system, set where definitions come from, and
# set up what registry to use
unitsystem = mx_gen_shader.UnitSystem.create(shadergen.getTarget())
unitsystem.loadLibrary(stdlib)
unitsystem.setUnitConverterRegistry(registry)

if unitsystem:
    print('Set unit system on code generator')
    shadergen.setUnitSystem(unitsystem)


# %% [markdown]
# This sets up how to perform unit conversions, but does not specify what unis the scene geometry is using.
# This can be specified as in an "options" structure found on the  context.
# 
# The API interface is: <a href="https://materialx.org/docs/api/class_gen_options.html"  target="_blank">GenOptions</a>.

# %%
# Set the target scene unit to be `meter` on the context options
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
# After all of this setup, code can now be generated.
# 1. First a `createValidName()` utility is called to ensure that the shader name produced is valid. 
# 2. Then the generator's <a href="https://materialx.org/docs/api/class_shader_generator.html" target="_blank">generate()</a> interface is called with this name, the "renderable" element, and the generation context. Note that derived classes override `generate()` to perform custom generation.
# 
# Upon success a new <a href="https://materialx.org/docs/api/class_shader.html" target="_blank">Shader</a> instance is created. Note that this is a special interface used to keep track of an entire shader. This instance can be inspected to extract information required for rendering.

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
# For hardware languages like GLSL, vertex, and pixel shader code is generated. OSL and MDL only produce
# pixel shader code. To complete this example the pixel shader code is queried from the Shader and
# shown below.
# 
# Code can be queried via the <a href="https://materialx.org/docs/api/class_shader.html" target="_blank">getSourceCode()</a> interface with an argument indicating which code to return. The code returned can be directly compiled and used by a renderer.
# 
# It is at this point in the `generateshader.py` script that validation is performed. (This will not be shown here.) 

# %%
pixelSource = ''
vertexSource = ''
if shader:
    errors = ''

    # Use extension of .vert and .frag as it's type is
    # recognized by glslangValidator
    if language in ['glsl', 'essl', 'vulkan']:
        vertexSource = shader.getSourceCode(mx_gen_shader.VERTEX_STAGE)
        display_markdown('### Vertex Source Code' , raw=True)
        display_markdown('------------------', raw=True)
        display_markdown('```ccc {' + vertexSource + '}```', raw=True)

    pixelSource = shader.getSourceCode(mx_gen_shader.PIXEL_STAGE)
    display_markdown('### Pixel Source Code' , raw=True)
    display_markdown('------------------', raw=True)
    display_markdown('```\n' + pixelSource + '\n```', raw=True)



