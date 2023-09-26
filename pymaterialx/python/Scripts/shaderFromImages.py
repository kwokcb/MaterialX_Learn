#!/usr/bin/env python
'''
Given a set of image files. Parse based on image names to create a new shader
'''

import sys, os, argparse
import MaterialX as mx

def skipLibraryElement(elem):
    return not elem.hasSourceUri()

def main():
    parser = argparse.ArgumentParser(description='Generate shader code for each material / shader in a document.')
    parser.add_argument(dest='inputFileName', help='Root name of image files to examine.')
    parser.add_argument(dest='inputFileRoot', help='Root name of image files to examine.')
    parser.add_argument('--imageType', default='png', help='Image file extension.')
    parser.add_argument('--library', dest='libraries', action='append', nargs='+', help='Library paths')
    parser.add_argument('--outputPath', dest='outputPath', help='File path to output shaders to. If not specified, is the location of the input document is used.')
    parser.add_argument('--shadingModel', dest='shadingModel', help='Shading model to create.')
    parser.add_argument('--mapping', dest='mappings', action='append', nargs='+', help='Custom mappings')
    opts = parser.parse_args()

    doc = mx.createDocument()
    imageName = mx.FilePath(opts.inputFileName).getBaseName()
    print('Image name: ', imageName)
    imagePath = mx.FileSearchPath(os.path.dirname(opts.inputFileName))
    searchPath = imagePath
    libraryFolders = []
    if opts.libraries:
        for libraryList in opts.libraries:
            for library in libraryList:
                libraryFolders.append(library)
    libraryFolders.append("libraries")
    stdlib = mx.createDocument()
    mx.loadLibraries(libraryFolders, searchPath, stdlib)
    doc.importLibrary(stdlib)

    #.casefold() 
    imageChannels = {}
    imageRoot = opts.inputFileRoot;
    for path in os.listdir(imagePath.asString()):
        # check if current path is a file
        if imageRoot in path:
            channel = path.replace(imageRoot, '')
            channel = channel.replace("." + opts.imageType, '')
            channel_key = channel.lower()
            if channel_key == 'basecolor':
                channel_key = 'base_color'
            elif channel_key == 'metallic':
                channel_key = 'metalness'
            elif channel_key == 'roughness':
                channel_key = 'specular_roughness'
            elif channel_key == 'specularlevel':
                channel_key = 'specular'
            imageChannels[channel_key] = path
        #if os.path.isfile(os.path.join(imagePath.asString(), path)):
    print(imageChannels)

    #doc = mx.createDocument()
    materialNodeName = doc.createValidChildName(imageRoot) + '_material'
    shaderNodeName = doc.createValidChildName(imageRoot) + '_shader'
    shaderNode = doc.addNode("standard_surface", shaderNodeName, "surfaceshader")
    #shaderNode.addInputsFromNodeDef()
    for inputChannel in imageChannels:
        print(inputChannel)
        input = shaderNode.addInputFromNodeDef(inputChannel) 
        if (input):
            imageNodeName = doc.createValidChildName(inputChannel + "_image")
            imageNode = doc.addNode("tiledimage", imageNodeName, input.getType())

            for tx in ['uvtiling', 'uvoffset', 'readlworldimagesize', 'realworldtilesize']:
                new1 = imageNode.addInputFromNodeDef(tx)
                if new1:
                    print('Added: ', tx)

            #imageNode.addInputsFromNodeDef()
            imageFileInput = imageNode.addInputFromNodeDef('file')
            if imageFileInput:
                imageFileInput.setValue(imageChannels[inputChannel])
                imageFileInput.setType('filename')
                print('Add input channel: ', inputChannel)

            if inputChannel != 'normal':
                input.setNodeName(imageNode.getName())
            else:
                imageNodeName = doc.createValidChildName(inputChannel + "_normalmap")
                normalMap = doc.addNode("normalmap", imageNodeName, 'vector3')
                lookup = normalMap.addInputFromNodeDef('in')
                #if lookup:
                lookup.setNodeName(imageNode.getName())
                input.setNodeName(normalMap.getName())

    materialNode = doc.addMaterialNode(materialNodeName, shaderNode)
    outputName = imagePath.asString() + '/' + materialNodeName + '.mtlx'
    print('Write: ', outputName)
    writeOptions = mx.XmlWriteOptions()
    writeOptions.writeXIncludeEnable = False
    writeOptions.elementPredicate = skipLibraryElement
    mx.writeToXmlFile(doc, outputName, writeOptions)

if __name__ == '__main__':
    main()
