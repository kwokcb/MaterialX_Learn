#!/usr/bin/env python
'''
Utility to convert between XML and JSON representations of a MaterialX document
'''
import MaterialX as mx
import json
import os, argparse

# We use a colon to separate the category and name of an element in the JSON hierarchy
JSON_CATEGORY_NAME_SEPARATOR = ':'
# The root of the JSON hierarchy
MATERIALX_DOCUMENT_ROOT = 'materialx'

### MTLX to JSON

# Convert MaterialX element to JSON
def elementToJSON(elem, jsonParent):
    '''
    Convert an MaterialX XML element to JSON.
    Will recursively traverse the parent/child Element hierarchy.
    '''
    if (elem.getSourceUri() != ""):
        return
    
    # Create a new JSON element for the MaterialX element
    jsonElem = {}

    # Add attributes
    for attrName in elem.getAttributeNames():
        jsonElem[attrName] = elem.getAttribute(attrName)

    # Add children
    for child in elem.getChildren():
        jsonElem = elementToJSON(child, jsonElem)
    
    # Add element to parent
    jsonParent[elem.getCategory() + JSON_CATEGORY_NAME_SEPARATOR + elem.getName()] = jsonElem
    return jsonParent

# Convert MaterialX document to JSON
def documentToJSON(doc):
    '''Convert an MaterialX XML document to JSON'''
    root = {}
    root["materialx"] = {}

    for attrName in doc.getAttributeNames():
        root[attrName] =  doc.getAttribute(attrName)

    for elem in doc.getChildren():
        elementToJSON(elem, root[MATERIALX_DOCUMENT_ROOT])

    return root

### JSON to MTLX

# Convert JSON element to MaterialX
def elementFromJSON(node, elem):
    '''
    Convert an JSON element to MaterialX
    '''
    for key in node:
        value = node[key]

        # Set attributes            
        if isinstance(value, str):
            elem.setAttribute(key, str(value))

        # Traverse chilren
        else:
            # Traverse down from root
            if key == MATERIALX_DOCUMENT_ROOT:
                elementFromJSON(value, elem)
                continue

            # Split key name by ":" to get category and name
            category, name = key.split(JSON_CATEGORY_NAME_SEPARATOR, 1)
            if category and not elem.getChild(name):
                child = elem.addChildOfCategory(category, name)
                elementFromJSON(value, child)

# Convert JSON to MaterialX document
def documentFromJSON(jsonDoc, doc):
    '''
    Convert a JSON document to MaterialX
    '''
    elementFromJSON(jsonDoc, doc)

### Utilities

def getFiles(rootPath, extension):
    filelist = []
    exts = (extension, extension.upper() )
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            if file.lower().endswith(exts):
                filelist.append(os.path.join(subdir, file)) 
    return filelist

def loadLibraries(searchPath, libraryFolders):
    status = ''
    lib = mx.createDocument()
    try:
        libFiles = mx.loadLibraries(libraryFolders, searchPath, lib)
        status = '- Loaded %d library definitions from %d files' % (len(lib.getNodeDefs()), len(libFiles))
    except mx.Exception as err:
        status = '- Failed to load library definitions: "%s"' % err

    return lib, status


def main():
    parser = argparse.ArgumentParser(description="Utility to convert between XML and JSON representations of a MaterialX document")
    parser.add_argument('--outputPath', dest='outputPath', default='', help='File path to output results to.')
    parser.add_argument(dest="inputFileName", help="Filename of the input document or folder containing input documents")
    parser.add_argument('--fromJSON', dest='fromJSON', action='store_true', help='Convert from JSON to XML. Default is XML to JSON.')

    opts = parser.parse_args()

     # Get absolute path of opts.outputPath
    if opts.outputPath:    
        opts.outputPath = os.path.abspath(opts.outputPath)
    outputPath = mx.FilePath(opts.outputPath)
    # Check that output path exists
    if outputPath.size() > 0 and not os.path.isdir(outputPath.asString()):
        print('Output path "%s" does not exist.' % outputPath.asString())
        exit(-1)

    print('------------------------- outputPath'    + opts.outputPath)

    # Set extension to be 'json' if converting from JSON (opts.JSON) to XML
    extension = 'json' if opts.fromJSON else 'mtlx'   
    fileList = []
    if os.path.isdir(opts.inputFileName): 
        fileList = getFiles(opts.inputFileName, extension)
    else:
        if opts.inputFileName.endswith(extension):
            fileList.append(opts.inputFileName)

    if not fileList:
        print('No files found with extension "%s"' % extension)
        exit(-1)

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

    for fileName in fileList:

        filePath = mx.FilePath(fileName)

        # Convert from JSON to XML
        if opts.fromJSON:
            jsonFile = open(fileName, 'r')
            if not jsonFile:
                continue
            jsonObject = json.load(jsonFile)
            if not jsonObject:
                continue

            newDoc = mx.createDocument() 
            #jsonObject = json.loads(doc_result)
            documentFromJSON(jsonObject, newDoc)
            if newDoc.getChildren():

                if os.path.isdir(outputPath.asString()):
                    filePath = outputPath / filePath.getBaseName()

                print('Write to MaterialX file: ' + filePath.asString().replace('.json', '_json.mtlx'))
                mx.writeToXmlFile(newDoc, filePath.asString().replace('.json', '_json.mtlx'))
       
        # Convert from XML to JSON
        else:
            doc = mx.createDocument()
            mx.readFromXmlFile(doc, fileName)
            if doc:
                # Convert entire document to JSON
                doc_result = documentToJSON(doc)

                if os.path.isdir(outputPath.asString()):
                    filePath = outputPath / filePath.getBaseName()

                # Write JSON to file
                with open(filePath.asString().replace('.mtlx', '_mtlx.json'), 'w') as outfile:
                    print('Write to JSON file: ' + filePath.asString().replace('.mtlx', '_mtlx.json'))
                    json.dump(doc_result, outfile, indent=2)
    
if __name__ == '__main__':
    main()
