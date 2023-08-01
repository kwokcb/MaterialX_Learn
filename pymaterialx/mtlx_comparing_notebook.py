# %% [markdown]
# ## Document Comparison
# 
# In this notebook we will look at how MaterialX Elements can be compared with one another.
# 
# The example case chosen is to determine what has changed between 2 versions of the standard
# libraries. In this case version 1.38 versus the current version used to test with.
# 
# The followin aspects will be covered:
# 1. Loading in different versions into separate Documents.
# 2. Looking at what has been added or removed.
# 3. Performing a detailed comparison between Elements.
# 
# ### Library Loading
# 
# We will first load in two versions of the standard libraries.
# - One is the "current" one found in the 'libraries' folder of the MaterialX
# Python distribition. 
# - The other is a downloaded version of the same libraries copied into a renamed folder. 

# %%
import MaterialX as mx
from mtlxutils.mxfile import *
from IPython.display import display_markdown

# Load the current standard libraries
currLibrary, currlibFiles, status = MtlxFile.createLibraryDocument()
print(status)

# Load in the old standard libraries
otherVersion = ''
libraryFolders = [ 'libraries1.38' ]
otherLibrary = mx.createDocument()
searchPath = mx.FileSearchPath('../resources/')
# Attempt to preserve the original version of the library
options = mx.XmlReadOptions()
options.upgradeVersion = False

libFiles = mx.loadLibraries(libraryFolders, searchPath, otherLibrary)
print('- Loaded %d old library definitions from %d files' % (len(otherLibrary.getNodeDefs()), len(libFiles)))

# %% [markdown]
# It is possible to selectively filter out which files by providing additional arguments to `loadLibraries` or to perform the equivalent traversal explicitly as shown below.

# %%
otherLibrary2 = mx.createDocument()
otherVersion2 = ''
loadedLibraries = set()
readOptions = mx.XmlReadOptions()
readOptions.upgradeVersion = False
for libraryName in libraryFolders:
    libraryPath = searchPath.find(libraryName)
    for path in libraryPath.getSubDirectories():
          for filename in path.getFilesInDirectory('mtlx'):
                file = path / filename;
                if file.asString() not in loadedLibraries:
                    mx.loadLibrary(file, otherLibrary2, searchPath, readOptions)                    
                    loadedLibraries.add(file.asString())
                    otherVersion2 = otherLibrary2.getVersionString()  

print('Read in %d definitions from %d files. Version: %s' % 
      (len(otherLibrary2.getNodeDefs()), len(loadedLibraries), otherVersion2))

# %% [markdown]
# Note that both libraries will return same version when querying using `getVersionString()` on the document.
# At the time of writing we are using a patch and thus grab the version from the Python package instead.
# 
# It would be useful if there was a way to find patch versions on documents but this is currently
# not supported. Integrations could write additional `patch` meta-data atttibutes but this would not
# be standard.

# %%
print('- Current library / package version: %s' % mx.getVersionString())
print('- Old library version: %s' % otherLibrary.getVersionString())

# %% [markdown]
# ### Testing for Definition Additions and Removals 
# 
# The first test is just a check on the number of definitions in each file. The result found is that there are more definitions, and there appear to be no definitions which have been removed.

# %%
# Compare number of nodedefs
currNodeDefs = currLibrary.getNodeDefs()
currNodeDefsCount = len(currNodeDefs)
otherNodeDefs = otherLibrary.getNodeDefs()
otherNodeDefsCount = len(otherNodeDefs) # There seems to be no way to get the previous version?
print('There are %d new definitions.' % (currNodeDefsCount - otherNodeDefsCount))
print('- Current library has %d nodedefs' % currNodeDefsCount)
print('- Other library has %d nodedefs' % otherNodeDefsCount)

# %% [markdown]
# To setup for comparision testing, we build up a dictionary of node definitions keyed by the name of the definition.
# 
# At time of writing the convention is that definitions cannot be defined at any location other that the child of root Document. Thus only the name is used as the key. The path could also be used for long term robustness if this convention ever changes.

# %%
# Create dictionary of current node definitions
currNodeDefSet = {}
for nodeDef in currNodeDefs:
    currNodeDefSet[nodeDef.getName()] = nodeDef

# Create dictionary of old node definitions
otherNodeDefSet = {}
for nodeDef in otherNodeDefs:
    otherNodeDefSet[nodeDef.getName()] = nodeDef


# %% [markdown]
# The first check is to see if any definitions have been removed. 
# 
# If a definition has been remapped then the hope is that the update process performed on load will handle this. For example when material nodes replaced material elements as part of 1.38.7 the update process performed the appropriate remapping.  
# 
# If the definition no longer exists then the integration will need to find out how to handle this. In general, this should hopefully never occur.

# %%
    
# Find out if any definitions were removed
removedNodeDefs = []
for nodeDef in otherNodeDefs:
    if nodeDef.getName() not in currNodeDefSet:
        removedNodeDefs.append(nodeDef)

text = ''  
if removedNodeDefs:
    removedNodeDefs = sorted(removedNodeDefs, key=lambda x: x.getName())
    text = text + '| Name | Category |\n'
    text = text + '| :--- | :--- |\n'
    for nd in removedNodeDefs:
        text = text + '| %s | %s |\n' % (nd.getName(), nd.getNodeString())

    delta = '%d node definitions removed' % len(removedNodeDefs)
    text = '<details open><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
    display_markdown(text, raw=True)

# %% [markdown]
# The next check is to see if any definitions have been added and list them out.
# 
# At the same time we cache a list of definitions which exist in both the old and new library versions for later
# comparison.

# %%
# Find out what new definitions have been added.
# Cache common definitions in `compareDetails` for further comparison.
compareDetails = []
newNodeDefs = []
for nodeDef in currNodeDefs:
    if nodeDef.getName() not in otherNodeDefSet:
        newNodeDefs.append(nodeDef)
    else:
        # Cache these two for more comparison
        otherNodeDef = otherNodeDefSet[nodeDef.getName()]
        compareDetails.append( [otherNodeDef, nodeDef] )

text = ''
if newNodeDefs:
    newNodeDefs = sorted(newNodeDefs, key=lambda x: x.getNodeString())
    text = text + '| Name | Category | NodeGroup |\n'
    text = text + '| :--- | :--- | :---| \n'
    for nd in newNodeDefs:
        text = text + '| <a href="../documents/definitions/%s.html">%s</a> | %s | %s |\n' % (nd.getNodeString(), nd.getName(), nd.getNodeString(), nd.getNodeGroup())

    delta = '%d node definitions added. (Sorted by category)' % len(newNodeDefs)
    text = '<details open><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
    display_markdown(text, raw=True)

# %% [markdown]
# We print out the category of these new definitions. It is possible that new categories of nodes have been added
# in addition to adding new variants on existing categories.
# 
# As there is no formal list of such categories, a check needs to be made by scanning all definitions. 

# %%
oldCategories = set()
for nodeDef in otherNodeDefs:
    oldCategories.add(nodeDef.getNodeString())
# Sort old categories
oldCategories = sorted(oldCategories)

newCategories = {}
for nodeDef in currNodeDefs:
    newCategory = nodeDef.getNodeString()
    if newCategory not in oldCategories:
        newCategories[newCategory] = [ nodeDef.getNodeGroup(), nodeDef.getType() ]        

if newCategories:
    text = '| Node category | Node group | Type |\n'
    text = text + '| --- | --- | --- |\n' 
    sorted_keys = sorted(newCategories.keys())
    sortedNewCategories = {}
    for key in sorted_keys:
        sortedNewCategories[key] = newCategories[key]                                 
    for category in sortedNewCategories:
        text = text + '| [%s](../documents/definitions/%s.html) | %s | %s |\n' % (category, category, newCategories[category][0], newCategories[category][1])

    delta = '%d new node categories found' % len(newCategories)
    text = '<details open><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
    display_markdown(text, raw=True)

# %% [markdown]
# Additional checks can be added for non definition elements such as geometry properties, and type definitions.
# For this notebook we will concentrate on definitions only.

# %% [markdown]
# ### Detailed Element Comparison
# 
# A comparison between 2 Elements in MaterialX is available the the equivalence operator `==` on an Element.
# Though this will indicate if they differ, it provides no information as to what has differed.
# 
# To accomplish this a new utility called `compareElements` has been written. In addition to providing explicit feedback on what has changed it will explicitly recurse to children by calling itself (instead of recursing using the `==` operator)
# 
# The basic properities tested are:
# 1. Element category
# 2. Element attribute names
# 3. Elememt attribute values
# 4. Child Element count and what children were added or removed.
# 5. Recursing on child Elements. This would generally be Inputs and Outputs in the case of defintions.
#    If comparing graph elements (GraphElement), children could be child Nodes or graphs (GraphElements). 
# 
# > Note that this is the exact same logic as the `==` operator at time of writing. It can be extended as needed but the basic logic for checking attrbutes and then recursing on child Elements should remain the same. 

# %% [markdown]
# A few additional utilities are added to support comparison logic:
# 
# 1. `getActiveChild()` and `getActiveChildren()` is added to support class inheritance. If this is not
# considered then the children compared will only be the ones that are explicitly specified for a given class.
# > Note that this would be a useful API to have and would complement the existing `getActiveInputs()`and `getActiveOutputs()` methods on an <a href="https://materialx.org/docs/api/class_interface_element.html" target="_blank">InterfaceElement</a>. It is mostly useful for comparison of implementations and definitions where the interface is being
# compared. It is less useful for a node instance since comparison logic is aimed at what is explicitly specified on
# instances.
# 
# 2. `getActiveAttribute()` and `getActiveAttributes()` is added to support class inheritance when querying for attributes.
# This serves the same purpose as the child methods to ensure inherited attributes are not missed.
# 
# 3. `diffLists()` is added to find the intersection and difference between two lists.
# 
# Inheritance functions used the <a href="https://materialx.org/docs/api/class_element.html" target="_blank">
# traverseInheritance()</a> API to traverse up the inheritance hierarchy.

# %%
def getActiveChild(element, name):
    '''
    Check if a child with a given name exists in the inheritance hierarchy for a given Element.
    '''
    for elem in element.traverseInheritance():
        child = elem.getChild(name)
        if child:
            return child
    return None

def getActiveChildren(element):
    '''
    Get all children (included inherited ones) for a given Element.
    '''
    children = []
    childset = set()
    for elem in element.traverseInheritance():
        for child in elem.getChildren():
            if child.getName() not in childset:
                children.append(child)
                childset.add(child.getName())
    return children    

def getActiveAttribute(element, name):
    ''' 
    Check if an attribute with a given name exists in the inheritance hierarchy for a given Element.
    '''
    for elem in element.traverseInheritance():
        child = elem.getAttribute(name)
        if child:
            return child
    return None

def getActiveAttributes(element):
    '''
    Get all attributes (included inherited ones) for a given Element.
    '''
    children = []
    childset = set()
    for elem in element.traverseInheritance():
        for child in elem.getAttributeNames():
            if child not in childset:
                children.append(child)
                childset.add(child)
    return children

def diffLists(list1, list2):
    '''
    Return items in either list1 or list2, and in both.
    '''
    if list1 != list2:
        # Find items in list1 not in list2
        onlyList1 = [item for item in list1 if item not in list2]
        # Find items in list2 not in list1
        onlyList2 = [item for item in list2 if item not in list1]
        # Find items in both lists
        common = [item for item in list1 if item in list2]
        return onlyList1, onlyList2, common
    return [], [], list1     

# %% [markdown]
# Using these utility functions, the logic for `compareElements()` is as follows:
# 1. Check category between elements
# 2. Compare attributes

# %%
def compareElements(nd1, nd2, indent, log):
    '''
    Compare two elements and print any differences.

    Tests performed:
    1. Element category
    2. Element attribute names
    3. Elememt attribute values
    4. Child Element count and what children are present in one but not the other.
    5. Recursing on child Elements.
    '''
    if not nd1 or not nd2:
        return True

    differs = False

    if nd1.getCategory() != nd2.getCategory():
        log.append(indent + '- Category changed on: `%s` from `%s` to `%s`' % (nd1.getName(), nd2.getCategory(), nd1.getCategory()))
        differs = True

    # Compare attributes.
    # Note: This does not work properly with inheritance yet.
    onlynd1, onlynd2, common = diffLists(getActiveAttributes(nd1), getActiveAttributes(nd2))
    if len(onlynd1) > 0 or len(onlynd2) > 0:
        for item in onlynd1:
            log.append(indent + '- attribute: `%s`=( `%s` ) removed from: `%s`' % 
                       ( item, getActiveAttribute(nd1, item), nd1.getName()))
        for item in onlynd2:
            log.append(indent + '- attribute: `%s`=( `%s` ) added to: `%s`' % 
                       ( item, getActiveAttribute(nd2, item), nd2.getName()))
        differs = True

    for attr in common:
        if nd2.getAttribute(attr) != nd1.getAttribute(attr):
            log.append(indent + '  - attribute: `%s` changed on `%s` from `( %s )` to `( %s )`' % 
                       (attr, nd1.getName(), nd1.getAttribute(attr), nd2.getAttribute(attr)))
            differs = True

    # Compare children. This also checks for children that inherited 
    c1 = [c.getName() for c in getActiveChildren(nd1)] 
    c2 = [c.getName() for c in getActiveChildren(nd2)]
    if len(c1) != len(c2):
        log.append(indent + '- Number of children on: `%s` changed from ( %s ) to ( %s )' % (nd1.getName(), len(c1), len(c2)))
        differs = True

    # Get list of added, removed, and common children.
    onlynd1, onlynd2, common = diffLists(c1, c2)

    # Log children that are removed. Emit value if is a value element.
    for childName in onlynd1:
        child = nd1.getChild(childName)
        childName = child.getNamePath().removeprefix(child.getParent().getNamePath())
        childType = child.getCategory()
        if child.isA(mx.ValueElement):
            log.append(indent + '- %s `%s` removed from `%s`. Value=( %s )' % (childType, childName, nd1.getNamePath(), child.getValueString()))
        else:
            log.append(indent + '- %s `%s` removed from `%s`' % (childType, childName, nd1.getNamePath()))
        differs = True

    # Log child that are added. Emit value if is a value element.
    for childName in onlynd2:
        child = nd2.getChild(childName)
        childName = child.getNamePath().removeprefix(child.getParent().getNamePath())
        childType = child.getCategory()
        if child.isA(mx.ValueElement):
            log.append(indent + '- %s `%s` added to `%s`. Value=( %s )' % (childType, childName, nd2.getNamePath(), child.getValueString()))
        else:
            log.append(indent + '- %s `%s` add to `%s`' % (childType, childName, nd2.getNamePath()))
        differs = True

    # Recurse on common children.
    for childName in common:
        c1child = getActiveChild(nd1, childName)
        c2child = getActiveChild(nd2, childName)
        if compareElements(c1child, c2child, indent, log):
            differs = True

    return differs

# %% [markdown]
# > Note that unlike the C++ implementation children are not compared by index as the ordering may have changed between versions, thus resulting in false mismatches appearing. 
# 
# > **It may be useful to update the C++ implementation to be independent of ordering.**

# %% [markdown]
# Given this utility, we scan through all the definitions which exist in both libraries.
# 
# Some items of interest include changes in default value for inputs on some nodes, as well as addition of uniform qualifiers to some nodes.

# %%
#text = '### Compare old and current definitions in detail\n'
text = '| Name | Change  |\n'
text = text + '| --- | --- |\n'

changed = 0
for item in compareDetails:
    nd1 = item[0]
    nd2 = item[1]
    # Use the built in comparitor first
    difference = (nd1 != nd2)
    if difference:
        # Perform details comparison
        text = text + '| <a href="../documents/definitions/%s.html">%s</a> | ' % (nd1.getNodeString(), nd1.getName())
        log = []
        difference = compareElements(nd1, nd2, '', log) 
        if difference:
            for line in log:
                text = text + line + '<br>'
            text = text + '|\n'
            changed = changed + 1

delta = '%d definitions modified' % changed
text = '<details open><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
display_markdown(text, raw=True)


# %% [markdown]
# ## Target and Implementation Comparison
# 
# Next we cover how add logic to see if implementations have been added or removed, or
# if existing implementations have changed. This includes checking in the context of whether new `target`s have
# been added or not.

# %% [markdown]
# ### Target Check
# 
# The list of targets can be queried using `getTargetDefs()` on each librari respectively and the
# compared.

# %%
## Get old targets
oldTargets = []
for target in otherLibrary.getTargetDefs():
    oldTargets.append(target.getName())
print('Old targets:', oldTargets)

## Check for new targets
currTargets = []
for target in currLibrary.getTargetDefs():
    currTargets.append(target.getName())
print('Current targets:', currTargets)

newTargets = list(set(currTargets) - set(oldTargets))
if newTargets:
    print('New targets:', newTargets)

# %% [markdown]
# ### Implementation Check
# 
# As with definitions, implementations can be compared, either in the context of their associated definition or independently. As an implementation is generally of no use unless it is used in a definition we will present the comparison logic using the latter context.
# 
# #### Listing Implementations
# 
# It can be useful to examine the available implementations based on what, if any, code generation `target``
# they are associated with. 
# * If a implementation has no target then it is generally a node graph implementation but could also be generated programmatically via a common code generator which has no specific code target. For example the <a href ="https://materialx.org/docs/api/class_shader_generator.html" target="_blank">ShaderGenerator</a> class implements non-target specific code generation for <a href="https://github.com/AcademySoftwareFoundation/MaterialX/tree/main/source/MaterialXGenShader/Nodes" target="_blank">certain node types</a>.
# * Different targets may choose to implement logic differently than others. For example one may use a nodegraph, while another may use shader code, or generate the code programmatically.
# * Some targets may not support implementations for certain nodes.
# 
# A utility called `get_implementations()` scans for all implementations for a given `target``.

# %%
def get_implementations(nodedefs, target, allimpls):
    '''
    Build a dictionary of nodedefs and their corresponding implementations.
    
    The dictionary is keyed by the nodedef name and the value is a list of the implementation and 
    source file name.
    '''
    implementations = {}
    for nodedef in nodedefs:
        impl = nodedef.getImplementation(target)
        # This may be a nodegraph or an implementation
        if impl:
            # Skip if already used
            if impl.getName() in allimpls:
                continue
            # Skip if it's a nodegraph and target is not empty
            if len(target) > 0 and impl.isA(mx.NodeGraph):
                continue

            if target != 'essl':
                allimpls.add(impl.getName())
            implementations[nodedef.getName()] = [impl, mx.FilePath(impl.getSourceUri()).getBaseName()]
    return implementations

# %% [markdown]
# This utility can then be used to scan through all `target`s for each library.

# %%
def print_implementations(nodedefs, targets, allimpls, title):
    '''
    Display all the implementations for the given nodedefs and targets.
    '''
    display_markdown(title, raw=True)
    for target in targets:
        impls = get_implementations(nodedefs, target, allimpls)

        if len(target) == 0:
            result = '| Definition | NodeGraph | File |\n'
        else:
            result = '| Definition | Implementation | File |\n'
        result = result + '| --- | --- | --- |\n'
        for impl in impls:
            result = result + '|' + impl + '|' + impls[impl][0].getName() + '|' + impls[impl][1] + '\n'
        text = '<details><summary>' + str(len(impls)) + (' shaders: ' + target if target else ' node graphs') + '</summary>\n\n' + result+ '\n</details>\n' 
        display_markdown(text, raw=True)

# Scan for all the current targets
title = '**Current Library Definitions / Implementations**\n'
alltargets = currTargets
alltargets.append('')
allimpls = set()
print_implementations(currNodeDefs, alltargets, allimpls, title)

# Scan for all the previous targets
title = '**Previous Library Definitions / Implementations**\n'
alltargets = oldTargets
alltargets.append('')
allimpls = set()
print_implementations(otherNodeDefs, alltargets, allimpls, title)

# %% [markdown]
# We can see from the results, that 2 new targets were introduced as well as a number of new implementations written as source code and node graphs. The discrepancy, in the source code counts gives a hint as to the extent support for certain node definitions. That is, implementations for a given target may not be available for certain nodes. An example is `ambientocclusion` which is not supported by hardware shader targets at time of
# writing.

# %% [markdown]
# #### Comparing Implementations
# 
# We will first check the number of implementations which are associated with a definition in each library.
# We use the `getNodeDef()` to skip any unassociated implementations.
#  
# We must check for implementations which are either:
# 1. Source implementations using <a href="https://materialx.org/docs/api/class_document.html" target="_blank">
# getImplementations()</a> but also check explicity for:
# 2. Node graphs using  <a href="https://materialx.org/docs/api/class_document.html" target="_blank">
# getNodeGraphs()</a>
# 
# This differs from when getting an implementation from a node definition which will return either a source
# implementation or a node graph implementation when using `getImplementation()`.`

# %%
# Collect all Implementation and NodeGraph elements from two libraries
allImpls = set()
implsNoDef = set()
for i in currLibrary.getImplementations():
    if i.getNodeDef():
        allImpls.add(i.getName())
    else:
        implsNoDef.add(i.getName())
for i in currLibrary.getNodeGraphs():
    if i.getNodeDef():
        allImpls.add(i.getName())
    else:
        implsNoDef.add(i.getName())
print('Current implementation count:', len(allImpls))

allImpls2 = set()
for i in otherLibrary.getImplementations():
    if i.getNodeDef():
        allImpls2.add(i.getName())
        allImpls.add(i.getName())
    else:
        implsNoDef.add(i.getName())
for i in otherLibrary.getNodeGraphs():
    if i.getNodeDef():
        allImpls2.add(i.getName())
        allImpls.add(i.getName())
print('Previous implementation count:', len(allImpls2))

# %% [markdown]
# As with definitions we can compare the implementations which are in both libraries in detail.

# %%
title = '| Name | Node Category | Node Type |\n'
title = title + '| --- | --- | --- |\n'

allImpls = sorted(allImpls)
added = 0
addedText = title
removed = 0
removedText = title

title = '| Name | Change |\n| --- | --- |\n'
changed = 0
changedText = title

for item in allImpls:
    
    # Check for new implementations. Note that we check for source implementations
    # as well as node graph implementations.
    impl = otherLibrary.getImplementation(item)
    if not impl:
        impl = otherLibrary.getNodeGraph(item)
    if not impl:
        ns = 'None'
        nt = 'None'
        curimpl = currLibrary.getChild(item)
        if curimpl:
            nd = curimpl.getNodeDef()
            if nd:
                ns = nd.getNodeString()
                nt = nd.getType()
        addedText = addedText + '| %s | <a href="../documents/definitions/%s.html">%s</a> | %s | \n' % (item, ns, ns, nt) 
        added = added + 1
        continue
    
    # Check for implementations which have been removed. Note that we check for source implementations
    # as well as node graph implementations.
    impl2 = currLibrary.getImplementation(item)
    if not impl2:
        impl2 = currLibrary.getNodeGraph(item)
    if not impl2:
        oldimpl = currLibrary.getChild(item)
        if oldimpl:
            nd = oldimpl.getNodeDef()
            if nd:
                ns = nd.getNodeString()
                nt = nd.getType()        
        removedText = removedText + '| %s | %s | %s | \n' % (item, ns, nt)
        removed = removed + 1
        continue
    
    # Check for implementations which have been modified.
    # Use the built in comparitor first before performing a detailed comparison.
    difference = (impl != impl2)
    if difference:
        ns = 'None'
        nt = 'None'
        if impl2:
            nd = impl2.getNodeDef()
            if nd:
                ns = nd.getNodeString()                
        changedText = changedText + '| <a href="../documents/definitions/%s.html">%s</a> | ' % (ns, item)
        # Perform detailed comparison
        log = []
        difference = compareElements(impl, impl2, '', log) 
        if difference:
            for line in log:
                changedText = changedText + line + '<br>'
            changedText = changedText + '|\n'
            changed = changed + 1


delta = '%d implementations added' % added
text = '<details><summary>' + delta + '</summary>\n\n' + addedText + '\n' + '</details>\n' 
display_markdown(text, raw=True)

delta = '%d implementations removed' % removed
text = '<details><summary>' + delta + '</summary>\n\n' +  removedText + '\n' + '</details>\n' 
display_markdown(text, raw=True)

delta = '%d implementations modified' % changed
text = '<details><summary>' + delta + '</summary>\n\n' + changedText + '\n' + '</details>\n' 
display_markdown(text, raw=True)


# %% [markdown]
# ### Higher Level Comparisons
# 
# As can be seen, the comparisons only provide low level details of count and value changes but not any higher level
# semantic meaning. Some examples include:
# 
# - The change to inline source code was done for consistency and performance reasons but shows up as a a few hundred attribute changes. Some additional logic could be added to detect a `file` attribute to `sourcecode` attribute but
# this could be "brittle" long-term if these attribute names ever changed. Additional information such as how to
# perform this update would be useful. For example the script used to perform this can be found in 
# <a href="./inlineImplementationFiles.py" target="_blank">inlineImplementationFiles.py</a> file included here.
# 
# - Changes for node graph implementations are very hard to understand as only textual comparison is performed
# with possible new values and connections reflected when comparing the definitions.
# 
# It would probably be more useful to traverse the graphs via it's connections to give a better sense of whether there have been any topological changes (added / removed nodes, changes in connections). Better visual feedback could be given by drawing out the graphs as diagrams. This is beyond the scope of this notebook.
# 
# - Changes due to inheritance, whether added, removed or changed, are very hard determine though the change in the `inherit`
# attribute or a version change is a first indicator. The utility inheritance functions added here would be useful if added to the core distribution.
# 
# - There is a very large number of changes between the previous and current patch release tested (at time of writing).
# The same comparison could be performed between patches to see incremental changes.
# 


