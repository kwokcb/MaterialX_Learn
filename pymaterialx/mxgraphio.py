import MaterialX as mx
import argparse, os
from mtlxutils.mxtraversal import MtlxGraphBuilder, MxMermaidGraphExporter

# Version check
from mtlxutils.mxbase import *
haveVersion1387 = haveVersion(1, 38, 7) 
if not haveVersion1387:
    print("** Warning: Recommended minimum version is 1.38.7 for tutorials. Have version: ", mx.__version__)

# Write predicate
def skipLibraryElement(elem):
    return not elem.hasSourceUri()

def getFiles(rootPath):
    ''''''
    filelist = []
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            print('Scan file: ' + file  + ' in ' + subdir)
            if file.endswith('mtlx'):
                filelist.append(os.path.join(subdir, file)) 
    return filelist

def loadFile(filename):
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

    mx.readFromXmlFile(doc, filename)
    return doc


def loadLibraries(searchPath, libraryFolders):
    '''Load MaierialX libraries.'''
    status = ''
    lib = mx.createDocument()
    try:
        libFiles = mx.loadLibraries(libraryFolders, searchPath, lib)
        status = '- Loaded %d library definitions from %d files' % (len(lib.getNodeDefs()), len(libFiles))
    except mx.Exception as err:
        status = '- Failed to load library definitions: "%s"' % err

    return lib, status

def createWorkingDocument(libraries):
    '''Create a working document and import any libraries'''
    doc = mx.createDocument()
    for lib in libraries:
        doc.importLibrary(lib)

    return doc

def main():
    parser = argparse.ArgumentParser(description="Create graph diagrams from a MaterialX document.")
    parser.add_argument(dest="inputPath", help="Path of the input MaterialX document or folder.")
    parser.add_argument('--outputPath', dest='outputPath', default='', help='File path to output graphs to.')
    parser.add_argument('--library', dest='libraries', action='append', nargs='+', help='An additional relative path to a custom data library folder (e.g. "libraries/custom")')
    parser.add_argument('--path', dest='paths', action='append', nargs='+', help='An additional absolute search path location (e.g. "/projects/MaterialX")')
    parser.add_argument("-o", "--output", dest="outputFilename", help="Filename of the output document.")
    parser.add_argument('--orientation', dest='orientation', default='LR', help='Orientation of graphs. LR = left to right, TB = top to bottom. RL and BT are the opposite directions. Default is LR.')
    parser.add_argument('--graphs', dest='graphs', default='', help='Comma separated list of graphs to include in the graph. If empty, all node definitions are included. Example: "image,material"')
    parser.add_argument('--emitCategory', dest='emitCategory', default=False, help='Emit category information in the graph. Default is false.')
    parser.add_argument('--emitType', dest='emitType', default=False, help='Emit node type information in the graph. Default is false.')

    opts = parser.parse_args()

    # Load standard libraries
    libraries = []
    searchPath = mx.getDefaultDataSearchPath()
    libraryFolders = mx.getDefaultDataLibraryFolders()
    stdlib, status = loadLibraries(searchPath, libraryFolders)
    if not stdlib:
        print('Error loading standard libraries: "%s"' % status)
        exit(-1)
    else:
        print(status)
    libraries.append(stdlib)

    # Check for additional use libraries
    userPath = mx.FileSearchPath()
    userLibraryFolders = []
    if opts.paths:
        for pathList in opts.paths:
            for path in pathList:
                searchPath.append(path)
                userPath.append(path)
    if opts.libraries:
        for libraryList in opts.libraries:
            for library in libraryList:
                userLibraryFolders.append(library)
    if userLibraryFolders:
        userlib, status = loadLibraries(userPath, userLibraryFolders)
        if not userlib:
            print('Error loading user libraries: "%s"' % status)
            exit(-1)
        else:
            print(status)
        libraries.append(userlib)    

    rootPath = opts.inputPath
    filelist = []
    if os.path.isdir(rootPath): 
        filelist = getFiles(rootPath)
    elif os.path.isfile(rootPath):
        filelist = [rootPath]

    print('Found %d MaterialX files' % len(filelist))

    for inputFilename in filelist:
        try:
            # Absolute path to inputFilename
            baseInputFileName = inputFilename
            inputFilename = os.path.abspath(inputFilename)
            print('Read document: ' + inputFilename)
            doc = createWorkingDocument(libraries)
            if not doc:
                print('- Error creating working document')
                continue
            try:
                mx.readFromXmlFile(doc, inputFilename)
            except mx.ExceptionFileMissing as err:
                print('- Error reading file: ', err)
                continue
            except mx.ExceptionParseError as err:
                print('- Error reading file: ', err)
                continue

            # Build the graph dictionary and connections
            graphBuilder = MtlxGraphBuilder(doc)
            graphBuilder.setIncludeGraphs(opts.graphs)
            graphBuilder.execute()

            if not graphBuilder.getDictionary():
                print('No nodes found.')
                continue
            if not graphBuilder.getConnections():
                print('No connections found.')
                continue

            # Export connectivity to JSON file
            outputFileName = mx.FilePath(inputFilename.replace('.mtlx', '_connections.json'))
            if opts.outputPath:
                outputFileName = mx.FilePath(opts.outputPath) / outputFileName.getBaseName()
            print('- Write connectivity file:', outputFileName.asString())
            graphBuilder.exportToJSON(outputFileName.asString(), baseInputFileName)

            # Export to Mermaid in Markdown file
            #graphBuilder2 = MtlxGraphBuilder(None)
            #graphBuilder2.importFromJSON(outputFileName)
            exporter = MxMermaidGraphExporter(graphBuilder.getDictionary(), graphBuilder.getConnections())
            exporter.setOrientation(opts.orientation)
            exporter.setEmitCategory(opts.emitCategory)
            exporter.setEmitType(opts.emitType)
            exporter.execute()

            outputFileName = mx.FilePath(inputFilename.replace('.mtlx', '.md'))
            if opts.outputPath:
                outputFileName = mx.FilePath(opts.outputPath) / outputFileName.getBaseName()

            print('- Write Mermaid graph to file:' + outputFileName.asString())
            exporter.export(outputFileName.asString())

        except mx.ExceptionFileMissing as err:
            print(err)

if __name__ == '__main__':
    main()
