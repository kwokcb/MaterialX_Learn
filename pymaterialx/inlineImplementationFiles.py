
import os, argparse
import MaterialX as mx

def getFiles(rootPath):
    filelist = []
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            if file.endswith('mtlx'):
                filelist.append(os.path.join(subdir, file)) 
    return filelist

def skipLibraryElement(elem):
    return not elem.hasSourceUri()

def inlineImplementation(doc, filename):
    """
    Inline any implementations found and update the document
    """
    FILE_ATTR = 'file'
    SOURCECODE_ATTR = 'sourcecode'
    INLINE_EXTENSION = 'inline'

    inlineFilesFound = set()

    inputFilePath = mx.FilePath(filename)
    inputFilePath = inputFilePath.getParentPath()

    impls = doc.getImplementations()
    if len(impls):
        print('Found: %d' % len(impls), 'impls in file: ', filename)
    implChanged = 0
    for impl in impls:
        if impl.isA(mx.NodeGraph):
            continue

        fileAttr = impl.getAttribute(FILE_ATTR)
        if fileAttr:
            filePath = mx.FilePath(fileAttr)
            if filePath and filePath.getExtension() == INLINE_EXTENSION:
                # Read in the file
                filePath = inputFilePath / filePath

                inlineFile = open(filePath.asString(), 'r')
                if inlineFile:
                    inlineFilesFound.add(filePath.asString())
                    inlineText = inlineFile.readlines()
                    outputLine = ''
                    for line in inlineText:
                        outputLine = outputLine + line.rstrip('\r\n')
                    if outputLine:
                        impl.removeAttribute(FILE_ATTR)
                        impl.setAttribute(SOURCECODE_ATTR, outputLine)
                        print('Replace impl', impl.getName(), 'file: ', filePath.asString(), 'with:', outputLine)
                        implChanged = implChanged + 1
                    inlineFile.close()

    if True: #implChanged:
        print('Modified: %d', implChanged, 'implementations in file. Writing out new file:', filename)
        writeOptions = mx.XmlWriteOptions()
        mx.writeToXmlFile(doc, filename, writeOptions)

    return inlineFilesFound

def inlineFiles(rootPath):

    readDoc = False
    readOptions = mx.XmlReadOptions()
    # Make sure to keep comments and new lines
    readOptions.readComments = True
    readOptions.readNewlines = True
    inlineFilesFound = set()

    if os.path.isdir(rootPath): 
        filelist = getFiles(rootPath)
        for inputFilename in filelist:
            try:  
                libDoc = mx.createDocument()      
                mx.readFromXmlFile(libDoc, inputFilename, mx.FileSearchPath(), readOptions)
                # Perform inline for any implementations
                inlineFilesFound.update(inlineImplementation(libDoc, inputFilename))
                readDoc = True                 
            except mx.ExceptionFileMissing as err:
                print(err)
    else:
        try:
            libDoc = mx.createDocument()              
            mx.readFromXmlFile(libDoc, rootPath, mx.FileSearchPath(), readOptions)
            inlineFilesFound = inlineImplementation(libDoc, inputFilename)
            readDoc = True
        except mx.ExceptionFileMissing as err:
            print(err)

    return inlineFilesFound

def main():
    parser = argparse.ArgumentParser(description="Replace inline file references with the code from the files for all implementations.")
    parser.add_argument(dest="inputFilename", help="Path of the input MaterialX document or folder.")

    opts = parser.parse_args()

    rootPath = opts.inputFilename;
    inlineFilesFound = inlineFiles(rootPath)

    for inlineFile in inlineFilesFound:
        print('Delete inline file:', inlineFile)
        if os.path.exists(inlineFile):
            os.remove(inlineFile)


if __name__ == '__main__':
    main()