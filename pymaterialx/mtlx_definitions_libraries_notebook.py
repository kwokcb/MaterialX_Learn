# %% [markdown]
# # Node Definitions and Node Libraries
# 
# This notebook will examine the creation usage definitions found in libraries.
# 
# Aspects covered include:
# 1. Loading in 3rd-party definition libraries.
# 2. 3rd-party exported content (Mtlx / Usd)
# 3. Creating / editing graphs using 3rd-party definitions. 
# 4. 3rd-party definitions implemented with source code
# 
# ### Node Libraries
# 
# * The existing definition is provided as part of the core distribution.
# * For third-party libraries this notebook will examine at two existing libraries for: Maya and Houdini. 
#   | When available the Blender libraries may also be examined.
# 
# The basic data flow examined is shown below:
# 
# <img src="images/houdini_maya_blender_library_usage.png" width="80%">
# 
# Note that regardless of all libraries are in MaterialX form so can be accessed outside of the application integraion.
# 
# ## Core Library Setup

# %%
# MaterialX and MaterialX utilities
import MaterialX as mx
import mtlxutils.mxfile as mxf
from mtlxutils.mxnodegraph import MtlxNodeGraph as mxg
# For markdown display
from IPython.display import display_markdown

# Version check
from mtlxutils.mxbase import *
haveVersion1387 = haveVersion(1, 38, 7) 
if not haveVersion1387:
    print("** Warning: Recommended minimum version is 1.38.7 for tutorials. Have version: ", mx.__version__)

stdlib = mx.createDocument()
searchPath = mx.getDefaultDataSearchPath()
libraryFolders = mx.getDefaultDataLibraryFolders()
try:
    libFiles = mx.loadLibraries(libraryFolders, searchPath, stdlib)
    print('Loaded %s standard library definitions' % len(stdlib.getNodeDefs()))
except mx.Exception as err:
    print('Failed to load standard library definitions: "', err, '"')

doc = mx.createDocument()
doc.importLibrary(stdlib)

# Write predicate
def skipLibraryElement(elem):
    return not elem.hasSourceUri()

# %% [markdown]
# ## 1. Using 3rd-Party Definition Libraries
# 
# ### 1.1 Example: Maya Libraries
# 
# * Comes the MayaUsd plug-in but can also be found on <a href="https://github.com/Autodesk/maya-usd/tree/dev/lib/mayaUsd/render/MaterialXGenOgsXml/libraries" target="_blank">GitHub</a>
# * Core part of Usd distribution and found in `mayausd\USD/libraries`. This come with all shader implementation for core shading languages: MDL, OSL, MSL, GLSL and variants: Vulkan, ESSL. 
# * Additional part found in `mayausd/MayaUSD/libraries`
#   * Maya nodes are encoded as MaterialX nodegraphs so has interchange compatibility. 
#   * However, the distribution appears to only come with GLSL implementations for custom Maya MaterialX nodes. This includes direct lighting, specific colorspace transforms and tangent utilities.
#   * MayaUSD with custom shader generation derived from the GLSL to output to GLSL and DirectX shaders consumable by the Maya hardware shading system. Derived Vulkan, and ESSL generators could also consume these implementations but MSL, OSL and MDL will naturally not be supported.  
# 
# For the most part these libraries can be referenced outside of Maya by providing the appropriate library name and search path to the `importLibraries()` interface. For example a Maya "Blinn" shader code could be created as it's definition exists.
# 
# In the following code we add a search path (to the installed Maya definitions) and a library name (`adsk`) and load
# in the definitions the same wat the "standard" definitions loaded in. We create a new document called `mayalib` for loading.  

# %%
mayalib = mx.createDocument()
# Maya libraries were copied here for demonstration purposes. The actual install location can be used locally.
searchPath = "C:/Users/home/Desktop/Houd_Maya_Libs"
libraryFolders = [ 'maya' ]
try:
    libFiles = mx.loadLibraries(libraryFolders, searchPath, mayalib)
    print('Loaded %s Maya definitions' % len(mayalib.getNodeDefs()))    
except mx.Exception as err:
    print('Failed to load standard library definitions: "', err, '"')

# Import custom definitions into same document
doc.importLibrary(mayalib)


# %% [markdown]
# ### Discovering Custom Definitions
# 
# The definitions can be queried as used to create new instances as desired. In the example one of each node will be created.
# The utility function `addNode()` (found in `mtlxutils`) is used for instance creation. 

# %%
def createLibraryDictionary(lib):
    """
    Utility to examine a library document
    """
    libDict = dict()

    # Create a category indxed dictionary of the available definitions 
    for nodedef in lib.getNodeDefs():
        category = nodedef.getNodeString()
        if category in libDict:            
            libDict[category].append(nodedef.getName())
        else:
            libDict[category] = [nodedef.getName()]
    
    return libDict

def createInstanceFromLibrary(libDict):
    count = 0
    for category in libDict:
        print('- Category[%d]:' % count, category, '')
        for defname in libDict[category]: 
            nodedef = doc.getDescendant(defname)
            #print('  - Definition:', defname, 'type:', nodedef.getType())
            newNode = mxg.addNode(doc, defname, '')
            print('    - Instance:', newNode)
            doc.removeChild(newNode.getName())
        count = count + 1
    
mayalibDict = createLibraryDictionary(mayalib)
if mayalibDict:
    createInstanceFromLibrary(mayalibDict)
else:
    print('No definitions found.')

# %% [markdown]
# ### Creating Graphs Using Custom Nodes
# 
# The following example will create a graph mixing both core as well as custom nodes. Once the definitions are 
# loaded in they can be added and manipulated in the same way as any of the core nodes.

# %%
comment = doc.addChildOfCategory('comment')
comment.setDocString(' Add in a custom Maya Blinn node ')
mayaBlinn = mxg.addNode(doc, 'MayaND_blinn_surfaceshader', 'blinn')
if not mayaBlinn:
    print('Failed to create a instance of the definition: MayaND_blinn_surfaceshader')
else:
    mayaBlinn.addInputsFromNodeDef()

comment = doc.addChildOfCategory('comment')
comment.setDocString(' Add in a custom Maya File Texture node ')
filetexture = mxg.addNode(doc, 'MayaND_fileTexture_color3', 'filetexture')
if not filetexture:
    print('Failed to create a instance of the definition: MayaND_fileTexture_color3')
else:
    filetexture.addInputsFromNodeDef()

writeOptions = mx.XmlWriteOptions()
writeOptions.writeXIncludeEnable = False
writeOptions.elementPredicate = mxf.MtlxFile.skipLibraryElement

if mayaBlinn and filetexture:
    comment = doc.addChildOfCategory('comment')
    comment.setDocString(' Add in a custom standard image node ')     
    imageNode = mxg.addNode(doc, 'ND_tiledimage_color3', 'image')

    # Connect image -> filetexture -> MayaBlinn
    mxg.connectNodeToNode(filetexture, 'inColor', imageNode, '')
    mxg.connectNodeToNode(mayaBlinn, 'color', filetexture, '')

    documentContents = mx.writeToXmlString(doc, writeOptions)

    text = '<details open><summary>Initial Maya MaterialX Document</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
    display_markdown(text , raw=True)

# %% [markdown]
# # Definition and Instance Validation
# 
# It is always worthwhile to run validation (`validate()`) when creating and using definition documents. Note that the function exists at different levels from <a href="https://materialx.org/docs/api/class_document.html" target="_blank">Document</a> down to individual nodes so validation can be selectively performed.
# 
# For instance that validation issues are discovered when creating instances of `filetexture` and `MayaBlinn`. 
# These are minor warnings dealing with lack of initialization of input values. 
# - The issue on `normalCamera` is due to an issue with `validate()` validation recognizing that the definition has a  `defaultgeomprop`.
# - The issue on `colorSpace` is due to an missing default value in Maya node definition.

# %%
valid, error = doc.validate()
if not valid:
    print('Initial document is invalid:\n', '\n '.join(mx.splitString(error,'\n')))
else:
    print('Document is valid')

print('Patch document...')
# Remove the attribute to patch
if mayaBlinn:
    mayaBlinn.removeChild('normalCamera')
if filetexture:
    filetexture.getInput('colorSpace').setValueString('')

valid, error = doc.validate()
if not valid:
    print('Document is invalid: ', error)
else:
    print('Document is valid after patch.')

documentContents = mx.writeToXmlString(doc, writeOptions)
text = '<details open><summary>Patched Maya MaterialX Document</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
display_markdown(text , raw=True)    

# %% [markdown]
# ### Integration with Node Graph Editors
# 
# By including the search path and library names to the MaterialX node editor which comes with the core distribution, graphs can be
# created and edited with this tool.
# 
# The following is a similar nodegraph example but created in the editor.
# 
# <img src="images/MayaBlinn_NodeEditor.png" width="80%">
# 
# ```xml
# <?xml version="1.0"?>
# <materialx version="1.38" colorspace="lin_rec709">
#   <surfacematerial name="MayaBliinChecker" type="material" xpos="14.442029" ypos="-2.456897">
#     <input name="surfaceshader" type="surfaceshader" nodename="MayaBlinn_1" />
#   </surfacematerial>
#   <MayaBlinn name="MayaBlinn_1" type="surfaceshader" xpos="12.239130" ypos="-3.112069">
#     <input name="color" type="color3" nodename="fileTexture_color3" />
#   </MayaBlinn>
#   <fileTexture name="fileTexture_color3" type="color3" xpos="9.014493" ypos="-3.198276">
#     <input name="inColor" type="color3" nodename="image_color3" />
#     <input name="invert" type="boolean" value="true" />
#     <input name="uvCoord" type="vector2" value="0, 0" />
#     <input name="exposure" type="float" value="0" />
#   </fileTexture>
#   <image name="image_color3" type="color3" xpos="6.898551" ypos="-3.163793">
#     <input name="file" type="filename" value="" fileprefix="checker.png" />
#   </image>
# </materialx>
# ```
# ### Conversion Via Usd
# 
# Note that <a href="https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=GUID-5C076445-22FB-4C74-9147-43672BCF88CD" target="_blank">LookdevX</a> is the Maya 2024 native editor for Usd and MaterialX graphs stored as UsdShade.
# It is possible to convert between Usd and MaterialX representations though the process requires
# additional conversion steps in either direction. 
# 
# For example this Usd file from Maya was translated to MaterialX using the logic found in the Usd notebook:
# ```usd
# #usda 1.0
# 
# def Sphere "Sphere1" (
#     prepend apiSchemas = ["MaterialBindingAPI"]
# )
# {
#     uniform bool doubleSided = 0
#     rel material:binding = </mtl/MyMaterial>
# }
# 
# def Scope "mtl"
# {
#     def Material "MyMaterial" (
#         prepend apiSchemas = ["NodeGraphNodeAPI"]
#     )
#     {
#         token outputs:mtlx:surface.connect = </mtl/MyMaterial/MyShader.outputs:out>
#         uniform float2 ui:nodegraph:node:pos = (-1.7199334, -0.5843111)
# 
#         def Shader "MyShader" (
#             prepend apiSchemas = ["NodeGraphNodeAPI"]
#         )
#         {
#             uniform token info:id = "ND_standard_surface_surfaceshader"
#             color3f inputs:base_color.connect = </mtl/MyMaterial/MyGraph.outputs:out>
#             token outputs:out
#             uniform float2 ui:nodegraph:node:pos = (-0.5611111, -0.85555553)
#         }
# 
#         def NodeGraph "MyGraph" (
#             prepend apiSchemas = ["NodeGraphNodeAPI"]
#         )
#         {
#             color3f outputs:out.connect = </mtl/MyMaterial/MyGraph/MyImage.outputs:out>
#             uniform float2 ui:nodegraph:node:pos = (-2.211111, -0.23888889)
# 
#             def Shader "MyImage" (
#                 prepend apiSchemas = ["NodeGraphNodeAPI"]
#             )
#             {
#                 uniform token info:id = "ND_image_color3"
#                 color3f outputs:out
#                 uniform float2 ui:nodegraph:node:pos = (-0.7916667, -0.8055556)
#             }
#         }
#     }
# 
#     def Material "MyMayaMaterial" (
#         prepend apiSchemas = ["NodeGraphNodeAPI"]
#     )
#     {
#         token outputs:mtlx:surface.connect = </mtl/MyMayaMaterial/MayaBlinn1.outputs:outColor>
#         uniform float2 ui:nodegraph:node:pos = (-0.36928108, 0.3856211)
# 
#         def Shader "MayaBlinn1" (
#             prepend apiSchemas = ["NodeGraphNodeAPI"]
#         )
#         {
#             uniform token info:id = "MayaND_blinn_surfaceshader"
#             color3f inputs:color.connect = </mtl/MyMayaMaterial/MyBlinnGraph.outputs:out>
#             token outputs:outColor
#             uniform float2 ui:nodegraph:node:pos = (-0.5888889, -0.7222222)
#         }
# 
#         def NodeGraph "MyBlinnGraph" (
#             prepend apiSchemas = ["NodeGraphNodeAPI"]
#         )
#         {
#             color3f outputs:out.connect = </mtl/MyMayaMaterial/MyBlinnGraph/MyImage2.outputs:out>
#             uniform float2 ui:nodegraph:node:pos = (-2.0555556, 0.17222223)
# 
#             def Shader "MyImage2" (
#                 prepend apiSchemas = ["NodeGraphNodeAPI"]
#             )
#             {
#                 uniform token info:id = "ND_image_color3"
#                 color3f outputs:out
#                 uniform float2 ui:nodegraph:node:pos = (-0.55833334, -0.6111111)
#             }
#         }
#     }
# }
# ```
# Resulting MaterialX file:
# ```xml
# <?xml version="1.0"?>
# <materialx version="1.38">
#   <surfacematerial name="MyMaterial" type="material">
#     <input name="surfaceshader" type="surfaceshader" nodename="MyShader" />
#   </surfacematerial>
#   <standard_surface name="MyShader" type="surfaceshader" nodedef="ND_standard_surface_surfaceshader">
#     <input name="base_color" type="color3" nodegraph="MyGraph" />
#   </standard_surface>
#   <nodegraph name="MyGraph">
#     <output name="out" type="color3" nodename="MyImage" />
#     <image name="MyImage" type="color3" nodedef="ND_image_color3" />
#   </nodegraph>
#   <surfacematerial name="MyMayaMaterial" type="material">
#     <input name="surfaceshader" type="surfaceshader" nodename="MayaBlinn1" />
#   </surfacematerial>
#   <MayaBlinn name="MayaBlinn1" type="surfaceshader" nodedef="MayaND_blinn_surfaceshader">
#     <input name="color" type="color3" nodegraph="MyBlinnGraph" />
#   </MayaBlinn>
#   <nodegraph name="MyBlinnGraph">
#     <output name="out" type="color3" nodename="MyImage2" />
#     <image name="MyImage2" type="color3" nodedef="ND_image_color3" />
#   </nodegraph>
# </materialx>
# ```

# %% [markdown]
# ### Custom Source Code Implementations
# 
# Source code implementations in the Maya library can also be examined by using `getImplementations()` for each shader API target returned from `getTargetDefs()`.
# 
# The general recommendation is to implement definitions using node graphs as
# **any source code implementation** may or may not be portable depending on the level of support for the languages required for a integration. 
# 
# | Note that code generation logic currently relies on source code implementations all color space transforms (at time of writing) -- and these are what show up as supplemental implementations inside the Maya library.
# 
# The hope is that this will migrate to a more portable and OCIO conformant representation in the future. 
# In lieu of this, **it is recommended to propose to the ASWF MaterialX TSC** to add any new color management transforms 
# to the core distribution to have a common reusable implementation.

# %%
# Print out custom source code implementations for each target.
print('Custom implementations:')
targets = stdlib.getTargetDefs()
for target in targets:
    printTarget = True
    for impl in mayalib.getImplementations():
        if impl.getTarget() == target.getName():
            if printTarget:
                print('Target: ', target)
                printTarget = False
            print('-', impl.getName(), ' nodedef:', impl.getNodeDefString())
            print('  File:', impl.getAttribute('file'), 'Function:', impl.getAttribute('function'))
            #print(impl)

# %% [markdown]
# ### 1.2 Example: Houdini Libraries
#   
# The distribution of Houdini examiend (19.5.605): 
# * Comes with core libraries installed.
# * Has a `libraries` folder organization is slightly different by placing some additional definitions in a `houdini` folder under the same parent folder as the "core" libraries. i.e. the `libraries` folder. 
#   * One advantage of this that additional folders do not need to be searched for other than `libraries`, but
#   * The folder area now has intermixed standard and non-standard definitions / implementations so may be hard determine which are Houdini specific.
#  
# #### Loading Libraries
# The same process can be used to load in the custom definitions by pointing to the appropriate folder and setting the search path. Below is an example pointing to a local folder containing the content.
# 
# Note that it is possible to load in a version which is at or newer than the one shipping with Houdini as long as only the custom definition folders are loaded in after the standard libraries.
# 
# This shown in the example below where the additional `houdini` library (which is at 1.38.4) is loaded in independently after the libraries which are part
# of the distribution used for this notebook (which is at 1.38.8). This works as the an upgrade process is performed on load of the `houdini` library.
# There is no "downgrade" process so reading into a version older than 1.38.4 may not work or have compatibility issues.

# %%
houdinilib = mx.createDocument()
# This sample uses the 19.5.605 Houdini libraries for demonstration purposes. The actual install location can be used locally.
searchPath = "C:/Users/home/Desktop/Houd_Maya_Libs"
libraryFolders = [ 'houdini' ]
try:
    libFiles = mx.loadLibraries(libraryFolders, searchPath, houdinilib)
    print('Loaded %s Houdini definitions' % len(houdinilib.getNodeDefs()))    
except mx.Exception as err:
    print('Failed to load Houdini library definitions: "', err, '"')

# Import custom definitions into same document
doc.importLibrary(houdinilib)

# %%
houdiniDict = createLibraryDictionary(houdinilib)
createInstanceFromLibrary(houdiniDict)

# %% [markdown]
# * Library adheres to the "standard" recommendations for node definition naming 
# * Both have UI elements
# * `nodegroup` is set to be `houdini` which makes it harder to classify for code generation, but Houdini does
# not directly use a MaterialX code generator to produce VEX.
# 
# <img src="images/Houdini_Node_Editor.png" width=80%>

# %% [markdown]
# ### Houdini MaterialX Export
# 
# Houdini allows for creation of a VEX `subnet` which contains MaterialX native definitions as well as the any custom Houdini definitions.
# The approach of encapsulating an subnet "asset" as a MaterialX compound nodegraph allows for any inputs and outputs to naturally be mappable 
# to MaterialX and allows for correspondence to a Usd Material (**which is a graph**). This is similar to the Maya approach for encapsulation,
# though it is premature to comment on mapping to MaterialX as this export workflow is not supported yet. 
# 
# Note that both must contend with how to handle MaterialX `surfacematerial` or `volumematerial` Material nodes which is the "natural" semantic mapping for
# a Usd Material (node graph). **For now both do no handle these MaterialX nodes.**
# 
# * Export to a MaterialX document is directly exposed (unlike in Maya currently). For this, the `vop2mtlx` Python script can be used directly or via the Houdini user interface. 
#   
#   <img src="images/Houdini_Subnet_Mtlx_Save.png" width="30%">
# 
# In either case, an asset (`hda`) must be created from the subnet before export. The additional `houdini` library definitions are recogized by the converter.
# 
#   Note that nodes not in shader graphs connected to outputs are not currently exported by default from the UI. This and
#   addition options are available as script arguments.
# 
# * Houdini does perform some validity checking based on what is supported by
# the version of MaterialX used. For instance nested subnets (nodegraphs) export will result in an error.
# 
# An interesting point to keep in mind is that `vop2mtlx` does not embed any `houdini` definitions
# within the MaterialX document.  
# * This follows the general "rule-of-thumb" that definitions should be separated from working documents and
# to not add any "include" references (XML xincludes) to definitions. This avoids the downside of either definitions being duplicated and statically embedded in these documents or having fixed library dependency locations. As a historical note, the `Adobe Substance Designer MaterialX plug-in` when available also kept custom definitions in a separate Adobe library and did not add any "include" dependencies.
# * Embedding can cause issues if a definition changes over time, as the embedded version may become inconsistent. As will be covered when creating definitions additional attributes such as version number can partially alleviate this type of issue.

# %% [markdown]
# 
# Below is a comparison of an example created in Houdini, and the exported result in the MaterialX Graph Editor
# 
# * Top level nodegraph
# 
# <img src="images/MTLXEditor_Houdini_Top_Level.png" width="50%">
# 
# * Expanded nodegraph contents
# 
# <img src="images/MTLXEditor_Houdini_Graph_Expanded.png" width="100%">
# 
# 

# %% [markdown]
# With the following MaterialX document exported. Note that:
# *  The file was edited a bit to remove  a number of default inputs on `standardsurface` for brevity, as Houdini exports all inputs even if they
# have default values
# * There is one top level nodegraph correspondig to the Houdini subnet
# ```xml
# <?xml version="1.0"?>
# <materialx version="1.38">
#   <!-- Generated in Houdini from /mat/HoudiniGraph -->
#   <nodegraph name="NG_HoudiniGraph_surfaceshader_surfaceshader">
#     <surface_unlit name="surface_unlit1" type="surfaceshader">
#       <input name="emission" type="float" nodename="hmtlxhcatmullrom1" value="1" />
#       <input name="emission_color" type="color3" value="1, 1, 1" />
#       <input name="transmission" type="float" value="0" />
#       <input name="transmission_color" type="color3" value="1, 1, 1" />
#       <input name="opacity" type="float" value="1" />
#     </surface_unlit>
#     <output name="mtlx_houd_out" type="surfaceshader" nodename="surface_unlit1" />
#     <standard_surface name="standard_surface1" type="surfaceshader">
#       <input name="base" type="float" nodename="ramplr1" value="1" />
#       <input name="base_color" type="color3" nodename="image1" value="0.8, 0.8, 0.8" />
#     </standard_surface>
#     <output name="stdsurf_out" type="surfaceshader" nodename="standard_surface1" />
#     <hcatmullrom name="hmtlxhcatmullrom1" type="float">
#       <input name="t" type="float" value="0.8" />
#       <input name="tension" type="float" value="0.5" />
#       <input name="key0" type="float" value="0.94" />
#       <input name="key1" type="float" value="1.44" />
#       <input name="key2" type="float" value="0.7" />
#       <input name="key3" type="float" value="1.44" />
#     </hcatmullrom>
#     <ramplr name="ramplr1" type="float">
#       <input name="valuel" type="float" value="0" />
#       <input name="valuer" type="float" value="1" />
#       <input name="texcoord" type="vector2" value="0, 0" />
#     </ramplr>
#     <image name="image1" type="color3">
#       <input name="file" type="filename" value="checker.png" />
#       <input name="layer" type="string" value="" />
#       <input name="default" type="color3" value="0, 0, 0" />
#       <input name="texcoord" type="vector2" value="0, 0" />
#       <input name="uaddressmode" type="string" value="periodic" />
#       <input name="vaddressmode" type="string" value="periodic" />
#       <input name="filtertype" type="string" value="linear" />
#       <input name="framerange" type="string" value="" />
#       <input name="frameoffset" type="integer" value="0" />
#       <input name="frameendaction" type="string" value="constant" />
#     </image>
#   </nodegraph>
# </materialx>


