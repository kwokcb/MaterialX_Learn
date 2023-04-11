# %% [markdown]
# # USD and MaterialX NodeGraphs
# 
# This notebook will look at some of the basic interop between MaterialX and USD focusing on nodegraphs and nodes.
# Material assignment will not be examined, nor is the intent to provide a tutorial about Usd, which can be found in other places
# such as from <a href="https://openusd.org/release/tut_usd_tutorials.html" target="_blank">Pixar</a>, <a href="https://docs.omniverse.nvidia.com/prod_usd/prod_usd/python-snippets.html" target="_blank">NVIDIA</a>, and <a href="https://www.sidefx.com/docs/houdini/solaris/usd.html" target="_blank">Houdini</a>
# 
# Topics covered include:
# 1. Usd and MaterialX Package Setup
# 2. Translating a Usd file with MaterialX materials to MaterialX format, focusing on traversal, pathing, and connection mapping. 
# 3. Translating a MaterialX into Usd format with the same focus.
# 
# > Neither translators are intended to be a full importer or exporter but rather usable for learning purposes, noting that
# <a href="https://github.com/PixarAnimationStudios/USD/tree/release/pxr/usd/usdMtlx" target="_blank">UsdMtlx</a> import is not available as part of the core Usd Python package, and code such as <a href="https://github.com/PixarAnimationStudios/USD/blob/release/pxr/imaging/hdSt/materialXFilter.h" target="_blank">UsdFilter</a> for HDStorm is specifically targeted for a given render delegate and is also not exposed.

# %% [markdown]
# ## 1. Usd Setup
# 
# To use Usd the "core" package can be installed as follows: 

# %%
#pip install usd-core

# %% [markdown]
# After installation various packages can be imported.  `Usd`, `UsdShade`, `Sdf`, and `Gf` are the main packages used. The MaterialX package is also imported. 

# %%
from pxr import Usd
from pxr import UsdShade
from pxr import Sdf
from pxr import Gf

# For Markdown output display
from IPython.display import display_markdown

import MaterialX as mx

major, minor, build = Usd.GetVersion() 
print('Using Usd Version:', str(major) + "." + str(minor) + "." + str(build))
print('Using MaterialX Version:', mx.getVersionString())

# %% [markdown]
# As input, we load in an example Usd file that contains a shading network with a series of nodegraph connections and nodes which have MaterialX definitions. As there is no concept of a layer hierarchy in MaterialX, all layers in the imported <a href="https://openusd.org/release/api/class_usd_stage.html" target="_blank">Stage</a> are pre-"flattened" using `Stage.Flatten()` 

# %%
# Load in a sample file
stage_unflattend = Usd.Stage.Open('data/sphere_with_nodegraphs.usda') 

# Flatten layers
layer = stage_unflattend.Flatten()
stage = Usd.Stage.Open(layer)

# Print as String
stringResult = layer.ExportToString()
display_markdown('### Flattened Usd File', raw=True)
display_markdown('```usd\n' + stringResult + '\n```\n', raw=True)

# %% [markdown]
# ## 2. Usd Traversal
# 
# As a starting point, a simple tree traversal logic is added. Note that this just traverses the entire stage and prints out the prims and their attributes.

# %%
# Start from the root
prim = stage.GetPrimAtPath('/')

# Utility to recursive traverse and print out children, and their attributes
def printChildren(indent, prim):
    children = prim.GetChildren()
    for child in children:
        if child:
            print('%s - Name %s, Path %s' % (indent, child.GetName(), child.GetPrimPath())) 
            for attr in child.GetAttributes():
                if attr.Get():
                    print(indent, '  -', attr.GetName() + ' : ', attr.Get())
            printChildren(indent + '  ', child)    

# Print out tree
printChildren(' ', prim)

# %% [markdown]
# ## 3. Examining Shader Graphs
# 
# This can be refined to only examine shading nodes and ports.
# 
# Two utility functions are added:
#  
# * `printValueElements()` selectively examines inputs and outputs using `GetInputs()` and `GetOutputs` on a <a href="https://openusd.org/release/api/class_usd_shade_shader.html" target="_blank">UsdShadeShader</a>, or <a href="https://openusd.org/release/api/class_usd_shade_node_graph.html" target="_blank">UsdShadeNodeGraph</a>.  Tokens are not considered in this example. 
# 
# * `printShaderNodes()` performs the traversal from a root prim visiting prims which would map to MaterialX -- namely "node graphs", "material" and "shader" nodes. Any geometry and tree nesting is ignored. 

# %%
def printValueElements(shaderInterface, indent):
    """
    Print out the inputs and outputs 
    """
    for input in shaderInterface.GetInputs():
        if input:
            print(indent, '- Input:', input.GetBaseName())
    for output in shaderInterface.GetOutputs():
        if output:
            print(indent, '- Output:', output.GetBaseName())

def printShaderNodes(indent, prim):
    """
    Print out shader node information
    """
    # Use RTTI to find the desired types
    if prim.IsA(UsdShade.NodeGraph):
        print(indent, '- Nodegraph: %s, Path %s' % (prim.GetName(), prim.GetPrimPath()))
        nodegraph = UsdShade.NodeGraph(prim)
        printValueElements(nodegraph, indent + '  ')

    elif prim.IsA(UsdShade.Material): 
        print(indent, '- Material %s, Path %s' % (prim.GetName(), prim.GetPrimPath()))
        material = UsdShade.Material(prim)
        printValueElements(material, indent + '  ')

    elif prim.IsA(UsdShade.Shader): 
        shader = UsdShade.Shader(prim)
        print(indent, '- Shader %s, Path %s' % (prim.GetName(), prim.GetPrimPath()))
        print(indent, '  - Nodedef: ', (shader.GetIdAttr().Get()))
        printValueElements(shader, indent + '  ')

    # Visit children
    children = prim.GetChildren()
    if children:
        childIndent = indent+'  '
        for child in children:
            printShaderNodes(childIndent, child)

# Traverse and print output "shader" contents
prim = stage.GetPrimAtPath('/')
printShaderNodes(' ', prim)

# %% [markdown]
# ## 4. Usd to MaterialX Translation
# 
# The previous example is modified to create MaterialX graphs, shaders and materials. 
# 
# Note that the shading network contains nested nodegraphs. That is a nodegraph can contain another nodegraph. 
# While this is part of the MaterialX specification, full support for this does not currently exist at time of writing. 
# For the purposes of translation / interop, logic is included which can general enough to support any level of graph nesting.
# 
# As required a user can perform a "flattening" process by traversing through the node connections to remove nodegraph nesting as is done for `UsdMtlx` for conversion from Usd to MaterialX. This is not included as part of the logic for this example.
# 
# ### 4.1 Setup
# The first step is to add in a basic setup for MaterialX to create a working document and load in standard definitions.

# %%
# Perform basic setup
libraryPath = mx.FilePath('libraries')
stdlib = mx.createDocument()
searchPath = mx.FileSearchPath()
libFiles = mx.loadLibraries([ libraryPath ], searchPath, stdlib)

doc = mx.createDocument()
doc.importLibrary(stdlib)

# Write predicate
def skipLibraryElement(elem):
    return not elem.hasSourceUri()

# %% [markdown]
# ### 4.2 Translation Logic
# 
# Next, translation logic is broken up into a series of utilities which perform Usd to MaterialX mappings.
# 
# #### 4.2.1 Type and Value Mapping
# 
# The first of these are utilities for value and type mapping:
# * The utility `mapUsdTypeToMtlx()` maps native Usd type strings to MaterialX native type strings. 
# * The utility `mapUsdValueToMtlx()` is used to map a Usd `Gf` value to a MaterialX string value.
# 
# > Note: Both mappings only handle a subset of all possible mappings. 

# %%
def mapUsdTypeToMtlx(usdType):
    """ 
    Map a Usd type string to a MaterialX type string.
    Note this is not a complete mapping.
    """
    usdTypeString = str(usdType)
    mtlxType = 'color3'
    if 'color3' in usdTypeString:
        mtlxType ='color3'
    elif 'float4' in usdTypeString:
        mtlxType ='vector4'
    elif 'vector3' in usdTypeString:
        mtlxType ='vector3'
    elif 'float2' in usdTypeString:
        mtlxType ='vector2'
    elif 'float' == usdType:
        mtlxType ='float'
    elif 'string' in usdTypeString:
        mtlxType = 'string'
    elif 'int' in usdTypeString:
        mtlxType = 'integer'
    elif 'bool' in usdTypeString:
        mtlxType = 'boolean'
    elif 'asset' in usdTypeString:
        mtlxType = 'filename'
    elif 'token' in usdTypeString:
        mtlxType = 'token'
    else: 
        mtlxType = usdTypeString
        print('--> Mapping of Usd type failed:', usdTypeString)
    return mtlxType

def mapUsdValueToMtlx(mtlxType, usdValue):
    """
    Map a Usd value to a MaterialX value.  
    Note this is not a complete mapping. Ideally, if this is a value on a node
    input / output, then the definition can be queried to get the default value.
    """
    mtlxValue = None
    if mtlxType == 'float':
        if not usdValue:
            mtlxValue = '0'
        else:
            mtlxValue = str(usdValue)
    elif mtlxType == 'integer':
        if not usdValue:
            mtlxValue = '0'
        else:
            mtlxValue = str(usdValue)
    elif mtlxType == 'boolean':                    
        if not usdValue:
            mtlxValue = 'false'
        else:
            mtlxValue = str(usdValue).lower() 
    elif mtlxType == 'string' or mtlxType == 'displacementshader' or mtlxType == 'surfaceshader':                    
        if not usdValue:
            mtlxValue = ''
        else:
            mtlxValue = usdValue
    elif mtlxType == 'filename':        
        if not usdValue:
            mtlxValue = ''
        else:
            mtlxValue = str(usdValue).removeprefix('@').removesuffix('@')
    elif mtlxType == 'vector2':
        if not usdValue:
            mtlxValue = '0, 0'
        else:
            mtlxValue = str(usdValue[0]) + ','  + str(usdValue[1])
    elif mtlxType == 'color3' or mtlxType == 'vector3':
        if not usdValue:
            mtlxValue = '0, 0, 0'
        else:
            mtlxValue = str(usdValue[0]) + ','  + str(usdValue[1]) + ','  + str(usdValue[2])
    elif mtlxType == 'color4' or mtlxType == 'vector4':
        if usdValue is None:
            mtlxValue = '0, 0, 0, 0'
        else:
            mtlxValue = str(usdValue[0]) + ','  + str(usdValue[1]) + ','  + str(usdValue[2]) + ','  + str(usdValue[3])

    if mtlxValue is None:
        print('--> Mapping of Usd Value %s failed for MaterialX type %s' % (usdValue, mtlxType))

    return mtlxValue

# Mapping from Sdf type to MaterialX type.
# It is possible to map using Sdf type. This function is unused in this example 
def mapUsdSdfTypeToMtlx(usdType):
    mtlxUsdMap = dict()
    mtlxUsdMap[Sdf.ValueTypeNames.Asset] = 'filename' 
    mtlxUsdMap[Sdf.ValueTypeNames.String] = 'string'
    mtlxUsdMap[Sdf.ValueTypeNames.Bool] = 'boolean' 
    mtlxUsdMap[Sdf.ValueTypeNames.Int] = 'integer' 
    mtlxUsdMap[Sdf.ValueTypeNames.Color3f] = 'color3' 
    mtlxUsdMap[Sdf.ValueTypeNames.Color4f] = 'color4' 
    mtlxUsdMap[Sdf.ValueTypeNames.Float] = 'float' 
    mtlxUsdMap[Sdf.ValueTypeNames.Float2] = 'vector2'     
    mtlxUsdMap[Sdf.ValueTypeNames.Float3] = 'vector3'     
    mtlxUsdMap[Sdf.ValueTypeNames.Vector3f] = 'vector3'     
    mtlxUsdMap[Sdf.ValueTypeNames.Float4] = 'vector4'   
    
    if usdType in mtlxUsdMap:
        return mtlxUsdMap[usdType]
    return 'string'

# %% [markdown]
# #### 4.2.2 Multiple Output Detection
# 
# `isMultiOutput` is used to determine if the Usd prim (nodegraph, shader or material)
# has multiple outputs. 
# 
# This detection is required as MaterialX connections has a specific syntax to specify the output (port) on an upstream element and this syntax is only added for upstream elements which have multiple outputs ('multioutput') 

# %%
def isMultiOutput(prim):
    """ Test if the Usd prim has multiple outputs """
    outputCount = 0
    if prim.IsA(UsdShade.NodeGraph):
        usdNodegraph = UsdShade.NodeGraph(prim)
        outputCount = len(usdNodegraph.GetOutputs())
    elif prim.IsA(UsdShade.Material): 
        usdMaterial = UsdShade.Material(prim)
        outputCount = len(usdMaterial.GetOutputs())
    elif prim.IsA(UsdShade.Shader):     
        usdShader = UsdShade.Shader(prim)
        outputCount = len(usdShader.GetOutputs())

    return outputCount > 1

# %% [markdown]
# #### 4.2.3 Value Element (Input / Output) Mapping
# 
# `emitMtlxValueELements` handles the mapping of Usd inputs and outputs to MaterialX inputs and outputs. 
# 
# This includes:  
# * Creating the input / output. 
#   * Unlike Usd which has explicit outputs, **MaterialX never specifies outputs on nodes**, only on nodegraphs. 
#   * This difference is handled when visiting Usd outputs.
# * Setting a value **or** (*)
# * Setting connection attributes. 
#   * <a href="https://openusd.org/release/api/class_usd_shade_input.html" target="_blank">`GetConnectedSources()`</a> in Usd is roughly requivalent to <a href="https://materialx.org/docs/api/class_input.html" target="_blank">`getConnectedNode()`</a> in MaterialX. One interesting difference is that "valid" vs "invalid" sources can be returned.
#   * Unlike Usd which has a single `connect` syntax and corresponding API for connection logic and behaviour, MaterialX can require multiple attributes to specified to when creating / modifying a connection. 
#   * This depends on:     
#     * if the upstream element is a `nodegraph` or `node`, or `interface input` then 1 of 3 different attributes are set; 
#     * if the upstream element has multiple outputs (`multioutput` type), an additional `output` attribute is required; and
#     * if there is a specific channel extracted from the upstream port, an additional `channel` attribute is required. Logic for channels is not included as part of this example.
#   * **Ideally if MaterialX adopted a similar syntax to Usd then the mapping would be vastly simplified.**
# 
# __Notes__
# 
# 1. Additional layer nesting in Usd not directly related to the shading network is not preserved in this example. This could be handled by additional nodegraph nesting or something like `namepspace` nesting could be used. The former is less lossy, as `namespace`s are flattened on import from MaterialX in `UsdMtlx` at the current time. 
# 
# 2. It is assumed that the Usd string representation for a value can be mapped to a MaterialX one. For example, the string representation for a vector3 (`(v1, v2, v3)`) in Usd is valid syntax in MaterialX (`v1, v2, v3`).
# 
# 3. For a Usd port with a  `token` type the type of the created MaterialX input / output is set based on the port's name if the Usd Port name is a  'surface' or 'displacement' shader. This logic is encapsulated in the utility function `mapUsdTokenToStype()` (There  appears to be no way by just examining the Usd shading network to determine the type without this assumption at this time).
# 
# (*) MaterialX only allows either a connection or value to be specified on a port.

# %%
def mapUsdTokenToType(mtlxType, usdBaseName):
    """
    Utility to test the base name for a semantic match to a surface or displacement shader
    If found return the appropriate MaterialX type. Othewise the type is simply `token`.
    """
    usdBaseNameSplit = mx.splitString(usdBaseName, ':')
    testName = usdBaseNameSplit[len(usdBaseNameSplit)-1]            
    if 'displacement' == str(testName) or 'displacementshader' == str(testName):
        mtlxType = 'displacementshader'
    elif 'surface' == str(testName) or 'surfaceshader' == str(testName):
        mtlxType = 'surfaceshader'
    return mtlxType


def emitMtlxValueElements(shader, parent, emitOutputs):
    """
    Emit MaterialX value elements (currently only Inputs and Outputs)
    This is not a complete translation of all value element attributes.
    """
    for input in shader.GetInputs():

        # Only output if there is a value or a connection
        if input:

            # Map Usd type to Mtlx type and create an input
            usdType = input.GetTypeName()
            mtlxType = mapUsdTypeToMtlx(usdType)
            usdBaseName = input.GetBaseName()
            mtlxType = mapUsdTokenToType(mtlxType, usdBaseName)
            usdBaseName = usdBaseName.replace(':', '_')    

            # Add a connection if encountered
            if input.HasConnectedSource():
                newInput = parent.addInput(usdBaseName, mtlxType)

                # Only consider "valid" inputs.
                usdSources, invalidSources = input.GetConnectedSources() 
                if usdSources and usdSources[0]:
                    # Check UsdShadeConnectionSourceInfo to extract
                    # out the upstream information
                    usdSource1 = usdSources
                    sourcePrim = usdSource1[0].source.GetPrim()
                    sourcePort = usdSource1[0].sourceName # e.g. out
                    sourceDirection = usdSource1[0].sourceType # e.g. Input / Output
                    sourceType = usdSource1[0].typeName # e.g. color3f

                    # Handle the complex MaterialX attribute syntax
                    # for specifying a connection.
                    # ---------------------------------------------
                    # Assume a node->input connection to start
                    mtlxConnectString = 'nodename'
                    mtlxConnectItem = sourcePrim.GetName()

                    # An input->input connection is denoted using
                    # "interfacename", but no "node", or "nodegraph"
                    if sourceDirection == UsdShade.AttributeType.Input:
                        mtlxConnectString = 'interfacename'
                        mtlxConnectItem = sourcePort

                        # Set the connection
                        newInput.setAttribute(mtlxConnectString, mtlxConnectItem)

                    else:
                        # A nodegraph->output connect uses "nodegraph" vs "node"                        
                        if sourcePrim.IsA(UsdShade.NodeGraph):
                            mtlxConnectString = 'nodegraph'

                        # Set the connection
                        newInput.setAttribute(mtlxConnectString, mtlxConnectItem)

                        # An output->intput connection is denoted using
                        # an additional `output` attribute` if the source is 
                        # does not have multiple outputs
                        if sourceDirection == UsdShade.AttributeType.Output:
                            if isMultiOutput(sourcePrim):
                                newInput.setAttribute('output', sourcePort)                    
 
            # Set value if not connected.
            else:
                usdVal = input.Get()
                if usdVal is not None:
                    newInput = parent.addInput(usdBaseName, mtlxType)
                    if newInput:
                        mtlxVal = mapUsdValueToMtlx(mtlxType, usdVal)
                        if mtlxVal is not None:
                            newInput.setValueString(mtlxVal)
    
    # Emit outputs if specified. Unlike Usd, outputs are not explicitly defined
    # except for nodegraph. The branching toggle `emitOuputs` allows for outputs to be selectively emitted.
    if emitOutputs:
        for output in shader.GetOutputs():
            if output:

                usdType = output.GetTypeName()

                mtlxType = mapUsdTypeToMtlx(usdType)
                usdBaseName = output.GetBaseName()
                #usdFullName = output.GetFullName()
                
                mtlxType = mapUsdTokenToType(mtlxType, usdBaseName)
                usdBaseName = usdBaseName.replace(':', '_')    
                newOutput = parent.addOutput(usdBaseName, mtlxType)

                if output.HasConnectedSource():
                    usdSources, invalidSources = output.GetConnectedSources() 
                    if usdSources and usdSources[0]:
                        # Check UsdShadeConnectionSourceInfo
                        usdSource1 = usdSources[0]
                        sourcePrim = usdSource1.source.GetPrim()
                        sourcePort = usdSource1.sourceName
                        sourceDirection = usdSource1.sourceType
                        sourceType = usdSource1.typeName

                        mtlxConnectString = 'nodename'
                        mtlxConnectItem = sourcePrim.GetName()

                        # An input->output connection should never occur
                        # and is ignored
                        #if sourceDirection == UsdShade.AttributeType.Input:

                        # Handle adding in node or nodegraph depending on source
                        # prim type.                                
                        if sourcePrim.IsA(UsdShade.NodeGraph):
                            mtlxConnectString = 'nodegraph'

                        newOutput.setAttribute(mtlxConnectString, mtlxConnectItem)

                        # Handle output->output connection
                        if sourceDirection == UsdShade.AttributeType.Output:
                            if isMultiOutput(sourcePrim):
                                newOutput.setAttribute('output', sourcePort)


# %% [markdown]
# #### 4.2.4 Top Level Translation Logic
# 
# A final utility interface called `emitMaterialX()` wraps up the top level translation logic.
# 
# As in the previous example a tree traversal is performed. 
# 
# The main addition is to create a MaterialX a `shader`, `nodegraph` or `material` when encountered and then adding in child portsusing the MaterialX utilities described.
# 
# For shader nodes, an additional check for an associated definition is performed. The MaterialX definition identifier is assumed to be available in the default `id` attribute using the `UsdShadeShader` interface <a href="https://openusd.org/release/api/class_usd_shade_shader.html" target="_blank">GetIdAttr().</a> 
# 
# Notes:
# 1. Usd materials are considered to be *node graphs*, while in MaterialX materials are *nodes* which connect to surface, volume or displacement shaders. During conversion anything else must be located at the same level as the material and not nested within the material graph as in Usd. Previously to version 1.38.6, MaterialX materials were closer in nature to Usd materials as they also embedded shader associations as part of the material and materials were not nodes.
# 2. Usd separates out the functional API from the primitive and as such an interface needs to be instantiated given a `UsdPrim`. This differs from MaterialX which does not separate out the functional API, with all types deriving from a common `Element` class.
# 3. Saved paths in Usd are *absolute* while paths in MaterialX are *relative* to the current parent scope. Usd has a root path specifier '/' while MaterialX does not. 
# 4. No specific logic is required to handle different definition versions as long as a different `nodedef` identifier is used for different versions. This should be the case within MaterialX and when MaterialX `nodedefs` are loaded into the Usd shader registriy (`Sdr`) 
# 
# As MaterialX supports native definitions for Usd shader nodes these can also be handled. For example we assume if the node definition is `UsdPreviewSurface` that this maps directly to a MaterialX node. 

# %%

def emitMaterialX(stage, indent, prim, parent):
    """
    Emit MaterialX for a given Usd Stage starting at a given root.
    Currently only nodegraphs, material and shader nodes are supported.
    """
    if prim:
        # Test if it's a material first as a material is a nodegraph
        if prim.IsA(UsdShade.Material) and not prim.GetChildren(): 
            doc = parent.getDocument()
            usdMaterial = UsdShade.Material(prim)
            mtlxName = parent.createValidChildName(prim.GetName())
            mtlxMaterial = parent.addMaterialNode(mtlxName)
            emitMtlxValueElements(usdMaterial, mtlxMaterial, False)

        elif prim.IsA(UsdShade.NodeGraph):
            doc = parent.getDocument()
            usdNodegraph = UsdShade.NodeGraph(prim)
            mtlxName = parent.createValidChildName(prim.GetName())
            mtlxNodeGraph = parent.addChildOfCategory('nodegraph', mtlxName)
            parent = mtlxNodeGraph
            emitMtlxValueElements(usdNodegraph, mtlxNodeGraph, True)

        elif prim.IsA(UsdShade.Shader): 
            usdShader = UsdShade.Shader(prim)
            mtlxNodeDefId = ''
            
            # Note: Only consider when the definition is specified in the identifier
            usdImplAttr = usdShader.GetImplementationSourceAttr()
            if usdImplAttr.Get() == 'id':
                mtlxNodeDefId = usdShader.GetIdAttr().Get()

            # Do a manual rename for built in UsdPreviewSurface
            # Could be done for other built-ins which have MaterialX
            # definitions.
            if mtlxNodeDefId == 'UsdPreviewSurface':
                mtlxNodeDefId = 'ND_UsdPreviewSurface_surfaceshader'

            # Look for an existing definition. If found add an instance and populate
            # it's inputs and outputs.
            doc = parent.getDocument()
            mtlxNodeDef = doc.getNodeDef(mtlxNodeDefId)
            if mtlxNodeDef:
                mtlxShadername = parent.createValidChildName(prim.GetName())
                shaderNode = parent.addNodeInstance(mtlxNodeDef, mtlxShadername)                
                emitMtlxValueElements(usdShader, shaderNode, False)
            else:
                print('Skipping shader node %s: No MaterialX definition found.' % prim.GetName())  

        children = prim.GetChildren()
        for child in children:
            emitMaterialX(stage, indent+indent, child, parent)

def convertUsdToMtlx(stage, stdlib):

    doc = mx.createDocument()
    doc.importLibrary(stdlib)

    # Start at the root and emit child nodes 
    prim = stage.GetPrimAtPath('/')
    children_refs = prim.GetChildren()
    for child in children_refs:
        emitMaterialX(stage, ' ', child, doc)

    return doc

doc = convertUsdToMtlx(stage, stdlib)

# Write results to Markdown / file
writeOptions = mx.XmlWriteOptions()
writeOptions.writeXIncludeEnable = False
writeOptions.elementPredicate = skipLibraryElement
documentContents = mx.writeToXmlString(doc, writeOptions)

display_markdown('### Resulting Generated MaterialX', raw=True)
display_markdown('```xml\n' + documentContents + '\n```\n', raw=True)

mx.writeToXmlFile(doc, 'test_usd_mtlx.mtlx', writeOptions)

# %% [markdown]
# ## 5. Updating MaterialX / Usd Inputs 
# 
# There are different ways to approach handling an edit in Usd and then updating the corresponding MaterialX.
# This example only handles **value** changes by updating matching inputs via `path` lookups in Usd and MaterialX.
# 
# That is, the absolute Usd `path` is used to find the Usd input in the `stage`, and the corresponding MaterialX input in the working `document`. 
# * The stage interface <a href="https://openusd.org/release/api/class_usd_stage.html" target="_blank">GetPrimAtPath()</a> is used to lookup the node to edit in Usd, and 
# * The document interface <a href="https://materialx.org/docs/api/class_element.html" target="_blank">getDescendent()</a> used for MaterialX.
# * The input on each node is then found using <a href="https://openusd.org/release/api/class_usd_shade_connectable_a_p_i.html" target="_blank">GetInput()</a> and <a href="https://materialx.org/docs/api/class_interface_element.html" target="_blank">getInput()</a> for Usd and MaterialX respectively.
# 
# Note that the Usd `path` differs from the MaterialX `path` as MaterialX does not accept a path that starts with
# '/' in it's path related interfaces. 
# > *This would be a good discrepancy to address, which could just be an implementation issue*.
# 
# Monitoring and updating for graph connections is beyond the scope of this example, but it is useful to consider whether the target workflow involves just MaterialX data model updates or if code generation is involved as is the case for render delegates using MaterialX code generation.

# %%
# Note that the MaterialX path cannot start with '/' otherwise `getDescendent)` will fail to
# find the element. 
mtlxPath = 'collect1/my_materialx_subnet/mtlxstandard_surface1' 

# Add additional path nesting in the Usd stage
usdPath = '/mySphere/mtl/' + mtlxPath 

# Input to modify
inputName = 'coat_roughness'

# Update the input in Usd
currentValue = 999
prim = stage.GetPrimAtPath(usdPath)
if prim:
    stdsurf = UsdShade.Shader(prim)
    surfInput = stdsurf.GetInput(inputName)
    if surfInput:
        currentValue = surfInput.Get()
        surfInput.Set(0.9)

        print('Modified Usd from: %g to %g' % (currentValue, surfInput.Get()))

# Update the input in MaterialX
currentValue = 999
mtxlStdSurf = doc.getDescendant(mtlxPath)
if mtxlStdSurf:
    mtlxSurfInput = mtxlStdSurf.getInput(inputName)
    if mtlxSurfInput:
        currentValue = mtlxSurfInput.getValueString()
        mtlxSurfInput.setValue(0.9)

        print('Modified MaterialX from: %s to %s' % (currentValue, mtlxSurfInput.getValueString()))


# %% [markdown]
# ## 6. MaterialX to Usd Example
# 
# For completeness, we add in sample logic to convert from MaterialX to Usd. This is not meant to be a substitute for the `UsdMtlx` plugin. By default this module is not currently available as part of the core Python package for Usd
# so is not available unless a custom / local build is used.
# 
# To start, manual creation of Usd nodes based on the `marble` example demonstrates usage of some basic interfaces of shaders, materials, graphs, and ports.
# 
# Logic to consider includes creating the appropriate UsdShade type, setting a definition (`nodedef`) association, translating value and type constructs, and forming port connections. 
# 
# Of note:
# 1. Outputs are explicitly created on nodes as well as nodegraphs (unlike MaterialX)
# 2. The explicit setting of the node definition name as the as the identifier to the <a href="https://openusd.org/release/api/class_sdr_registry.html" target="_blank">SdrRegistry</a>

# %%

def createSimpleMtlx(stage):
    """
    Hard coded simple MaterialX to Usd example which produces 
    part of the marble example. 
    """        
    material = UsdShade.Material.Define(stage, '/Marble_3D')

    # Create a standard surface shader
    stdSurfShader = UsdShade.Shader.Define(stage, '/SR_marble1')
    stdSurfShader.CreateIdAttr("ND_standard_surface_surfaceshader")
    stdSurfShader.CreateInput("base_color", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(0.8, 0.8, 0.8))
    stdSurfShader.CreateInput("specular_roughness", Sdf.ValueTypeNames.Float).Set(0.1)
    stdSurfShader.CreateInput("subsurface", Sdf.ValueTypeNames.Float).Set(0.4)
    stdSurfShader.CreateInput("subsurface_color", Sdf.ValueTypeNames.Float).Set(0.0)

    # Connect shader to material. Note that an output is explicitly created.
    nodeOutput = material.CreateSurfaceOutput()
    if nodeOutput:
        nodeOutput.ConnectToSource(stdSurfShader.ConnectableAPI(), "surface")

    # Create upstream pattern graph
    patternGraph = UsdShade.NodeGraph.Define(stage, '/NG_marble1')
    graphOutput = patternGraph.CreateOutput('out', Sdf.ValueTypeNames.Color3f)

    # Connect graph to shader input. Note that as with MaterialX, the existing value is not removed,
    base_color = stdSurfShader.GetInput('base_color')
    if base_color:
        base_color.ConnectToSource(patternGraph.ConnectableAPI(), "out")
        base_color.Set(Gf.Vec3f(1, 1, 1))

marbleStage = Usd.Stage.CreateInMemory()
createSimpleMtlx(marbleStage)
stringResult = marbleStage.GetRootLayer().ExportToString()
display_markdown('```usd\n' + stringResult + '\n```\n', raw=True)

# %% [markdown]
# ### 6.1 MaterialX to Usd Utilities
# 
# For arbitrary MaterialX graphs, a series of utilities is provided to perform the translation.
# 
# This is again to show any notable differences in nomenclature, API, and mappings between Usd and MaterialX
# but in this case for the reverse mapping from MaterialX to Usd. 
# 
# All logic creates the minimal amount of nesting to reflect how MaterialX does not support nesting via non-nested node graphs.

# %% [markdown]
# #### 6.1.1 MaterialX to Usd : Type and Value Mapping
# 
# The `mapMtxToUsdType()` and `mapMtxToUsdValue()` utilities provide mappings for type and value respectively. 
# The mapping is from MaterialX type name to an Usd <a href="https://openusd.org/release/api/class_sdf_value_type_name.html" target="_blank">Sdf</a> type, and from a MaterialX `Value` to a Usd `Gf` value. 

# %%
def mapMtxToUsdType(mtlxType):
    """
    Map a MaterialX type to an Usd Sdf type

    Parameters:
    -----------
    - mtxType : string
        MaterialX type 
    """
    mtlxUsdMap = dict()
    mtlxUsdMap['filename'] = Sdf.ValueTypeNames.Asset
    mtlxUsdMap['string'] = Sdf.ValueTypeNames.String
    mtlxUsdMap['boolean'] = Sdf.ValueTypeNames.Bool
    mtlxUsdMap['integer'] = Sdf.ValueTypeNames.Int
    mtlxUsdMap['float'] = Sdf.ValueTypeNames.Float
    mtlxUsdMap['color3'] = Sdf.ValueTypeNames.Color3f
    mtlxUsdMap['color4'] = Sdf.ValueTypeNames.Color4f
    mtlxUsdMap['vector2'] = Sdf.ValueTypeNames.Float2    
    mtlxUsdMap['vector3'] = Sdf.ValueTypeNames.Vector3f    
    mtlxUsdMap['vector4'] = Sdf.ValueTypeNames.Float4    
    mtlxUsdMap['surfaceshader'] = Sdf.ValueTypeNames.Token

    if mtlxType in mtlxUsdMap:
        return mtlxUsdMap[mtlxType]
    return Sdf.ValueTypeNames.Token

def mapMtxToUsdValue(mtlxType, mtlxValue):
    """
    Map a MaterialX value of a given type to a Usd value.
    Note: Not all types are included here.
    """
    usdValue = '__'
    if mtlxType == 'float':
        usdValue = mtlxValue
    elif mtlxType == 'integer':
        usdValue = mtlxValue
    elif mtlxType == 'boolean':                    
        usdValue = mtlxValue
    elif mtlxType == 'string':                    
        usdValue = mtlxValue
    elif mtlxType == 'filename':  
        usdValue = mtlxValue
    elif mtlxType == 'vector2':
        usdValue = Gf.Vec2f( mtlxValue[0], mtlxValue[1] )
    elif mtlxType == 'color3' or mtlxType == 'vector3':
        usdValue = Gf.Vec3f( mtlxValue[0], mtlxValue[1], mtlxValue[2] )
    elif mtlxType == 'color4' or mtlxType == 'vector4':
        usdValue = Gf.Vec4f( mtlxValue[0], mtlxValue[1], mtlxValue[2], mtlxValue[3] )

    return usdValue

# %% [markdown]
# #### 6.1.2 MaterialX to Usd Connection Mapping
# 
# The logic to create connections is simpler going from MaterialX to Usd as all that is required is to assemble the appropriate absolute prim path.
# 
# Similar to the logic shown for the *Nodegraph Traversal* book, node and interface discovery needs to be performed
# by parsing the `node`, `nodegraph`, `interface` and `output` attributes. 
# 
# Note that when looking for the node to connect to, the document root has an empty path string so logic must be
# added to insert the required Usd root string '/'. **Again this would not be required if the root '/' specifier
# was supported in MaterialX, and the document path (from `getNamePath()` return '/' instead of an empty string)** 
# 
# Also note that for this example, geometric bindings including `defaultgeomprop` are not handled to create upstream input streams as they are in `UsdMtlx`.

# %%
def emitUsdConnections(node, stage):
    """ 
    Emit connections between MaterialX elements as Usd connections for 
    a given MaterialX node.

    Paramters:
    - node : 
        MaterialX node to examine
    - stage :
        Usd stage to write connection to
    """
    if not node:
        return

    for valueElement in node.getActiveValueElements():
        isInput = valueElement.isA(mx.Input) 
        isOutput = valueElement.isA(mx.Output)
        if  isInput or isOutput:

            interfacename = ''

            # Find out what type of element is connected to upstream:
            # node, nodegraph, or interface input.
            mtlxConnection = valueElement.getAttribute('nodename')
            if not mtlxConnection:
                mtlxConnection = valueElement.getAttribute('nodegraph')
            if not isOutput:
                if not mtlxConnection:
                    mtlxConnection = valueElement.getAttribute('interfacename')
                    interfacename = mtlxConnection 

            connectionPath = ''
            if mtlxConnection:

                # Handle input connection by searching for the appropriate parent node.
                # - If it's an interface input we want the parent nodegraph. Otherwise
                # we want the node or nodegraph specified above.
                # - If the parent path is the root (getNamePath() is empty), then this is to 
                # nodes at the root document level. 
                if isInput:
                    parent = node.getParent()
                    if parent.getNamePath():
                        if interfacename:
                            connectionPath = '/' + parent.getNamePath()
                        else:
                            connectionPath = '/' + parent.getNamePath() + '/' + mtlxConnection
                    else:
                        # The connectio is to a prim at the root level so insert a '/' identifier
                        # as getNamePath() will return an empty string at the root Document level.
                        if interfacename:
                            connectionPath = '/'
                        else:
                            connectionPath = '/' + mtlxConnection

                # Handle output connection by looking for sibling elements
                else:
                    parent = node.getParent()                    
                    
                    # Connection is to sibling under the same nodegraph
                    if node.isA(mx.NodeGraph):
                        connectionPath = '/' + node.getNamePath() + '/' + mtlxConnection
                    else:
                        # Connection is to a nodegraph parent of the current node 
                        if parent.getNamePath():
                            connectionPath = '/' + parent.getNamePath() + '/' + mtlxConnection
                        # Connection is to the root document.
                        else:
                            connectionPath = '/' + mtlxConnection

                # Find the source prim
                # Assumes that the source is either a nodegraph, a material or a shader
                sourcePrim = None
                sourcePort = 'out'
                source = stage.GetPrimAtPath(connectionPath)
                if source:
                    if source.IsA(UsdShade.NodeGraph):
                        sourcePrim = UsdShade.NodeGraph(source)
                    elif source.IsA(UsdShade.Material): 
                        sourcePrim = UsdShade.Material(source)
                    elif source.IsA(UsdShade.Shader): 
                        sourcePrim = UsdShade.Shader(source)

                    # Special case handle interface input vs an output
                    if interfacename:
                        sourcePort =  interfacename
                    else:                          
                        sourcePort = valueElement.getAttribute('output')
                        if not sourcePort:
                            sourcePort = 'out'
                    if sourcePort:
                        mtlxConnection = mtlxConnection + '. Port:' + sourcePort

                else:
                    print('> Failed to find source at path:', connectionPath)

                # Find destination prim and port and make the appropriate connection.
                # Assumes that the destination is either a nodegraph, a material or a shader
                destInput = None
                if sourcePrim:
                    dest = stage.GetPrimAtPath('/' + node.getNamePath())
                    if not dest:
                        print('> Failed to find dest at path:', node.getNamePath())
                    else:
                        destPort = None
                        portName = valueElement.getName()
                        destNode = None
                        if dest.IsA(UsdShade.NodeGraph):
                            destNode = UsdShade.NodeGraph(dest)
                        elif dest.IsA(UsdShade.Material): 
                            destNode = UsdShade.Material(dest)
                        elif dest.IsA(UsdShade.Shader): 
                            destNode = UsdShade.Shader(dest)
                        else:
                            print('> Encountered unsupport destinion type')

                        # Find downstream port (input or output)
                        if destNode:
                            if isInput:
                                destPort = destNode.GetInput(portName)
                            else:
                                destPort = destNode.GetOutput(portName)                                

                        # Make connection to interface input, or node/nodegraph output
                        if destPort:
                            if interfacename:
                                interfaceInput = sourcePrim.GetInput(sourcePort) 
                                if interfaceInput:
                                    if not destPort.ConnectToSource(interfaceInput):
                                        print('> Failed to connect: ', source.GetPrimPath(), '-->', destPort.GetFullName())
                            else:
                                sourcePrimAPI = sourcePrim.ConnectableAPI()
                                if not destPort.ConnectToSource(sourcePrimAPI, sourcePort):
                                    print('> Failed to connect: ', source.GetPrimPath(), '-->', destPort.GetFullName())


# %% [markdown]
# #### 6.1.3 MaterialX to Usd Value Element Mapping
# 
# Similar to how MaterialX <a href="https://materialx.org/docs/api/class_value_element.html" target="_blank">ValueElements</a> are created from Usd, the `emitUsdValueElements()` utility parses `ValueElements` to create Usd inputs and outputs. 
# 
# In this example code, it is possible to create all the inputs based on the MaterialX definition if desired to provide a 'complete' interface for the Usd shader instance. For compactness, MaterialX does not create these additional inputs when instantiating a MaterialX node instance by default. It may be useful to do so for Usd instantiation to avoid any later dependency on the original MaterialX definition, especially if they are not registered in the Usd shader registry (`Sdr`). 
# 
# Any inputs created from definitions will have default values which are overwritten by any values explicitly specified on the node instance. 
# 
# <a href="https://materialx.org/docs/api/class_interface_element.html" target="_blank">getActiveValueElements()</a> instead of `getValueElements()` is used when examining definitions and instances to ensure that inherited inputs or outputs are included.

# %%
def emitUsdValueElements(node, usdNode, emitAllValueElements):
    """
    Emit MaterialX value elements in Usd.

    Parameters
    ------------    
    node: 
        MaterialX node with value elements to scan
    usdNode:
        UsdShade node to create value elements on.
    emitAllValueElements: bool
        Emit value elements based on node definition, even if not specified on node instance.      
    """
    if not node:
        return    
 
    # Instantiate with all the nodedef inputs (if emitAllValueELements is True).
    # Note that outputs are always created.
    nodedef = node.getNodeDef()
    if nodedef:
        for valueElement in nodedef.getActiveValueElements():
            if valueElement.isA(mx.Input):
                if emitAllValueElements:
                    mtlxType = valueElement.getType()
                    usdType = mapMtxToUsdType(mtlxType)
                    usdInput = usdNode.CreateInput(valueElement.getName(), usdType)

                    if len(valueElement.getValueString()) > 0:
                        mtlxValue = valueElement.getValue()
                        usdValue = mapMtxToUsdValue(mtlxType, mtlxValue)
                        if usdValue != '__':
                            usdInput.Set(usdValue)

            elif valueElement.isA(mx.Output):
                usdOutput = usdNode.CreateOutput(valueElement.getName(), mapMtxToUsdType(valueElement.getType()))

            else:
                print('- Skip mapping of definition element: ', valueElement.getName(), '. Type: ', valueElement.getCatetory())

    # From the given instance add inputs and outputs and set values.
    # This may override the default value specified on the definition.
    for valueElement in node.getActiveValueElements():
        if valueElement.isA(mx.Input):
            mtlxType = valueElement.getType()
            usdType = mapMtxToUsdType(mtlxType)
            usdInput = usdNode.CreateInput(valueElement.getName(), usdType)

            # Set value. Note that we check the length of the value string
            # instead of getValue() as a 0 value will be skipped.
            if len(valueElement.getValueString()) > 0:
                mtlxValue = valueElement.getValue()
                usdValue = mapMtxToUsdValue(mtlxType, mtlxValue)
                if usdValue != '__':
                    usdInput.Set(usdValue)

        elif valueElement.isA(mx.Output):
            usdOutput = usdNode.GetInput(valueElement.getName())
            if not usdOutput:
                usdOutput = usdNode.CreateOutput(valueElement.getName(), mapMtxToUsdType(valueElement.getType()))

        else:
            print('- Skip mapping of element: ', valueElement.getNamePath(), '. Type: ', valueElement.getCatetory())


# %% [markdown]
# #### 6.1.4 Emitting Usd Shading Graphs
# 
# To emit the Usd shading network a utility function called `emitUsdShaderGraph()` is added.
# 
# * For each node, nodegraph, or material in the MaterialX document a corresponding node is created in Usd using:
#   * `UsdShade.Shader.Define()`, 
#   * `UsdShade.NodeGraph.Define()`, and 
#   * `UsdShade.Material.Define()` respectively. 
# * All MaterialX node instances are checked for a corresponding MaterialX definition (`nodedef`), and if found will set
# the identifier as the shader id for the Usd shader node.
# * Connections are then made between Usd nodes based on the connections found on MaterialX nodes.

# %%
def emitUsdShaderGraph(doc, stage, mxnodes, emitAllValueElements):
    """
    Emit Usd shader graph to a given stage from a list of MaterialX nodes.

    Parameters
    ------------    
    doc: 
        MaterialX source document
    stage:
        Usd target stage
    mxnodes:
        MaterialX shader nodes.
    emitAllValueElements: bool
        Emit value elements based on node definition, even if not specified on node instance.      
    """
    # Emit Usd nodes
    for v in mxnodes:
        elem = doc.getDescendant(v)

        # Note that MaterialX does not use absolute path notation while Usd
        # does. This will result in an error when trying set the path
        usdPath = '/' + elem.getNamePath()

        nodeDef = None
        usdNode = None
        if elem.getType() == 'material':
            usdNode = UsdShade.Material.Define(stage, usdPath)                
        elif elem.isA(mx.Node):
            nodeDef = elem.getNodeDef()
            usdNode = UsdShade.Shader.Define(stage, usdPath)
        elif elem.isA(mx.NodeGraph):
            usdNode = UsdShade.NodeGraph.Define(stage, usdPath)

        if usdNode:
            if nodeDef:
                usdNode.SetShaderId(nodeDef.getName())
            emitUsdValueElements(elem, usdNode, emitAllValueElements)

    # Emit connections between Usd nodes
    for v in mxnodes:
        elem = doc.getDescendant(v)
        usdPath = '/' + elem.getNamePath()

        if elem.getType() == 'material':
            emitUsdConnections(elem, stage)                
        elif elem.isA(mx.Node):
            emitUsdConnections(elem, stage)                
        elif elem.isA(mx.NodeGraph):
            emitUsdConnections(elem, stage)                


# %% [markdown]
# #### Top Level Conversion Logic
# 
# The sample wrapper for conversion is called `convertMtlxToUsd()` which takes as input a MaterialX filename,
# creates a stage in memory and then performs the conversion.
# 
# As noted in the <a href="https://kwokcb.github.io/MaterialX_Learn/documents/documents.html">Documents</a> learning material MaterialX has one working document, and the node definitions are required to be part of this document. To avoid accidentally translating those definitions, the scene nodes are first determined using a utility: `findMaterialXNodes()`.

# %%
def findMaterialXNodes(doc):
    """
    Find all nodes in a MaterialX document
    """
    visitedNodes = []
    treeIter = doc.traverseTree()
    for elem in treeIter:
        path = elem.getNamePath()
        if path in visitedNodes:
            continue
        visitedNodes.append(path)
    return visitedNodes

# %% [markdown]
# 
# Pruning based on source URI could also be performed as for export but it is easier to pre-parse the document without any definitions before loading in the definitions.

# %%
def convertMtlxToUsd(mtlxFileName, emitAllValueElements):
    """
    Read in a MaterialX file and emit it to a new Usd Stage
    Dump results for display and save to usda file.

    Parameters:
    -----------
    mtlxFileName : string
        Name of file containing MaterialX document. Assumed to end in ".mtlx"
     emitAllValueElements: bool
        Emit value elements based on node definition, even if not specified on node instance.         
    """
    stage = Usd.Stage.CreateInMemory()
    
    doc = mx.createDocument()
    mtlxFilePath = mx.FilePath(mtlxFileName)
    if not mtlxFilePath.exists():
        print('Failed to read file: ', mtlxFilePath.asString())
        return
    
    # Find nodes to transform before importing the definition library
    mx.readFromXmlFile(doc, mtlxFileName)
    mxnodes = findMaterialXNodes(doc)
    doc.importLibrary(stdlib)
    
    # Translate
    emitUsdShaderGraph(doc, stage, mxnodes, emitAllValueElements)
        
    # Examine the results and save to file
    stringResult = stage.GetRootLayer().ExportToString()
    display_markdown('```usd\n' + stringResult + '\n```\n', raw=True)

    usdFile = mtlxFileName.removesuffix('.mtlx')
    usdFile = usdFile + '.usda'
    stage.Export(usdFile, False)

    return stage

# %% [markdown]
# ### Test Files
# 
# Conversion to a few test files is performed, including performing the reverse translation of the Usd sample file shown previously.

# %% [markdown]
# #### Sample Marble
# 
# For the `marble` example, we turn on the option that will create a Usd node input using all the inputs specified on the definition of each MaterialX shader node instance.

# %%
testFile = 'data/standard_surface_marble_solid.mtlx'

# Convert to Usd. Indicate to include all inputs based on a MaterialX node's definition
# as opposed to just those explicitly specified on the node instance.
display_markdown('#### Sample Marble Converted from MaterialX', raw=True)
includeDefinitionInputs = True
stage = convertMtlxToUsd(testFile, includeDefinitionInputs)

# Convert back to MaterialX
doc = convertUsdToMtlx(stage, stdlib)
result, error = doc.validate()
if error:
    print(error)
writeOptions = mx.XmlWriteOptions()
writeOptions.writeXIncludeEnable = False
writeOptions.elementPredicate = skipLibraryElement
documentContents = mx.writeToXmlString(doc, writeOptions)
display_markdown('#### ... And Converted Back To MaterialX', raw=True)
display_markdown('```xml\n' + documentContents + '\n```\n', raw=True)

# %% [markdown]
# #### Sample Nodegraph from NodeGraph Tutorial
# 
# Here the example MaterialX file produced from the *Nodegraph* book is converted.

# %%
testFile = 'data/sample_nodegraph.mtlx'
display_markdown('#### Sample Tutorial Nodegraph Converted from MaterialX', raw=True)
stage = convertMtlxToUsd(testFile, False)

# Convert back to MaterialX
doc = convertUsdToMtlx(stage, stdlib)
writeOptions = mx.XmlWriteOptions()
writeOptions.writeXIncludeEnable = False
writeOptions.elementPredicate = skipLibraryElement
documentContents = mx.writeToXmlString(doc, writeOptions)
display_markdown('#### ... And Converted Back To MaterialX', raw=True)
display_markdown('```xml\n' + documentContents + '\n```\n', raw=True)

# %% [markdown]
# #### Re-import Usd Example Converted to MaterialX
# 
# Finally, the MaterialX file converted from Usd previously is re-converted back into Usd.
# 
# For validation purposes bi-directional conversion and compare is useful to ensure there is no loss of data when
# performing data model interop. At time of writing, this round trip logic is not easily accessible.

# %%
testFile = 'blender_to_mtlx.mtlx'
display_markdown('#### Nested Nodegraph Converted from MaterialX', raw=True)
stage = convertMtlxToUsd(testFile, False)

# %% [markdown]
# ## Appendix: Mapping Usd Types To MaterialX Types
# 
# For a completeness a full mapping of the following applicable Usd types should be performed. Most are mappable but type mapping can be "lossy" as there is no concept of type precision (half, float, double) for instance.

# %%
typestring = ''
for t in dir(Sdf.ValueTypeNames):
    if t.startswith('__'):
        continue
    typestring = typestring + '- Type : ' + str(t) + '\n'
display_markdown('### Usd Types', raw=True)
display_markdown(typestring, raw=True)


