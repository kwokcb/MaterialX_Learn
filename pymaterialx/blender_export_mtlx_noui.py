# %% [markdown]
# ## Blender and MaterialX
# 
# In this notebook, we take a look at MaterialX export from an application -- in this case Blender.
# The key items covered are:
# * Discovery of MaterialX package and version within an application.
# * Current bespoke conversion via code in lieu of any data driven option.
# * Recording the on-going progression of MaterialX integration into Blender as 3.5 is the first default inclusion of MaterialX. That is, this notebook will be updated as new versions of Blender come out with enhanced MaterialX support. This will include how to use  custom MaterialX libraries for Blender nodes when available. *See the Libraries / Definitions notebook on current library integrations*
# 
# The Python MaterialX module which is available as part of the distribution  as of `Blender 3.5`. 
# This can be found roughly here relative to the install location:
# ```
#   <install location>/Blender Foundation/Blender 3.5/3.5/python/lib/site-packages/MaterialX
# ```
# 
# The logic presented shows how usage of custom nodes can be converted back to a "standard" shader node representation (in this case MaterialX but USD could be another target). Native applications nodes such as found in Blender are not considered "standard". Naturally the long term ideal is that a MaterialX nodes are natively represented in an application like Blender in 
# which case something like an export / import process is "trivial".
# 
# The notebook thus shows the "fragility" of logic built on top of node and value types on one end, but it 
# does reuse of MaterialX node graph utilities in `mxutils/mxnodegraph` (See the 
# <a href="mtlx_graphs_notebook.html" target="_blank">Nodegraph</a> notebook)
# 
# Plug-ins such as `AMD's ProRender` plug-in which includes native MaterialX nodes is a full integration with 
# complete exporter code that can found <a href="https://github.com/GPUOpen-LibrariesAndSDKs/BlenderUSDHydraAddon" target="_blank">here</a>. 
# 
# The logic found here is however detached from any particular plug-in so can also be used as "starter code" if desired.
# 
# The code can be run from within Blender itself or standalone if the user installs the <a href="https://pypi.org/project/bpy" target="_blank">Blender Python package</a> 
# 
# > Note that:
# > * The minimal Python version is 3.10. This is built with Blender which is in progress but is not currently a Python version which is built as part of the MaterialX Release distribution.
# > * The MaterialX version is 1.38.6 at time of writing.  
# 
# As MaterialX support in Blender is in progress, so the only workflow
# that will be shown is to target the existing `Principal Material` as
# export to `UsePreviewSurface` to avoid writing a lot of code targeted at the short term. 
# 
# ### Target: USDPreviewSurface
# ```xml
#  <UsdPreviewSurface name="SR_default" type="surfaceshader">
#     <input name="diffuseColor" type="color3" value="0.18, 0.18, 0.18" />
#     <input name="emissiveColor" type="color3" value="0, 0, 0" />
#     <input name="useSpecularWorkflow" type="integer" value="0" />
#     <input name="specularColor" type="color3" value="0, 0, 0" />
#     <input name="metallic" type="float" value="0" />
#     <input name="roughness" type="float" value="0.5" />
#     <input name="clearcoat" type="float" value="0" />
#     <input name="clearcoatRoughness" type="float" value="0.01" />
#     <input name="opacity" type="float" value="1" />
#     <input name="opacityThreshold" type="float" value="0" />
#     <input name="ior" type="float" value="1.5" />
#     <input name="normal" type="vector3" value="0, 0, 1" />
#     <input name="displacement" type="float" value="0" />
#     <input name="occlusion" type="float" value="1" />
#   </UsdPreviewSurface>
#   ```

# %% [markdown]
# ### Integration Targets
# 
# Code shown here can be executed within Blender itself as shown below.
# 
# <img loading="lazy" src="images/blender_materialx_python_export_final.png" width=60%>
# 
# or within Visual Studio Code.
# 
# <img loading="lazy" src="images/blender_materialx_python_export_vscode_2.png" width=60%>
# 
# With the results available to use for any MaterialX integration such as MaterialXView below.
# <img loading="lazy" src="images/blender_materialXView_final.png" width=60%>
# 

# %% [markdown]
# ## Blender Setup
# 
# The Blender Python package is imported for usage after installation.

# %%
# Import blender package
import bpy

# %% [markdown]
# ## MaterialX Setup
# 
# The basic setup imports the MaterialX package and uses additional utilities introduced in other notebooks
# for node / nodegraph and file handling.
# 

# %%
# Import MaterialX package
import MaterialX as mx

# Version check
from mtlxutils.mxbase import * 
haveVersion1387 = haveVersion(1,38,7)
if not haveVersion1387:
    print("** Warning: Recommended version is 1.38.7 for tutorials. Have version: ", mx.__version__)

# %% [markdown]
# To test for the existence of MaterialX, it is possible to examine the site packages included with Blender.
# Blender versions 3.5 and above includes MaterialX so that package would be found. Otherwise, MaterialX
# needs to be installed as an extra step. As of 1.38.7, the data libraries are included as part of the MaterialX package
# but not be found in Blender 3.5.
# 
# > Note that it is possible to simplify coding for the 3.5 and higher release by copying over the 1.38.6 `libraries` folder from a release into the Blender package location. 
# 
# > Also note that the code is run outside of Blender so will return the package location relative to this notebook.

# %%
# This code needs to be run within Blender to return the appropriate result.

# 1. Find the Blender Python site packages folder 
# When run inside Blender a path like this will be returned by default (on Windows)
# ['C:\\Program Files\\Blender Foundation\\Blender 3.5\\3.5\\python', 
#  'C:\\Program Files\\Blender Foundation\\Blender 3.5\\3.5\\python\\lib\\site-packages'] 
import site, os
packages = site.getsitepackages()

foundPackage = False
librariesRoot = ''
materialXRoot = ''
for package in packages:
    pythonRoot = mx.FilePath(package)

    # 2. Find the location of the MaterialX package
    materialXRoot = pythonRoot / mx.FilePath('MaterialX') 

    if os.path.exists(materialXRoot.asString()):
        foundPackage = True
        librariesRoot = materialXRoot / "libraries"
        if not os.path.exists(librariesRoot.asString()):
            librariesRoot = ''
        break

if foundPackage:
    print('MaterialX package location:', materialXRoot.asString())
    if librariesRoot:
        print('Default data libraries found at:', librariesRoot.asString())
    else:
        print('Default data libraries are not part of the MaterialX package.')
else:
    print('MaterialX package not found')        

# %% [markdown]
#   
# 
# An additional utility is added to write the output to file and Markdown display.

# %%
# Import graph and file utiities
from mtlxutils.mxnodegraph import MtlxNodeGraph as mxg
from mtlxutils.mxfile import MtlxFile as mxf

# For Markdown output display
from IPython.display import display_markdown

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
        writeOptions.elementPredicate = mxf.skipLibraryElement

    if markdown_title:
        documentContents = mx.writeToXmlString(doc, writeOptions)
        display_markdown(markdown_title, raw=True)
        display_markdown('```xml\n' + documentContents + '\n```\n', raw=True)
    
    if filePath:
        mx.writeToXmlFile(doc, filePath, writeOptions)

# %% [markdown]
# ## Blender to MaterialX Conversion Utilities 
# 
# A series of bespoke utilities have been written to handle Blender based on the current version (3.5) used.

# %% [markdown]
# ### Blender Value to MaterialX Node Input
# 
# * `blender_createMtlxInput()` : Handles creating an named input port on given shader node given the Blender value. 
#    * There is no explicit runtime type identification (`RTTI`) thus type is derived based MaterialX definition port type, and Python type. 
#    * Blender vector type length is sanity checked and clamped against MaterialX vector types. 
#    * Blender floats are replicated if the MaterialX port is a vector. 
# * `floatToStr()` is a simple utility to format string output for floats with fixed precision

# %%
def floatToStr(val):
    """ 
    Emit formatted float value to string
    """
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
            valueString = floatToStr(blenderVal)  
        else:
            blenderValString = []
            for i in range(0,valueLength):
                blenderValString.append(floatToStr(blenderVal))
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
                    blenderValString.append(floatToStr(blenderVal[i]))
            valueString = ','.join(blenderValString)

    if len(valueString):        
        newInput = node.addInput(portName, portType)
        if newInput:
            newInput.setValueString(valueString) 
    
    return newInput

# %% [markdown]
# ### Mapping of Blender Nodes / Inputs to MaterialX
# 
# * `blender_init_node_dictionary()` is used to create a dictionary (mapping) from specific Blender nodes to MaterialX nodes. There appears to be no schema to define Blender nodes so hard-coded port names use for port mapping.
# * `blender_createMtlxShaderNode()`is used to create a MaterialX shader node from a Blender shader node. As a Blender Material maps to a MaterialX shader, we create two nodes when a material is encountered. A proper mapping of `Blender Material Output` nodes is not performed here as these best match a MaterialX material node.

# %%

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

    mtlxShadername = name + ('_' + 'Shader' if isMaterial else '')
    mtlxShaderNode = mxg.addNode(doc, shaderNodeDefinition, mtlxShadername)
    if not mtlxShaderNode:
        return None

    # Create MaterialX material and shader for each Blender material
    if isMaterial:
        mtlxMaterialNode = mxg.addNode(doc, 'ND_surfacematerial', name)
        if mtlxMaterialNode:
            # Connect the material node to the output of the graph
            mxg.connectNodeToNode(mtlxMaterialNode, 'surfaceshader', mtlxShaderNode, '')          

    return mtlxShaderNode

# %% [markdown]
# ## Main Blender to MaterialX Converter
# 
# The main logic finds all root material nodes and converts that node and any directly connected upstream Blender `Texture Image` node, or `Normal Map` node. This is not in any way meant to be a full graph traverser, but there should be sufficient base logic to be able to create such a traverser. 

# %%
def blender_connectImageNode(doc, SHADER_NODE_map, mtlxInput, blenderNode):
    nodeDefinition = SHADER_NODE_map['TEX_IMAGE']
    nodeDefinition = nodeDefinition + mtlxInput.getType() 
    mtxImageNode = blender_createMtlxShaderNode(doc, blenderNode.label, nodeDefinition, False)

    # Connect input to new node
    if mtxImageNode:
        imagePath = ''
        if blenderNode.image:
            imagePath = blenderNode.image.filepath_from_user() 
        fileInput = mtxImageNode.addInput('file', 'filename')
        fileInput.setValueString(imagePath)
        mxg.connectNodeToNode(mtlxInput.getParent(), mtlxInput.getName(), mtxImageNode, '')
    
    return mtxImageNode

def blender_connectNormalMapNode(doc, SHADER_NODE_map, mtlxInput, blenderNode):
    """ 
    Create a MaterialX normal map node from a Blender node
    Connected the new node to an downstream input 
    """
    nodeDefinition = SHADER_NODE_map['NORMAL_MAP']
    mtxNormalMap = blender_createMtlxShaderNode(doc, blenderNode.label, nodeDefinition, False) 
    mxg.connectNodeToNode(mtlxInput.getParent(), mtlxInput.getName(), mtxNormalMap, '')                               
    return mtxNormalMap

def blender_getUpstreamNode(blenderInput):
    if not blenderInput:
        return None
    link = blenderInput.links[0] if blenderInput.links else None
    if link and link.is_valid:
        return link.from_node
    return None

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
            # Creat a corresponding MaterialX material / shader node
            shaderNodeDefinition = SHADER_NODE_map[shaderType]
            if not shaderNodeDefinition:
                print('Skip handling of node', materialNode)
                continue

            mtlxShaderNode = blender_createMtlxShaderNode(doc, m.name, shaderNodeDefinition, shaderType == 'BSDF_PRINCIPLED')
            if not mtlxShaderNode:
                continue
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
                    newInput = blender_createMtlxInput(portName, val, mtlxShaderNode, mtlxShaderNodeDef)                         
                    if portName == 'normal':
                        newInput.setValueString('0,0,1') 

                # Check for upstream connections
                if not newInput:
                    continue

                connectedNode = blender_getUpstreamNode(ninput)
                if connectedNode:
                    mtxNormalMap = None
                    # Add a MaterialX normal map node for each Blender normal map node
                    if connectedNode.type == 'NORMAL_MAP':                                
                        mtxNormalMap = blender_connectNormalMapNode(doc, SHADER_NODE_map, newInput, connectedNode)
                        # Traverse upstream
                        colorInput = connectedNode.inputs['Color']
                        if colorInput:
                            connectedNode = blender_getUpstreamNode(colorInput)

                    # Add an MaterialX image node for each Blender texture image node
                    mtxImageNode = None
                    if connectedNode.type == 'TEX_IMAGE':                                
                        mtxImageNode = blender_connectImageNode(doc, SHADER_NODE_map, newInput, connectedNode)

                    # Connect normal map and image node if both found
                    if mtxNormalMap and mtxImageNode:
                        mxg.connectNodeToNode(mtxNormalMap, 'normal', mtxImageNode, '')                        

# %%
if __name__ == "__main__":
    bpy.ops.wm.open_mainfile(filepath="data/test.blend")
    doc, libFiles, status = mxf.createWorkingDocument()
    shaderNodeMap = blender_init_node_dictionary('ND_UsdPreviewSurface_surfaceshader')
    blender_materialx(doc, shaderNodeMap)
    writeMaterialX(doc, 'data/blender_to_mtlx.mtlx', '**Blender To MaterialX Result**')

# %% [markdown]
# ### Diagram of Blender Graph
# Using the Mermaid graph utilities we can visualize the resulting graph:

# %%
from mtlxutils.mxtraversal import *
from mtlxutils.mxfile import *

# Load in document and create a Mermaid graph
doc, libFiles, status = MtlxFile.createWorkingDocument()
mx.readFromXmlFile(doc, 'data/blender_to_mtlx.mtlx')
roots = doc.getMaterialNodes()
graph = MtlxMermaid.generateMermaidGraph(roots, 'LR')

from IPython.display import display_markdown
strgraph = '```mermaid\n'
for line in graph:
    if line:
        strgraph = strgraph + line + '\n'
strgraph = strgraph + '```\n' 
display_markdown(strgraph, raw=True)

# %% [markdown]
# <img loading="lazy" src="images/mermaid_blender_graph.svg" width=80%>


