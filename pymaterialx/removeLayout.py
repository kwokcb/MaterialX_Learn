'''
Remove layout attributes from a document
'''
import MaterialX as mx
from mtlxutils import mxfile
import os, argparse

def getFiles(rootPath):
    filelist = []
    exts = ('mtlx', 'MTLX' )
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            if file.lower().endswith(exts):
                filelist.append(os.path.join(subdir, file)) 
    return filelist

def main():
    parser = argparse.ArgumentParser(description="Remove layout attributes from a document.")
    parser.add_argument(dest="inputFileName", help="Filename or directory of the input document(s).")
    parser.add_argument('--newfile', dest='newfile', default=False, action='store_true',
        help="Create a new file named <original_file>'_nolayout.mtlx'. Default is false. .")
    opts = parser.parse_args()

    fileList = []
    if os.path.isdir(opts.inputFileName): 
        fileList = getFiles(opts.inputFileName)
    else:
        fileList.append(opts.inputFileName)

    for fileName in fileList:

        doc = mx.createDocument()
        try:
            mx.readFromXmlFile(doc, fileName)
        except mx.ExceptionFileMissing as err:
            print('File %s could not be loaded: "' % fileName, err, '"')
            continue
        except mx.Exception as err:
            print('File %s fail to load properly: "' % fileName, err, '"')
            continue

        mxfile.MtlxFile.removeLayout(doc)

        # Write out the document
        if opts.newfile:
            path = mx.FilePath(fileName)
            path.removeExtension()
            fileName = path.asString() + '_nolayout.mtlx'
        mx.writeToXmlFile(doc, fileName)

if __name__ == '__main__':
    main()
