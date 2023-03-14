# %% [markdown]
# # USD and MaterialX NodeGraphs
# 
# This notebook will look at some of the basic interop between MaterialX and USD focusing on nodegraphs and nodes.
# Material assignment will not be examined, nor is the intent to provide a tutorial about Usd, which can be found in other places
# such as from <a href="https://docs.omniverse.nvidia.com/prod_usd/prod_usd/python-snippets.html" target="_blank">NVIDIA</a>, and <a href="https://www.sidefx.com/docs/houdini/solaris/usd.html" target="_blank">Houdini</a>
# 
# Topics covered include:
# 1. Usd and MaterialX Package Setup
# 2. Reading in a Usd file with MaterialX materials
# 3. Traverse the Usd stage and extract out materials and shader graphs.
# Some basic attributes will be extracted to demonstrate some points and is not meant
# to be a full exporter.

# %% [markdown]
# ## Usd Setup
# 
# In addition to MaterialX Usd modules naturally need to be imported. As a starting point Usd "core" can be installed as follows: 

# %%
pip install usd-core

# %% [markdown]
# After installation various packages can be imported.  `Usd`, `UsdShade`, `Sdf` are the main packages required. The MaterialX package is also imported. 

# %%
from pxr import Usd
from pxr import UsdShade
from pxr import Sdf

# Not necessary
from pxr import UsdGeom

import MaterialX as mx

[ major, minor, build ] = Usd.GetVersion()  
print('Using Usd Version:', str(major) + "." + str(minor) + "." + str(build))
print('Using MaterialX Version:', mx.getVersionString())

# %% [markdown]
# As input, we load in an example Usd file that contains a shading network with nodes which have MaterialX definitions.

# %%
# Load in a sample file
stage = Usd.Stage.Open('sphere_with_nodegraphs.usda') 

# Flatten layers
stage.Flatten()

# Print as String
stringResult = stage.GetRootLayer().ExportToString()
print(stringResult)

# %% [markdown]
# Some minor modifications will be made

# %%
prim = stage.GetPrimAtPath('/mySphere/mtl/collect1/my_materialx_subnet/mtlxstandard_surface1')
stdsurf = UsdShade.Shader(prim)
surfInput = stdsurf.GetInput('coat_roughness')
surfInput.Set(1.0)

print(surfInput.Get())

# %% [markdown]
# ## Start Traversal
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
# ## Examining Shader Graphs
# 
# This can be refined to only example shader network nodes and ports.
# 
# Two utility functions are be added:
#  
# * `printValueElements` selectively examines inputs and outputs using `GetInputs()` and `GetOutputs` on a shader. Tokens are not considered in this example. 
# 
# * `printShaders` performs the traversal from a root prim visiting prims which would map to MaterialX -- namely "node graphs", "material" and "shader" nodes. Any geometry and tree nesting is ignored. For shader nodes, an additional check for the a definition is made.
# using `GetIdAttr()`. 
# 
# Note that the Python API for Usd requires explicit casting to the desired type before
# methods for that type can be used.

# %%
def printValueElements(shader, indent):
    for input in shader.GetInputs():
        if input:
            print(indent, '- Input:', input.GetBaseName())
    for output in shader.GetOutputs():
        if output:
            print(indent, '- Output:', output.GetBaseName())

def printShaderNodes(indent, prim):
    """
    Print out shader nodes
    """
    # Use RTTI to check for type. Ignore all other types
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
# ## Usd to MaterialX Example
# 
# Finally, to the previous example logic is added to create MaterialX elements which correspond to Usd elements. 
# 
# The first step is to add in a basic setup for MaterialX to create a working document and load in standard definitions.
# 

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
# To aid in the translation, a series of utilities is used to perform Usd to MaterialX mappings:
# 
# 1. The utility `mapUsdTypeToMtlx()` maps native Usd types to MaterialX native type. This is just for example and is not a complete mapping.

# %%

def mapUsdTypeToMtlx(usdType):
    """ Map a Usd type to a MaterialX type. Note this is not a complete mapping"""
    usdTypeString = str(usdType)
    mtlxType = 'color3'
    if 'color3' in usdTypeString:
        mtlxType ='color3'
    elif 'vector3' in usdTypeString:
        mtlxType ='vector3'
    elif 'float' == usdType:
        mtlxType ='float'
    elif 'token' in usdTypeString:
        mtlxType = 'TOKEN'
    else:
        mtlxType = 'usdType'
        #print('-----> handle type:', usdType)
    return mtlxType


# %% [markdown]
# 2. `isMultiOutput` is used to determine if the Usd prim (nodegraph, shader or material)
# has multiple outputs. This is required as MaterialX connection has specific syntax to specify the output (port) on an upstream element, but this is only done for upstream elements which have multiple outputs ('multioutput') 

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
# 3. `emitMtlxValueELements` handles the mapping of Usd inputs and outputs to MaterialX inputs and outputs. This includes:
#   * Creating the input / output. Unlike Usd which has explicit outputs, MaterialX never specifies outputs on nodes, only on nodegraphs. This difference is handled when visiting Usd outputs.
#   * Setting a value **or**
#   * Setting connection attributes. Unlike Usd which has a single `connect` syntax and corresponding API for connection logic and behaviour, MaterialX is purely string based and can require multiple attributes specified for a connection. This depends on: 
#     * if the upstream element is a `nodegraph` or `node`; 
#     * if the connection is to an upstream `interface` input or output; and 
#     * if the upstream node has multiple outputs (`multioutput`)
#     * if there is a specific channel extracted from the upstream port. This logic is not included as part of this example.
# 
# Notes:
# 
# 1. Additional scoping in Usd is not preserved in this example. (Something like `namepspace` could be used for export to MaterialX but this does not translate to nesting in Usd on import). 
# 
# 2. It is assumed that the Usd string representation for a value can be 
# mapped to a MaterialX one. For example, the string representation for a vector3 (`(v1, v2, v3)`) in Usd is valid syntax in MaterialX (`v1, v2, v3`).
# 
# 3. For a port with a  `token` type the type of the created MaterialX input / output can be set based on the port's name if the Usd Port name is a  'surface' or 'displacement' shader.
# (There appears to be no way by just examining the Usd shader network to determine the type without this assumption at this time)

# %%

def emitMtlxValueElements(stage, shader, indent, parent, emitOutputs):
    """
    Emit MaterialX value elements (currently only Inputs and Outputs)
    This is not a complete translation of all value element attributes.
    """
    for input in shader.GetInputs():

        # Only output if there is a value or a connection
        if input and (input.Get() or input.HasConnectedSource()):

            # Map Usd type to Mtlx type and create an input
            usdType = input.GetTypeName()
            mtlxType = mapUsdTypeToMtlx(usdType)
            usdInputName = input.GetBaseName()
            newInput = parent.addInput(usdInputName, mtlxType)

            # Add a connection if it exists
            if input.HasConnectedSource():
                usdSources = input.GetConnectedSources() 
                if usdSources and usdSources[0]:
                    # Check UsdShadeConnectionSourceInfo to extract
                    # out the upstream information
                    usdSource1 = usdSources[0]
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
                        newInput.setAttribute(mtlxConnectString, mtlxConnectItem)#sourcePrim.GetName())

                    else:
                        # A nodegraph->output connect uses "nodegraph" vs "node"                        
                        if sourcePrim.IsA(UsdShade.NodeGraph):
                            mtlxConnectString = 'nodegraph'

                        # Set the connection
                        newInput.setAttribute(mtlxConnectString, mtlxConnectItem)#sourcePrim.GetName())

                        # An output->intput connection is denoted using
                        # an additional `output` attribute` if the source is 
                        # does not have multiple outputs
                        if sourceDirection == UsdShade.AttributeType.Output:
                            if isMultiOutput(sourcePrim):
                                newInput.setAttribute('output', sourcePort)                    
 
            # Set value if not connected.
            # Note that no Usd string -> MaterialX string remapping is
            # added here and may be required for more complex types.
            else:
                val = input.Get()
                if val:
                    mtlxVal = str(val)
                    mtlxVal = mtlxVal.removeprefix('(')
                    mtlxVal = mtlxVal.removesuffix(')')
                    newInput.setValueString(mtlxVal)
    
    # Emit outputs if specified. Unlike Usd, outputs are not explicitly defined
    # except for nodegraph. This branching toggle allows this behaviour.
    if emitOutputs:
        for output in shader.GetOutputs():
            if output:

                usdType = output.GetTypeName()

                mtlxType = mapUsdTypeToMtlx(usdType)
                usdBaseName = output.GetBaseName()
                usdFullName = output.GetFullName()

                #help(usdBaseName)
                usdBaseName = usdBaseName.replace(':', '_')
    
                # Do a simple remapping without any real remapping table
                if 'displacement' in str(usdFullName):
                    mtlxType = 'displacementshader'
                elif 'surface' in str(usdFullName):
                    mtlxType = 'surfaceshader'
                newOutput = parent.addOutput(usdBaseName, mtlxType)

                if output.HasConnectedSource():
                    usdSources = output.GetConnectedSources() 
                    if usdSources and usdSources[0]:
                        # Check UsdShadeConnectionSourceInfo
                        usdSource1 = usdSources[0]
                        sourcePrim = usdSource1[0].source.GetPrim()
                        sourcePort = usdSource1[0].sourceName
                        sourceDirection = usdSource1[0].sourceType
                        sourceType = usdSource1[0].typeName

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
# As in the previous example a tree traversal is performed. The main addition is to create a MaterialX `shader`, `nodegraph` or `material` when encountered and then adding in child inputs and outputs using the MaterialX utilities.
# 
# Note that there is no specific logic to handle different definition versions as this should not be required if a different `nodedef` identifier is used for different versions.  *This should be the case, when MaterialX `nodedefs` are loaded into Usd.* 
# 
# As MaterialX supports native definitions for Usd shader nodes these can also be handled. For example we assume if the node definition is `UsdPreviewSurface` that this maps directly to a MaterialX node. 

# %%

def emitMaterialX(stage, indent, prim, parent):
    """
    Emit MaterialX for a given Usd Stage starting at a given root.
    Currently only nodegraphs, material and shader nodes are supported.
    """
    if prim:
        if prim.IsA(UsdShade.NodeGraph):
            doc = parent.getDocument()
            usdNodegraph = UsdShade.NodeGraph(prim)
            mtlxName = parent.createValidChildName(prim.GetName())
            mtlxNodeGraph = parent.addChildOfCategory('nodegraph', mtlxName)
            parent = mtlxNodeGraph
            emitMtlxValueElements(stage, usdNodegraph, indent, mtlxNodeGraph, True)

        elif prim.IsA(UsdShade.Material): 
            doc = parent.getDocument()
            usdMaterial = UsdShade.Material(prim)
            mtlxName = parent.createValidChildName(prim.GetName())
            mtlxMaterial = parent.addMaterialNode(mtlxName)
            emitMtlxValueElements(stage, usdMaterial, indent, mtlxMaterial, False)

        elif prim.IsA(UsdShade.Shader): 
            usdShader = UsdShade.Shader(prim)
            mtlxNodeDef = ''
            
            # Note: Only consider when the definition is specified in the identifier
            usdImplAttr = usdShader.GetImplementationSourceAttr()
            if usdImplAttr.Get() == 'id':
                mtlxNodeDef = usdShader.GetIdAttr().Get()

            # Do a manual rename for built in UsdPreviewSurface
            # Could be done for other built-ins which have MaterialX
            # definitions.
            if mtlxNodeDef == 'UsdPreviewSurface':
                mtlxNodeDef = 'ND_UsdPreviewSurface_surfaceshader'

            doc = parent.getDocument()
            mtlxNodeDef = doc.getNodeDef(mtlxNodeDef)
            if mtlxNodeDef:
                mtlxShadername = parent.createValidChildName(prim.GetName())
                shaderNode = parent.addNodeInstance(mtlxNodeDef, mtlxShadername)                
                emitMtlxValueElements(stage, usdShader, indent, shaderNode, False)
            else:
                print('Skipping shader node %s: No MaterialX definition found.' % prim.GetName())  

        children = prim.GetChildren()
        for child in children:
            emitMaterialX(stage, indent+indent, child, parent)

doc = mx.createDocument()
doc.importLibrary(stdlib)

# Start at the root and emit
prim = stage.GetPrimAtPath('/')
children_refs = prim.GetChildren()
for child in children_refs:
    emitMaterialX(stage, ' ', child, doc)

# Write results to string / file
writeOptions = mx.XmlWriteOptions()
writeOptions.writeXIncludeEnable = False
writeOptions.elementPredicate = skipLibraryElement
documentContents = mx.writeToXmlString(doc, writeOptions)
print(documentContents)

status, error = doc.validate()
if error:
    print(error)

mx.writeToXmlFile(doc, 'test_usd_mtlx.mtlx', writeOptions)

# %% [markdown]
# ### Updating MaterialX / Usd Inputs 
# 
# There are different ways to approach handling a edit in Usd and then updating the corresponding MaterialX.
# This example only handles **value** changes by updating matching inputs via `path` lookups in Usd and MaterialX.
# 
# That is, the absolute Usd `path` is used to find the Usd input in the `stage`, and the corresponding MaterialX input in the working `document`. 
# * The interface `GetPrimAtPath()` is used to lookup the node to edit in Usd, and 
# * The interface `getDescendent()` used for MaterialX.
# * The input on each node is then found using `GetInput()` and `getInput()` for Usd and MaterialX respectively.
# 
# Note that the Usd `path` differs from the MaterialX `path` in this example due to additional nesting in Usd.
# 
# Monitoring and updating for graph connections is beyond the scope of this example, but is useful to consider whether the target workflow
# involves just MaterialX data model updates or if code generation is involved as is the case for render delegates using MaterialX
# code generation.

# %%
mtlxPath = '/collect1/my_materialx_subnet/mtlxstandard_surface1' 
usdPath = '/mySphere/mtl' + mtlxPath 

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
mtxlStdSurf = doc.getDescendant('collect1/my_materialx_subnet/mtlxstandard_surface1')
if mtxlStdSurf:
    mtlxSurfInput = mtxlStdSurf.getInput(inputName)
    if mtlxSurfInput:
        currentValue = mtlxSurfInput.getValueString()
        mtlxSurfInput.setValue(0.9)

        print('Modified MaterialX from: %s to %s' % (currentValue, mtlxSurfInput.getValueString()))


# %% [markdown]
# ## Appendix: Mapping Usd Types To MaterialX Types
# 
# For a completeness a full mapping of the following applicable Usd types should be performed. Most are mappable but type mapping can be "lossy" as there is no concept of type precision (half, float, double) for instance.

# %%
for t in dir(Sdf.ValueTypeNames):
    if t.startswith('__'):
        continue
    print('- Type:', t)


