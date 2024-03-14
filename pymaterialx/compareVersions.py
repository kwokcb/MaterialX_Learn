
import sys, os, argparse
import MaterialX as mx

def loadLibrary(libraryFolders, searchPath, readOptions, newLibrary):
    loadedFiles = set()
    readOptions = mx.XmlReadOptions()
    readOptions.upgradeVersion = False
    for libraryName in libraryFolders:
        libraryPath = searchPath.find(libraryName)
        for path in libraryPath.getSubDirectories():
            for filename in path.getFilesInDirectory('mtlx'):
                    file = path / filename;
                    if file.asString() not in loadedFiles:
                        mx.loadLibrary(file, newLibrary, searchPath, readOptions)                    
                        loadedFiles.add(file.asString())
    return loadedFiles

def loadLibraries(sourceLibraryPath, otherLibraryPath):
    # Attempt to preserve the original version of the library
    options = mx.XmlReadOptions()
    options.upgradeVersion = False

    # Load the Source standard libraries
    currlibFiles = []
    currLibrary = mx.createDocument()
    sourceLibraryFolders = []
    sourceSearchPath = mx.FileSearchPath()
    currentVersion = mx.getVersionString()
    if sourceLibraryPath:
        sourceLibraryFolders.append(sourceLibraryPath)
    else:
        sourceLibraryFolders = mx.getDefaultDataLibraryFolders()
        sourceSearchPath = mx.getDefaultDataSearchPath()
    currlibFiles = mx.loadLibraries(sourceLibraryFolders, sourceSearchPath, currLibrary)
    # There isn't any way to get a libraries verion string since it's not stored anywhere
    #if sourceLibraryPath:
    #    currentVersion = currLibrary.getVersionString()

    # Load in the old standard libraries
    otherVersion = ''
    libraryFolders = [ otherLibraryPath ]
    otherLibrary = mx.createDocument()
    searchPath = mx.FileSearchPath()
    libFiles = mx.loadLibraries(libraryFolders, searchPath, otherLibrary)

    print('### Libraries Loaded')
    print('- Loaded %d first library definitions from %d files. Version %s' %
           (len(currLibrary.getNodeDefs()), len(currlibFiles), currentVersion))
    print('  - First library location: %s. Search path: "%s"' % (sourceLibraryFolders,
                sourceSearchPath.asString()))
    
    print('- Loaded %d second library definitions from %d files. Version %s' % 
          (len(otherLibrary.getNodeDefs()), len(libFiles), otherLibrary.getVersionString()))
    print('  - Second library location: %s. Search path: "%s"' % (libraryFolders,
                searchPath.asString()))

    return currLibrary, otherLibrary

def printDefinitions(currLibrary, otherLibrary):

    currNodeDefs = currLibrary.getNodeDefs()
    currNodeDefsCount = len(currNodeDefs)
    otherNodeDefs = otherLibrary.getNodeDefs()
    otherNodeDefsCount = len(otherNodeDefs) # There seems to be no way to get the previous version?    

    print('* First library has %d nodedefs.' % currNodeDefsCount)
    print('* Second library has %d nodedefs' % otherNodeDefsCount)

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

        text = text + '<table class="table-fixed table shadow table-striped table-hover table-responsive">\n'
        text = text + '<tr><th> Name <th> Category </tr>\n'
        for nd in removedNodeDefs:
            text = text + '<tr><td> %s <td> %s </tr>\n' % (nd.getName(), nd.getNodeString())
        text = text + '</table>\n'

        delta = '%d node definitions removed' % len(removedNodeDefs)
        text = '<details><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
        print(text)

    # Find out what new definitions have been added.
    # Cache common definitions in <code>compareDetails<code> for further comparison.
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
        text = text + '<table class="table-fixed table shadow table-striped table-hover table-responsive">\n'
        text = text + '<tr><th> Name <th> Category <th> NodeGroup </tr>\n'
        for nd in newNodeDefs:
            text = text + '<tr><td> <a href="../documents/definitions/%s.html">%s</a> <td> %s <td> %s </tr>\n' % (nd.getNodeString(), nd.getName(), nd.getNodeString(), nd.getNodeGroup())
        text = text + '</table>\n'

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
        text = '<table class="table-fixed table shadow table-striped table-hover table-responsive">\n'

        text = text + '<tr><th> Node category <th> Node group <th> Type </tr>\n'
        sorted_keys = sorted(newCategories.keys())
        sortedNewCategories = {}
        for key in sorted_keys:
            sortedNewCategories[key] = newCategories[key]                                 
        for category in sortedNewCategories:
            text = text + '<tr><td> <a href="../documents/definitions/%s.html">%s</a> <td> %s <td> %s </tr>\n' % (category, category, newCategories[category][0], newCategories[category][1])

        text = text + '</table>\n'

        delta = '%d new node categories were added' % len(newCategories)
        text = '<details><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
        print(text)

    return compareDetails

class MaterialXCompare:
    '''
    MaterialX Element Comparator
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
            log.append(indent + '- Category changed on: <code>%s</code> from <code>%s</code> to <code>%s</code>' % (nd1.getName(), nd2.getCategory(), nd1.getCategory()))
            differs = True

        # Compare attributes.
        # Note: This does not work properly with inheritance yet.
        onlynd1, onlynd2, common = MaterialXCompare.diffLists(MaterialXCompare.getActiveAttributes(nd1), MaterialXCompare.getActiveAttributes(nd2))
        if len(onlynd1) > 0 or len(onlynd2) > 0:
            for item in onlynd1:
                log.append(indent + '- attribute: <code>%s</code>=( <code>%s</code> ) removed from: <code>%s</code>' % 
                        ( item, MaterialXCompare.getActiveAttribute(nd1, item), nd1.getName()))
            for item in onlynd2:
                log.append(indent + '- attribute: <code>%s</code>=( <code>%s</code> ) added to: <code>%s</code>' % 
                        ( item, MaterialXCompare.getActiveAttribute(nd2, item), nd2.getName()))
            differs = True

        for attr in common:
            if nd2.getAttribute(attr) != nd1.getAttribute(attr):
                log.append(indent + '  - attribute: <code>%s</code> changed on <code>%s</code> from <code>( %s )</code> to <code>( %s )</code>' % 
                        (attr, nd1.getName(), nd1.getAttribute(attr), nd2.getAttribute(attr)))
                differs = True

        # Compare children. This also checks for children that inherited 
        c1 = [c.getName() for c in MaterialXCompare.getActiveChildren(nd1)] 
        c2 = [c.getName() for c in MaterialXCompare.getActiveChildren(nd2)]
        if len(c1) != len(c2):
            log.append(indent + '- Number of children on: <code>%s</code> changed from ( %s ) to ( %s )' % (nd1.getName(), len(c1), len(c2)))
            differs = True

        # Get list of added, removed, and common children.
        onlynd1, onlynd2, common = MaterialXCompare.diffLists(c1, c2)

        # Log children that are removed. Emit value if is a value element.
        for childName in onlynd1:
            child = nd1.getChild(childName)
            childName = child.getNamePath().removeprefix(child.getParent().getNamePath())
            childType = child.getCategory()
            if child.isA(mx.ValueElement):
                log.append(indent + '- %s <code>%s</code> removed from <code>%s</code>. Value=( %s )' % (childType, childName, nd1.getNamePath(), child.getValueString()))
            else:
                log.append(indent + '- %s <code>%s</code> removed from <code>%s</code>' % (childType, childName, nd1.getNamePath()))
            differs = True

        # Log child that are added. Emit value if is a value element.
        for childName in onlynd2:
            child = nd2.getChild(childName)
            childName = child.getNamePath().removeprefix(child.getParent().getNamePath())
            childType = child.getCategory()
            if child.isA(mx.ValueElement):
                log.append(indent + '- %s <code>%s</code> added to <code>%s</code>. Value=( %s )' % (childType, childName, nd2.getNamePath(), child.getValueString()))
            else:
                log.append(indent + '- %s <code>%s</code> add to <code>%s</code>' % (childType, childName, nd2.getNamePath()))
            differs = True

        # Recurse on common children.
        for childName in common:
            c1child = MaterialXCompare.getActiveChild(nd1, childName)
            c2child = MaterialXCompare.getActiveChild(nd2, childName)
            if MaterialXCompare.compareElements(c1child, c2child, indent, log):
                differs = True

        return differs

 
def printDefinitionComparison(currLibrary, otherLibrary, compareDetails):

    text = '<table class="table-fixed table shadow table-striped table-hover table-responsive">\n'
    text = text + '<tr><th> Name <th> Change <tr>\n'
    #text = text + '| --- | --- |\n'

    changed = 0
    for item in compareDetails:
        nd1 = item[0]
        nd2 = item[1]
        # Use the built in Comparator first
        difference = (nd1 != nd2)
        if difference:
            # Perform details comparison
            text = text + '<tr><td> <a href="../documents/definitions/%s.html">%s</a> <td>\n\n ' % (nd1.getNodeString(), nd1.getName())
            log = []
            difference = MaterialXCompare.compareElements(nd1, nd2, '', log) 
            if difference:
                for line in log:
                    text = text + line + '<br>'
                text = text + '</tr>\n'
                changed = changed + 1
    text = text + '</table>\n'

    delta = '%d definitions modified' % changed
    text = '<details><summary>' + delta + '</summary>\n\n' + text + '\n' + '</details>\n' 
    print(text)

def printTargetComparison(currLibrary, otherLibrary):
    ## Get old targets
    oldTargets = []
    for target in otherLibrary.getTargetDefs():
        oldTargets.append(target.getName())

    ## Check for new targets
    currTargets = []
    for target in currLibrary.getTargetDefs():
        currTargets.append(target.getName())
    
    # Sort targets alphabetically
    currTargets = sorted(currTargets)
    oldTargets = sorted(oldTargets)

    print('* First library shader targets: *%s*' % currTargets)
    print('* Second library shader targets: *%s*' % oldTargets)

    newTargets = list(set(currTargets) - set(oldTargets))
    if newTargets:
        # Sort newTargets alphabetically
        newTargets = sorted(newTargets)
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

        result = '<table class="table-fixed table shadow table-striped table-hover table-responsive">'

        if len(target) == 0:
            result = result + '<tr><th>Definition</th><th>NodeGraph</th><th>File</th></tr>'
        else:
            result = result + '<tr><th>Definition</th><th>Implementation</th><th>File</th></tr>'
        for impl in impls:
            result = result + '<tr>'
            result = result + '<td>' + impl + '<td>' + impls[impl][0].getName() + '<td>' + impls[impl][1] + '\n'
            result = result + '</tr>'

        result = result  +  '</table>'

        text = '<details><summary>' + str(len(impls)) + (' shaders: ' + target if target else ' node graphs') + '</summary>\n\n' + result+ '\n</details>\n' 
        print(text)
        print('\n')

def printImplementations(currLibrary, otherLibrary, currTargets, oldTargets):

    # Scan for all the Source targets
    title = '##### First Library Definitions / Implementations\n'
    alltargets = currTargets
    alltargets.append('')
    allimpls = set()
    currNodeDefs = currLibrary.getNodeDefs()
    print_implementations(currNodeDefs, alltargets, allimpls, title)

    # Scan for all the previous targets
    print('<p></p>\n')
    title = '##### Second Library Definitions / Implementations\n'
    alltargets = oldTargets
    alltargets.append('')
    allimpls = set()
    otherNodeDefs = otherLibrary.getNodeDefs()
    print_implementations(otherNodeDefs, alltargets, allimpls, title)

def printImplementationComparison(currLibrary, otherLibrary):


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

    print('First library implementation count: %d' % len(allImpls))
    print('Second library implementation count: %d\n' % len(allImpls2))

    title = '<table class="table-fixed table shadow table-striped table-hover table-responsive">\n'
    title = title + '<tr><th> Name <th> Node Category <th> Node Type <th></tr>\n'
    #title = title + '| --- | --- | --- |\n'

    allImpls = sorted(allImpls)
    added = 0
    addedText = title
    removed = 0
    removedText = title

    title = '<table class="table-fixed table shadow table-striped table-hover table-responsive">\n'
    title = title + '<tr><th> Name <th> Change </tr>\n'
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
            addedText = addedText + '<tr><td> %s <td> <a href="https://kwokcb.github.io/MaterialX_Learn/documents/definitions/%s.html">%s</a> <td> %s </tr>\n' % (item, ns, ns, nt) 
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
                    removedText = removedText + '<tr><td> %s <td> %s <td> %s </tr> \n' % (item, ns, nt)
                    removed = removed + 1
            continue
        
        # Check for implementations which have been modified.
        # Use the built in Comparator first before performing a detailed comparison.
        difference = (impl != impl2)
        if difference:
            ns = 'None'
            nt = 'None'
            if impl2:
                nd = impl2.getNodeDef()
                if nd:
                    ns = nd.getNodeString()                
            changedText = changedText + '<tr><td> <a href="https://kwokcb.github.io/MaterialX_Learn/documents/definitions/%s.html">%s</a> <td> ' % (ns, item)
            # Perform detailed comparison
            log = []
            difference = MaterialXCompare.compareElements(impl, impl2, '', log) 
            if difference:
                for line in log:
                    changedText = changedText + line + '<br>'
                changedText = changedText + '</tr>\n'
                changed = changed + 1


    delta = '%d implementations added' % added
    if added > 0:
        addedText = addedText + '</table>\n'
        text = '<details><summary>' + delta + '</summary>\n\n' + addedText + '\n' + '</details>\n' 
        print(text)

    delta = '%d implementations removed' % removed
    if removed > 0:
        removedText = removedText + '</table>\n'
        text = '<details><summary>' + delta + '</summary>\n\n' + removedText + '\n' + '</details>\n' 
        print(text)

    delta = '%d implementations modified' % changed
    if changed > 0:
        changedText = changedText + '</table>\n'
        text = '<details><summary>' + delta + '</summary>\n\n' + changedText + '\n' + '</details>\n' 
        print(text)

def main():
    parser = argparse.ArgumentParser(description='Compare definitions between two MaterialX libraries.')
    parser.add_argument(dest='otherLibrary', help='Path to root of the second library to compare against')
    parser.add_argument('--sourceLibrary', dest='sourceLibrary', default='', 
                        help='Path to root of first library to compare against. Default is the Python package library')

    opts = parser.parse_args()

    if not os.path.isdir(opts.otherLibrary):
        print('Error: Target library path not found or not a directory: ', opts.otherLibrary)
        sys.exit(1)
    if (opts.sourceLibrary):
        if not os.path.isdir(opts.sourceLibrary):
            print('Error: Source library path not found or not a directory: ', opts.sourceLibrary)
            sys.exit(1)

    print('<!--Start-->')
    print('\n')
    print("## MaterialX Library Comparison\n")
    currLibrary, otherLibrary = loadLibraries(opts.sourceLibrary, opts.otherLibrary)
    print('\n')
    
    print("<hr>\n")
    print('### Node Definition Comparison\n')
    compareDetails = printDefinitions(currLibrary, otherLibrary)
    if compareDetails:
        print('\n')
        printDefinitionComparison(currLibrary, otherLibrary, compareDetails)
    print('\n')

    print("<hr>\n")
    print("### Implementations\n")
    otherTargets, currTargets = printTargetComparison(currLibrary, otherLibrary)
    printImplementations(currLibrary, otherLibrary, otherTargets, currTargets)
    print('\n')

    print("<hr>\n")
    print("### Implementation Comparison\n")
    printImplementationComparison(currLibrary, otherLibrary)
    print('\n')

    print('<!--End-->')


if __name__ == '__main__':
    main()
