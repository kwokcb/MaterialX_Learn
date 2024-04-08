# %% [markdown]
# # Creating Node Definitions 
# 
# This notebook will examine the creation of definitions for standard or custom libraries.
# 
# Aspects covered include:
# 1. Creating "robust" definitions from nodegraph implementations.
# 2. Creating efficient definitions from source code implementations.
# 3. "Publishing" definitions to libraries, including the core MaterialX libraries.
# 
# ## Core Library Setup
# 
# The basic setup will use the core MaterialX library as well as the nodegraph utilities found in 
# <a href="https://github.com/kwokcb/MaterialX_Learn/tree/main/pymaterialx/mtlxutils" target="_blank">mtlxutils</a>
# 
# As with other notebooks, we require the loading in the of the standard libraries and the creation
# of a working document.

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
# ## 1. Creating Definitions from Compound Graphs
# 
# Creating definitions from compound node graphs is the easiest way to create new definitions without worrying about shading language implementations if the language is supported. 
# 
# The basic logic for publishing from a nodegraph entails:
# * Making a copy a given compound graph
# * Turning the copy into a functional graph
# * Creating a definition based on the input and output interfaces on the functional graph
# * Adding in additional meta-data tagging as outlined in the definitions learning section:
#   * Node group
#   * Version
#   * Namespace
#   * UI properties
# * Creating a reference between the definition and the functional graph

# %% [markdown]
# ### Helpers
# 
# There is currently a helper interface on <a href="https://materialx.org/docs/api/class_document.html" target="_blank">Document</a> called `addNodeDefFromGraph()` that encapsulates the required logic for the most part. It does not:
# * Handle creating of definitions which inherit from each other, nor 
# * Update versioning on existing definitions with different versions.
# 
# The 1.38.7 version of the utility has some issues with which are being looked at. These issues can be addressed by patching the results.
# 
# The following is a simple utility wrapper sets up the creation parameters. It calls `adNodeDefFromGraph()` and returns both the definition (`nodedef`) and the functional graph created.

# %%
def createDefinitionAndFunctionalGraph(nodeGraph, cparam):
    '''
    Example of creating a definition. This has a fixed version, nodegroup and graph names. 

    Arguments:
    - nodeGraph : the compound node graph 
    - cparam : a set of node definition parameters keyed by semantic names.

    Returns:
    - Node definition and functional node graph
    '''
    definition = doc.addNodeDefFromGraph(nodeGraph, cparam['nodedefName'],
                            cparam['category'], cparam['version'], cparam['defaultversion'], 
                            cparam['nodegroup'], cparam['nodegraphName'])
    funcgraph = doc.getNodeGraph(cparam['nodegraphName'])

    return definition, funcgraph

# %% [markdown]
# The `getNodeGroups()` helper scans for existing node group names defined by the standard library using the interface <a href="https://materialx.org/docs/api/class_document.html" target="_blank">Document.getNodeDefs()</a> to get all of the definitions, and <a href="https://materialx.org/docs/api/class_node_def.html" target="_blank">NodeDef.getNodeGroup()</a> to find any specified node group.
# 
# Using these group names allows:
# * Any associated group semantic meanings to be discoverable by code generation. For example `texture2d` and `pbr` have semantic meanings. 
# * For naming consistency avoiding excessive partitioning into too many disparate groups.
# 
# Integrations may which to run this type of logic to examine for existing node groups independently from 
# definition creation workflows. 

# %%
def getNodeGroups(library):
    '''
    Find all the existing node group names on definitions 

    Inputs:
    - library : Definition library which defines the node groups.
    '''
    nodeGroups = set()
    for nd in library.getNodeDefs():
        group = nd.getNodeGroup()
        if group:
            nodeGroups.add(group)

    return nodeGroups


# %% [markdown]
# The helper is used below to print out the available node groups in the standard libraries:

# %%
print('Existing node groups on definitions:')
nodeGroups = getNodeGroups(stdlib)
for ng in sorted(nodeGroups):
    print(' - %s' % ng)

# %% [markdown]
# The `findCompoundGraphs()` help scans a document and returns a list of compound `nodegraphs` in a document.
# 
# **To differentiate between a compound and an functional graph**, the API interface 
# <a href="https://materialx.org/docs/api/class_node_graph.html" target="_blank">NodeGraph.getNodeDef()</a> can be used.
# If a non empty definition is returned from `getNodeDef()` then the graph is a functional graph.
# 
# A list of library file names is passed to filter out any compound graphs that were loaded in from a definition
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
# ### Associations Stored In Implementations
# 
# The association between a definition and a functional graph can be stored in an implementation as of version `1.38.5`.
# It is possible to find these implementations by comparing the definition name with the implementation's `nodedef` attribute name, by calling <a href="https://materialx.org/docs/api/class_interface_element.html" target="_blank">Interface.getNodeDefString()</a> to see if there is a definition match.
# > At time of writing the node graph query interface is not exposed in the Python API but the attribute can be queried directly. Note that an Implementation is derived from Interface.
# 
# The helper `getImplementationForNodedef()` shows this logic. In the example we are looking for Autodesk `standard surface` which uses implementations for definition / functional graph associations for different definition versions. Both are queried for below.
# 
# > Note that source code associations always used implementations for associations as there is no 
# mechanism for source code to reference back to it's definition as there is no explicit "source code" element in 
# MaterialX.
# 

# %%
def getAllImplementations(doc):
    '''
    Print out all implementations
    '''
    for impl in doc.getImplementations():
        print(impl)

def getImplementationForNodedef(doc, definition):
    '''
    Get an implemenation which matches a definition which is implemented
    as a functional nodegraph
    '''
    if not definition or not doc:
        return None
    for impl in doc.getImplementations():
        # Missing getNodeGraphString() expose in Python API 
        if impl.getNodeDefString() == definition.getName() and impl.getAttribute('nodegraph'): #impl.getNodeGraphString()            
            return impl
    return None

# Look for two versions of standard surface
definition = doc.getNodeDef('ND_standard_surface_surfaceshader')
definition_old = doc.getNodeDef('ND_standard_surface_surfaceshader_100')

# Find the implementations for each definition
impl = getImplementationForNodedef(doc, definition)
if impl:
    print('Found implementation: %s, definition %s and graph %s' % (impl.getName(), impl.getNodeDefString(),
                                                                        impl.getAttribute('nodegraph')))
else:
    print('Failed to find implementation element for definition %s' % (definition.getName()))

impl = getImplementationForNodedef(doc, definition_old)
if impl:
    print('Found implementation: %s, definition %s and graph %s' % (impl.getName(), impl.getNodeDefString(),
                                                                        impl.getAttribute('nodegraph')))
else:
    print('Failed to find implementation element for definition %s' % (definition.getName()))    

# %% [markdown]
# 
# ### Extracting Out A Definition
# 
# Once a new definition created, we will want to export the definitions and functional graphs (and implementations) into either a new document or an existing definition library document. To do so the contents need to be copied into the desired document.
# 
# The help function `addDefinitionToDocument()` will copy a definition, functional graph pair either 1 or 2 separate documents. As there is no "copy" function from one document to another, an empty definition and graph needs to be created first using <a href="https://materialx.org/docs/api/class_document.html" target="_blank">Document.addNodeDef()</a> and 
# <a href="https://materialx.org/docs/api/class_document.html" target="_blank">Document.addNodeGraph()</a> respectively. and then the contents copied over using the 
# <a href="https://materialx.org/docs/api/class_element.html" target="_blank">Element.copyContentFrom()</a> interface respectively.
# 
# If the association between the functional graph and definition:
# * resides on node graph, this will be copied over when `copyContentFrom()` is called on the graph.
# * is stored on a separate `implementation` instead then that must also be copied by creating a new implementationusing 
# <a href="https://materialx.org/docs/api/class_document.html" target="_blank">Document.addImplementation()</a>
# and copying it's contents over.
# 

# %%

def addDefinitionToDocument(definition, funcgraph, defDoc, graphDoc=None, defComment='', graphComment=''):
    '''
    Copy a definition and functional node graph to a new document.
    If there is a implementation which associates the definition and graph
    copyy that as well.

    Arguments:
    - definition : nodedef to copy
    - funcgraph : Functional graph to copy
    - defDoc : Destination document for definition
    - graphDoc: Optional destination document for functional graph
    - defComment : Optional comment to prepend to the destination document's definition
    - graphComment : Optional comment to prepend to the destination document's functional graph
    '''
    if definition and funcgraph:

        # Add definition comment
        if defComment:
            comment = defDoc.addChildOfCategory('comment')
            comment.setDocString(defComment)                 

        # Create a new definition, and copy the content over. Make sure
        # to use the existing name and category.
        nodeDef = defDoc.addNodeDef(definition.getName(), '', definition.getCategory())
        nodeDef.copyContentFrom(definition)        

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

        # If an implementation exists, copy that over as well. This will be added to 
        # node graph document if a separate one is specified.
        impl = getImplementationForNodedef(definition.getDocument(), definition)
        if impl:
            newImpl = graphDoc.addImplementation()
            newImpl.copyContentFrom(impl) 

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
# ### Example
# 
# As an example we will load in an example compound graph and use it to create a definition. The Python utility <a href="createdefinition.py" target="_blank">(`createdefinition`)</a> encapsulates this logic and provides a command line interface for various options.
# 
# The main logic loads in an example file, creates new definition/functional graph pairs and writes them to
# separate separate document(s).
# 
# For the 1.38.7 version API, the following creation parameters are set:
# 
# * A `category` name. 
#   * It is **very important to choose a unique name** for this as it is the name of the element which
# could be used in a shared definition library. 
#   * In general you want something that takes into account the signature of the graph interface as well as any key definition attributes such as version. 
#   * A sample identifier creator is provided called `generateIdentifier()` which takes in a nodegraph. An alternative version takes in a list of outputs: `generateIdentifierFromOutputs()`. *This is useful for source code definitions as described later on.* 
#   * There are no strict guidelines for category name but users should use `createValidName()` to ensure a valid element name is used.
# 
# * The "standard" prefixes of `ND_` and `NG_` are used as node definition and node graph name prefixes and codified in the `createDefinitionIdentifier()` and `createGraphIdentifier()` utilities. An `IMPL_` can be used if the association is set using a separate implementation element. 
# 
# * A version is always added. For initial definitions the version number of `1.0` and the flag is set to indicate that this is the default version.
# 
# * A node group is always added. This setting is difficult to infer based on just the compound node graph so can be a user speified choice based on the available groups returned from `getNodeGroups()` or a new custom one.

# %%

def generateIdentifier(category, version, nodeGraph):
    '''
    Utility to generate a unique identifier for a definition. Takes into account
    category, version and a node graphs signature.
    '''
    outputTypes = []
    for output in nodeGraph.getOutputs():
        outputTypes.append(output.getType())
    return generateIdentifierFromOutputs(category, version, outputTypes)

def generateIdentifierFromOutputs(category, version, outputTypes):
    '''
    Utility to generate a unique identifier for a definition. Takes into account
    category, version and list of output types.
    '''
    identifier = category

    if version:
        identifier = identifier + '_' + version

    for outputType in outputTypes:
        identifier = identifier + '_' + outputType

    return mx.createValidName(identifier)

def createDefinitionIdentifier(identifier):
    ''' 
    Create the definition element id
    '''
    nodedefName = 'ND_' + identifier
    return nodedefName

def createGraphIdentifier(identifier):
    ''' 
    Create the functional node graph element id
    '''
    nodegraphName = 'NG_' + identifier
    return nodegraphName

def createImplIdentifier(identifier):
    ''' 
    Create the implementation element id
    '''
    nodegraphName = 'IMPL_' + identifier
    return nodegraphName

# Read in an example with a compound graph
doc, libFiles = mxf.MtlxFile.createWorkingDocument()
mx.readFromXmlFile(doc, mx.FilePath('./data/test_procedural.mtlx'))

# Determine the node group and version
availableGroupNames = getNodeGroups(doc)
nodegroup = 'texture2d' if 'texture2d' in availableGroupNames else list(availableGroupNames)[0]
version = '1.0'
isDefaultVersion = True

compoundGraphs = findCompoundGraphs(doc, libFiles)
for nodeGraph in compoundGraphs: 
    cparam = {}
    # Set the category name. Just use the nodegraph name for now
    category = nodeGraph.getName().lower()
    # Create a new identifier
    id = generateIdentifier(category, version, nodeGraph)
    # Get definition and graph name
    cparam['nodedefName'] = createDefinitionIdentifier(id)
    cparam['nodegraphName'] = createGraphIdentifier(id)   
    cparam['category'] = category
    cparam['version'] = version
    cparam['defaultversion'] = isDefaultVersion
    cparam['nodegroup'] = nodegroup

    # Create new definition and functional graph
    definition, funcgraph = createDefinitionAndFunctionalGraph(nodeGraph, cparam)

    # Copy the definition to a destination document(s)
    defDoc = mx.createDocument()
    comment = ' Node: <' + category + '> '
    addDefinitionToDocument(definition, funcgraph, defDoc, defDoc, comment, comment)
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
    # Set the category name. Just use the nodegraph name for now
    category = nodeGraph.getName().lower()
    # Create a new identifier
    id = generateIdentifier(category, version, nodeGraph)
    # Get definition and graph name
    cparam['nodedefName'] = createDefinitionIdentifier(id)
    cparam['nodegraphName'] = createGraphIdentifier(id)   
    cparam['category'] = category
    cparam['version'] = version
    cparam['defaultversion'] = isDefaultVersion
    cparam['nodegroup'] = nodegroup

    # Create new definition and functional graph
    definition, funcgraph = createDefinitionAndFunctionalGraph(nodeGraph, cparam)

    # Add documentation and namespace as well as patch up definition and functional graph
    documentation = 'Documentation for new definition: ' + nodeGraph.getName()
    namespace = 'mynamespace'
    patchDefinition(definition, funcgraph, documentation, namespace)

    # Copy the definition to a destination document(s)
    defDoc = mx.createDocument()
    graphDoc = None
    defComment = ' Definition: nodeGraph.getName() '
    graphComment = ' Functional graph for definition: nodeGraph.getName() '
    
    addDefinitionToDocument(definition, funcgraph, defDoc, graphDoc, defComment, graphComment)
    if defDoc:
        documentContents = writeDocToString(defDoc)
        writeDocToMarkdown(documentContents)
    break

# %% [markdown]
# ## 2. Creating Definitions from Source Code
# 
# When creating a custom source node in MaterialX there are basically three things that needs to be created:
# 
# 1. A `<nodedef>` element specifying the signature of the node.
# 2. An `<implementation>` element that tells the code generator where it can find the source code for the node, for a particular target/language. You need one such element for each target you want to support. For the standard library: GLSL (and Vulkan, ESSL variants), OSL, MDL, and MSL should be supported. 
# 3. The source code for the node.

# %% [markdown]
# ### 2.1 Creating the Interface
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
# 
# This can be done by setting the `mx.Output.DEFAULT_INPUT_ATTRIBUTE` (`defaultnput`) attribute on an output. Note that it is only valid to set this on an output in a definition.  In this case the default value for the output is the input "in1".
# 
# Below is some sample code to create a source code definition interface using the helper `addSourceNodeDefinition()`. It reuses the unique identifier creation logic via `generateIdentifierFromOutputs()` for consistency.
# 
# The definitions interface is manually populated it with the desired inputs and outputs. Of note is that the inputs must have default values in order to pass validation, and the
# output type is `color3` which is incorporated into the identifier as with the functional graph logic.

# %%
def addSourceNodeDefinition(doc, cparam):
    '''
    Add a node definition which uses the standard naming convention.
    No definition is created if a node of the same name already exists in the document 
    '''
    id = generateIdentifierFromOutputs(cparam['category'], cparam['version'], cparam['outputs'])
    nodedefName = createDefinitionIdentifier(id) 

    existingDef = doc.getChild(nodedefName)
    if existingDef:
        return None

    newDef = doc.addChildOfCategory('nodedef', nodedefName)
    newDef.setVersionString(cparam['version'])
    newDef.setNodeGroup(cparam['nodegroup'])
    newDef.setNodeString(cparam['category'])
    return newDef

# Create a working document and add a nodedef
doc, libFiles = mxf.MtlxFile.createWorkingDocument()

cparam = {}
category = nodeGraph.getName().lower()
id = generateIdentifier(category, version, nodeGraph)
cparam['nodedefName'] = createDefinitionIdentifier(id)
cparam['category'] = 'myadd_explicit'
cparam['version'] = '1.0'
cparam['defaultversion'] = True
cparam['nodegroup'] = 'math'
cparam['outputs'] = ['color3']

output_type = 'color3'
input_type = 'color3'
comment = doc.addChildOfCategory('comment')
comment.setDocString(' Definition of a simple node <myadd>, adding two colors. ')
newDef = addSourceNodeDefinition(doc, cparam)

# Add some inputs and outputs, making sure to set values for the inputs
inputs = [ ["in1", input_type, "1.0, 0.0, 0.0"], ["in2", input_type, "0.0, 0.0, 0.0"] ]
outputs = [ ["out", output_type, "in1"] ]
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
# As an alternative, the interface could be created as a compound `nodegraph` by first using existing graph editing tools and then create a definition based on it. 
# 
# For example this graph was created interactively in the MaterialX Graph Editor:
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
def copyGraphInterface(newDef, refNodeGraph):
    '''
    Create a source code definition with the interface being provided by a reference node graph
    '''
    # Copy the children over from the nodegraph. Cache and restore attributes on the nodedef
    # which get written over when the copy occurs
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

# %% [markdown]
# As in the previous example the default input value is set manually. It cannot be set compound nodegraph before hand as this is considered to be invalid.

# %%
# Create new workgin document
sourceCodeDoc, libFiles = mxf.MtlxFile.createWorkingDocument()

# Read in reference nodegraph
refdoc, reflibFiles = mxf.MtlxFile.createWorkingDocument()
mx.readFromXmlFile(refdoc, mx.FilePath('./data/myadd_compound_graph.mtlx'))

# Create a new empty definition
cparam = {}
category = nodeGraph.getName().lower()
id = generateIdentifier(category, version, nodeGraph)
cparam['nodedefName'] = createDefinitionIdentifier(id)
cparam['category'] = 'myadd'
cparam['version'] = '1.0'
cparam['defaultversion'] = True
cparam['nodegroup'] = 'math'
cparam['outputs'] = ['color3']

comment = sourceCodeDoc.addChildOfCategory('comment')
comment.setDocString(' Definition of a simple node <myadd>, adding two colors. ')
inline_definition = addSourceNodeDefinition(sourceCodeDoc, cparam)

# Copy the interface from a reference graph
refNodeGraph = refdoc.getNodeGraph('myadd')
if refNodeGraph:

    copyGraphInterface(inline_definition, refNodeGraph)
    for child in inline_definition.getOutputs():
        child.setAttribute(mx.Output.DEFAULT_INPUT_ATTRIBUTE, 'in1')

if sourceCodeDoc:
    docString = writeDocToString(sourceCodeDoc)
    writeDocToMarkdown(docString)

# %% [markdown]
# ### 2.2 Creating Implementation Elements
# 
# To support the "standar"d shading languages an implementation will be made for each target.
# At this point a choice needs to be made on whether the code can be inlined or not. 
# * If it can then the `implementation` element will hold the code in it's `sourcecode` attribute. 
# * If not then additional source code files need to be created and a `file` and `function` attribute need to be added. 
# 
# 1. The helper `getTargetDefs()` will find all the "standard" targets defined. 
# 2. The helper `createImplementations()` will create on implementation per target and set up the association to the definition using `Implementation.setNodeDef()`, and the target using `Implementation.setTarget()`.
# 
# For consistency we reuse the identifier for the definition but modify it's prefix to be the "standard" one of 'IMPL_'
# The `target` is added as a post-fix to the identifier to disambiguate by target. For example:
# ```
# ND_myadd_1_0_color3
# ```
# ends up with the following implementation identifiers:
# ```
# IMPL_myadd_1_0_color3_genglsl for target: genglsl
# IMPL_myadd_1_0_color3_genmdl for target: genmdl
# IMPL_myadd_1_0_color3_genmsl for target: genmsl
# IMPL_myadd_1_0_color3_genosl for target: genosl
# ```
# 
# > At time of writing there has been no instances of requiring implementations to be versioned.

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
    # Reuse the same id signature as for the nodedef but replace the prefix.
    implName = createImplIdentifier(nodedef.getName().removeprefix('ND_'))
    category = nodedef.getNodeString() 
    type = nodedef.getType()
    impls = []
    for target in targets:
        comment = doc.addChildOfCategory('comment')
        comment.setDocString(' Implementation of <%s> for target %s and type %s ' % (category, target, type))
        impl = doc.addImplementation(implName + '_' + target)
        impl.setNodeDef(nodedef)
        impl.setTarget(target)
        impls.append(impl)

    return impls

# Create the implementations for all targets based on the nodedef
inlined_doc = mx.createDocument()
inlined_doc.copyContentFrom(sourceCodeDoc)
targets = getTargetDefs(inlined_doc)
for nodedef in inlined_doc.getNodeDefs():
    if nodedef.hasSourceUri():
        continue
    inlined_impls = createImplementations(inlined_doc, nodedef, targets)
    break

print('Created implementations for definition: %s' % nodedef.getName())
for impl in inlined_impls:
    print('- %s. Target:%s' % (impl.getName(), impl.getTarget()))

# %% [markdown]
# ### 2.3 Adding Source Code
# 
# #### 2.3.1 Adding Inlined Source Code
# 
# For this implementation example we will first show inlined code which uses tokens to represent arguments. Tokens use '{{' and '}}' delimiters.
# 
# In this example the code logic is:
# ```
#  '{{in1}} + {{in2}}'
#  ```
#  where `in1` corresponds to the nodedef input `in1` and `in2` to the nodedef input `in2`
# 
#  The help `setImplementationSourceCode_v1()` will find all implementations for a definitions and it's targets and set the inlineded coud.

# %%
def setImplementationSourceCode_v1(doc, nodedef, targets, sourceCode):
    '''
    Set the same inlined source code for all targets of a nodedef. 
    '''
    #category = nodedef.getNodeString() 
    #type = nodedef.getType()
    implName = createImplIdentifier(nodedef.getName().removeprefix('ND_'))
    #implName = 'IM_' + category + '_' + type 
    for target, code in zip(targets, sourceCode):
        impl = doc.getImplementation(implName + '_' + target)
        if impl:
            impl.setAttribute('sourcecode', code)



# Set the source code for all targets based on the nodedef.
# In this case all inline implementations are identical.
sourceCode = [ '{{in1}} + {{in2}}' ]
sourceCode = sourceCode * len(targets)
for nodedef in inlined_doc.getNodeDefs():
    if nodedef.hasSourceUri():
        continue
    setImplementationSourceCode_v1(inlined_doc, nodedef, targets, sourceCode)

docString = mxf.MtlxFile.writeDocumentToString(inlined_doc, mxf.MtlxFile.skipLibraryElement)
writeDocToMarkdown(docString)

mxf.MtlxFile.writeDocumentToFile(inlined_doc, './data/myadd_definition.mtlx', mxf.MtlxFile.skipLibraryElement)

# %% [markdown]
# #### 2.3.2 Adding Source Code Files For Implementations
# 
# If the code cannot be inlined then a new function name is required, with the general guideline to prefix the function name with the string `mx_` followed by catagory and type. For consistency the file names for source code will use the same convention.
# 
# Thus for this example:
# * `mx_myadd_color3` is the function name and
# * `mx_myadd_color3.<shader language extension>` is used for the shader name, where `<shader language extension>` is the native shading language suffix name (e.g. `osl` for the OSL shading language or `msl` for Metal) 
# 
# The utility function `setImplementationSourceCode_v1()` is extended to differentiate between inline and file source code and called `setImplementationSourceCode()`. The API interfaces <a href="https://materialx.org/docs/api/class_implementation.html" target="_blank">Implementation.setFunction() and
# Implementation.setFile()</a> 

# %%
def setImplementationSourceCode(doc, nodedef, targets, sourceCode, inlined):
    '''
    Add source code references.
    - If inlined then the code is embedded in the `sourcecode` attribute
    - If stored in a file then the filename is set using setFile() and the function set using setFunction()
    '''
    type = nodedef.getType()
    category = nodedef.getNodeString()
    implName = createImplIdentifier(nodedef.getName().removeprefix('ND_'))
    #implName = 'IM_' + category + '_' + type 

    # Set inlined code
    if inlined:
        for target, code in zip(targets, sourceCode):
            impl = doc.getImplementation(implName + '_' + target)
            if impl:
                    impl.setAttribute('sourcecode', code)
    # Set file / function code reference
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
filesource_doc.copyContentFrom(sourceCodeDoc)

targets = getTargetDefs(filesource_doc)
for nodedef in filesource_doc.getNodeDefs():
    if nodedef.hasSourceUri():
        continue
    createImplementations(filesource_doc, nodedef, targets)

    sourceCode = [ 'placeholder text']
    sourceCode = sourceCode * len(targets)
    setImplementationSourceCode(filesource_doc, nodedef, targets, sourceCode, False)

    break

docString = mxf.MtlxFile.writeDocumentToString(filesource_doc, mxf.MtlxFile.skipLibraryElement)
writeDocToMarkdown(docString)

mxf.MtlxFile.writeDocumentToFile(filesource_doc, './data/myadd_definition_file.mtlx', mxf.MtlxFile.skipLibraryElement)

# %% [markdown]
# ## 3. Adding Definitions To A "Library"
# 
# When a definition is refined to the point where it can be made available generally, there are a few choices to how they are organized and where they will reside. For instance a new definition could either be part of a custom library or potentially contributed back the the MaterialX standard libraries.
# 
# ### 3.1 "Standard" Library Organization
# 
# Below shows a layout for how the standard libraries are organized on the left.
# 
# <img src="../documents/images/definition_library_org.jpg" width="80%">
# 
# For example if we consider the grouping on the left to be `stdlib`, then it is composed of:
# * A separate file `stdlib_defs.mtlx` containing all definitions (`_defs`)
# * A separate file `stdlib_ng.mtlx` containing all Functional node graph implementations. (`_ng`)
# * A separate file containing all per-target source code implementation reference. Files are of in per-target sub-folders and of the form: `<target>/stdlib_<target>_impl.mtlx` files.  For example `genglsl/stdlib_genglsl_impl.mtlx` is the implementation file for GLSL (genglsl target)).
# 
# This structure is repeated for the pbr library: `pbrlib`.
# 
# Higher level functional nodegraph implementation-only libraries such as `bxdf` are built on top of `pbrilb` and `stdlib`. 
# 
# ### 3.2 Custom Library Organization
# In the diagram we show a custom library (on the right) which reflects the "standard" libraries. 
# 
# There are however many choices as shown on the far right.
# 
# For instance functional nodegraphs could be kept separate from other graphs, and/or they could be kept within the file as definition or as two separate files. The same holds true implementations and implementation files. For instance the implementation, functional nodegraph and definition could all reside in the same file as a self-contained grouping.
# 
# ### 3.3 Semantic Groupings
# Different attributes could be used for organization such as `category`, `node group`, `namespace`and `version`.
# 
# ### 3.4 Library Identification and Dependencies
# Note that there is no formal concept of a library and thus no concept of library or definition dependencies. For example `stdlib` is just a folder name where definitions reside. The definitions themselves have no reference to a given library identifier.
# 
# If a definition from the `bxdf` library is created without loading in  `stdlib` and / or `pbrlib` then this dependency may only be detected at graph evaluation time (e.g. for code generation)
# 
# Also as noted, `include` dependencies are **not** recommended to be specified explicitly as they are file references. There is no concept of library identifier dependence.

# %% [markdown]
# 
# ### 3.5 Adding A Custom Definition to the "Standard" library
# 
# A desirable feature is to be able to add definitions into the MaterialX standard libraries.
# As definitions have no delineation within a file (beyond an XML comment string), an initial option is to just 
# append the definitions, implementations, and functional graphs into the appropriate files.
# 
# At time of writing, utilities to aid in this process are under discussion / design currently, with a possible recommended
# workflow forth-coming. Note that version `1.38.8` is the minimum version to be able to preserve comments and
# newlines properly on XML load and save.
# 
# #### 3.5.1 Handling Definitions with Functional Graph Implementations 
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
documentation = 'Custom marble texture defintion: ' + category
namespace = ''
patchDefinition(definition, funcgraph, documentation, namespace)

defDoc = mx.createDocument()
graphDoc = mx.createDocument()
addDefinitionToDocument(definition, funcgraph, defDoc, graphDoc, 'Custom marble definition: : mymarble ', 'Functional graph implementation of custom marble: mymarble ')

writeToMarkdown('##### Definition document')
documentContents = writeDocToString(defDoc)
writeDocToMarkdown(documentContents)

writeToMarkdown('##### Functional Graph document')
documentContents = writeDocToString(graphDoc)
writeDocToMarkdown(documentContents)



# %% [markdown]
#  If the `stdlib` files are used instead then the definition and graph will be appended to
# existing files.
# 
# The first thing to discover is what are the relevant library files. The helper
# `getStandardLibraryFilePaths()` will return the location of the definition file, nodegraph file, and
# any implementation files per target.

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



# %% [markdown]
# This helper is used to find all the relevant files for `stdlib` relative to the default `libraries` folder:

# %%
# Find the files used for `stdlib`
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
# ( Newline preservation is available as of version 1.38.8 ).

# %%
# Get the relative library file names
targets = getTargetDefs(doc)
libraryName = 'stdlib'
defFilePath, graphFilePath, implFilePaths = getStandardLibraryFilePaths(libraryName, targets)

# Get the default `libraries` location to use as a root for the relative file paths
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
addDefinitionToDocument(definition, funcgraph, defDoc, graphDoc, 'Custom marble definition: : mymarble ', ' Functional graph implementation of custom marble: mymarble ')

# Examine the document
writeOptions = mx.XmlWriteOptions()
writeOptions.writeXIncludeEnable = False
writeOptions.elementPredicate = mxf.MtlxFile.skipLibraryElement

documentContents = mx.writeToXmlString(defDoc, writeOptions)
text = '<details><summary>Standard Libray Definitions with New Definiont</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
# Commented out for performance reasons. Uncomment to set file
#display_markdown(text , raw=True)  

documentContents = mx.writeToXmlString(graphDoc, writeOptions)
text = '<details><summary>Standard Libray Graphs with New Graph</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
# Commented out for performance reasons. Uncomment to set file
# display_markdown(text , raw=True)  

# Confirm existence and clean-up
findGraph = graphDoc.getNodeGraph(funcgraph.getName())
if findGraph:
    print('Functional graph: %s added to: %s' % (funcgraph.getName(), graphFilePath.asString()))
    graphDoc.removeChild(funcgraph.getName())
    findGraph = graphDoc.getNodeGraph(funcgraph.getName())

findDef = defDoc.getNodeDef(definition.getName())
if findDef:
    print('Definition: %s added to: %s' % (definition.getName(), defFilePath.asString()))
    defDoc.removeChild(definition.getName())
    findDef = defDoc.getNodeGraph(definition.getName())


# %% [markdown]
# #### 3.5.2 : Handling Definitions with Source Code Implementation 
# 
# In this example we take the previous custom `myadd` definition and add it's definition to the `stdlib` definition file and
# add all of it's implementations to eh appropriate per target implementation files.
# 
# The help `addSourceDefinitionToDocument()` handles the additions.

# %%
def addSourceDefinitionToDocument(definition, impls, defDoc, implDocs, defComment='', implComment=''):
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


# %% [markdown]
# Use the help, each definition with inline implementations previously created is added to `stdlib`. Definitions with non-inlined implementations would use the same logic as the only difference is the source code references stored on the attributes of the implementations.

# %%

if inlined_impls:
    implDocs = []
    implDocPaths = []
    skipped_targets = []
    for implFilePath, target in zip(implFilePaths, targets):
        implFilePath = mx.FilePath(defaultLibFolder[0]) / implFilePath
        implDocPaths.append(implFilePath)
        implDoc = mx.createDocument()
        try:
            mx.readFromXmlFile(implDoc, implFilePath, defaultSearchPath)
            implDocs.append(implDoc)
        except mx.ExceptionFileMissing as err:
            implDocs.append(implDoc)
            skipped_targets.append(target)
            print('No target (%s) impl file to append to %s' % (target, implFilePath.asString()))
        
    # Add the definition to the definition document and implementations to the implementation documents.        
    addSourceDefinitionToDocument(inline_definition, inlined_impls, defDoc, implDocs, 'Custom add definition (mxadd)', 'Custom add implementation (mxadd)')

    # Examine the definition document
    documentContents = mx.writeToXmlString(defDoc, writeOptions)
    text = '<details><summary>Standard Libray Definitions with New Definition</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
    # Uncommented out due to performance of displaying text. Uncomment to set actual files.
    #display_markdown(text , raw=True) 

    findDef = defDoc.getNodeDef(inline_definition.getName())
    if findDef:
        print('- Definition: %s added to: %s' % (inline_definition.getName(), defFilePath.asString()))
        defDoc.removeChild(inline_definition.getName())
        findDef = defDoc.getNodeGraph(inline_definition.getName())

    # Examine the implementation documents
    for implDoc, inline_impl, target, implPath in zip(implDocs, inlined_impls, targets, implDocPaths):
        if target in skipped_targets:
            continue

        documentContents = mx.writeToXmlString(implDoc, writeOptions)
        text = '<details><summary>Implementation for target ' + target + '</summary>\n\n' + '```xml\n' + documentContents + '```\n' + '</details>\n' 
        # Uncommented out due to performance of displaying text. Uncomment to set actual files.
        #display_markdown(text , raw=True)  

        implName = inline_impl.getName()
        if implDoc.getImplementation(implName):
            print('- Source implementation: %s added to file: %s' % (implName, implPath.asString()))
            implDoc.removeChild(implName)


