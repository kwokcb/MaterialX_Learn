#!/usr/bin/env python
'''
Print markdown documentation for each nodedef in the given document or documents in a folder
'''

import sys, os, argparse, shutil, io
import MaterialX as mx
from mtlxutils.mxtraversal import MtlxGraphBuilder, MxMermaidGraphExporter

class libraryHtml:
    def writeHeader(f):
        print('', file=f)

    def writeFooter(f):
        print('', file=f)

HEADERS = ('Name', 'Type', 'Default Value',
           'UI name', 'UI min', 'UI max', 'UI Soft Min', 'UI Soft Max', 'UI step', 'UI group', 'UI Advanced', 'Doc', 'Uniform')

ATTR_NAMES = ('uiname', 'uimin', 'uimax', 'uisoftmin', 'uisoftmax', 'uistep', 'uifolder', 'uiadvanced', 'doc', 'uniform' )

# Find all MaterialX files
def getFiles(rootPath):
    filelist = []
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            if file.endswith('mtlx'):
                filelist.append(os.path.join(subdir, file)) 
    return filelist

def printGlossery(doc, opts, f):

    printHeader(opts, f, 'body_header.html', 'MaterialX Elements - Glossary', False)

    print('<div class="col-12 p-4 pt-2 pl-2 pb-0">', file=f)
    print('<h2>Library Glossary</h3>', file=f)

    headerfile = open('glossary_header_buttons.html', 'r')
    headerines = headerfile.readlines()
    for line in headerines:
        print('%s' % line, end = '', file=f)
    headerfile.close()

    typedefs = []
    for td in doc.getTypeDefs():
        typedefs.append( td.getName() )
    typedefs.sort()

    table_start = ''
    incfile = open('table_header.html', 'r')
    inclines = incfile.readlines()
    for line in inclines:
        table_start = line
        break;
    incfile.close()

    table_start = '<table class="table-fixed table shadow table-light table-striped table-hover table-borderless table-responsive" style="font-size: 90%">'
    table_end = '</table>'
    tablehead_start = '<thead class="table-primary">'
    tablerow_start = '<tr>'
    tablehead_item = '<th scope="col" style="width:%d%%">%s</th>'
    tablerow_end = '</tr>'
    tablehead_end = '</thead>'
    tabledata_item = '<td style="width:%d%%">%s</td>'
    tablebody_start = '<tbody>'
    tablebody_end = '</tbody>'
            
    ###################################################
    # Types
    ###################################################

    print('<div class="tab-content" id="pills-tabContent">', file=f)
    print('<div class="tab-pane fade show active" id="pills-types" role="tabpanel"'
            'aria-labelledby="pills-types-tab" tabindex="0">', file=f)
    print('<div class="card shadow border-outline-secondary mb-4">', file=f)
    print('<div class="card-body">', file=f)   

    incfile = open('../documents_internal/typedefs.html', 'r')
    inclines = incfile.readlines()
    for line in inclines:
        print('%s' % line, end = '', file=f)
    incfile.close()

    print(table_start, file=f)
    print(tablehead_start, file=f)
    print(tablerow_start, file=f)
    print(tablehead_item % (25, 'type'), file=f)
    print(tablehead_item % (20, 'semantic'), file=f)
    print(tablehead_item % (20, 'context'), file=f)
    print(tablehead_item % (35, 'Description'), file=f)
    print(tablerow_end, file=f)
    print(tablehead_end, file=f)
    print(table_end, file=f)

    print('<div class="row px-2 pt-0 vh-30 overflow-auto" style="height: 300">', file=f)
    print(table_start, file=f)
    print(tablebody_start, file=f)
    for name in typedefs:
        # Skip none type
        print(tablerow_start, file=f)
        td = doc.getTypeDef(name)
        print(tabledata_item % (25, name), file=f)
        semantic = td.getSemantic()
        print(tabledata_item % (20, semantic), file=f)
        context = td.getContext()
        print(tabledata_item % (20, context), file=f)
        if name == 'none':
            print(tabledata_item % (35, '<b>Deprecated<b>'), file=f)
        elif name == 'filename':
            print(tabledata_item % (35, 'URI to a file'), file=f)
        elif name == 'geomname':
            print(tabledata_item % (35, 'Geometry DAG path. Use in material assignments'), file=f)
        elif name.endswith('shader'):
            prefix = name.removesuffix('shader')
            print(tabledata_item % (35, prefix + ' ' + 'shader'), file=f)
        elif name.endswith('array'):
            prefix = name.removesuffix('array')
            print(tabledata_item % (35, prefix + ' ' + 'array'), file=f)
        elif name.endswith('33'):
            prefix = name.removesuffix('33')
            print(tabledata_item % (35, '3 by 3 ' + prefix), file=f)
        elif name.endswith('44'):
            prefix = name.removesuffix('44')
            print(tabledata_item % (35, '4 by 4 ' + prefix), file=f)
        elif name.endswith('3'):
            prefix = name.removesuffix('3')
            print(tabledata_item % (35, '3 component ' + prefix), file=f)
        elif name.endswith('4'):
            prefix = name.removesuffix('4')
            print(tabledata_item % (35, '4 component ' + prefix), file=f)
        else:
            print(tabledata_item % (35, name), file=f)
        print(tablerow_end, file=f)
    print(tablebody_end, file=f)
    print(table_end, file=f)

    print('</div>', file=f)
    print('</div>', file=f)
    print('</div>', file=f)
    print('</div>', file=f)
    print('</div>', file=f)
    
    ###################################################
    # geom props
    ###################################################
    print('<div class="tab-content" id="pills-tabContent">', file=f)
    print('<div class="tab-pane fade show" id="pills-geometry" role="tabpanel"'
            'aria-labelledby="pills-geometry-tab" tabindex="0">', file=f)
    print('<div class="card shadow border mb-4">', file=f)
    print('<div class="card-body">', file=f)   

    incfile = open('../documents_internal/geomprops.html', 'r')
    inclines = incfile.readlines()
    for line in inclines:
        print('%s' % line, end = '', file=f)
    incfile.close()

    print(table_start, file=f)
    print(tablehead_start, file=f)
    print(tablerow_start, file=f)
    print(tablehead_item % (20, 'name'), file=f)
    print(tablehead_item % (20, 'type'), file=f)
    print(tablehead_item % (20, 'geomprop'), file=f)
    print(tablehead_item % (20, 'space'), file=f)
    print(tablehead_item % (20, 'Description'), file=f)
    print(tablerow_end, file=f)
    print(tablehead_end, file=f)

    print(tablebody_start, file=f)
    for geomprop in doc.getGeomPropDefs():
        print(tablerow_start, file=f)
        name = geomprop.getName()
        print(tabledata_item % (20, name), file=f)
        print(tabledata_item % (20, geomprop.getType()), file=f)
        print(tabledata_item % (20, geomprop.getGeomProp()), file=f)
        print(tabledata_item % (20, geomprop.getSpace()), file=f)
        desc = name
        if name.endswith('object'):
            prefix = name.removesuffix('object') 
            suffix = ' in object space'
        elif name.endswith('world'):
            prefix = name.removesuffix('world')
            suffix =' in world space'
        else:
            prefix = name
            suffix = ""
        if prefix =='P':
            prefix = "Position"
        elif prefix == 'T':
            prefix = "Tangent"
        elif prefix == 'B':
            prefix = "Bitangent"
        elif prefix == 'N':
            prefix = "Normal"
        elif prefix == 'UV0':
            prefix = "First texture coordinate set"
        desc = prefix + suffix
        print(tabledata_item % (20, desc), file=f)
        print(tablerow_end, file=f)
    print(tablebody_end, file=f)
    print(table_end, file=f)  

    print('</div></div></div></div>', file=f)

    ###################################################
    # Units
    ###################################################
    print('<div class="tab-content" id="pills-tabContent">', file=f)
    print('<div class="tab-pane fade show" id="pills-units" role="tabpanel"'
            'aria-labelledby="pills-units-tab" tabindex="0">', file=f)
    print('<div class="card shadow border mb-4">', file=f)
    print('<div class="card-body">', file=f)   

    incfile = open('../documents_internal/unitdefs.html', 'r')
    inclines = incfile.readlines()
    for line in inclines:
        print('%s' % line, end = '', file=f)
    incfile.close()

    for ud in doc.getUnitDefs():
        unittype = ud.getAttribute('unittype')
        print('<p>', file=f)
        print('<div class="btn btn-sm shadow" style="pointer-events: none;" id="%s">%s</div>'
                % ("Unit Type", "Unit Type: " + unittype), file=f)
        print('<br><br>', file=f)

        print(table_start, file=f)
        print(tablehead_start, file=f)
        print(tablerow_start, file=f)
        print(tablehead_item % (30, 'unit'), file=f)
        print(tablehead_item % (30, 'scale'), file=f)
        print(tablehead_item % (30, 'Description'), file=f)
        print(tablerow_end, file=f)
        print(tablehead_end, file=f)

        print(tablebody_start, file=f)
        for unit in ud.getChildren():            
            print(tablerow_start, file=f)
            print(tabledata_item % (30, unit.getName()), file=f)
            print(tabledata_item % (30, unit.getAttribute('scale')), file=f)
            print(tabledata_item % (30, unit.getName()), file=f)
            print(tablerow_end, file=f)
        print(tablebody_end, file=f)
        print(table_end, file=f)
        print('</li>', file=f)

    print('</div></div></div></div>', file=f)

    ###################################################
    # Get color management. Hacky way for now
    ###################################################

    print('<div class="tab-content" id="pills-tabContent">', file=f)
    print('<div class="tab-pane fade show" id="pills-cm" role="tabpanel"'
            'aria-labelledby="pills-cm-tab" tabindex="0">', file=f)
    print('<div class="card shadow border mb-4">', file=f)
    print('<div class="card-body">', file=f)   

    incfile = open('../documents_internal/cmdefs.html', 'r')
    inclines = incfile.readlines()
    for line in inclines:
        print('%s' % line, end = '', file=f)
    incfile.close()

    print(table_start, file=f)
    print(tablehead_start, file=f)
    print(tablerow_start, file=f)
    print(tablehead_item % (34, 'Source Color Space'), file=f)
    print(tablehead_item % (33, 'Destination Color Space'), file=f)
    print(tablehead_item % (33, 'Color Type'), file=f)
    print(tablerow_end, file=f)
    print(tablehead_end, file=f)
    cmnodes = []
    for cmnode in doc.getNodeDefs():
        if cmnode.getNodeGroup() == 'colortransform':
            print(tablerow_start, file=f)
            cmnodes.append(cmnode.getName())
            name = cmnode.getName()
            name = name.removeprefix('ND_')
            namesplit = name.split('_to_')
            type = 'color3'
            if 'color4' in namesplit[1]:
                namesplit[1] = namesplit[1].removesuffix('_color4')
                type = 'color4'
            else:
                namesplit[1] = namesplit[1].removesuffix('_color3')
            print(tabledata_item % (34, namesplit[0]), file=f)
            print(tabledata_item % (34, namesplit[1]), file=f)
            print(tabledata_item % (33, type), file=f)
            print(tablerow_end, file=f)

    print(table_end, file=f)

    print('</div>'*7, file=f)

    printFooter(opts, f)

# Create a dictionary with node group as the primary key for a list of associated
# node types
def getNodeDictionary(doc):
    nodegroups = { "" } 
    nodetypes = { "" }
    nodegroupdict = {}
    for nd in doc.getNodeDefs():
        nodestring = nd.getNodeString() 
        nodetypes.add( nodestring )
        nodegroup = nd.getNodeGroup()
        if not nodegroup:
            nodegroup = "undefined"
        nodegroups.add( nodegroup )
        if not nodegroup in nodegroupdict.keys():
            nodegroupdict[nodegroup] = { nodestring }
        else:
            nodegroupdict[nodegroup].add(nodestring)

    for nd in nodegroupdict:
        nodegroupdict[nd] = sorted(nodegroupdict[nd])

    keys = list(nodegroupdict.keys())
    keys.sort()
    sortednodegroupdict = {i: nodegroupdict[i] for i in keys}
    return sortednodegroupdict

def printNodeDictionary(doc, nodegroupdict, opts, f, forceShow=False):
    if opts.documentType == "html":

        # Add in left column
        if opts.documentType == "html":
            print('   <div class="col-auto p-0">', file=f)            
            print('     <div class="row vh-100 overflow-auto" id="noddict_row">', file=f)
            print('       <div class="col-auto pt-2 pl-2">', file=f)
            print('         <div class="container-fluid">', file=f)
            if opts.separateFiles and not forceShow:
                print('           <div id="sidebar" class="collapse collapse-horizontal">', file=f)
            else:
                print('           <div id="sidebar" class="collapse show collapse-horizontal">', file=f)

        printNodeDictionaryHTML(doc, nodegroupdict, opts, f)

        if opts.documentType == "html":
            print('           </div>', file=f)
            print('         </div>', file=f)
            print('       </div>', file=f)
            print('     </div>', file=f)
            print('   </div>', file=f)

    else:
        printNodeDictionaryMD(doc, nodegroupdict, opts, f)

# Print out dictionary in Markdown format
def printNodeDictionaryMD(doc, nodegroupdict, opts, f):
    for ng in nodegroupdict:
        if opts.documentType == "html":
            print('<h3>Node Group: ' + ng + '</h3>', file=f)
        elif opts.documentType == 'md':
            print('### Node Group: ' + ng, file=f)
        else:
            print('/// @defgroup ' + ng + " Group: " + ng, file=f)
            print('///@{', file=f)

        groupString = ""
        for n in nodegroupdict[ng]:
            groupString += '[' + n + '](#node-' + n + ') '
        print('* ' + groupString, file=f)

        print('---------', file=f)
    else:
        print(' ', file=f)

def printNodeDictionaryHTML(doc, nodegroupdict, opts, f):

    print('<form class="m-2 d-flex" role="search">', file=f)
    print(' <input id="searchTOC" class="form-control-sm p-1 ms-2 me-0" type="text" placeholder="Filter value"'
            ' aria-label="Search">', file=f)
    print('    <div class="m-0 p-1 btn btn-sm btn-outline-secondary" onclick="return filterTOC()">Filter</div>', file=f)
    print('</form>', file=f)

    print('    <button class="btn btn-sm btn-outline-secondary border-0" type="button" data-bs-toggle="collapse"'
          ' data-bs-target="#nodeGroupIndex" aria-expanded="false"'
          ' aria-controls="nodeGroupIndex">'
          ' <img src="../images/caret-right-fill.svg">'
          ' Node Groups'
        ' </button>'
        , file=f
    )
    print('<div class="collapse show pb-0" id="nodeGroupIndex">', file=f)

    # Add node groups
    for ng in nodegroupdict:
        print('<div class="ps-3">', file=f)
        print('<button class="btn btn-sm btn-outline-secondary border-0 py-0" type="button"'
              ' data-bs-toggle="collapse" data-bs-target="#collapse_%s"'
              ' aria-expanded="false" aria-controls="collapse_%s">'
                ' <img src="../images/caret-right-fill.svg">'
              ' %s'
              ' </button>' % (ng, ng, ng), file=f)
        print('</div>', file=f)

        # Add items per node group
        print('<div class="collapse ps-5" id="collapse_%s">' % ng, file=f)
        print('<div class="d-grid gap-0 col-6">', file=f)
        nl = nodegroupdict[ng]
        for n in nl:
            #print('--- Add dict item: ', n)
            if opts.separateFiles:
                print('<a class="idx text-left btn btn-sm btn-outline-secondary border-0 py-0" type="button" href="%s">%s</a>' % (n+".html", n), file=f)
            else:
                print('<a class="idx text-left btn btn-sm btn-outline-secondary border-0 py-0" type="button" href="#%s">%s</a>' % (n, n), file=f)
        print('</div>', file=f)
        print('</div>', file=f)

    print('</div>', file=f)

    #for x in range(0, 20):
    #    print('<p>&nbsp</p>', file=f)

    #for ng in nodegroupdict:
    #    if opts.documentType == "html":
    #        print('<h3>Node Group: ' + ng + '</h3>')
    #    elif opts.documentType == 'md':
    #        print('### Node Group: ' + ng)
    #    else:
    #        print('/// @defgroup ' + ng + " Group: " + ng)
    #        print('///@{')

    #    groupString = ""
    #    if opts.documentType == "html":
    #        for n in nodegroupdict[ng]:
    #            groupString += '<a href="#%s">%s</a> ' % (n, n)
    #        print('<ul>')
    #        print('<li>' + groupString)
    #        print('</ul>')
    #    elif opts.documentType == 'md':
    #        for n in nodegroupdict[ng]:
    #            groupString += '[' + n + '](#' + n + ') '
    #        print('* ' + groupString)
    #    else:
    #        for n in nodegroupdict[ng]:
    #            print('/// @brief class ' + n + ' in ' + ng)
    #        print('///@}')

    #if opts.documentType == "html":
    #    print('<hr>')
    #elif opts.documentType == 'md':
    #    print('---------')
    #else:
    #    print(' ')


def printNodeDefHeader(opts, f):
    if opts.documentType == 'html':
        print('   <div class="col flex-grow-1 ps-md-0 pt-2">', file=f)
        print('       <div class="row vh-100 overflow-auto" id="nodedefrow">', file=f)
        print('           <div class="col-12 flex-grow-1 pt-2 pl-2">', file=f)
        print('               <div class="container-fluid">', file=f)
        print('<div class="ps-2 p-0 nav-item"><a class="nav-link greyhover" data-bs-target="#sidebar" ' 
              + 'data-bs-toggle="collapse"><img src="../images/layout-text-sidebar.svg">'
              + 'Node Index</a></div>', file=f)


def printNodeDefFooter(opts, f):
    if opts.documentType == 'html':
        print('               </div>', file=f)
        print('           </div>', file=f)
        print('       </div>', file=f)
        print('   </div>', file=f)


# Print the document for node definitions in a file
def printNodeDefs(doc, opts, nodedict, f, compareLibDict):

    currentNodeString = ""

    outputPath = opts.outputPath

    # Output index.html page. 
    rootfile = f
    if opts.separateFiles:
        if opts.documentType == 'html':
            if len(opts.outputFile) > 0:
                f = open(outputPath + "/" + opts.outputFile + ".html", "w")
            else:
                f = open(outputPath + "/index.html", "w")
            printHeader(opts, f, 'body_header.html', 'MXLearn -- Definitions')
            printNodeDictionary(doc, nodedict, opts, f, True)
            printFooter(opts, f)
            f.close()
    else:
        printHeader(opts, f, 'body_header.html', 'MXLearn -- All Definitions')
        printNodeDictionary(doc, nodedict, opts, f)

        # Add nodedef container
        printNodeDefHeader(opts, f)

    # Dictionary of string buffer outputs to use for file output after
    # being filled in.
    filedict = {}
    # HTML output
    if opts.documentType == 'html':

        for nd in doc.getNodeDefs():

            nodeString = nd.getNodeString()
            sourceURI = mx.FilePath(nd.getSourceUri())
            nodeLibrary = sourceURI.getBaseName().split('_')[0]

            #impl = nd.getImplementation()
            #dict_implName = impl.getName() if impl else ''

            if not nodeString in filedict.keys():

                if opts.separateFiles:
                    filename = "outputPath/" + nodeString + ".html"
                    f = io.StringIO(filename)
                    filedict[nodeString] = [f, [nodeLibrary]]

                    # Add header, dictionary
                    printHeader(opts, f, 'body_header.html', 'MXLearn ' + nodeString)
                    printNodeDictionary(doc, nodedict, opts, f)

                    # Add nodedef container
                    printNodeDefHeader(opts, f)
                else:
                    filename = "outputPath/" + nodeString + ".html"
                    f = io.StringIO(filename)
                    filedict[nodeString] = [f, [nodeLibrary]]

                #print("**** Output node type: ", nodeString)

                # Add node header
                print("<br>", file=f)
                print('<b><a id="%s" class="ms-2 mb-0">' % nodeString, file=f)
                print('Category: %s' % (nodeString), file=f)
                print('</a></b>', file=f)

            else:
                if nodeLibrary not in filedict[nodeString][1]:
                    filedict[nodeString][1].append(nodeLibrary)
                f = filedict[nodeString][0]

            # Implementation name. Check dictionary and show
            # The library version that the implementation is from.
            implName = ''
            if compareLibDict:
                curVersion = mx.getVersionString()
                for libVersion in compareLibDict:
                    lib = compareLibDict[libVersion]
                    if not lib.getChild(nd.getName()):
                        implName = curVersion
                        break
                    curVersion = libVersion                                    

            if len(implName) == 0:
                implName = '1.38.0 or earlier'
            if len(implName) > 0:
                #print('------ library version is', implName, ' for def: ', nd.getName())
                print('<details open class="p-0">'
                        '<summary class="p-0 card-header-sm rounded bg-opacity-50 m-4 py-0 p-0 mb-0 mt-1">'
                        '%s <button type="button" class="btn bit-sm disabled btn-outline-secondary pt-0 pb-0">%s</button></summary>' 
                        % (nd.getName(), implName), file=f)
            else:
                print('<details open class="p-0">'
                        '<summary class="p-0 card-header-sm rounded bg-opacity-50 m-4 py-0 p-0 mb-0 mt-1">'
                        '%s</summary>' 
                        % (nd.getName()), file=f)
            
            # Implementation Details            
            print('<div class="m-0 mt-0">', file=f)
            print('<div class="row">', file=f)
            print('<div class="col-12">', file=f)
            print('<div class="card shadow border mb-4">', file=f)
            print('<div class="card-body">', file=f)

            # Add row with 2 columns
            print('<div class="row">', file=f)
            
            # ----------------------------------------------------------
            # Top Section
            # ----------------------------------------------------------
            impl = nd.getImplementation()
            if impl:
                nodeLibrary = ''
                sourceURIFull = mx.FilePath(impl.getSourceUri())
                # Pop off the last part of the path until the parent path is "libraries"
                while sourceURIFull.getParentPath().getBaseName() != 'libraries':
                    sourceURIFull = sourceURIFull.getParentPath()
                sourceURI = sourceURIFull
                if not sourceURI.isEmpty():
                    sourceURI = sourceURI.getBaseName()
                    nodeLibrary = sourceURI.split('_')[0]
                #print('library: ', nodeLibrary, ' for impl' , impl.getName())

                if nodeLibrary:
                    print('<div class="col-sm card-text"><b>Library </b>'
                        ' <button type="button"'
                        ' class="btn btn-sm btn-outline-secondary pt-0 pb-0">'
                        '%s</button></div>' % nodeLibrary, file=f)

            # Group
            if len(nd.getNodeGroup()):
                print('<div class="col-sm card-text"><b>Node Group </b>'
                    ' <button type="button"'
                    ' class="btn btn-sm btn-outline-secondary pt-0 pb-0">'
                    '%s</button></div>' % nd.getNodeGroup(), file=f)

            # Type
            print('<div class="col-sm card-text"><b>Type </b>'
                ' <button type="button"'
                ' class="btn btn-sm btn-outline-secondary pt-0 pb-0">'
                ' %s</button></div>' % nd.getType(), file=f)

            # Version        
            ver = nd.getVersionString()
            if not ver:
                ver = "1.0" 
            inh = nd.getInheritString()
            inheritString = ''
            if (len(inh) > 0):
                inheritString = ' <b>. Inherits From </b><button type="button"' + ' class="btn btn-sm btn-outline-secondary pt-0 pb-0">' + inh + '</button>'
            print('<div class="col-sm card-text">'
                ' <b>Version : </b>%s %s %s</div>'                 
                % (ver, ("(default)" if nd.getDefaultVersion() else ""), inheritString), file=f)

            print('</div>', file=f)

            desc = nd.getAttribute('doc')
            if len(desc):
                print('<div class="row"><div class="col card-text"><b>Description :</b> %s</div></div>' % desc, file=f)


            print('<div class="row">', file=f)
            # ------------------------------------------------------
            # Left hand image preview / render
            # ------------------------------------------------------
            print('<div class="col-md-5 p-2">', file=f)

            # Test for interactive viewer
            interactiveViewer = nd.getName() == "ND_gltf_pbr_surfaceshader" 
            if interactiveViewer:
                me = open('../documents_internal/modelviewer.html', 'r')
                melines = me.readlines()
                for line in melines:
                    print('%s' % line, end = '', file=f)
                me.close()
                print('<p></p>', file=f)
            else:
                # Preview image(s)
                outputList = nd.getActiveOutputs() #if opts.showInherited  else nd.getOutputs()
                multiimage = len(outputList) > 1
                if multiimage: 
                    print('<p class="card-text">', file=f)
                    print('<div col>', file=f)
                    print('<div class="row row-cols-3 g-0 d-flex justify-content-start">', file=f)
                for out in outputList:
                    outName = out.getName()

                    imageName = 'material_' + nd.getName().removeprefix('ND_') + '_' + outName + '_genglsl.png'
                    imageName = '../resources/mtlx/nodedef_materials/' + imageName                
                    if not os.path.exists(imageName):
                        #print('-- Cannot find image: ', imageName)
                        imageName = 'images/no_image.png'

                    if multiimage: 
                        print('<div class="col ps-0 pe-0 ms-0 me-0">', file=f)
                        print('<img loading="lazy" src="../%s" class="img-thumbnail thumbnail-padding rounded float-left" width="100%%" alt=%s>'  
                            % (imageName, imageName), file=f) 
                        print('<div style="font-size: %s">%s</div>' % ('70%', outName), file=f)
                        print('</div>', file=f)
                    else:
                        print('<img loading="lazy" src="../%s" class="img-thumbnail rounded float-left" alt=%s style="min-width:64px">' 
                            % (imageName, imageName), file=f) 

                if multiimage:
                    print('</div>', file=f)      
                    print('</div>', file=f)      
                
            print('</div>', file=f)

            # ------------------------------------------------------
            # Right hand basic info
            # ------------------------------------------------------
            print('<div style="font-size:small;" class="col-md-7 border-left pt-2" >', file=f)
            
            #  Parameters
            #
            print('<div class="card-text"><b>Parameters:</b>', file=f)

            # - Print buttons. Default to use "compact" menu vs
            #   a series of buttons.
            inputList = nd.getActiveInputs() if opts.showInherited  else nd.getInputs()            
            tokenList = nd.getActiveTokens() if opts.showInherited  else nd.getTokens()
            outputList = nd.getActiveOutputs() if opts.showInherited  else nd.getOutputs()
            totalList = inputList + tokenList + outputList
            
            compactParams = True
            menuid = nd.getName() + "_menu"

            firstPortName = 'No Parameters'
            if len(totalList) > 0:
                firstPortName = totalList[0].getName()
            if compactParams:
                print('<ul class="nav nav-pills" role="dropdown">', file=f)
                print('<div class="btn btn-sm btn-outline-secondary dropdown-toggle" type="button" id="%s"'
                        'data-bs-toggle="dropdown" aria-expanded="false">'
                        '%s</div>' % (menuid, firstPortName), file=f)
                
                print('<ul class="dropdown-menu overflow-auto" style="max-height: 15em" aria-labelledby="%s">' % menuid, file=f)
            else:
                print('<ul class="nav nav-pills" role="tablist">', file=f)


            makeactive = True
            menuIdString = "'" + menuid + "'"
            onclickAction = ' onclick="document.getElementById(' + menuIdString + ').textContent = this.textContent;" '

            for port in totalList:

                portName = port.getName()
                button_label = portName
                if port.isA(mx.Output): 
                    button_label = "<b>" + portName + "</b>"
                portid = nd.getName() + "_" + port.getName()

                if not compactParams:
                   print('<li class="nav-item" role="presentation">'
                    ' <button class="nav-link %s" '
                    ' data-bs-toggle="pill" data-bs-target="#pills-%s"'
                    ' type="button" role="tab" aria-controls="pills-%s"'
                    ' aria-selected="true">%s</button>' 
                    % ("active" if makeactive else "", portid, portid, button_label), file=f)
                else:
                  print('<li class="nav-item dropdown-item" role="presentation">', file=f)
                  print(
                    ' <div class="nav-item %s" '
                    ' data-bs-toggle="tab" data-bs-target="#pills-%s"'
                    ' role="tab" aria-controls="pills-%s"'
                    ' aria-selected="true" %s>%s</div>'
                    '</li>' % ("active" if makeactive else "", portid, portid, onclickAction, button_label), file=f)
                makeactive = False
            print('</ul>', file=f)
            if compactParams:
                print('</ul>', file=f)

            print('</div>', file=f)

            print('<br>', file=f)
                    
            makeactive = True
            for port in totalList:
                # - Content per parameter
                portid = nd.getName() + "_" + port.getName()
                print('<div class="tab-content">', file=f)
                print(' <div class="tab-pane %s" id="pills-%s"' % ("show active" if makeactive else "", portid), file=f)
                print('  role="tabpanel" aria-labelledby="pills-%s-tab" tabindex="0">' % portid, file=f)

                # Description
                portdoc = port.getAttribute('doc')
                if len(portdoc) > 0:
                    print('  <div class="form-group row g-2">', file=f)
                    print('  <label class="col-2 col-form-label col-form-label-sm">Doc</label>', file=f)
                    print('    <div class="col-10">', file=f)
                    if len(portdoc) > 128:
                        print('      <textarea class="form-control form-control-sm" rows="3"', file=f)
                    else:
                        print('      <textarea class="form-control form-control-sm" rows="2"', file=f)
                    print('        style="resize: none;" disabled>%s </textarea>' % portdoc, file=f)
                    print('    </div>', file=f)
                    print('  </div>', file=f)
                    #print('  <br>')

                # Default Value
                val = port.getValue()
                valstr = port.getValueString()
                portType = port.getType()
                valueLabel = "Value "

                # - Special handling of default value on Output Elements
                if port.isA(mx.Output): 
                    valstr = port.getAttribute('default')
                    if len(valstr) > 0: 
                        val = mx.Value.createValueFromStrings(valstr, portType)
                        if not val:
                            valstr = ""
                        else:
                            valstr = val.getValueString()
                            val = val.getData()
                            valueLabel = "Disabled Value"
                    else:
                        # This is a connection so make the type a string
                        if port.hasAttribute('defaultinput'):
                            valstr = port.getAttribute('defaultinput')
                            val = valstr
                            portType = 'string'
                            valueLabel = "Disabled Value"

                # - Regular handling of value on Input Elements
                haveval = len(valstr) > 0 or portType == 'string' or portType == 'filename'
                useSliders = True
                valueSize = 1
                portUIMin = port.getAttribute('uimin')
                portUIMax = port.getAttribute('uimax')
                portUIStep = port.getAttribute('uistep')
                if haveval:
                    if (portType == 'boolean'):
                        print('  <div class="form-group row g-1">', file=f)
                        print('      <label', file=f)
                        print('          class="col-2 col-form-label col-form-label-sm">%s</label>' % valueLabel, file=f)
                        print('      <div class="col-10">', file=f)
                        print('          <input id="%s" type="text" class="form-control form-control-sm" value="%s" disabled>' % (portid, valstr), file=f)
                        print('      </div>', file=f)
                        print('  </div>', file=f)

                    elif (portType == 'string' or portType == 'filename'):
                        print('  <div class="form-group row g-1">', file=f)
                        print('      <label', file=f)
                        print('          class="col-2 col-form-label col-form-label-sm">%s</label>' % valueLabel, file=f)
                        print('      <div class="col">', file=f)
                        print('          <input type="text" class="form-control form-control-sm" value="%s" disabled>' % val, file=f)
                        print('      </div>', file=f)
                        print('  </div>', file=f)

                    elif (portType == 'float' or portType == 'integer'):
                        print('  <div class="form-group row g-1">', file=f)
                        print('      <label', file=f)
                        print('          class="col-2 col-form-label col-form-label-sm">%s </label>' % valueLabel, file=f)
                        print('      <div class="col">', file=f)
                        if (interactiveViewer and haveval and portType == 'float' and useSliders):
                            uimin = ""
                            uimax = ""
                            uistep = "step=0.001"
                            if (portUIMin and len(portUIMin) > 0):
                                uimin = 'min="%f"' % float(portUIMin)
                            if (portUIMax and len(portUIMax) > 0):
                                uimax = 'max="%f"' % float(portUIMax)
                            if (portUIStep and len(portUIStep) > 0):
                                uistep = 'step="%f"' % float(portUIStep)
                            #print('add slider: ', portid, '. uimin: ', uimin, ' uimax: ', uimax, ' uistep: ', uistep, '. Value: ', val)
                            print('          <input id="%s" type="range" class="form-range form-range-sm" %s %s %s value="%g" %s>' 
                                  % (portid, uimin, uimax, uistep, val if haveval else 0, "enabled" if interactiveViewer else "disabled"), file=f)
                            print('      </div><div class="col">', file=f)
                            print('          <input id="%s_slider" type="number" class="form-control form-control-sm" %s %s %s value="%g" %s>' 
                                  % (portid, uimin, uimax, uistep, val if haveval else 0, "enabled" if interactiveViewer else "disabled"), file=f)
                            #print('          <label class="form-control form-control-sm"><span id="%s_slider">%f</span></label>' % (portid, val), file=f)
                        else:
                            print('          <input id="%s" type="number" class="form-control form-control-sm" step="0.01" value="%g" %s>' 
                                                % (portid, val if haveval else 0, "enabled" if interactiveViewer else "disabled"), file=f)
                        print('      </div>', file=f)
                        print('  </div>', file=f)

                    elif portType in { 'matrix33', 'matrix44' }:
                        gridSize = 3 if portType == 'matrix33' else 4
                        colSize = 3 if portType == 'matrix33' else 2
                        # Note that the [] operators do not seem to work in Python
                        # so must use string parsing which is a bit ugly.
                        gridValues = mx.splitString(valstr,", ")
                        for i in range(gridSize):
                            label = valueLabel if i == 0 else ""

                            print('  <div class="form-group row g-1">', file=f)
                            print('      <label class="col-2 col-form-label col-form-label-sm">%s</label>' % label, file=f)
                            
                            print('      <div class="col-%d">' % colSize, file=f)
                            print('          <input type="number" class="form-control form-control-sm" value="%s" disabled>' 
                                            % gridValues[i*gridSize], file=f)
                            print('      </div>', file=f)
                            
                            print('      <div class="col-%d">' % colSize, file=f)
                            print('          <input type="number" class="form-control form-control-sm" value="%s" disabled>' 
                                            % gridValues[i*gridSize+1], file=f)
                            print('      </div>', file=f)

                            print('      <div class="col-%d">' % colSize, file=f)
                            print('          <input type="number" class="form-control form-control-sm" value="%s" disabled>' 
                                            % gridValues[i*gridSize+2], file=f)
                            print('      </div>', file=f)

                            if gridSize == 4:
                                print('      <div class="col-%d">' % colSize, file=f)
                                print('          <input type="number" class="form-control form-control-sm" value="%s" disabled>' 
                                                % gridValues[i*gridSize+3], file=f)
                                print('      </div>', file=f)

                            print('</div>', file=f)
                     

                    elif (portType == 'vector2' 
                        or portType == 'vector3' 
                        or portType == 'vector4' 
                        or portType == 'color3' 
                        or portType == 'color4'):

                        widths = [2,3,3,3]
                        if portType in ['vector2']:
                            widths = [5,5]
                        elif portType in ['vector3']:
                            widths = [3,3,3]
                        elif portType in ['vector4', 'color4']:
                            widths = [2,2,2,2]                              

                        print('  <div class="form-group row g-1">', file=f)
                        print('      <label class="col-2 col-form-label col-form-label-sm">%s</label>' % valueLabel, file=f)

                        if portType == 'color3':
                            hexval = [int(255*val[0]), int(255*val[1]), int(255*val[2])]
                            #print('      <div class="col-2">', file=f)
                            #print('          <input type="text" class="form-control form-control-s value="%02x%02x%02x" disabled>' 
                            #            % (hexval[0], hexval[1], hexval[2]), file=f)                                        
                            #print('      </div>', file=f)                        
                            colorspace = port.getColorSpace()
                            if len(colorspace) > 0:
                                print('   <div class="col-2">', file=f)
                                print('     <input id="%s", type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                                % (portid, colorspace), file=f)
                                print('   </div>', file=f)
                            if colorspace != "none":
                                print('      <div class="col-2">', file=f)
                                print('          <input class="custom_colorbox2" id="%s" type="color" value="#%02x%02x%02x" %s>' % (portid, hexval[0], hexval[1], hexval[2], 
                                                                                                           "" if interactiveViewer else "disabled"), file=f)                                        
                                print('      </div>', file=f)

                        elif portType == 'color4' :
                            hexval = [int(255*val[0]), int(255*val[1]), int(255*val[2])]
                            #print('      <div class="col-1">', file=f)
                            #print('          <input type="text" class="form-control form-control-sm" value="%02x%02x%02x" disabled>' 
                            #            % (hexval[0], hexval[1], hexval[2]), file=f)                                        
                            #print('      </div>', file=f)          
                            colorspace = port.getColorSpace()
                            if len(colorspace) > 0:
                                print('   <div class="col-1">', file=f)
                                print('     <input id="%s" type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                                % (portid, colorspace), file=f)
                                print('   </div>', file=f)
                            if colorspace != "none":
                                print('      <div class="col-2">', file=f)
                                print('          <input id="%s" class="custom_colorbox2" type="color" value="#%02x%02x%02x" %s>' % (portid, hexval[0], hexval[1], hexval[2],
                                                                                                           "" if interactiveViewer else "disabled"), file=f)                                        
                                print('      </div>', file=f)
                            valueSize = 4

                        print('      <div class="col-%d">' % widths[0], file=f)
                        print('          <input id="%s" type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                        % (portid + "_0", val[0] if haveval else -1), file=f)
                        print('      </div>', file=f)
                        
                        print('      <div class="col-%d">' % widths[1], file=f)
                        print('          <input id="%s" type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                        % (portid + "_1", val[1] if haveval else -1), file=f)
                        print('      </div>', file=f)

                        valueSize = 2

                        if portType != 'vector2':
                            print('      <div class="col-%d">' % widths[2], file=f)
                            print('          <input id="%s" type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                            % (portid + "_2", val[2] if haveval else -1), file=f)
                            print('      </div>', file=f)
                            valueSize = 3

                        if portType == 'vector4' or portType == 'color4':
                            print('      <div class="col-%d">' % widths[3], file=f)
                            print('          <input id="%s" type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                            % (portid + "_3", val[3] if haveval else -1), file=f)
                            print('      </div>', file=f)
                            valueSize = 4
                        


                        print('  </div>', file=f)

             # Type / Uniform
                portType = port.getType()
                print('  <div class="form-group row g-2">', file=f)
                print('  <label class="col-2 col-form-label col-form-label-sm">Type</label>', file=f)
                widths = [ 10, 0]
                if port.getAttribute('uniform'):
                    widths = [8, 2]
                print('   <div class="col-%d">' % widths[0], file=f)
                #print('     <button type="button" class="btn btn-sm btn-outline-secondary pt-0 pb-0">%s</button>'
                #                % portType)
                print('     <input type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                % portType, file=f)
                print('   </div>', file=f)
                if port.getAttribute('uniform'):                                
                    print('   <div class="col-%d">' % widths[1], file=f)
                    print('     <label>Uniform</label>', file=f)
                    print('     <input type="checkbox" class="form-check-input form-check-sm" disabled %s>' 
                                    % ("checked" if port.getAttribute('uniform') else ""), file=f)
                    print('   </div>', file=f)
                print('  </div>', file=f)

                # Unit type / Unit
                portUnit = port.getAttribute('unit')
                portUnitType = port.getAttribute('unittype')
                if len(portUnit) > 0 or len(portUnitType):
                    print('<div class="form-group row g-1">', file=f)
                    print('<label class="col-2 col-form-label col-form-label-sm">Unit Type / Unit: </label>', file=f)
                    print(' <div class="col-2">', file=f)
                    print('   <button type="button" class="btn btn-sm btn-outline-secondary pt-0 pb-0">%s</button>'
                                % (str(portUnitType) if len(portUnitType) else "none"), file=f)
                    print('   <button type="button" class="btn btn-sm btn-outline-secondary pt-0 pb-0">%s</button>'
                                % (str(portUnit) if len(portUnit) else "none"), file=f)
                    print(' </div>', file=f)
                    print('</div>', file=f)

                # Default Geom Property
                defaultgeomprop = port.getAttribute('defaultgeomprop')
                if len(defaultgeomprop) > 0:
                    print('  <div class="form-group row g-1">', file=f)
                    print('      <label', file=f)
                    print('          class="col-2 col-form-label col-form-label-sm">Geometry Input: </label>', file=f)
                    print('      <div class="col-2">', file=f)
                    print('          <input type="text" class="form-control form-control-sm" value="%s" disabled>' % defaultgeomprop, file=f)
                    print('      </div>', file=f) 
                    print('  </div>', file=f)                    

                # Enumeration
                portenum = port.getAttribute('enum') 
                if (len(portenum) > 0):
                    print('  <div class="form-group row g-1">', file=f)
                    print('      <label', file=f)
                    print('          class="col-2 col-form-label col-form-label-sm">Possible Values: </label>', file=f)

                    enumlist = portenum.split(',')
                    if len(enumlist) == 0:
                        enumlist = portenum.split(', ')
                    enumlistSize = len(enumlist)
                    print('      <div class="col-2">', file=f)
                    print('        <select class="form-select form-select-sm" style="font-size:90%%" size="%d" disabled>'
                        % enumlistSize, file=f)
                    for enumopt in enumlist:
                        print('          <option>%s</option>' % enumopt, file=f)
                    print('       </select>', file=f)
                    print('      </div>', file=f)                            
                    
                    portenumValues = port.getAttribute('enumvalues')
                    if len(portenumValues) > 0:
                        enumValuelist = portenumValues.split(',')
                        if len(enumValuelist) == 0:
                            enumValuelist = portenumValues.split(', ')
                        enumValuelistSize = len(enumValuelist)
                        if enumValuelistSize > 0:
                            if valueSize > 1:
                                print('      <div class="col-4">', file=f)
                            else:
                                print('      <div class="col-2">', file=f)
                            print('        <select class="form-select form-select-sm" style="font-size:90%%" size="%d" disabled>'
                                % (enumValuelistSize / valueSize), file=f)
                            for i in range(0,enumValuelistSize,valueSize):
                                #enumValueOpt = enumValuelist
                                val = '       <option>'
                                for j in range(0,valueSize):
                                    val += enumValuelist[i+j] + " "
                                val += '</option>'
                                print(val, file=f)
                            print('        </select>', file=f)
                            print('       </div>', file=f)                            
                    
                    print('  </div>', file=f)
                        
                # UI
                # - name, group, advanced
                portUIName = port.getAttribute('uiname')
                portUIGroup = port.getAttribute('uifolder')
                portUIAdvanced = port.getAttribute('uiadvanced')
                if len(portUIName) > 0 or len(portUIGroup) > 0 or len(portUIAdvanced) > 0: 
                    if len(portUIName) == 0:
                        portUIName = "none"
                    if len(portUIGroup) == 0:
                        portUIGroup = "none"
                    if len(portUIAdvanced) == 0:
                        portUIAdvanced = "false"

                    print('<div class="form-group row g-1">', file=f)
                    print('<label class="col-2 col-form-label col-form-label-sm">UI Name | Grp. | Adv.</label>', file=f)
                    print(' <div class="col-4">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIName), file=f)
                    print(' </div>', file=f)
                    print(' <div class="col-3">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIGroup), file=f)
                    print(' </div>', file=f)
                    print(' <div class="col-3">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIAdvanced), file=f)
                    print(' </div>', file=f)
                    print('</div>', file=f)

                # - min / max / step
                portUIMin = port.getAttribute('uimin')
                portUIMax = port.getAttribute('uimax')
                portUIStep = port.getAttribute('uistep')
                if len(portUIMin) > 0 or len(portUIMax) > 0 or len(portUIStep) > 0: 
                    print('<div class="form-group row g-1">', file=f)
                    print('<label class="col-2 col-form-label col-form-label-sm">UI Min | Max | Step: </label>', file=f)
                    print(' <div class="col-4">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIMin), file=f)
                    print(' </div>', file=f)
                    print(' <div class="col-3">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIMax), file=f)
                    print(' </div>', file=f)
                    print(' <div class="col-3">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIStep), file=f)
                    print(' </div>', file=f)
                    print('</div>', file=f)

                print(' </div>', file=f)
                print('</div>', file=f)

                makeactive = False

            print('</div>', file=f)
            print('</div>', file=f)            

            # Implementation section
            #
            if impl:
                print('<p class="card-text"><b></b>', file=f)

                mdoutput = ''
                if impl.isA(mx.NodeGraph):
                    print('<details><summary><b>Node Graph</b>', file=f)
                    print('<img class="bg-light" src="../images/diagram-3.svg">', file=f)
                    print('</summary>', file=f) 

                    if not opts.nodegraph:
                        print('%s' % impl.getName(), file=f)
                    else:
                        outputList = []
                        for out in impl.getOutputs():
                            outputList.append(out.getNamePath())
                        
                        builder = MtlxGraphBuilder(impl)
                        builder.execute()
                        graphio = MxMermaidGraphExporter(builder.getDictionary(), builder.getConnections())
                        graphio.setOrientation('TB')
                        graphio.execute()
                        mdoutput = graphio.getGraph(False)
                        #mdoutput = mdoutput.replace('```mermaid', '')
                        #mdoutput = mdoutput.replace('```', '')
                        #mdoutput = mdoutput.replace('/default', '/default1')

                        #print('<li> <em>Nodegraph</em>: %s' % ng.getName())
                        if mdoutput:
                            print('<button id="%s_mrender" class="mrender btn btn-sm btn-outline-secondary">Draw Graph</button>' % nd.getName(), file=f)
                            print('<button id="%s_mrcopy" class="mrcopy btn btn-sm btn-outline-secondary">Copy Graph</button>' % nd.getName(), file=f)
                            print('<pre><code class="language-mermaid">', file=f)
                            # Output graph
                            print('<div id="%s_mrender_mermaid_output" class="border rounded p-2 mermaid" hidden>' % nd.getName(), file=f)
                            print('</div>', file=f)
                            # Input text
                            print('<div id="%s_mrender_mermaid_input" class="mermaid" hidden>' % nd.getName(), file=f)
                            print(mdoutput, file=f)
                            print('\n', file=f)
                            print('</div></code></pre>\n', file=f) 

                elif impl.isA(mx.Implementation):

                    print('<details><summary><b>Code Implementation</b>', file=f)
                    print('<img src="../images/code-square.svg">', file=f)
                    print('</summary>', file=f)
                    print('<br>', file=f)

                    allimpl = doc.getMatchingImplementations(nd.getName())
                    # sort all allimpl
                    allimpl.sort(key=lambda x: x.getAttribute('target'))
                    for impl in allimpl:

                        targetString = impl.getAttribute('target')
                        print('  <div class="form-group row g-2">', file=f)
                        print('  <label class="col-2 col-form-label col-form-label-sm">Target:</label>', file=f)
                        print('   <div class="col-2">', file=f)
                        print('     <input type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                        % impl.getAttribute('target'), file=f)
                        print('   </div>', file=f)
                        print('  </div>', file=f)

                        foundimpl = False

                        srcfile = impl.getAttribute('file')
                        if len(srcfile) > 0:                        
                            print('  <div class="form-group row g-2">', file=f)
                            print('  <label class="col-2 col-form-label col-form-label-sm">File:</label>', file=f)
                            print('   <div class="col-8">', file=f)
                            isURL = srcfile.startswith('http')
                            if not isURL:
                                sourceUri = mx.FilePath(nd.getSourceUri())
                                sourceUri = sourceUri.getParentPath()
                                sourceUri = mx.FilePath(sourceUri.getBaseName())
                                libraryName = "https://github.com/AcademySoftwareFoundation/MaterialX/tree/main/libraries"
                                libraryName = libraryName + '/' + sourceUri.asString()
                                libraryName = libraryName + '/' + targetString + '/' + srcfile
                                hrefString = libraryName 
                            else:
                                hrefString = srcfile

                            print('  <a href="%s" target="_blank">' % hrefString, file=f)
                            print('     <input type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                            % srcfile, file=f)
                            print('  </a>', file=f)
                            print('   </div>', file=f)
                            print('  </div>', file=f)
                            foundimpl = True

                        srccode = impl.getAttribute('sourcecode')
                        if len(srccode) > 0:
                            print('  <div class="form-group row g-2">', file=f)
                            print('  <label class="col-2 col-form-label col-form-label-sm">Code:</label>', file=f)
                            print('    <div class="col-8">', file=f)
                            print('      <textarea class="form-control form-control-sm" rows="3"', file=f)
                            print('        style="resize: none;" disabled>%s </textarea>' % srccode, file=f)
                            print('    </div>', file=f)
                            print('  </div>', file=f)
                            foundimpl = True

                        srcfunct = impl.getAttribute('function')
                        if len(srcfunct) > 0:                        
                            print('  <div class="form-group row g-2">', file=f)
                            print('  <label class="col-2 col-form-label col-form-label-sm">Function:</label>', file=f)
                            print('   <div class="col-4">', file=f)
                            print('     <input type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                            % srcfunct, file=f)
                            print('   </div>', file=f)
                            print('  </div>', file=f)
                        
                        if not foundimpl:
                            print('  <div class="form-group row g-2">', file=f)
                            print('  <label class="col-2 col-form-label col-form-label-sm">Code:</label>', file=f)
                            print('    <div class="col-4">', file=f)
                            print('     <input type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                            % 'Via Code Generation', file=f)
                            print('    </div>', file=f)
                            print('  </div>', file=f)

                        print('<hr>', file=f)

                print('</details>', file=f)
                print('</p>', file=f)  

            print('</div>', file=f)
            print('</div>', file=f)
            print('</div>', file=f)


            #    print('<tr>')
            #    infos = []
            #    if port in outputList:
            #        infos.append('<em>'+ port.getName() + '</em>')
            #    elif port in tokenList:
            #        infos.append(port.getName())
            #    else:
            #        infos.append('<b>'+ port.getName() + '</b>')
            #    infos.append(port.getType())
            #    val = port.getValue()
            #    if val and port.getType() == "float":
            #        val = round(val, 6)
            #    infos.append(str(val))
            #   for attrname in ATTR_NAMES:
            #       infos.append(port.getAttribute(attrname))
            #    for info in infos:
            #        print('<td>' + info + '</td>')
            #    print('</tr>')
            #print('</table>')
            #print('</p></details>')
            print('</div>', file=f)
            print('</details>', file=f)


        # Write buffers to disk
        if opts.separateFiles:
            # Write each buffer to a separate file
            for nodeString in filedict.keys():
                buf = filedict[nodeString][0]
                printNodeDefFooter(opts, buf)
                printFooter(opts, buf)
                f = open(outputPath + "/" + nodeString + '.html', 'w')
                buf.seek(0)
                shutil.copyfileobj(buf, f)            
                #print('Wrote file: ' + outputPath + "/" + nodeString + '.html', 'libraries:', 
                #      filedict[nodeString][1])
                f.close()
        else:
            # Write al buffers to root file
            f = rootfile
            for nodeString in filedict.keys():
                buf = filedict[nodeString][0]
                print(buf.getvalue(), file=f)
            printNodeDefFooter(opts, f)
            printFooter(opts, f)
            f.close()

    # Markdown output
    elif opts.documentType == 'md':
        for nd in doc.getNodeDefs():
            nodeString = nd.getNodeString()
            if currentNodeString != nodeString:
                print('### Category: *%s*' % nodeString, file=f)
                currentNodeString = nodeString
            print('<details open><summary>%s</summary>' % nd.getName(), file=f)
            print('<p>', file=f)
            print(' ', file=f)
            print('* *Nodedef*: %s' % nd.getName(), file=f)
            print('* *Type*: %s' % nd.getType(), file=f)
            print('* *Group*: %s' % ( nd.getNodeGroup() if len(nd.getNodeGroup()) else "none"), file=f)
            implversion = nd.getVersionString()
            if len(implversion) == 0:
                implversion = "1.0"
            print('* *Version*: %s. Is default: %s' % (implversion, nd.getDefaultVersion()), file=f)
            if len(nd.getInheritString()) > 0:
                print('- *Inherits From*: %s' % nd.getInheritString(), file=f)
            docstring = nd.getAttribute('doc')
            if not docstring:
                docstring = "UNDOCUMENTED"
            print('* *Doc*: %s' % docstring, file=f)
            if opts.nodegraph:
                mdoutput = ''
                ng = nd.getImplementation()
                if ng and ng.isA(mx.NodeGraph):
                    outputList = []
                    for out in ng.getOutputs():
                        outputList.append(out.getNamePath())

                    builder = MtlxGraphBuilder(ng)
                    builder.execute()
                    graphio = MxMermaidGraphExporter(builder.getDictionary(), builder.getConnections())
                    graphio.setOrientation('TB')
                    graphio.execute()
                    mdoutput = graphio.getGraph(False)
                    mdoutput = mdoutput.replace('```mermaid', '')
                    mdoutput = mdoutput.replace('```', '')
                    mdoutput = mdoutput.replace('/', '_')
                    #mdoutput = mdoutput.replace('default', 'default1')

                    #mdoutput = graphio.write(ng, outputList)
                    print('* *Nodegraph*: %s' % ng.getName(), file=f)
                    if mdoutput:
                        print('\n', file=f)
                        print('```mermaid', file=f)
                        print(mdoutput, file=f)
                        print('```', file=f)
                    else:
                        print('None', file=f)
                else:
                    print('* *Implementation*: Non-graph', file=f)
            
            print(' \n', file=f)
            print('| ' + ' | '.join(HEADERS) + ' |', file=f)
            print('|' + ' ---- |' * len(HEADERS) + '', file=f)
            inputList = nd.getActiveInputs() if opts.showInherited  else nd.getInputs()
            tokenList = nd.getActiveTokens() if opts.showInherited  else nd.getTokens()
            outputList = nd.getActiveOutputs() if opts.showInherited  else nd.getOutputs()
            totalList = inputList + tokenList + outputList;
            for port in totalList:
                infos = []
                if port in outputList:
                    infos.append('*'+ port.getName() + '*')
                elif port in tokenList:
                    infos.append(port.getName())
                else:
                    infos.append('**'+ port.getName() + '**')
                infos.append(port.getType())
                val = port.getValue()
                if val and port.getType() == "float":
                    val = round(val, 6)
                infos.append(str(val))
                for attrname in ATTR_NAMES:
                    infos.append(port.getAttribute(attrname))
                print('| ' + " | ".join(infos) + ' |', file=f)

        print('</p></details>', file=f)
        print(' ', file=f)


# Read in a single document or documents in a folder
# Return false if any document cannot be read
def readDocuments(rootPath, doc):

    readDoc = True
    # Read in comments and doc strings.
    # Currently these are hard to parse to get node definition documentation
    # as they are just top level "comment" elements.
    readOptions = mx.XmlReadOptions()
    readOptions.readComments = True

    if os.path.isdir(rootPath): 
        filelist = getFiles(rootPath)
        for inputFilename in filelist:
            try:  
                libDoc = mx.createDocument()              
                mx.readFromXmlFile(libDoc, inputFilename, mx.FileSearchPath(), readOptions)
                doc.importLibrary(libDoc)
            except mx.ExceptionFileMissing as err:
                print(err)
    else:
        try:
            libDoc = mx.createDocument()              
            mx.readFromXmlFile(libDoc, rootPath, mx.FileSearchPath(), readOptions)
            doc.importLibrary(libDoc)
        except mx.ExceptionFileMissing as err:
            print(err)
            readDoc = False

    return readDoc


def printHeader(opts,f, body_header, title, addIndex=True):
    if opts.documentType == "html":

        headerfile = open('header.html', 'r')
        headerines = headerfile.readlines()
        for line in headerines:
            line = line.replace('<title></title>', '<title>' + title + '</title>')
            line = line.replace('_TOP_FOLDER_', '../..')
            print('%s' % line, end = '', file=f)
        headerfile.close()

        print('<body class="min-vh-100">', file=f)

        # Set up side menu
        indexItem = '<li class="nav-item"><a class="nav-link greyhover" data-bs-target="#sidebar" data-bs-toggle="collapse"><img src="_TOP_FOLDER_/documents/images/layout-text-sidebar.svg">Index</a></li>'

        print('', file=f)
        topfile = open(body_header, 'r', encoding="utf-8")
        toplines = topfile.readlines()
        for line in toplines:
            # Insert "index" item
            if addIndex:
                line = line.replace('<!--INDEX_ITEM-->', indexItem)            
            line = line.replace('_TOP_FOLDER_', '../..')
            print('%s' % line, end = '', file=f)
        topfile.close()

        print('', file=f)
        topfile = open('navigation.html', 'r', encoding="utf-8")
        toplines = topfile.readlines()
        for line in toplines:
            # Insert "index" item
            if addIndex:
                line = line.replace('<!--INDEX_ITEM-->', indexItem)            
            line = line.replace('_TOP_FOLDER_', '../..')
            print('%s' % line, end = '', file=f)
        topfile.close()

        # Add in container 
        # 
        print('<div class="container-fluid px-0">', file=f)
        print(' <div class="row ">', file=f)                     

def printFooter(opts, f):
    if opts.documentType == "html":
        print('', file=f)
        topfile = open('footer.html', 'r', encoding="utf-8")
        toplines = topfile.readlines()
        for line in toplines:
            print('%s' % line, end = '', file=f)
        topfile.close()

        print("<script>", file=f)
        print('  var searchInput = document.getElementById("searchTOC")', file=f)
        print('  if (searchInput) {', file=f)
        print('   searchInput.addEventListener("keypress", filterOnEnter);', file=f)
        print('  }', file=f)
        print('  var renderButtons = document.querySelectorAll(".mrender");', file=f)
        print('  if (renderButtons) {', file=f)
        print('     renderButtons.forEach((renderButton) => { renderButton.addEventListener("click", renderMermaid); });', file=f)
        print('  }', file=f)
        print('  var copyButtons = document.querySelectorAll(".mrcopy");', file=f)
        print('  if (copyButtons) {', file=f)
        print('     copyButtons.forEach((copyButton) => { copyButton.addEventListener("click", copyMermaid); });', file=f)
        print('  }', file=f)
        print('  var collapses = document.querySelectorAll("[data-bs-toggle=\'collapse\']");', file=f)
        print('  if (collapses) {', file=f)
        print( '    collapses.forEach((collapseItem) => { collapseItem.addEventListener("click", toggleIndexArea); });', file=f)
        print('  }', file=f)
        print("</script>", file=f)
        print('<script src="../js/gltf_pbr_helpers.js"></script>', file=f)
        print('<script src="../js/ui_helpers.js"></script>', file=f)        

        print('</body>', file=f)
        print('</html>', file=f)

def main():
    parser = argparse.ArgumentParser(description="Print documentation for each nodedef in the given document.")
    parser.add_argument(dest="inputFilename", help="Path of the input MaterialX document or folder.")
    parser.add_argument('--compareLib', dest='compareLib', default='', help='Compare against this library')
    parser.add_argument('--docType', dest='documentType', default='md', help='Document type. Default is "md" (Markdown). Specify "html" for HTML output')
    parser.add_argument('--showInherited', default=False, action='store_true', help='Show inherited inputs. Default is False')
    parser.add_argument('--nodegraph', default=False, action='store_true', help='Show nodegraph implementation if any. Default is False')
    parser.add_argument('--outputPath', default="_doc_dump", help="Output path. Default is the current path")
    parser.add_argument('--outputFile', default="Definitions_By_Group", help="Root output file name. Default is 'Definitions_By_Group.<docType>'")
    parser.add_argument('--separateFiles', default=False, type=bool, help="Output separate files. Default is False")

    opts = parser.parse_args()

    # Check for output file name. If none then dump everything to std output.
    outputFileName = ""
    f = sys.stdout
    if len(opts.outputFile) > 0:
        outputFileName = opts.outputFile + "." + opts.documentType

    # Create output path if not exist
    if len(outputFileName) > 0:
        outputPath = opts.outputPath + "/"
        if not os.path.exists(outputPath):
            os.mkdir(outputPath)

    # Check if we are writing to a single file
    if not opts.separateFiles:
        f = open(outputPath + outputFileName, "w")
        print('Writing output to file: ', outputPath + outputFileName)

    rootPath = opts.inputFilename;
    doc = mx.createDocument()
    readDocuments(rootPath, doc)    

    # Get current version
    major, minor, patch = mx.getVersionIntegers()
    print('Build dict for: major %d minor %d patch %d' % (major, minor, patch))
    # Look for previous version libraries
    comparePath = mx.FilePath(opts.compareLib)
    compareLibDict = dict()
    # Add the current version
    compareLibDict[mx.getVersionString()] = doc
    while minor >= 38:
        if patch == 0:
            patch = 9
            minor = minor - 1
        else:
            patch = patch - 1
        prevVersion = '%d.%d.%d' % (major, minor, patch)
        compareLibPath = comparePath / ("libraries_" + prevVersion)
        if compareLibPath.exists():
            compareDoc = mx.createDocument()
            readDocuments(compareLibPath.asString(), compareDoc)
            compareLibDict[prevVersion] = compareDoc 
            print('Add comparison version %s from %s' % (prevVersion, compareLibPath.asString()))

    nodedict = getNodeDictionary(doc)
    printNodeDefs(doc, opts, nodedict, f, compareLibDict) 

    # Print type dictionary
    if not opts.separateFiles and opts.documentType == 'html':
        print('Writing Glossary to file: ', outputPath + "library_glossary.html")
        f = open(outputPath + "library_glossary.html", "w")
        printGlossery(doc, opts, f)
        f.close()

if __name__ == '__main__':
    main()
