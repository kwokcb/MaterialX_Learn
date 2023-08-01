'''
Utility to create Markdown files containing Mermaid graphs for all MaterialX renderable elements 
found in a given folder or file.

By default the output image(s) is written to the current working directory. 
'''
import MaterialX as mx
import MaterialX.PyMaterialXGenShader as mx_gen_shader
from mtlxutils.mxtraversal import *
from mtlxutils.mxfile import *
from mtlxutils.mxshadergen import *

import sys, os, argparse

def createMermaidString(doc, orientation='LR'):
    '''Create a Mermaid graph from a MaterialX document.'''

    graph = None
    
    # For now just looks for material nodes
    nodes = mx_gen_shader.findRenderableElements(doc, False)
    if not nodes:
        nodes = doc.getMaterialNodes()
        if not nodes:
            for docnode in doc.getNodes():
                if docnode.getType() == mx.SURFACE_SHADER_TYPE_STRING:
                    nodes.append(docnode)

    roots = nodes #doc.getMaterialNodes()
    if roots:
        graph = MtlxMermaid.generateMermaidGraph(roots, orientation)
    return graph

def writeMermaidString(outputPath, graph):
    '''Write a Mermaid graph to a file.'''

    with open(outputPath, 'w') as f:
        strgraph = '```mermaid\n'
        for line in graph:
            if line:
                strgraph = strgraph + line + '\n'
        strgraph = strgraph + '```\n' 

        f.write(strgraph)
        f.close()

# Find all MaterialX files
def getFiles(rootPath):
    ''''''
    filelist = []
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            if file.endswith('mtlx'):
                filelist.append(os.path.join(subdir, file)) 
    return filelist

def loadLibraries(searchPath, libraryFolders):
    '''Load standard MaierialX libraries.'''
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
    parser = argparse.ArgumentParser(description="Create Markdown files with Mermaid graphs from MaterialX node graphs.")
    parser.add_argument(dest="inputPath", help="Path of the input MaterialX document or folder.")
    parser.add_argument('--outputPath', dest='outputPath', default='.', help='File path to output graphs to.')
    parser.add_argument('--library', dest='libraries', action='append', nargs='+', help='An additional relative path to a custom data library folder (e.g. "libraries/custom")')
    parser.add_argument('--path', dest='paths', action='append', nargs='+', help='An additional absolute search path location (e.g. "/projects/MaterialX")')
    parser.add_argument('--orientation', dest='orientation', default='LR', help='Orientation of graphs. LR = left to right, TB = top to bottom. Default is LR.')

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

    # More options can be added later
    orientation = opts.orientation
    for inputFilename in filelist:
        try:
            # Absoluate path to inputFilename
            print('Read document: ' + os.path.abspath(inputFilename))
            doc = createWorkingDocument(libraries)
            if not doc:
                print('**** Error creating working document')
                continue
            try:
                mx.readFromXmlFile(doc, inputFilename)
            except mx.ExceptionFileMissing as err:
                print('***** Error reading file: ', err)
                continue
            except mx.ExceptionParseError as err:
                print('***** Error reading file: ', err)
                continue

            graph = createMermaidString(doc, orientation)
            if graph:
                outputFileName = mx.FilePath(inputFilename.replace('.mtlx', '.md'))
                if opts.outputPath:
                    outputFileName = mx.FilePath(opts.outputPath) / outputFileName.getBaseName()
                print('Write graph to ' + outputFileName.asString())
                writeMermaidString(outputFileName.asString(), graph)

        except mx.ExceptionFileMissing as err:
            print(err)

if __name__ == '__main__':
    main()

