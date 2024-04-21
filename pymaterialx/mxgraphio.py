import MaterialX as mx
import argparse, os
from mtlxutils.mxtraversal import MtlxGraphBuilder, mermaidGraphExporter

# Version check
from mtlxutils.mxbase import *
haveVersion1387 = haveVersion(1, 38, 7) 
if not haveVersion1387:
    print("** Warning: Recommended minimum version is 1.38.7 for tutorials. Have version: ", mx.__version__)

# Write predicate
def skipLibraryElement(elem):
    return not elem.hasSourceUri()

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

def main():
    parser = argparse.ArgumentParser(description="Create graph diagrams from a MaterialX document.")
    parser.add_argument(dest="inputFilename", help="Filename of the input document.")
    parser.add_argument("-o", "--output", dest="outputFilename", help="Filename of the output document.")
    parser.add_argument('--orientation', dest='orientation', default='LR', help='Orientation of graphs. LR = left to right, TB = top to bottom. RL and BT are the opposite directions. Default is LR.')
    parser.add_argument('--graphs', dest='graphs', default='', help='Comma separated list of graphs to include in the graph. If empty, all node definitions are included. Example: "image,material"')
    parser.add_argument('--emitCategory', dest='emitCategory', default=False, help='Emit category information in the graph. Default is false.')
    parser.add_argument('--emitType', dest='emitType', default=False, help='Emit node type information in the graph. Default is false.')

    opts = parser.parse_args()

    # Check that file exists
    if not os.path.exists(opts.inputFilename):
        print('File not found:', opts.inputFilename)
        exit(-1)

    doc = loadFile(opts.inputFilename)

    if not doc:
        print('Failed to load doc:', opts.inputFileName)
        exit(-1)

    # Build the graph dictionary and connections
    graphBuilder = MtlxGraphBuilder(doc)
    graphBuilder.setIncludeGraphs(opts.graphs)
    graphBuilder.execute()

    if not graphBuilder.getDictionary():
        print('No nodes found.')
    if not graphBuilder.getConnections():
        print('No connections found.')

    if opts.outputFilename:
        filename = opts.outputFilename + '.json'
    else:    
        filename = mx.FilePath(opts.inputFilename)
        filename.removeExtension()
        filename = filename.asString() + '_connections.json'
    print('Write connections to JSON file:', filename)
    graphBuilder.exportToJSON(filename, opts.inputFilename)

    # Export graph to mermaid
    graphBuilder2 = MtlxGraphBuilder(None)
    graphBuilder2.importFromJSON(filename)
    exporter = mermaidGraphExporter(graphBuilder2.getDictionary(), graphBuilder2.getConnections())
    exporter.setOrientation(opts.orientation)
    exporter.setEmitCategory(opts.emitCategory)
    exporter.setEmitType(opts.emitType)
    exporter.execute()

    if opts.outputFilename:
        filename = opts.outputFilename + '.md'
    else:    
        filename = mx.FilePath(opts.inputFilename)
        filename.removeExtension() 
        filename = filename.asString() + '_graph.md'
    print('Write graph to:' + filename)
    exporter.export(filename)

if __name__ == '__main__':
    main()
