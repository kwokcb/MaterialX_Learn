# %% [markdown]
# # OpenUSD Tooling for  MaterialX
# 
# ## Introduction
# 
# In this book we will look at general tools to take MaterialX and convert it to USD.
# Namely we are interested in `UsdMtlx` and utilities from the `Usd Toolset`. Note that `usdview` is also a useful basic tool for inspecting and visualizing USD files. 
# 
# At time of writing the the Python package for Usd from PyPi does not include these tools.
# 
# While it is possible to download the repository and build it yourself, using prebuilt binaries is less trouble. For instance NVIDIA has pre-built binaries for Linux and Windows available <a href="https://developer.nvidia.com/usd" target="_blank">here</a> 
# ( A download of one of these binaries is used for this notebook. If you are working with a specific build for an integration such as a DCC such as Maya or Houdini, that can be used instead. )
# 
# For these builds, ensure that the correct Python and library paths are set up. See <a href="https://openusd.org/release/tut_usd_tutorials.html" target="_blank">the USD tutorials</a> for more information. Instead of setting the `PYTHONPATH` it is possible to install the Python libraries in your Python (virtual) environment.

# %%
import os

# Print path reference which should include the Python path of the USD build
print('PYTHON PATH :', '"' + os.getenv('PYTHONPATH') + '"')

# %% [markdown]
# ### Setup OpenUSD and MaterialX
# 
# In the code below we import both the MaterialX and Usd core library

# %%
from pxr import Usd
import MaterialX as mx

# For Markdown output display
from IPython.display import display_markdown

major, minor, build = Usd.GetVersion() 
print('Using Usd Version:', str(major) + "." + str(minor) + "." + str(build))
print('Using MaterialX Version:', mx.getVersionString())


# %% [markdown]
# For the purposes of examining the output, we add a couple of utility functions to print file directly or as XML.

# %%
def printFileRaw(file):
    f = open(file, 'r')
    print(f.read())
    f.close()

def printFileAsXML(file, title, fmt):
    f = open(file, 'r')
    text = '<details><summary>' + title + '</summary>\n\n' + '```' + fmt + '\n' + f.read() + '```\n' + '</details>\n' 
    display_markdown(text , raw=True)            
    f.close()

# %% [markdown]
# ### Checking Shader Registry for MaterialX Nodes
# 
# Next we want to check that the node definitions for MaterialX are registered in the shader definition registry 
# (<a href="https://openusd.org/dev/api/class_sdr_registry.html" target="_blank">Sdr</a>)
# 
# By default USD will not discover the MaterialX definition libraries. It is thus necessary to explicitly specify the path to these libraries. We use the `PXR_PLUGINPATH_NAME` environment variable to do this by setting it to the `libraries` folder of the MaterialX distribution. 
# 
# To test that the path is properly registered `Sdr.Registry().GetSearchURIs()` can be used.
# 
# Another check that can be performed is to find the available node "source types" using `Sdr.Registry().GetAllNodeSourceTypes()`, for which MaterialX is `mtlx`.
# 
# The "convention" used for MaterialX is to prefix node definition identifiers with `ND_`. We can use this to check that the MaterialX nodes are available in the shader registry.

# %%
# Import Sdr module
from pxr import Sdr

# Check that we have MaterialX definitions
usdmtlxPath = os.environ.get('PXR_MTLX_STDLIB_SEARCH_PATHS')
print('Pixar MaterialX Library Path:' + '"' + usdmtlxPath + '"')

sourceTypes = Sdr.Registry().GetAllNodeSourceTypes()
if 'mtlx' in sourceTypes:
    print('Sdr MaterialX source type \"mtlx\" is registered')
else:
    print('Sdr MaterialX source type \"mtlx\" is not registered')

print('Sdr Search Paths:')
for uri in Sdr.Registry().GetSearchURIs():
    print("- \"" + uri + "\"")

# Get the names of definitions in Sdr
documentContents = ''
if Sdr.Registry():
    for node in Sdr.Registry().GetNodeNames():        
        documentContents = documentContents + ('- %s\n' % node)

text = '<details><summary>Shader Registry Nodes</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
display_markdown(text , raw=True)        


# %% [markdown]
# ## Referencing a MaterialX File from within USD
# 
# With MaterialX nodes registered it is possible to specify MaterialX nodes. One simple way to use MaterialX is to reference a MaterialX document from within a USD file. 
# 
# In the example below a basic geometry is created, a MaterialX document is referenced and a material is bound to the geometry.

# %% [markdown]
# ```usd
# #usda 1.0
# (
#     defaultPrim = "mxCapsule"
#     upAxis = "Y"
#     metersPerUnit = 0.01
# )
# 
# def Capsule "mxCapsule" (
#     prepend apiSchemas = ["MaterialBindingAPI"]
# )
# {
#     rel material:binding = </MaterialX/Materials/Marble_3D>
# }
# 
# 
# def Scope "MaterialX" (
#     references = @./gltf_sample_marble.mtlx@</MaterialX>
# )
# {
# }
# ```

# %% [markdown]
# ### "Flattening" The MaterialX Reference
# 
# To see the expanded contents of the reference file, `usdcat` can be used to "flatten" the reference using hte `-f` command option.

# %%
usd_with_materialXRef = './data/gltf_sample_marble_ref.usda'
usd_without_materialxRef = usd_with_materialXRef
usd_without_materialxRef = usd_without_materialxRef.replace('_ref.usda', '_no_ref.usda')
cmd = 'usdcat ' + usd_with_materialXRef + ' -f -o ' + usd_without_materialxRef + '> flatten.log 2>&1'
print('- Run: ' + '"' + cmd + '"')
result = os.system(cmd)
print('  - Flattening status: %s' % ('Success' if result == 0 else 'Failed'))
if result != 0:
    printFileRaw('flatten.log')

printFileAsXML(usd_without_materialxRef, 'Flattened Usd Content', 'usd')

# %% [markdown]
# To test that the file is valid, `usdview` can be used to examine the file as shown below.
# <image src="../documents/images/gltf_sample_ref_flattened_usdview.png" width="800px">

# %% [markdown]
# ### UsdMtlx API

# %% [markdown]
# Another way to load in MaterialX is via the `UsdMtlx` module.
# 
# At time of writing there the exposed API entry points in Python are:
# MaterialX input from file or string: 
#   - `TestFile()`: To import from a MaterialX file.
#   - `TestString()`: To import from a MaterialX string (XML). 
# 
# There are no APIs in this module to export to MaterialX at the current time.
# 
# > Note that a utility function was written to discover the module functions as the test `inspect.isfunction` does not seem to detect detect Boost Python function members. ( Currently `Boost`` is used to expose the C++ API to Python. )

# %%
from pxr import UsdMtlx
import inspect

def is_function(obj):
    if hasattr(obj, "__class__"):
        cl = getattr(obj, '__class__')
        if obj.__class__.__name__ == "builtin_function_or_method":
            return True    
    return False

members = inspect.getmembers(UsdMtlx)

# Filter the members to find Boost functions.
usdMtlx_functions = [member for member in members if is_function(member[1])]

# Print the functions found.
for name, function in usdMtlx_functions:
    print(f"- UsdMtlx function: {name}")


# %% [markdown]
# These utilities are sufficient to perform conversion from MaterialX to a USD stage. 
# 
# The stage can then be modified / saved as desired. 
# 
# In the example below we take the same MaterialX file, load it into a stage and write it to a file. 
# 
# Note that:
# 1. The MaterialX file is is not a referenced. 
# 2. There appears no way to import a MaterialX document into an existing stage. 
# 2. Additional meta data is added which stored the MaterialX documents rendering color space. (At time of writing input color spaces are not supported.)
# 
# To create the equivalent of the USD file above, the appropriate geometry and binding can be added to the stage.

# %%
# Read in a sample MaterialX file into a new stage
stage = UsdMtlx._TestFile('./data/gltf_sample_marble.mtlx')
#colorspace = stage.GetColorSpace()

# Export the stage to disk and also output for display.
exportedUsd = './data/gltf_sample_marble_usdmtlx.usda'
exported = stage.GetRootLayer().Export(exportedUsd)
if exported:
    print('Converted MaterialX to Usd file:', exportedUsd)

stringResult = stage.GetRootLayer().ExportToString()
text = '<details><summary>UsdMtlx Conversion Results</summary>\n\n' + '```usd\n' + stringResult + '```\n' + '</details>\n' 
display_markdown(text , raw=True)



