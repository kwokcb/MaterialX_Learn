#!/usr/bin/env python
'''
Command line interface to convert from Usd a file to a MaterialX file 
'''
import os
import argparse

from pxr import Usd

import MaterialX as mx
import mtlxutils.mxfile as mxf
import mtlxutils.mxusd as mxusd

def main():
    parser = argparse.ArgumentParser(description='Usd input file.')
    parser.add_argument(dest='usdFileName', help='Path containing Image file to convert.')
    parser.add_argument('--outputPath', dest='outputPath', default='', help='File path to output documents to. If not specified, is the location of the input document is used.')
    parser.add_argument('--path', dest='paths', action='append', nargs='+', help='An additional absolute search path location (e.g. "/projects/MaterialX")')
    parser.add_argument('--library', dest='libraries', action='append', nargs='+', help='An additional relative path to a custom data library folder (e.g. "libraries/custom")')
    parser.add_argument('--insertComments', dest='insertComments', type=mx.stringToBoolean, default=False, help='Add Usd correspondance comments to document. Default is False')

    opts = parser.parse_args()

    # Check input Usd file
    usdFileName = opts.usdFileName
    if not os.path.exists(usdFileName):
        print('Cannot find Usd file: ', usdFileName)
        exit(-1)    

    # Create output path if required
    outputFilePath = ''
    pathExists = True
    if opts.outputPath:
        outputFilePath = mx.FilePath(opts.outputPath)
        pathExists = os.path.exists(outputFilePath.asString())
    if not pathExists:
        print('Created folder: ', outputFilePath.asString())
        os.makedirs(outputFilePath.asString())

    # Set up MTLX file name
    mtlxFilePath = mx.FilePath(usdFileName)
    if outputFilePath:
        baseName = mx.FilePath(usdFileName).getBaseName()
        mtlxFilePath = outputFilePath / mx.FilePath(baseName)
    mtlxFilePath.removeExtension()
    mtlxFilePath.addExtension('mtlx')

    # Start conversion 
    major, minor, build = Usd.GetVersion() 
    print('- Using Usd Version %s, and MaterialX Version %s' %
        ((str(major) + "." + str(minor) + "." + str(build)), mx.getVersionString()))

    # 1. Read in and flatten Usd 
    stage_unflattend = Usd.Stage.Open(usdFileName) 
    if not stage_unflattend:
        exit(-1)
    layer = stage_unflattend.Flatten()
    stage = Usd.Stage.Open(layer)

    # Create converter and run to emit a new MaterialX document
    doc = None
    converter = mxusd.UsdToMtlx()
    converter.insertComments = opts.insertComments
    doc = converter.emit(stage, opts.paths, opts.libraries)
    if doc:
        print('- Converted Usd file: "%s" to MaterialX file: "%s"' % (usdFileName, mtlxFilePath.asString()))
        mxf.MtlxFile.writeDocumentToFile(doc, mtlxFilePath, mxf.MtlxFile.skipLibraryElement)
        if converter.skippedNodes:
            print('  - Warning: Nodes without MaterialX definitions were not translated: ' + ', '.join(converter.skippedNodes))
    else:
        print(' Failed to convert Usd file: ', usdFileName)


if __name__ == "__main__":
    main()
