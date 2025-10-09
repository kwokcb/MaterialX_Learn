import sys, os, argparse
import MaterialX as mx
import json

def loadLibrary(libraryFolders, searchPath, readOptions, newLibrary):
    loadedFiles = set()
    readOptions = mx.XmlReadOptions()
    readOptions.upgradeVersion = False
    for libraryName in libraryFolders:
        libraryPath = searchPath.find(libraryName)
        for path in libraryPath.getSubDirectories():
            for filename in path.getFilesInDirectory('mtlx'):
                file = path / filename
                if file.asString() not in loadedFiles:
                    mx.loadLibrary(file, newLibrary, searchPath, readOptions)
                    loadedFiles.add(file.asString())
    return list(loadedFiles)

def loadLibraries(sourceLibraryPath, otherLibraryPath):
    options = mx.XmlReadOptions()
    options.upgradeVersion = False

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

    otherLibrary = mx.createDocument()
    libraryFolders = [otherLibraryPath]
    searchPath = mx.FileSearchPath()
    libFiles = mx.loadLibraries(libraryFolders, searchPath, otherLibrary)

    return currLibrary, otherLibrary

class MaterialXCompare:
    @staticmethod
    def getActiveChild(element, name):
        for elem in element.traverseInheritance():
            child = elem.getChild(name)
            if child:
                return child
        return None

    @staticmethod
    def getActiveChildren(element):
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
        for elem in element.traverseInheritance():
            child = elem.getAttribute(name)
            if child:
                return child
        return None

    @staticmethod
    def getActiveAttributes(element):
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
        onlyList1 = [item for item in list1 if item not in list2]
        onlyList2 = [item for item in list2 if item not in list1]
        common = [item for item in list1 if item in list2]
        return onlyList1, onlyList2, common

    @staticmethod
    def compareElements(nd1, nd2, indent=''):
        log = []
        differs = False

        if nd1.getCategory() != nd2.getCategory():
            log.append(f"{indent}- Category changed from {nd2.getCategory()} to {nd1.getCategory()}")
            differs = True

        only1, only2, common = MaterialXCompare.diffLists(
            MaterialXCompare.getActiveAttributes(nd1),
            MaterialXCompare.getActiveAttributes(nd2)
        )
        for attr in only1:
            log.append(f"{indent}- Attribute {attr} removed")
            differs = True
        for attr in only2:
            log.append(f"{indent}- Attribute {attr} added")
            differs = True
        for attr in common:
            val1 = nd1.getAttribute(attr)
            val2 = nd2.getAttribute(attr)
            if val1 != val2:
                log.append(f"{indent}- Attribute {attr} changed from {val2} to {val1}")
                differs = True

        c1 = [c.getName() for c in MaterialXCompare.getActiveChildren(nd1)]
        c2 = [c.getName() for c in MaterialXCompare.getActiveChildren(nd2)]
        only1c, only2c, commonc = MaterialXCompare.diffLists(c1, c2)

        for child in only1c:
            log.append(f"{indent}- Child {child} removed")
            differs = True
        for child in only2c:
            log.append(f"{indent}- Child {child} added")
            differs = True
        for child in commonc:
            c1child = MaterialXCompare.getActiveChild(nd1, child)
            c2child = MaterialXCompare.getActiveChild(nd2, child)
            child_log, child_diff = MaterialXCompare.compareElements(c1child, c2child, indent + "  ")
            if child_diff:
                log.extend(child_log)
                differs = True

        return log, differs

def collectNodeDefs(currLibrary, otherLibrary):
    currNodeDefs = {nd.getName(): nd for nd in currLibrary.getNodeDefs()}
    otherNodeDefs = {nd.getName(): nd for nd in otherLibrary.getNodeDefs()}

    added = []
    removed = []
    modified = []

    for name, nd in currNodeDefs.items():
        if name not in otherNodeDefs:
            added.append({
                "name": name,
                "category": nd.getNodeString(),
                "group": nd.getNodeGroup(),
                "type": nd.getType()
            })
        else:
            nd2 = otherNodeDefs[name]
            log, differs = MaterialXCompare.compareElements(nd, nd2)
            if differs:
                modified.append({
                    "name": name,
                    "category": nd.getNodeString(),
                    "group": nd.getNodeGroup(),
                    "type": nd.getType(),
                    "differences": log
                })

    for name, nd in otherNodeDefs.items():
        if name not in currNodeDefs:
            removed.append({
                "name": name,
                "category": nd.getNodeString(),
                "group": nd.getNodeGroup(),
                "type": nd.getType()
            })

    return added, removed, modified

def collectTargets(currLibrary, otherLibrary):
    currTargets = sorted([t.getName() for t in currLibrary.getTargetDefs()])
    otherTargets = sorted([t.getName() for t in otherLibrary.getTargetDefs()])
    addedTargets = sorted(list(set(currTargets) - set(otherTargets)))
    return currTargets, otherTargets, addedTargets

def collectImplementations(currLibrary, otherLibrary):
    allCurr = {i.getName(): i for i in currLibrary.getImplementations()} 
    allCurr.update({i.getName(): i for i in currLibrary.getNodeGraphs()})
    allOther = {i.getName(): i for i in otherLibrary.getImplementations()} 
    allOther.update({i.getName(): i for i in otherLibrary.getNodeGraphs()})

    added, removed, modified = [], [], []

    for name, impl in allCurr.items():
        if name not in allOther:
            nodeDef = impl.getNodeDef()
            added.append({
                "name": name,
                "nodeString": nodeDef.getNodeString() if nodeDef else "None",
                "type": nodeDef.getType() if nodeDef else "None",
                "source": mx.FilePath(impl.getSourceUri()).getBaseName() if impl.getSourceUri() else ""
            })
        elif name in allOther:
            log, diff = MaterialXCompare.compareElements(impl, allOther[name])
            if diff:
                nodeDef = impl.getNodeDef()
                modified.append({
                    "name": name,
                    "nodeString": nodeDef.getNodeString() if nodeDef else "None",
                    "type": nodeDef.getType() if nodeDef else "None",
                    "differences": log
                })

    for name, impl in allOther.items():
        if name not in allCurr:
            nodeDef = impl.getNodeDef()
            removed.append({
                "name": name,
                "nodeString": nodeDef.getNodeString() if nodeDef else "None",
                "type": nodeDef.getType() if nodeDef else "None"
            })

    return added, removed, modified

def main():
    parser = argparse.ArgumentParser(description='Compare two MaterialX libraries into JSON.')
    parser.add_argument("otherLibrary", help="Path to second library")
    parser.add_argument("--sourceLibrary", default="", help="Path to first library")
    parser.add_argument("--out", default="comparison.json", help="Output JSON file")
    opts = parser.parse_args()

    if not os.path.isdir(opts.otherLibrary):
        print("Error: otherLibrary path not found")
        sys.exit(1)
    if opts.sourceLibrary and not os.path.isdir(opts.sourceLibrary):
        print("Error: sourceLibrary path not found")
        sys.exit(1)

    currLibrary, otherLibrary = loadLibraries(opts.sourceLibrary, opts.otherLibrary)

    data = {}

    # NodeDefs
    addedNodes, removedNodes, modifiedNodes = collectNodeDefs(currLibrary, otherLibrary)
    data["nodeDefs"] = {
        "added": addedNodes,
        "removed": removedNodes,
        "modified": modifiedNodes
    }

    # Targets
    currTargets, oldTargets, addedTargets = collectTargets(currLibrary, otherLibrary)
    data["targets"] = {
        "first": currTargets,
        "second": oldTargets,
        "added": addedTargets
    }

    # Implementations
    addedImpls, removedImpls, modifiedImpls = collectImplementations(currLibrary, otherLibrary)
    data["implementations"] = {
        "added": addedImpls,
        "removed": removedImpls,
        "modified": modifiedImpls
    }

    with open(opts.out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
