#!/usr/bin/env python
'''
Create documents with each definition as a separate material
'''

import sys, os, argparse
import MaterialX as mx


# Find all MaterialX files
def getFiles(rootPath):
    filelist = []
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            if file.endswith('mtlx'):
                filelist.append(os.path.join(subdir, file)) 
    return filelist

# Print the document for node definitions in a file
def createMaterials(doc, opts):

    ignoreNodeList = [ "surfacematerial", "volumematerial", "constant", "arrayappend", "dot_filename" ]
    ignoreTypeList = [  "volumeshader", "lightshader" ]

    nodedefs = doc.getNodeDefs()
    nodedefCount = str(len(nodedefs))
    if nodedefCount == 0:
        print('No definitions to create materials for')
    else:    
        print('Create materials for %s definitions' % nodedefCount)

    for nodedef in nodedefs:

        outdoc = mx.createDocument()

        # Create node
        nodeName = nodedef.getName()
        functionName = nodeName.removeprefix('ND_')
        functionName = outdoc.createValidChildName(functionName)

        node = outdoc.addNodeInstance(nodedef, functionName)
        node.removeAttribute('nodedef')

        for input in nodedef.getActiveInputs():
            inputName = input.getName()
            inputType = input.getType()
            valueElem = node.getInput(inputName)
            if (not valueElem):
                newElem = node.addInput(inputName, inputType)
                newElem.copyContentFrom(input)
                newElem.removeAttribute('doc')
            #    if newElem and input.hasValueString():
            #        newElem.setValueString(input.getValueString())

        # Add outputs if none on node
        for output in nodedef.getActiveOutputs():
            outputName = output.getName()
            outputType = output.getType()
            outputElem = node.getOutput(outputName)
            if (not outputElem):
                outputElem = node.addOutput(outputName, outputType)

            shaderNodeName = outdoc.createValidChildName('shader_' + node.getName() + '_' + outputName)                
            materialNodeName = outdoc.createValidChildName('material_' + node.getName() + '_' + outputName)                

            isMultiOutput = nodedef.getType() == 'multioutput'

            if outputType == 'EDF':
                shaderNode = outdoc.addNode("surface", shaderNodeName, "surfaceshader")
                edfInput = shaderNode.addInput('edf', 'EDF')
                edfInput.setNodeName(node.getName())
                if isMultiOutput:
                    edfInput.setAttribute('output', outputName)
                materialNode = outdoc.addMaterialNode(materialNodeName, shaderNode)
            elif outputType == 'BSDF':
                shaderNode = outdoc.addNode("surface", shaderNodeName, "surfaceshader")
                edfInput = shaderNode.addInput('bsdf', 'BSDF')
                edfInput.setNodeName(node.getName())
                if isMultiOutput:
                    edfInput.setAttribute('output', outputName)
                materialNode = outdoc.addMaterialNode(materialNodeName, shaderNode)
            elif outputType == 'surfaceshader':
                materialNode = outdoc.addMaterialNode(materialNodeName, node)
            elif outputType == 'volumeshader':
                materialNode = outdoc.addMaterialNode(materialNodeName, node)
            #elif outputType == 'displacementshader':
            elif outputType in { 'float', 'vector2', 'vector3', 'color3', 'color4' }:
                if outputType == 'float':
                    shaderNode = outdoc.addNode("surface_unlit", shaderNodeName, "surfaceshader")
                    newInput = shaderNode.addInput('emission', 'float')
                    newInput.setNodeName(node.getName())
                    if isMultiOutput:
                        newInput.setAttribute('output', outputName)
                else:

                    # Input to convert is upstream node
                    convertNodeName = node.getName()
                    if outputType != 'color3':

                        needExtraConvert = False

                        # Add conversion node in between as there is no vec2 -> color3 node type
                        # Would be nice to have this added to avoid this extra step.
                        if outputType in { 'vector2'}:
                            convertName = 'convert_' + outputType + '_vector3'
                            convertNodeName = outdoc.createValidChildName(convertName)
                            convertNode = outdoc.addNodeInstance(doc.getNodeDef('ND_' + convertNodeName), convertNodeName)
                            newInput = convertNode.addInput('in', outputType)
                            newInput.setNodeName(node.getName())
                            if isMultiOutput:
                                newInput.setAttribute('output', outputName)
                            needExtraConvert = True
                            # Set output type to vector3 for next convert
                            outputType = 'vector3'

                        convertName = 'convert_' + outputType + '_color3'
                        convert2NodeName = outdoc.createValidChildName(convertName)
                        convertNode = outdoc.addNodeInstance(doc.getNodeDef('ND_' + convert2NodeName), convert2NodeName)
                        newInput = convertNode.addInput('in', outputType)
                        newInput.setNodeName(convertNodeName)                        
                        if isMultiOutput and not needExtraConvert:
                            newInput.setAttribute('output', outputName)
                        convertNodeName = convert2NodeName                            

                    shaderNode = outdoc.addNode("surface_unlit", shaderNodeName, "surfaceshader")
                    newInput = shaderNode.addInput('emission_color', 'color3')
                    newInput.setNodeName(convertNodeName)
                    if isMultiOutput:
                        newInput.setAttribute('output', outputName)
                    materialNode = outdoc.addMaterialNode(materialNodeName, shaderNode)

        filename = opts.outputPath + '/' + functionName + ".mtlx"
        print("Write defintion file: %s" % filename)
        mx.writeToXmlFile(outdoc, filename)

# Read in a single document or documents in a folder
# Return false if any document cannot be read
def readDocuments(rootPath, doc):

    readDoc = True

    if os.path.isdir(rootPath): 
        filelist = getFiles(rootPath)
        for inputFilename in filelist:
            try:
                mx.readFromXmlFile(doc, inputFilename)
            except mx.ExceptionFileMissing as err:
                print(err)
    else:
        try:
            mx.readFromXmlFile(doc, rootPath)
        except mx.ExceptionFileMissing as err:
            print(err)
            readDoc = False

    return readDoc

def main():
    parser = argparse.ArgumentParser(description="Print documentation for each nodedef in the given document.")
    parser.add_argument(dest="libraryPath", help="Path of the input MaterialX document or folder definitions.")
    parser.add_argument('--outputPath', dest='outputPath', help='File path to output materials.')

    opts = parser.parse_args()

    # Read library
    rootPath = opts.libraryPath;
    doc = mx.createDocument()
    readDocuments(rootPath, doc)    

    # Create output directory
    if opts.outputPath:
        if not os.path.exists(opts.outputPath):
            os.makedirs(opts.outputPath)

    # Create material files
    createMaterials(doc, opts) 

if __name__ == '__main__':
    main()
