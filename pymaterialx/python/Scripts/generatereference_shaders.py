#!/usr/bin/env python
'''
Utility to generate the shader for materials found in a MaterialX document. One file will be generated
for each material / shader found. The currently supported target languages are GLSL, OSL, MDL and ESSL.
'''

import sys, os, argparse, subprocess
import MaterialX as mx
import MaterialX.PyMaterialXGenShader as mx_gen_shader
import MaterialX.PyMaterialXGenGlsl as mx_gen_glsl
import MaterialX.PyMaterialXGenOsl as mx_gen_osl
import MaterialX.PyMaterialXGenMdl as mx_gen_mdl

def validateCode(sourceCodeFile, codevalidator, codevalidatorArgs):
    if codevalidator:
        cmd = codevalidator + ' ' + sourceCodeFile 
        if codevalidatorArgs:
            cmd += ' ' + codevalidatorArgs
        print('----- Run: '+ cmd)
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            result = output.decode(encoding='utf-8')
        except subprocess.CalledProcessError as out:                                                                                                   
            return (out.output.decode(encoding='utf-8'))
    return ""

def main():
    parser = argparse.ArgumentParser(description='Generate reference code for definition in a library.')
    parser.add_argument('--path', dest='paths', action='append', nargs='+', help='An additional absolute search path location (e.g. "/projects/MaterialX")')
    parser.add_argument('--library', dest='libraries', action='append', nargs='+', help='An additional relative path to a custom data library folder (e.g. "libraries/custom")')
    parser.add_argument('--target', dest='target', default='glsl', help='Target shader generator to use (e.g. "glsl, osl, mdl, essl, vulkan"). Default is glsl.')
    parser.add_argument('--outputPath', dest='outputPath', help='File path to output shaders to. If not specified, is the location of the input document is used.')
    parser.add_argument('--validator', dest='validator', nargs='?', const=' ', type=str, help='Name of executable to perform source code validation.')
    parser.add_argument('--validatorArgs', dest='validatorArgs', type=str, help='Optional arguments for code validator.')
    parser.add_argument('--vulkanGlsl', dest='vulkanCompliantGlsl', default=False, type=bool, help='Set to True to generate Vulkan-compliant GLSL when using the genglsl target.')
    parser.add_argument('--setupCMS', dest='setupCMS', default=False, type=bool, help='Set up color management.')
    parser.add_argument('--setupUnits', dest='setupUnits', default=False, type=bool, help='Set up unit system.')
    opts = parser.parse_args()

    print('*************', opts.validatorArgs)
    doc = mx.createDocument()
    #try:
    #    mx.readFromXmlFile(doc, opts.inputFilename)
    #except mx.ExceptionFileMissing as err:
    #    print('Generation failed: "', err, '"')
    #    sys.exit(-1)

    stdlib = mx.createDocument()
    searchPath = mx.FileSearchPath(os.getcwd())
    libraryFolders = []
    if opts.paths:
        for pathList in opts.paths:
            for path in pathList:
                searchPath.append(path)
    if opts.libraries:
        for libraryList in opts.libraries:
            for library in libraryList:
                libraryFolders.append(library)
    libraryFolders.append("libraries/stdlib")
    libraryFolders.append("libraries/pbrlib")
    libraryFolders.append("libraries/bxdf")
    libraryFolders.append("libraries/targets")

    try:
        mx.loadLibraries(libraryFolders, searchPath, stdlib)
        doc.importLibrary(stdlib)
    except mx.Error:
        print('Generation failed: "', mx.Error, '"')
        sys.exit(-1)

    valid, msg = doc.validate()
    if not valid:
        print('Validation warnings for input document:')
        print(msg)
        sys.exit(-1)

    gentarget = 'glsl'
    if opts.target:
        gentarget = opts.target
    if gentarget == 'osl':
        shadergen = mx_gen_osl.OslShaderGenerator.create()
    elif gentarget == 'mdl':
        shadergen = mx_gen_mdl.MdlShaderGenerator.create()
    elif gentarget == 'essl':
        shadergen = mx_gen_glsl.EsslShaderGenerator.create()
    elif gentarget == 'vulkan':
        shadergen = mx_gen_glsl.VkShaderGenerator.create()
    else:
        shadergen = mx_gen_glsl.GlslShaderGenerator.create()
            
    context = mx_gen_shader.GenContext(shadergen)
    context.registerSourceCodeSearchPath(searchPath)

    # If we're generating Vulkan-compliant GLSL then set the binding context
    if opts.vulkanCompliantGlsl:
        bindingContext = mx_gen_glsl.GlslResourceBindingContext.create(0,0)
        context.pushUserData('udbinding', bindingContext)

    genoptions = context.getOptions() 
    genoptions.shaderInterfaceType = mx_gen_shader.ShaderInterfaceType.SHADER_INTERFACE_COMPLETE
    #genoptions.addUpstreamDependencies = False
    genoptions.fileTextureVerticalFlip = True
    
    if opts.setupCMS:
        print('- Set up CMS ...')
        cms = mx_gen_shader.DefaultColorManagementSystem.create(shadergen.getTarget())  
        cms.loadLibrary(doc)
        shadergen.setColorManagementSystem(cms)  

    if opts.setupUnits:
        print('- Set up Units ...')
        unitsystem = mx_gen_shader.UnitSystem.create(shadergen.getTarget())
        registry = mx.UnitConverterRegistry.create()
        distanceTypeDef = doc.getUnitTypeDef('distance')
        registry.addUnitConverter(distanceTypeDef, mx.LinearUnitConverter.create(distanceTypeDef))
        angleTypeDef = doc.getUnitTypeDef('angle')
        registry.addUnitConverter(angleTypeDef, mx.LinearUnitConverter.create(angleTypeDef))
        unitsystem.loadLibrary(stdlib)
        unitsystem.setUnitConverterRegistry(registry)
        shadergen.setUnitSystem(unitsystem)
        genoptions.targetDistanceUnit = 'meter'

    pathPrefix = ''
    currenPath = os.getcwd()
    if opts.outputPath:
        if not os.path.exists(opts.outputPath):
            os.makedirs(opts.outputPath)
        os.chdir(opts.outputPath)
        #pathPrefix = opts.outputPath + os.path.sep
    print('- Shader output path: ' + pathPrefix)

    ignoreNodeList = [ 'arrayappend', 'curveadjust', "disney_brdf_2012", "disney_bsdf_2015", 
                      "surfacematerial", "volumematerial", "constant_filename", "dot_filename",
                     "convert_BSDF_material", "convert_EDF_material"]
    #[ "surfacematerial", "volumematerial", "constant", , "dot_filename",
                     
    ignoreTypeList = ["lightshader", "surfaceshader", "volumeshader", "lightshader" ]
    missingImplementations = []

    failedShaders = ""
    failedValidationShaders = ""
    nodedefs = doc.getNodeDefs()
    nodedefCount = str(len(nodedefs))
    print('Nodedef count: ' + nodedefCount)
    count = 1
    for nodedef in nodedefs:
        
        nodeName = nodedef.getName()

        if nodedef.getNodeString() in ignoreNodeList or nodedef.getType() in ignoreTypeList:
            print('--- Skip nodedef: ' + nodeName)
            continue

        #if nodedef.getNodeString() in ignoreNodeList:
        #    print('--- Skip nodedef: ' + nodeName)
        #    continue

        # Strip out the ND_ if it's there
        functionName = nodeName.removeprefix('ND_')
        functionName = doc.createValidChildName(functionName)
        print('-- %s / %s: Generate code for nodedef: ' % (str(count),nodedefCount)  + nodeName, ': ', functionName + '()')
        count = count + 1

        nodeinterface = nodedef.getImplementation()
        if not nodeinterface: 
            missingImplementations.append(nodeName)
            continue

        node = doc.addNodeInstance(nodedef, functionName)
        if not node:
            failedShaders += (nodeName + ' ')
            continue

        try:
            shader = shadergen.generate(functionName, node, context)   
        except:
            failedShaders += (nodeName + ' ')
            continue;
        
        if shader:
            # Use extension of .vert and .frag as it's type is
            # recognized by glslangValidator
            if gentarget in ['glsl', 'essl', 'vulkan']:
                pixelSource = shader.getSourceCode(mx_gen_shader.PIXEL_STAGE)
                filename = pathPrefix + shader.getName() + "." + gentarget + ".frag"
                file = open(filename, 'w+')
                file.write(pixelSource)
                file.close()
                errors = validateCode(filename, opts.validator, opts.validatorArgs)                

            else:
                pixelSource = shader.getSourceCode(mx_gen_shader.PIXEL_STAGE)
                filename = pathPrefix + shader.getName() + "." + gentarget
                file = open(filename, 'w+')
                file.write(pixelSource)
                file.close()
                errors = validateCode(filename, opts.validator, opts.validatorArgs)

            if opts.validator:
                if errors != "":
                    print("--- Validation failed for node: ", nodeName)
                    print("----------------------------")
                    print('--- Error log: ', errors)
                    print("----------------------------")
                    failedValidationShaders += (nodeName + ' ')
                else:
                    print("--- Validation passed for node:", nodeName)

        else:
            failedShaders += (nodeName + ' ')

    if len(missingImplementations) > 0:
        print("- %d definitions with missing implementations:" % len(missingImplementations))
        print(missingImplementations)
    if len(failedShaders) > 0:
        print("- Failed shader generation:")
        print(failedShaders)
    if len(failedValidationShaders) > 0:
        print("- Failed shader validation: ")
        print(failedValidationShaders)

    if opts.outputPath:
        os.chdir(currentPath)

    if failedShaders != "":
        sys.exit(-1)

if __name__ == '__main__':
    main()