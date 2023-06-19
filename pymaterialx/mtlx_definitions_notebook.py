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
# ## 2. Creating Definitions from Source Code
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
writeOptions = mx.XmlWriteOptions()
writeOptions.writeXIncludeEnable = False
writeOptions.elementPredicate = mxf.MtlxFile.skipLibraryElement

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


