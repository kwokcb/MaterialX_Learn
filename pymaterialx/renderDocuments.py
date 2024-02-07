'''
Utility to render all MaterialX renderable elements found in a given folder or file.
By default the output image(s) is written to the current working directory. 
'''
import MaterialX as mx
from mtlxutils import mxrenderer
import os, argparse

def loadLibraries(searchPath, libraryFolders):
    status = ''
    lib = mx.createDocument()
    try:
        libFiles = mx.loadLibraries(libraryFolders, searchPath, lib)
        status = '- Loaded %d library definitions from %d files' % (len(lib.getNodeDefs()), len(libFiles))
    except mx.Exception as err:
        status = '- Failed to load library definitions: "%s"' % err

    return lib, status

def createWorkingDocument(libraries):
    # Create a working document and import any libraries
    doc = mx.createDocument()
    for lib in libraries:
        doc.importLibrary(lib)

    return doc

def haveVersion(major, minor, patch):
    """
    Check if the current vesion matches a given version
    """ 
    imajor, iminor, ipatch = mx.getVersionIntegers()
    if imajor < major:
        return False
    if iminor < minor:
        return False
    if ipatch < patch:
        return False
    return True

def getFiles(rootPath):
    filelist = []
    exts = ('mtlx', 'MTLX' )
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            if file.lower().endswith(exts):
                filelist.append(os.path.join(subdir, file)) 
    return filelist

def main():
    parser = argparse.ArgumentParser(description="Extract out source implementation information.")
    parser.add_argument('--outputPath', dest='outputPath', default="", help="Output path. Default is empty.")
    parser.add_argument('--path', dest='paths', action='append', nargs='+', help='An additional absolute search path location (e.g. "/projects/MaterialX")')
    parser.add_argument('--library', dest='libraries', action='append', nargs='+', help='An additional relative path to a custom data library folder (e.g. "libraries/custom")')
    parser.add_argument('--geometryPath', dest='geometryPath', default="", help="Path to geometry shape. Default is empty")
    parser.add_argument('--size', dest='size', default=-1, type=int, help="Size of the render. Default is 512.")
    parser.add_argument(dest="inputFileName", help="Filename of the input document.")
    opts = parser.parse_args()

    if not haveVersion(1, 38, 7):
        print('Minimum MaterialX version is 1.38.7. Exiting')
        exit(-1)

    # Get absolute path of opts.outputPath
    if opts.outputPath:    
        opts.outputPath = os.path.abspath(opts.outputPath)
    outputPath = mx.FilePath(opts.outputPath)
    # Check that output path exists
    if outputPath.size() > 0 and not os.path.isdir(outputPath.asString()):
        print('Output path "%s" does not exist.' % outputPath.asString())
        exit(-1)

    fileList = []
    if os.path.isdir(opts.inputFileName): 
        fileList = getFiles(opts.inputFileName)
    else:
        fileList.append(opts.inputFileName)

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
    #print('-- user search path: ', searchPath.asString())
    #print('-- user library folders: ', libraryFolders)
    userlib, status = loadLibraries(userPath, userLibraryFolders)
    if not userlib:
        print('Error loading user libraries: "%s"' % status)
        exit(-1)
    else:
        print(status)
    libraries.append(userlib)

    renderer = None
    if fileList:
        w = h = opts.size
        # TODO: The files should be packaged and the resources added as part of the package. 
        # Load in lighting. 
        radianceFilePath = './data/lights/san_giuseppe_bridge.hdr'
        irradianceFilePath = './data/lights/irradiance/san_giuseppe_bridge.hdr'
        if not os.path.exists(radianceFilePath) or not os.path.exists(irradianceFilePath):
            print('-- Radiance or Irradiance file does not exist. Exiting')
            exit(-1)

        # Load in geometry.
        geometryShape = './data/sphere.obj'
        if len(opts.geometryPath) > 0:
            geometryShape = opts.geometryPath
        if not os.path.exists(geometryShape):
            print('-- Geometry shape "%s" does not exist. Exiting' % geometryShape)
            exit(-1)
        renderer = mxrenderer.initializeRenderer(stdlib, searchPath, radianceFilePath, irradianceFilePath, w, h, 
                                                 geometryShape)
        renderer.addToRenderLog('--------------------------')

    if not renderer:
        print('Error initializing renderer')
        exit(-1)

    for fileName in fileList:
        fullSearchPath = searchPath

        # Create a new working document for each file
        doc = createWorkingDocument(libraries)
        if not doc:
            print('Error creating working document')
            continue

        try:
            mx.readFromXmlFile(doc, fileName)        
            valid, msg = doc.validate()
            if not valid:
                raise mx.Exception(msg)

            # Add the absolute path directory of the file to the search path
            dirname = os.path.dirname(fileName)
            abspath = os.path.abspath(dirname)
            fullSearchPath.append(abspath)   

        except mx.ExceptionFileMissing as err:
            print('File %s could not be loaded: "' % fileName, err, '"')
            continue
        except mx.Exception as err:
            print('File %s fail to load properly: "' % fileName, err, '"')
            continue

        print('Render file:' + fileName)
        renderer.addToRenderLog('Render file:' + fileName + '. SearchPath: ' + fullSearchPath.asString())
        rendered, errors = mxrenderer.performRender(renderer, doc, fileName, outputPath, fullSearchPath)
        if not rendered:
            print('Error rendering file: "%s"' % fileName)
            print('Errors: "%s"' % errors)
        renderer.addToRenderLog('--- Finished rendering file "%s"\n' % fileName)

    # Open text file
    print('Wrote render log to: render_log.txt')
    with open('render_log.txt', 'w') as f:
        f.write('\n'.join(renderer.getRenderLog()))        

if __name__ == '__main__':
    main()
