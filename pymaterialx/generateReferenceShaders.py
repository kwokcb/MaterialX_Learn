import MaterialX as mx
import MaterialX.PyMaterialXGenGlsl as mx_gen_glsl
import MaterialX.PyMaterialXGenMdl as mx_gen_mdl
import MaterialX.PyMaterialXGenMsl as mx_gen_msl
import MaterialX.PyMaterialXGenOsl as mx_gen_osl
import MaterialX.PyMaterialXGenShader as mx_gen_shader

import os
import argparse
import logging

logger = logging.getLogger('MXGR')
logging.basicConfig(level=logging.INFO) 

def loadDefinitions(opts):
    stdlib = mx.createDocument()
    searchPath = mx.getDefaultDataSearchPath()
    libraryFolders = []
    if opts.paths:
        for pathList in opts.paths:
            for path in pathList:
                searchPath.append(path)
    if opts.libraries:
        for libraryList in opts.libraries:
            for library in libraryList:
                libraryFolders.append(library)
    libraryFolders.extend(mx.getDefaultDataLibraryFolders())
    mx.loadLibraries(libraryFolders, searchPath, stdlib)
    return stdlib, searchPath

def createGenerator(opts):
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
    elif gentarget == 'wgsl':
        shadergen = mx_gen_glsl.WgslShaderGenerator.create()
    elif gentarget == 'msl':
        shadergen = mx_gen_msl.MslShaderGenerator.create()
    else:
        shadergen = mx_gen_glsl.GlslShaderGenerator.create()

    return shadergen

def createGenContext(shadergen, doc, searchPath, inputFilename):
            
    shadergen.registerTypeDefs(doc)

    context = mx_gen_shader.GenContext(shadergen)
    context.getOptions().addUpstreamDependencies = True
    context.getOptions().fileTextureVerticalFlip = True

    codeSearchPath = searchPath
    codeSearchPath.append(os.path.dirname(inputFilename))
    context.registerSourceCodeSearchPath(codeSearchPath)

    return context

def main():
    parser = argparse.ArgumentParser(description='Generate shader code definitions in a library.')
    parser.add_argument('-p', '--path', dest='paths', action='append', nargs='+', help='An additional absolute search path location (e.g. "/projects/MaterialX")')
    parser.add_argument('-l', '--library', dest='libraries', action='append', nargs='+', help='An additional relative path to a custom data library folder (e.g. "libraries/custom")')
    parser.add_argument('-t', '--target', dest='target', default='glsl', help='Target shader generator to use (e.g. "glsl, osl, mdl, essl, vulkan, wgsl"). Default is glsl.')
    parser.add_argument('-op', '--outputPath', dest='outputPath', help='File path to output shaders to. If not specified, is the location of the input document is used.')
    parser.add_argument('-ot', '--outputTree', dest='outputTree', action='store_true', help='If set, output shaders to a tree structure mirroring the library structure.')
    parser.add_argument('-d', '--debug', dest='debug', action='store_true', help='If set, enable debug logging.')

    opts = parser.parse_args()

    if opts.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled.")

    outputPath = opts.outputPath if opts.outputPath else "./reference_" + opts.target + "_shaders"
    os.makedirs(outputPath, exist_ok=True)
    logger.info(f'Output path: {outputPath}')
    pathPrefix = outputPath + os.path.sep

    logger.info("Using MaterialX version: {mx.getVersionString()}")
    datalib, searchPaths = loadDefinitions(opts)
    nodedefs = datalib.getNodeDefs()
    nodedef_count = len(nodedefs)
    if nodedef_count == 0:
        logger.error("No node definitions were loaded. Exiting.")
        return
    
    logger.info(f"Loaded in %d node definitions {nodedef_count}") 
    generator = createGenerator(opts)
    target = generator.getTarget()
    logger.info(f"Using generator: {target}")
    context = createGenContext(generator, datalib, searchPaths, "")

    count = 0
    search_path_string = searchPaths.asString(",")
    search_path_list = search_path_string.split(",")

    for nodedef in nodedefs:
        nodeName = nodedef.getName()
        nodeType = nodedef.getType()
        sourceURL = "" 
        final_path = pathPrefix

        if opts.outputTree:
            sourceURL = nodedef.getSourceUri()
            # Remove any paths in searchPath from sourceURL:
            for path in search_path_list:
                if sourceURL.startswith(path):
                    sourceURL = sourceURL[len(path):]
                    break
            if sourceURL:
                dir_path = os.path.dirname(sourceURL)
                final_path = pathPrefix + dir_path
                os.makedirs(final_path, exist_ok=True)

        logger.debug(f"[{count}] Generating reference for node: {nodeName} {nodeType}")
        count = count + 1

        if nodeType == "material":
            logger.debug(f"Skipping material node definition: '{nodeName}'")
            continue

        nodeNode = nodedef.getNodeString()
        if nodeName.startswith("ND_"):
            nodeName = nodeName[3:]

        interface = nodedef.getImplementation(target)
        if not interface:
            logger.warning(f"Skip generating reference for unimplemented node '{nodeName}'")
            continue

        try:
            node = datalib.addNodeInstance(nodedef, nodeName)
        except Exception as err:
            logger.warning(f"Error creating node instance for '{nodeName}' : {str(err)}")
            continue

        try:
            shader = generator.generate(node.getName(), node, context)
        except Exception as err:
            logger.error(f"Error generating shader for node '{nodeName}': {str(err)}")
            datalib.removeChild(node.getName())
            continue

        if opts.target in ['glsl', 'essl', 'vulkan', 'msl', 'wgsl']:
            pixelSource = shader.getSourceCode(mx_gen_shader.PIXEL_STAGE)
            filename = final_path + "/" + shader.getName() + "." + opts.target + ".frag"
            logger.debug(f"- Wrote pixel shader to: {filename}")
            file = open(filename, 'w+')
            file.write(pixelSource)
            file.close()
            #errors = validateCode(filename, opts.validator, opts.validatorArgs)                

            vertexSource = shader.getSourceCode(mx_gen_shader.VERTEX_STAGE)
            filename = final_path + "/" + shader.getName() + "." + opts.target + ".vert"
            logger.debug(f"- Wrote vertex shader to: {filename}")
            file = open(filename, 'w+')
            file.write(vertexSource)
            file.close()
            #errors += validateCode(filename, opts.validator, opts.validatorArgs)

        else:
            pixelSource = shader.getSourceCode(mx_gen_shader.PIXEL_STAGE)
            filename = final_path + "/" + shader.getName() + "." + opts.target
            logger.debug(f"- Wrote shader to: {filename}")
            file = open(filename, 'w+')
            file.write(pixelSource)
            file.close()
            #errors = validateCode(filename, opts.validator, opts.validatorArgs)        
        
        datalib.removeChild(node.getName())

if __name__ == '__main__':
    main()
