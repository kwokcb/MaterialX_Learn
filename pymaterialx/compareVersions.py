
import sys, os, argparse
import MaterialX as mx

def loadLibraries(sourceLibraryPath, otherLibraryPath):
    # Load the Source standard libraries
    currLibrary = mx.createDocument()
    currlibFiles = mx.loadLibraries(mx.getDefaultDataLibraryFolders(), mx.getDefaultDataSearchPath(), currLibrary)

    # Load in the old standard libraries
    otherVersion = ''
    libraryFolders = [ otherLibraryPath ]
    otherLibrary = mx.createDocument()
    searchPath = mx.FileSearchPath()
    # Attempt to preserve the original version of the library
    options = mx.XmlReadOptions()
    options.upgradeVersion = False

    libFiles = mx.loadLibraries(libraryFolders, searchPath, otherLibrary)

    print('## Libraries Loaded')
    print('- Loaded %d source library definitions from %d files. Version %s' %
           (len(currLibrary.getNodeDefs()), len(currlibFiles), mx.getVersionString()))
    print('- Loaded %d other library definitions from %d files. Version %s' % 
          (len(otherLibrary.getNodeDefs()), len(libFiles), otherLibrary.getVersionString()))

    return currLibrary, otherLibrary

def printDefinitions(currLibrary, otherLibrary):

    currNodeDefs = currLibrary.getNodeDefs()
    currNodeDefsCount = len(currNodeDefs)
    otherNodeDefs = otherLibrary.getNodeDefs()
    otherNodeDefsCount = len(otherNodeDefs) # There seems to be no way to get the previous version?

    print('- Source library has %d nodedefs' % currNodeDefsCount)
    print('- Other library has %d nodedefs' % otherNodeDefsCount)

    currNodeDefSet = {}
    for nodeDef in currNodeDefs:
        currNodeDefSet[nodeDef.getName()] = nodeDef

    # Create dictionary of old node definitions
    otherNodeDefSet = {}
    for nodeDef in otherNodeDefs:
        otherNodeDefSet[nodeDef.getName()] = nodeDef
        
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
        text = '<details><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
        print(text)

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
        text = '<details><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
        print(text)

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

        delta = '%d new node categories were added' % len(newCategories)
        text = '<details><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
        print(text)

    return compareDetails

class MaterialXCompare:
    '''
    MaterialX Element Comparitor
    '''

    @staticmethod
    def getActiveChild(element, name):
        '''
        Check if a child with a given name exists in the inheritance hierarchy for a given Element.
        '''
        for elem in element.traverseInheritance():
            child = elem.getChild(name)
            if child:
                return child
        return None

    @staticmethod
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

    @staticmethod
    def getActiveAttribute(element, name):
        ''' 
        Check if an attribute with a given name exists in the inheritance hierarchy for a given Element.
        '''
        for elem in element.traverseInheritance():
            child = elem.getAttribute(name)
            if child:
                return child
        return None

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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
        onlynd1, onlynd2, common = MaterialXCompare.diffLists(MaterialXCompare.getActiveAttributes(nd1), MaterialXCompare.getActiveAttributes(nd2))
        if len(onlynd1) > 0 or len(onlynd2) > 0:
            for item in onlynd1:
                log.append(indent + '- attribute: `%s`=( `%s` ) removed from: `%s`' % 
                        ( item, MaterialXCompare.getActiveAttribute(nd1, item), nd1.getName()))
            for item in onlynd2:
                log.append(indent + '- attribute: `%s`=( `%s` ) added to: `%s`' % 
                        ( item, MaterialXCompare.getActiveAttribute(nd2, item), nd2.getName()))
            differs = True

        for attr in common:
            if nd2.getAttribute(attr) != nd1.getAttribute(attr):
                log.append(indent + '  - attribute: `%s` changed on `%s` from `( %s )` to `( %s )`' % 
                        (attr, nd1.getName(), nd1.getAttribute(attr), nd2.getAttribute(attr)))
                differs = True

        # Compare children. This also checks for children that inherited 
        c1 = [c.getName() for c in MaterialXCompare.getActiveChildren(nd1)] 
        c2 = [c.getName() for c in MaterialXCompare.getActiveChildren(nd2)]
        if len(c1) != len(c2):
            log.append(indent + '- Number of children on: `%s` changed from ( %s ) to ( %s )' % (nd1.getName(), len(c1), len(c2)))
            differs = True

        # Get list of added, removed, and common children.
        onlynd1, onlynd2, common = MaterialXCompare.diffLists(c1, c2)

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
            c1child = MaterialXCompare.getActiveChild(nd1, childName)
            c2child = MaterialXCompare.getActiveChild(nd2, childName)
            if MaterialXCompare.compareElements(c1child, c2child, indent, log):
                differs = True

        return differs


def printDefinitionComparision(currLibrary, otherLibrary, compareDetails):

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
            difference = MaterialXCompare.compareElements(nd1, nd2, '', log) 
            if difference:
                for line in log:
                    text = text + line + '<br>'
                text = text + '|\n'
                changed = changed + 1

    delta = '%d definitions modified' % changed
    text = '<details><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
    print(text)

def printTargetComparision(currLibrary, otherLibrary):
    ## Get old targets
    oldTargets = []
    for target in otherLibrary.getTargetDefs():
        oldTargets.append(target.getName())

    ## Check for new targets
    currTargets = []
    for target in currLibrary.getTargetDefs():
        currTargets.append(target.getName())

    print('* Source library shader targets:', currTargets)
    print('* Other library shader targets:', oldTargets)

    newTargets = list(set(currTargets) - set(oldTargets))
    if newTargets:
        print('* Shader targets added:', newTargets)

    return oldTargets, currTargets


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

def print_implementations(nodedefs, targets, allimpls, title):
    '''
    Display all the implementations for the given nodedefs and targets.
    '''
    print(title)
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
        print(text)

def printImplementations(currLibrary, otherLibrary, currTargets, oldTargets):

    # Scan for all the Source targets
    title = '#### Source Library Definitions / Implementations\n'
    alltargets = currTargets
    alltargets.append('')
    allimpls = set()
    currNodeDefs = currLibrary.getNodeDefs()
    print_implementations(currNodeDefs, alltargets, allimpls, title)

    # Scan for all the previous targets
    title = '#### Other Library Definitions / Implementations\n'
    alltargets = oldTargets
    alltargets.append('')
    allimpls = set()
    otherNodeDefs = otherLibrary.getNodeDefs()
    print_implementations(otherNodeDefs, alltargets, allimpls, title)

def printImplementationComparision(currLibrary, otherLibrary):


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

    print('- Source library implementation count:', len(allImpls))
    print('- Other library implementation count:', len(allImpls2))

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
            addedText = addedText + '| %s | <a href="https://kwokcb.github.io/MaterialX_Learn/documents/definitions/%s.html">%s</a> | %s | \n' % (item, ns, ns, nt) 
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
            changedText = changedText + '| <a href="https://kwokcb.github.io/MaterialX_Learn/documents/definitions/%s.html">%s</a> | ' % (ns, item)
            # Perform detailed comparison
            log = []
            difference = MaterialXCompare.compareElements(impl, impl2, '', log) 
            if difference:
                for line in log:
                    changedText = changedText + line + '<br>'
                changedText = changedText + '|\n'
                changed = changed + 1


    delta = '%d implementations added' % added
    text = '<details><summary>' + delta + '</summary>\n\n' + addedText + '\n' + '</details>\n' 
    print(text)

    delta = '%d implementations removed' % removed
    text = '<details><summary>' + delta + '</summary>\n\n' +  removedText + '\n' + '</details>\n' 
    print(text)

    delta = '%d implementations modified' % changed
    text = '<details><summary>' + delta + '</summary>\n\n' + changedText + '\n' + '</details>\n' 
    print(text)

def main():
    parser = argparse.ArgumentParser(description='Compare definitions between two MaterialX libraries.')
    parser.add_argument(dest='otherLibrary', help='Path to root of other library to compare against')
    parser.add_argument('--sourceLibrary', dest='sourceLibrary', default='', 
                        help='Path to root of source library to compare against. Default is the Python package library')

    opts = parser.parse_args()

    print("# MaterialX Library Compare")
    currLibrary, otherLibrary = loadLibraries(opts.sourceLibrary, opts.otherLibrary)
    
    print('## Node Definition Comparision')
    compareDetails = printDefinitions(currLibrary, otherLibrary)
    if compareDetails:
        printDefinitionComparision(currLibrary, otherLibrary, compareDetails)

    print("## Implementations")
    otherTargets, currTargets = printTargetComparision(currLibrary, otherLibrary)
    printImplementations(currLibrary, otherLibrary, otherTargets, currTargets)

    print("## Implementation Comparison")
    printImplementationComparision(currLibrary, otherLibrary)


if __name__ == '__main__':
    main()