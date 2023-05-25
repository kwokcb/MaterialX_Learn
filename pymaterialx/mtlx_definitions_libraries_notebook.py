# %% [markdown]
# # Node Definitions and Node Libraries
# 
# This notebook will examine the creation of definitions as well libraries.
# 
# Aspects covered include:
# 1. Using 3rd-party definition libraries.
# 2. Creating "robust" definitions from nodegraph implementations.
# 3. Creating efficient definitions from source code implementations.
# 4. "Publishing" definitions to libraries, including the core MaterialX libraries.
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

# %% [markdown]
# ## 2. Creating Definitions from Compound Graphs
# 
# Creating definitions from compound node graphs is the easiest way to create new definitions without worrying about shading language implementations if the language is supported. 
# 
# The basic logic for publishing from a nodegraph entails:
# * Copying a compound graph
# * Turning the copy into a functional graph
# * Creating a 
# * definition based on the input and output interfaces on the functional graph
# * Adding in additional meta-data tagging as outlined in the definitions learning section:
#   * Node group
#   * Version
#   * Namespace
#   * UI properties
# * Creating a reference between the definition and the functional graph
#  

# %% [markdown]
# ### Helpers
# 
# There is currently a helper interface on <a href="https://materialx.org/docs/api/class_document.html" target="_blank">Document</a> called `addNodeDefFromGraph()` that encapsulates the required logic for the most part. It does not:
# * Handle creating of definitions which inherit from each other, nor 
# * Update versioning on existing definitions with different versions.
# 
# The 1.38.7 version of the utility has some issues with it which is being looked at. These issues can be addressed by patching up the results.
# 
# The following is a simple utility wrapper sets up the creation parameters, calls `adNodeDefFromGraph()` and returns the definition (`nodedef`) and the functional graph created. 

# %%
def createDefinitionAndFunctionalGraph(nodeGraph, cparam):
    '''
    Example of creating a definition. This has a fixed version, nodegroup and graph names. 
    '''
    definition = doc.addNodeDefFromGraph(nodeGraph, cparam['nodedefName'],
                            cparam['category'], cparam['version'], cparam['defaultversion'], 
                            cparam['nodegroup'], cparam['nodegraphName'])
    funcgraph = doc.getNodeGraph(cparam['nodegraphName'])

    return definition, funcgraph

# %% [markdown]
# The `getNodeGroups()` utility will scan for existing node group names. Using existing group names allows for 
# * Any associated semantic meanings to be discoverable by code generation. For example `texture2d` and `pbr` have semantic meanings. 
# * Naming consistency and avoidance of excessive partitioning into too many disparate groups.
# Integrations may which to run this type of logic to examine for existing nodegroups. 

# %%
def getNodeGroups(library):
    '''
    Find all the existing node group names on definitions 
    '''
    nodeGroups = set()
    #mx::StringVec nodeGroups;
    for nd in library.getNodeDefs():
        group = nd.getNodeGroup()
        if group:
            nodeGroups.add(group)

    return nodeGroups

# %% [markdown]
# The `findCompoundGraphs()` utility scans and returns a list of compound `nodegraphs` in a document.
# A list of library file names is passed in as we wish to avoid any compound graphs that exist in a definition
# library.

# %%
def findCompoundGraphs(doc, libFiles):
    '''
    Search for compound graphs in a document. Skips any graphs found in 
    library files (passed in a a list of source URIs)
    '''
    compoundGraphs = []

    nodeGraphs = doc.getNodeGraphs()
    for nodeGraph in nodeGraphs:
        # Skip any nodegraph which is from a library
        if nodeGraph.getSourceUri() in libFiles:
            continue

        # Skip functional graphs
        if nodeGraph.getNodeDef():
            continue

        compoundGraphs.append(nodeGraph)
    return compoundGraphs

# %% [markdown]
# ### Example
# As an example we will load in an example compound graph and use it to create a definition. The Python utility <a href="createdefinition.py" target="_blank">(`createdefinition`)</a> encapsulates this logic and provides a command line interface for various options.
# 
# A compound nodegraph has no definition association. This can be tested by calling `getNodeDef()` on the nodegraph.
# If a `nodedef` is returned then it is instead a functional graph.

# %% [markdown]
# Once created, we will want to export the definitions and functional graphs into either a new document or an existing definition library document. To do so the contents need to be copied into the desired document.
# 
# The utility function `addDefinitionToDocument()` will copy a definition, functional graph pair either 1 or 2 seprate documents. As there is no "copy" function from one document to another, an empty definition and graph needs to be created first and then the contents copied over using the `copyContentFrom()` interface respectively.
# 
# As the association between the functional graph and definition resides on nodegraph, this will be copied over
# when `copyContentFrom()` is called. If the association is stored on an `implementation` instead then that must
# also be copied over.

# %%
def addDefinitionToDocument(definition, funcgraph, defDoc, graphDoc=None, defComment='', graphComment=''):
    '''
    Copy a definition and functional node graph to a new document.
    
    '''
    if definition and funcgraph:

        # Add definition comment
        if defComment:
            comment = defDoc.addChildOfCategory('comment')
            comment.setDocString(defComment)                 

        # Create a new definition, and copy the content over. Make sure
        # to use the existing name and category.
        newDef = defDoc.addNodeDef(definition.getName(), '', definition.getCategory())
        newDef.copyContentFrom(definition)        

        if not graphDoc:
            graphDoc = defDoc

        # Add graph comment
        if graphComment:
            comment = graphDoc.addChildOfCategory('comment')
            comment.setDocString(graphComment)                 

        # Create a new graph and copy the contents over. This will result in a functional graph.
        # Use the definiton document if no graph document specified
        newGraph = graphDoc.addNodeGraph(funcgraph.getName())
        newGraph.copyContentFrom(funcgraph)

# %% [markdown]
# Some additional utilities are proved to write the contents of the new definition document for display.

# %%
def writeDocToString(doc):
    writeOptions = mx.XmlWriteOptions()
    writeOptions.writeXIncludeEnable = False
    writeOptions.elementPredicate = mxf.MtlxFile.skipLibraryElement

    documentContents = mx.writeToXmlString(doc, writeOptions)
    return documentContents

def writeDocToMarkdown(documentContents):
    display_markdown('```xml\n' + documentContents + '\n```\n', raw=True)

def writeToMarkdown(val):
    display_markdown(val, raw=True)    

# %% [markdown]
# The main logic loads in an example file, and creates a new document for each definition/functional graph pair.
# 
# For the 1.38.7 version API, the following creation parameters are set:
# 
# * An arbitrary `category` name is chosen -- which is the compound node graph name. In general this should be set by the user.
# * The "standard" prefixes of `ND_` and `NG_` are used as node definition and node graph name prefixes.
# * A version is always added. For initial definitions the version number of `1.0` and the flag is set to indicate that this is the default version.
# * A node group is always added. This setting is difficult to infer based on just the compound node graph, so will probably require
# user input.

# %%

doc, libFiles = mxf.MtlxFile.createWorkingDocument()
mx.readFromXmlFile(doc, mx.FilePath('./data/test_procedural.mtlx'))

availableGroupNames = getNodeGroups(doc)
print('> Available node group names', ', '.join(availableGroupNames))

compoundGraphs = findCompoundGraphs(doc, libFiles)
for nodeGraph in compoundGraphs: 
    cparam = {}
    cparam['nodedefName'] = 'ND_' + nodeGraph.getName()
    cparam['category'] = nodeGraph.getName()
    cparam['version'] = '1.0'
    cparam['defaultversion'] = True
    cparam['nodegroup'] = 'texture2d'
    cparam['nodegraphName'] = 'NG_' + nodeGraph.getName()    
    definition, funcgraph = createDefinitionAndFunctionalGraph(nodeGraph, cparam)

    defDoc = mx.createDocument()
    addDefinitionToDocument(definition, funcgraph, defDoc)
    if defDoc:
        documentContents = writeDocToString(defDoc)
        writeDocToMarkdown(documentContents)
    break

# %% [markdown]
# ### 1.38.7 Definition Patching
# 
# For 1.38.7 we need to patch the result. This includes 
# * Setting the documentation string and adding any namespace.
# * Moving the interface inputs from the graph to the definition. ( Note that this is checked during Document `validate()` and will produce warnings if the functional graph has any inputs ). 
# * Removing any undesired attributes on nodes and ports.
# Both the definition and functional graph need to be patched.
# 
# The utility `patchDefinition` encapsulates this logic.

# %%
def patchDefinition(definition, funcgraph, documentation, namespace):
    if documentation:
        definition.setDocString(documentation)
    if namespace:
        definition.setNamespace(namespace)
        funcgraph.setNamespace(namespace)

    if not funcgraph:
        return

    for graphChild in funcgraph.getChildren():
        graphChild.removeAttribute('xpos')
        graphChild.removeAttribute('ypos')

    filterAttributes = { 'nodegraph', 'nodename', 'channels', 'interfacename', 'xpos', 'ypos' }

    # Transfer input interface from the graph to the nodedef
    for input in funcgraph.getInputs():
        nodeDefInput = definition.addInput(input.getName(), input.getType())
        if nodeDefInput:
            nodeDefInput.copyContentFrom(input)
            for filterAttribute in filterAttributes:
                nodeDefInput.removeAttribute(filterAttribute);
            nodeDefInput.setSourceUri('')
            input.setInterfaceName(nodeDefInput.getName())

    # Remove interface from the nodegraph
    for input in funcgraph.getInputs():
        funcgraph.removeInput(input.getName())

    # Copy the output interface from the graph to the nodedef
    for output in funcgraph.getOutputs():
        nodeDefOutput = definition.getOutput(output.getName())
        if nodeDefOutput:
            definition.removeOutput(output.getName())
        definition.addOutput(output.getName(), output.getType())
        if nodeDefOutput:
            nodeDefOutput.copyContentFrom(output)
            for filterAttribute in filterAttributes:
                nodeDefOutput.removeAttribute(filterAttribute)
            nodeDefOutput.setSourceUri('')    


# %% [markdown]
# Running with the patch results in the new corrected definition:

# %%
# Run definition creation again with patching logic
doc, libFiles = mxf.MtlxFile.createWorkingDocument()
mx.readFromXmlFile(doc, mx.FilePath('./data/test_procedural.mtlx'))

compoundGraphs = findCompoundGraphs(doc, libFiles)
for nodeGraph in compoundGraphs: 
    cparam = {}
    cparam['nodedefName'] = 'ND_' + nodeGraph.getName()
    cparam['category'] = nodeGraph.getName()
    cparam['version'] = '1.0'
    cparam['defaultversion'] = True
    cparam['nodegroup'] = 'texture2d'
    cparam['nodegraphName'] = 'NG_' + nodeGraph.getName()      
    definition, funcgraph = createDefinitionAndFunctionalGraph(nodeGraph, cparam)

    # Add documentation and namespace as well as patch up definition and functional graph
    documentation = 'Documentation for new definition: ' + nodeGraph.getName()
    namespace = 'mynamespace'
    patchDefinition(definition, funcgraph, documentation, namespace)

    defDoc = mx.createDocument()
    graphDoc = None
    defComment = ' Definition: nodeGraph.getName() '
    graphComment = ' Functional graph for definition: nodeGraph.getName() '
    
    addDefinitionToDocument(definition, funcgraph, defDoc, graphDoc, defComment, graphComment)
    if defDoc:
        documentContents = writeDocToString(defDoc)
        writeDocToMarkdown(documentContents)

# %% [markdown]
# ## 3. Creating Definitions from Source Code
# 
# When creating a custom node in MaterialX there are basically three things that needs to be created:
# 
# * A `<nodedef>` element specifying the signature of the node.
# * An `<implementation>` element that tells the code generator where it can find the source code for the node, for a particular target/language. You need one such element for each target you want to support. For the standard library: GLSL (and Vulkan, ESSL variants), OSL, MDL, and MSL should be supported. 
# * The source code for the node.
# 
# 
# 

# %% [markdown]
# ### Creating the Interface
# 
# There are no specific tools to directly creation `nodedef` interfaces. We will use a simple example which just adds 2 colors together:
# ```xml
#   <!-- Definition of a simple node <myad>, adding two colors. -->
#   <nodedef name="ND_myadd_color3" node="myadd">
#     <input name="in1" type="color3" value="1.0, 0.0, 0.0" />
#     <input name="in2" type="color3" value="0.0, 1.0, 0.0" />
#     <output name="out" type="color3" defaultinput="in1" />
#   </nodedef>
#   ```
# Note that it is a good practice to have a default routing from the input to the output if a node instance is disabled (is a pass-through).
# This can be done by setting the `mx.Output.DEFAULT_INPUT_ATTRIBUTE` attribute on an output. Note that it is only valid to set this on
# an output in a definition.  In this case the default value for the output is the input "in1".
# 

# %%
def addNodeDefinition(doc, category, type):
    '''
    Add a node definition which uses the standard naming convention.
    No definition is created if a node of the same name already exists in the document 
    '''
    prefix = 'ND_'
    nodedefName = prefix + category + '_' + type 

    existingDef = doc.getChild(nodedefName)
    if existingDef:
        return None

    newDef = doc.addChildOfCategory('nodedef', nodedefName)
    newDef.setNodeString(category)
    return newDef

doc, libFiles = mxf.MtlxFile.createWorkingDocument()
category = 'myadd'
output_type = 'color3'
comment = doc.addChildOfCategory('comment')
comment.setDocString(' Definition of a simple node <myadd>, adding two colors. ')
newDef = addNodeDefinition(doc, category, output_type)

# Example way to add in inputs and outputs
inputs = [ ["in1", "color3", "1.0, 0.0, 0.0"], ["in2", "color3", "0.0, 0.0, 0.0"] ]
outputs = [ ["out", "color3", "in1"] ]
for input in inputs:
    newInput = newDef.addInput(input[0], input[1])
    newInput.setValueString(input[2])
for output in outputs:
    newOutput = newDef.addOutput(output[0], output[1])
    if output[2]:
        newOutput.setAttribute(mx.Output.DEFAULT_INPUT_ATTRIBUTE, output[2])

documentContents = writeDocToString(doc)
writeDocToMarkdown(documentContents)

# %% [markdown]
# 
# As an alternative, the interface could be created as a compound `nodegraph` first using existing graph editing tools and then create a definition
# based on it. For example this graph was created interactively in the MaterialX Graph Editor:
# ```xml
# <nodegraph name="myadd">
#   <input name="in1" type="color3" value="1, 0, 0" xpos="11.021739" ypos="-3.568965" />
#   <input name="in2" type="color3" value="0, 0, 0" xpos="11.115942" ypos="-2.051724" />
#   <output name="out" type="color3" xpos="13.456522" ypos="-3.284483" />
# </nodegraph>
# ```
# A utility called `copyValueElements()` is used to copy inputs and outputs over.
# > Note that `copyValueElements()` replaces the attributes on the node so these need to be cached and restored.

# %%
def createDefinitionFromGraphReference(doc, category, output_type, refNodeGraph):
    newDef = addNodeDefinition(doc, category, output_type)

    # Copy the children over from the nodegraph
    newDefAttrs = newDef.getAttributeNames()
    newDefAttrValues = {}
    for newDefAttr in newDefAttrs:
        attr = newDef.getAttribute(newDefAttr)
        newDefAttrValues[newDefAttr] = attr
    newDef.copyContentFrom(refNodeGraph)
    for newDefAttr in newDefAttrs:
        newDef.setAttribute(newDefAttr, newDefAttrValues[newDefAttr])

    # Filter out undesired attributes including connections and ui position
    filterAttributes = { 'nodegraph', 'nodename', 'channels', 'interfacename', 'xpos', 'ypos' }
    for child in newDef.getChildren():
        for filterAttribute in filterAttributes:
            child.removeAttribute(filterAttribute)

    return newDef


# %% [markdown]
# As in the previous example the default input value is set manually. It cannot be set compound nodegraph before hand as this is considered to be invalid.

# %%

# Read in reference nodegraph
refdoc, reflibFiles = mxf.MtlxFile.createWorkingDocument()
mx.readFromXmlFile(refdoc, mx.FilePath('./data/myadd_compound_graph.mtlx'))

category = 'myadd'
output_type = 'color3'
refNodeGraph = refdoc.getNodeGraph('myadd')

sourceCodeDoc = None
inline_definition = None
if refNodeGraph:
    # Create a new empty definition
    sourceCodeDoc, libFiles = mxf.MtlxFile.createWorkingDocument()
    comment = sourceCodeDoc.addChildOfCategory('comment')
    comment.setDocString(' Definition of a simple node <myadd>, adding two colors. ')
    inline_definition = createDefinitionFromGraphReference(sourceCodeDoc, category, output_type, refNodeGraph)
    for child in inline_definition.getOutputs():
        child.setAttribute(mx.Output.DEFAULT_INPUT_ATTRIBUTE, 'in1')

if sourceCodeDoc:
    docString = writeDocToString(sourceCodeDoc)
    writeDocToMarkdown(docString)

# %% [markdown]
# ### Creating Implementations
# 
# To support the standard shading languages and implementation will be made for each target.
# At this point a choice needs to be made on whether the code can be inlined or not. If it can then the `implementation` element
# will hold the code in it's `sourcecode` attribute. If not then additional source code files need to be created and a `file` and `function`
# attribute need to be added. 
# 
# #### Inlined Source Code
# 
# For this implementation example we will first show inlined code which uses tokens to represent arguments. Tokens are use '{{' and '}}' delimiters.
# 
# In this example the code becomes:
# ```
#  '{{in1}} + {{in2}}'
#  ```
#  where `in1` corresponds to the nodedef input `in1` and `in2` to the nodedef input `in2`

# %%
def getTargetDefs(doc):
    targets = []
    for element in doc.getChildren():
        if element.getCategory() == 'targetdef':
            if element.getName() != 'essl':
                targets.append(element.getName())
    return targets

def createImplementations(doc, nodedef, targets):
    '''
    Create implementation elements for a set of targets based on a given definition (nodedef).
    All implementation names are of the form:
    
        IM_<category>_<output type>_<target>
    
    '''
    prefix = 'IM_'
    category = nodedef.getNodeString() 
    type = nodedef.getType()
    implName = prefix + category + '_' + type 
    impls = []
    for target in targets:
        #newline = doc.addChildOfCategory('newline')
        comment = doc.addChildOfCategory('comment')
        comment.setDocString(' Implementation of <%s> for target %s and type %s ' % (category, target, type))
        impl = doc.addImplementation(implName + '_' + target)
        impl.setNodeDef(newDef)
        impl.setTarget(target)
        impls.append(impl)

    return impls


def setImplementationSourceCode_v1(doc, nodedef, targets, sourceCode):
    category = nodedef.getNodeString() 
    type = nodedef.getType()
    implName = 'IM_' + category + '_' + type 
    for target, code in zip(targets, sourceCode):
        impl = doc.getImplementation(implName + '_' + target)
        if impl:
            impl.setAttribute('sourcecode', code)

# Create the implementations for all targets based on the nodedef
inlined_doc = mx.createDocument()
inlined_doc.copyContentFrom(sourceCodeDoc)
targets = getTargetDefs(inlined_doc)
inlined_impls = createImplementations(inlined_doc, newDef, targets)

# Set the source code for all targets based on the nodedef.
# In this case all inline implementations are identical.
sourceCode = [ '{{in1}} + {{in2}}' ]
sourceCode = sourceCode * len(targets)
setImplementationSourceCode_v1(inlined_doc, newDef, targets, sourceCode)

docString = mxf.MtlxFile.writeDocumentToString(inlined_doc, mxf.MtlxFile.skipLibraryElement)
writeDocToMarkdown(docString)

mxf.MtlxFile.writeDocumentToFile(inlined_doc, './data/myadd_definition.mtlx', mxf.MtlxFile.skipLibraryElement)

# %% [markdown]
# #### Source Code Files For Implementations
# 
# If the code cannot be inlined then a new function name is required, with the general guideline to prefix the function name with the string `mx_` followed by catagory and type. For consistency the file names for source code will use the same convention.
# 
# Thus for this example:
# * `mx_myadd_color3` is the function name and
# * `mx_myadd_color3.<shader language extension>` is used for the shader name, where `<shader language extension>` is the native shading language suffix name (e.g. `osl` for the OSL shading language or `msl` for Metal) 
# 
# The utility function `setImplementationSourceCode_v1` is extended to differentiate between inline and file source code and called `setImplementationSourceCode` 

# %%
def setImplementationSourceCode(doc, nodedef, targets, sourceCode, inlined):
    type = nodedef.getType()
    category = nodedef.getNodeString()
    implName = 'IM_' + category + '_' + type 

    if inlined:
        for target, code in zip(targets, sourceCode):
            impl = doc.getImplementation(implName + '_' + target)
            if impl:
                    impl.setAttribute('sourcecode', code)
    else:
        functionName = 'mx_' + category + '_' + type
        for target, code in zip(targets, sourceCode):
            impl = doc.getImplementation(implName + '_' + target)
            if impl:
                fileName = functionName
                impl.setFunction(functionName)
                fileExtension = target.removeprefix('gen')
                fileName = functionName + '.' + fileExtension
                impl.setFile(fileName)

                # Note: A possible option to add here would be to create the actual source files.

filesource_doc = mx.createDocument()
filesource_doc.copyContentFrom(doc)

targets = getTargetDefs(filesource_doc)
createImplementations(filesource_doc, newDef, targets)

sourceCode = [ 'placeholder text']
sourceCode = sourceCode * len(targets)
setImplementationSourceCode(filesource_doc, newDef, targets, sourceCode, False)

docString = mxf.MtlxFile.writeDocumentToString(filesource_doc, mxf.MtlxFile.skipLibraryElement)
writeDocToMarkdown(docString)

mxf.MtlxFile.writeDocumentToFile(filesource_doc, './data/myadd_definition_file.mtlx', mxf.MtlxFile.skipLibraryElement)

# %% [markdown]
# ## 4. Adding Definitions To A "Library"
# 
# When a definition is refined to the point where it can be made available generally, there are a few choices to how they are organized and where they will reside. For instance a new definition could either be part of a custom library or potentially contributed back the the MaterialX standard libraries.
# 
# ### "Standard" Library Organization
# 
# Below shows a layout for how the standard libraries are organized on the left.
# 
# <img src="../documents/images/definition_library_org.jpg" width="80%">
# 
# For example if we consider the groupin on the left to be `stdlib`, then is composed:
# * A separate file `stdlib_defs.mtlx` containing all definitions 
# * A separate file `stdlib_ng.mtlx` containing all Functional node graph implementations.
# * A separate file containing all per-target source code implementation reference. Files are of in per-target sub-folders and of the form: `<target>/stdlib_<target>_impl.mtlx` files.  For example `genglsl/stdlib_genglsl_impl.mtlx` is the implementation file for GLSL (genglsl target)).
# 
# This structure is repeated for the pbr library `pbrlib`.
# 
# Higher level functional nodegraph implementation only libraries such as `bxdf` are built on top of `pbrilb` and `stdlib`. 
# 
# ### Custom Library Organization
# In the diagram we show a custom library (on the right) which reflects the "standard" libraries. 
# 
# There are however many choices as shown on the far right.
# For instance functional nodegraphs could be kept separate from other graphs, and/or they could be kept within the file as definition or as two separate files. The same holds true implementations and implementation files. For instance the implementation, functional nodegraph and definition could all
# reside in the same file as a self-contained grouping.
# 
# ### Semantic Groupings
# Different attributes could be used for organization such as `category`, `node group`, `namespace`and `version`.
# 
# 
# ### Library Identification and Dependencies
# Note that there is no formal concept of a library and thus no concept of library or definition depeencies. 
# For example `stdlib` is just a folder name where definitions reside. The definitions themselves have no reference to a given library identifier.
# If a definition from the `bxdf` library is created without loading in  `stdlib` and / or `pbrlib` then this dependency may only 
# be detected at graph evaluation time (e.g. for code generation)
# 
# Also as noted, include dependencies are not recommended to be specified explicitly as they are file references. There is no
# concept of library identifier dependence.
# 

# %% [markdown]
# 
# ### Adding A Custom Definition to the "Standard" library
# 
# A desirable feature is to be able to add definitions into the MaterialX standard libraries.
# As definitions have no delineation within a file (beyond an XML comment string), an initial option is to just 
# append the definitions, implementations, and functional graphs into the appropriate files.
# 
# At time of writing, utilities to aid in this process are under discussion / design currently, with a possible recommended
# workflow forth-coming. Note that version `1.38.8` is the minimum version to be able to preserve comments and
# newlines properly on XML load and save.
# 
# #### Example 1: Definition with Functional Graph Implementation 
# In this example, we will take the nodegraph from the Marble example and produce separate documents using the
# `addDefinitionToDocument()`.
# 

# %%
doc, libFiles = mxf.MtlxFile.createWorkingDocument()
mx.readFromXmlFile(doc, 'data/standard_surface_marble_solid.mtlx')

nodeGraph = doc.getNodeGraph('NG_marble1')

category = 'mymarble'

cparam = {}
cparam['nodedefName'] = 'ND_' + category
cparam['category'] = category
cparam['version'] = '1.0'
cparam['defaultversion'] = True
cparam['nodegroup'] = 'texture2d'
cparam['nodegraphName'] = 'NG_' + category      
definition, funcgraph = createDefinitionAndFunctionalGraph(nodeGraph, cparam)

# Add documentation and namespace as well as patch up definition and functional graph
documentation = ' Custom marble texture defintion: ' + category
namespace = ''
patchDefinition(definition, funcgraph, documentation, namespace)

defDoc = mx.createDocument()
graphDoc = mx.createDocument()
addDefinitionToDocument(definition, funcgraph, defDoc, graphDoc, ' Custom marble definition: : mymarble ', ' Functional graph implementation of custom marble: mymarble ')

writeToMarkdown('### Definition document')
documentContents = writeDocToString(defDoc)
writeDocToMarkdown(documentContents)

writeToMarkdown('### Functional Graph document')
documentContents = writeDocToString(graphDoc)
writeDocToMarkdown(documentContents)



# %% [markdown]
#  If the `stdlib` files are used instead then the definition and graph will be appended to
# existing files.

# %%
def getStandardLibraryFilePaths(library, targets=[]):
    '''
    Get file paths based on a "standard" library configuration
    '''    
    DEFS_POSTFIX = '_defs'
    GRAPH_POSTFIX = '_ng'
    MTLX_EXTENSION = 'mtlx'
    IMPL_POSTFIX = '_impl'

    rootFilePath = mx.FilePath(library)

    defFilePath = mx.FilePath(library + DEFS_POSTFIX)
    defFilePath.addExtension(MTLX_EXTENSION)
    defFilePath = rootFilePath / defFilePath

    graphFilePath = mx.FilePath(library + GRAPH_POSTFIX)
    graphFilePath.addExtension(MTLX_EXTENSION)
    graphFilePath = rootFilePath / graphFilePath

    implFilePaths = []
    for target in targets:
        targetRoot = mx.FilePath(target)
        targetPath = mx.FilePath(library + '_' + target + IMPL_POSTFIX)
        targetPath.addExtension(MTLX_EXTENSION)
        targetPath = rootFilePath / targetRoot / targetPath
        implFilePaths.append(targetPath)

    return defFilePath, graphFilePath, implFilePaths


targets = getTargetDefs(doc)
libraryName = 'stdlib'
defFilePath, graphFilePath, implFilePaths = getStandardLibraryFilePaths(libraryName, targets)
writeToMarkdown('### File Paths for Library: %s ' % libraryName)
writeToMarkdown('* Definition File: %s' % defFilePath.asString())
writeToMarkdown('* Functional Graph File: %s' % graphFilePath.asString())
for implPath, target in zip(implFilePaths, targets):    
    writeToMarkdown('* Target( %s ) implementation file: %s' % (target, implPath.asString()))

# %% [markdown]
# With these file names available we can load in these documents, append to them and write them back out.
# Note that we turn on preservation of both comments and newlines so as to not lose any of the original formatting.

# %%
targets = getTargetDefs(doc)
libraryName = 'stdlib'
defFilePath, graphFilePath, implFilePaths = getStandardLibraryFilePaths(libraryName, targets)

defaultLibFolder = mx.getDefaultDataLibraryFolders()
defaultSearchPath = mx.getDefaultDataSearchPath()

# Read in files relative to default library search path
defDoc = mx.createDocument()
defFilePath = mx.FilePath(defaultLibFolder[0]) / defFilePath
mx.readFromXmlFile(defDoc, defFilePath, defaultSearchPath)

graphDoc = mx.createDocument()
graphFilePath = mx.FilePath(defaultLibFolder[0]) / graphFilePath
mx.readFromXmlFile(graphDoc, graphFilePath, defaultSearchPath)

# Append the definitions and functional graph to each document
addDefinitionToDocument(definition, funcgraph, defDoc, graphDoc, ' Custom marble definition: : mymarble ', ' Functional graph implementation of custom marble: mymarble ')

# Examine the document
documentContents = mx.writeToXmlString(defDoc, writeOptions)
text = '<details><summary>Standard Libray Definitions with New Definiont</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
display_markdown(text , raw=True)  

documentContents = mx.writeToXmlString(graphDoc, writeOptions)
text = '<details><summary>Standard Libray Graphs with New Graph</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
display_markdown(text , raw=True)  

# Confirm and clean-up
findGraph = graphDoc.getNodeGraph(funcgraph.getName())
if findGraph:
    print('Functional graph added to: %s' % graphFilePath.asString())
    graphDoc.removeChild(funcgraph.getName())
    findGraph = graphDoc.getNodeGraph(funcgraph.getName())

findDef = defDoc.getNodeDef(definition.getName())
if findDef:
    print('Definition added to: %s' % defFilePath.asString())
    defDoc.removeChild(definition.getName())
    findDef = defDoc.getNodeGraph(definition.getName())


# %% [markdown]
# #### Example 2: Definition with Source Code Implementation 
# 
# In this example we take the previous custom `myadd` definition and add it's definition to the `stdlib` definition file and
# add all of it's implementations to eh appropriate per target implementation files

# %%
def addDefinitionToDocument(definition, impls, defDoc, implDocs, defComment='', implComment=''):
    '''
    Copy a definition and implementations to a new document.
    
    '''
    if definition and impls and defDoc and implDocs:

        # Add definition comment
        if defComment:
            comment = defDoc.addChildOfCategory('comment')
            comment.setDocString(defComment)                 

        # Create a new definition, and copy the content over. Make sure
        # to use the existing name and category.
        newDef = defDoc.addNodeDef(definition.getName(), '', definition.getCategory())
        newDef.copyContentFrom(definition)        

        # Add implementations to appropriate implementation documents
        for impl, implDoc in zip(impls, implDocs):

            if not implDoc:
                continue

            # Add impl comment
            if implComment:
                comment = implDoc.addChildOfCategory('comment')
                comment.setDocString(implComment)                 

            # Create a new graph and copy the contents over. This will result in a functional graph.
            # Use the definiton document if no graph document specified
            newImpl = implDoc.addImplementation(impl.getName())
            newImpl.copyContentFrom(impl)

if inlined_impls:
    implDocs = []
    skipped_targets = []
    for implFilePath, target in zip(implFilePaths, targets):
        implFilePath = mx.FilePath(defaultLibFolder[0]) / implFilePath
        implDoc = mx.createDocument()
        try:
            mx.readFromXmlFile(implDoc, implFilePath, defaultSearchPath)
            implDocs.append(implDoc)
        except mx.ExceptionFileMissing as err:
            implDocs.append(implDoc)
            skipped_targets.append(target)
            print('No target (%s) impl file to append to %s' % (target, implFilePath.asString()))
        
    addDefinitionToDocument(inline_definition, inlined_impls, defDoc, implDocs, 'Custom add definition (mxadd)', 'Custom add implementation (mxadd)')

    # Examine the definition document
    documentContents = mx.writeToXmlString(defDoc, writeOptions)
    text = '<details><summary>Standard Libray Definitions with New Definition</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
    display_markdown(text , raw=True) 

    findDef = defDoc.getNodeDef(inline_definition.getName())
    if findDef:
        print('Definition %s added to: %s' % (inline_definition.getName(), defFilePath.asString()))
        defDoc.removeChild(inline_definition.getName())
        findDef = defDoc.getNodeGraph(inline_definition.getName())

    # Examine the implementation documents
    for implDoc, inline_impl, target in zip(implDocs, inlined_impls, targets):
        if target in skipped_targets:
            continue

        documentContents = mx.writeToXmlString(implDoc, writeOptions)
        text = '<details><summary>Implementation for target ' + target + '</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
        display_markdown(text , raw=True)  

        implName = inline_impl.getName()
        if implDoc.getImplementation(implName):
            print('- Source implementation added: %s' % implName)
            implDoc.removeChild(implName)


