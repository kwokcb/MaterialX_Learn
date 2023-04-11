import MaterialX as mx

class MtlxFile:

    @staticmethod
    def creatwWorkingDocument():
        """
        Create working document with libraries
        """
        libraryPath = mx.FilePath('libraries')
        stdlib = mx.createDocument()
        searchPath = mx.FileSearchPath()
        mx.loadLibraries([ libraryPath ], searchPath, stdlib)

        doc = mx.createDocument()
        doc.importLibrary(stdlib)
        return doc

    @staticmethod
    def skipLibraryElement(elem):
        return not elem.hasSourceUri()
    
