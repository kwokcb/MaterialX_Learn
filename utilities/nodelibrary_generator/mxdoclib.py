#!/usr/bin/env python
'''
Print markdown documentation for each nodedef in the given document or documents in a folder
'''

import sys, os, argparse, shutil, io
import MaterialX as mx

class libraryHtml:
    def writeHeader():
        print('', file=f)

    def writeFooter():
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

def printNodeDictionary(nodegroupdict, opts, f):
    if opts.documentType == "html":

        # Add in left column
        if opts.documentType == "html":
            print('   <div class="col-auto px-0">', file=f)
            print('     <div class="row vh-100 overflow-auto" id="noddict_row">', file=f)
            print('       <div class="col-12 pt-2 pl-2">', file=f)
            print('         <div class="container-md">', file=f)
            print('           <div id="sidebar" class="collapse show collapse-horizontal">', file=f)   

        printNodeDictionaryHTML(nodegroupdict, opts, f)

        if opts.documentType == "html":
            print('           </div>', file=f)
            print('         </div>', file=f)
            print('       </div>', file=f)
            print('     </div>', file=f)
            print('   </div>', file=f)

    else:
        printNodeDictionaryMD(nodegroupdict, opts, f)

# Print out dictionary in Markdown format
def printNodeDictionaryMD(nodegroupdict, opts, f):
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
            groupString += '[' + n + '](#' + n + ') '
        print('* ' + groupString, file=f)

        print('---------', file=f)
    else:
        print(' ', file=f)

def printNodeDictionaryHTML(nodegroupdict, opts, f):

    #print('<p>', file=f)

    print('<form class="d-flex" role="search">', file=f)
    print(' <input id="searchTOC" class="form-control me-2" type="text" placeholder="Search value"'
            ' aria-label="Search">', file=f)
    print('    <div class="btn btn-outline-primary" onclick="return filterTOC()">Filter</div>', file=f)
    print('</form>', file=f)

    #print('<a class="idx text-left btn btn-outline-primary border-0 py-0" type="button" href="index.html">'
    #' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-house" viewBox="0 0 16 16">'
    #' <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5ZM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5 5 5Z"/>'
    #' </svg>'
    #' Home</a>', file=f)
    #print('<br>', file=f)

    #if opts.separateFiles:
    #    print('<a class="text-left btn btn-outline-primary border-0 py-0" type="button" href="all_definitions.html">'
    #    ' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye" viewBox="0 0 16 16">'
    #    ' <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"/>'
    #    ' <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>'
    #    ' </svg>'
    #    ' All Definitions</a>', file=f)
    #    print('<br>', file=f)

    print('    <button class="btn btn-outline-primary border-0" type="button" data-bs-toggle="collapse"'
          ' data-bs-target="#nodeGroupIndex" aria-expanded="false"'
          ' aria-controls="nodeGroupIndex">'
          ' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right-fill" viewBox="0 0 16 16">'
          ' <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>'
          ' </svg>'                                        
          ' Node Groups'
        ' </button>'
        , file=f
    )
    print('<div class="collapse show" id="nodeGroupIndex">', file=f)

    # Add node groups
    for ng in nodegroupdict:
        print('<div class="ps-3">', file=f)
        print('<button class="btn btn-outline-primary border-0 py-0" type="button"'
              ' data-bs-toggle="collapse" data-bs-target="#collapse_%s"'
              ' aria-expanded="false" aria-controls="collapse_%s">'
                ' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right-fill" viewBox="0 0 16 16">'
                ' <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>'
                ' </svg>'                                        
              ' %s'
              ' </button>' % (ng, ng, ng), file=f)
        print('</div>', file=f)

        # Add items per node group
        print('<div class="collapse ps-5" id="collapse_%s">' % ng, file=f)
        print('<div class="d-grid gap-0 col-6">', file=f)
        nl = nodegroupdict[ng]
        for n in nl:
            if opts.separateFiles:
                print('<a class="idx text-left btn btn-outline-primary border-0 py-0" type="button" href="%s">%s</a>' % (n+".html", n), file=f)
            else:
                print('<a class="idx text-left btn btn-outline-primary border-0 py-0" type="button" href="#%s">%s</a>' % (n, n), file=f)
        print('</div>', file=f)
        print('</div>', file=f)

    print('</div>', file=f)

    for x in range(0, 20):
        print('<p>&nbsp</p>', file=f)

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


def printNodeDefHeader(f):
    print('   <div class="col ps-md-2 pt-2">', file=f)
    print('       <div class="row vh-100 overflow-auto" id="nodedefrow">', file=f)
    print('           <div class="col-12 pt-2 pl-2">', file=f)
    print('               <div class="container-md">', file=f)


def printNodeDefFooter(f):
    print('               </div>', file=f)
    print('           </div>', file=f)
    print('       </div>', file=f)
    print('   </div>', file=f)


# Print the document for node definitions in a file
def printNodeDefs(doc, opts, nodedict, f):

    currentNodeString = ""

    graphio = mx.MermaidGraphIo.create()
    graphOptions = mx.GraphIoGenOptions()
    graphOptions.setWriteSubgraphs(False)
    graphOptions.setOrientation(mx.GraphOrientation.LEFT_RIGHT)
    graphio.setGenOptions(graphOptions)

    outputPath = opts.outputPath

    # Output index.html page. 
    rootfile = f
    if opts.separateFiles:
        if opts.documentType == 'html':
            if len(opts.outputFile) > 0:
                f = open(outputPath + "/" + opts.outputFile + ".html", "w")
            else:
                f = open(outputPath + "/index.html", "w")
            printHeader(opts, f)
            printNodeDictionary(nodedict, opts, f)
            printFooter(opts, f)
            f.close()
    else:
        printHeader(opts, f)
        printNodeDictionary(nodedict, opts, f)

        # Add nodedef container
        printNodeDefHeader(f)

    # Dictionary of string buffer outputs to use for file output after
    # being filled in.
    filedict = {}
    # HTML output
    if opts.documentType == 'html':

        for nd in doc.getNodeDefs():

            nodeString = nd.getNodeString()

            if not nodeString in filedict.keys():

                if opts.separateFiles:
                    filename = "outputPath/" + nodeString + ".html"
                    f = io.StringIO(filename)
                    filedict[nodeString] = f

                    # Add header, dictionary
                    printHeader(opts, f)
                    printNodeDictionary(nodedict, opts, f)

                    # Add nodedef container
                    printNodeDefHeader(f)
                else:
                    filename = "outputPath/" + nodeString + ".html"
                    f = io.StringIO(filename)
                    filedict[nodeString] = f

                #print("**** Output node type: ", nodeString)

                # Add node header
                print("<br>", file=f)
                print('<b><a id="%s" class="m-4 mb-0">' % nodeString, file=f)
                print('Node: %s' % nodeString, file=f)
                print('</a></b>', file=f)

            else:
                #if opts.separateFiles:
                f = filedict[nodeString]        

            # Implementation name    
            print('<details>'
                    '<summary class="card-header-sm rounded bg-opacity-50 m-4 py-0 p-3 mb-0 mt-1">'
                    '%s</summary>' % nd.getName(), file=f)
            
            # Implementation Details            
            print('<div class="m-4 mt-0">', file=f)
            print('<div class="row">', file=f)
            print('<div class="col-12">', file=f)
            print('<div class="card border-primary border mb-4">', file=f)
            print('<div class="card-body">', file=f)

            # Preview image(s)
            outputList = nd.getActiveOutputs() #if opts.showInherited  else nd.getOutputs()
            print('<p class="card-text">', file=f)
            for out in outputList:
                outName = out.getName()

                imageName = 'images/nodes/material_' + nd.getName().removeprefix('ND_') + '_' + outName + '_osl.png'
                searchName = '../../documents/' + imageName
                if not os.path.exists(searchName):
                    imageName = 'images/nodes/material_' + nd.getName().removeprefix('ND_') + '_' + outName + '_glsl.png'
                    searchName = '../../documents/' + imageName
                if not os.path.exists(searchName):
                    #print('   ************** CANT find image: ', searchName)
                    imageName = 'images/nodes/' + nd.getName().removeprefix('ND_') + '_osl.png'
                    searchName = '../../documents/' + imageName
                    #print("look for %s" % searchName)
                if not os.path.exists(searchName):
                    #print('   ************** CANT find image: ', searchName)
                    imageName = 'images/nodes/' + nd.getName().removeprefix('ND_') + '_glsl.png'
                    searchName = '../../documents/' + imageName
                    #print("look for %s" % searchName)
                if not os.path.exists(searchName):
                    #print('      ************** CANT find image: ', searchName)
                    imageName = 'images/no_image.png'

                print('<img src="%s" class="rounded float-left" alt=%s style="width: 128px">' 
                    % (imageName, searchName), file=f)           
            print('</p>', file=f)

            # Type
            print('<p class="card-text"><b>Type </b>'
                ' <button type="button"'
                ' class="btn btn-sm btn-outline-secondary pt-0 pb-0">'
                ' %s</button></p>' % nd.getType(), file=f)
            
            # Group
            if len(nd.getNodeGroup()):
                print('<p class="card-text"><b>Node Group </b>'
                    ' <button type="button"'
                    ' class="btn btn-sm btn-outline-secondary pt-0 pb-0">'
                    '%s</button>'
                    '</p>' % nd.getNodeGroup(), file=f)

            print('<p class="card-text">'
                ' <b>Version</b>%s (%s).'
                ' <b>Inherits From </b><button type="button"'
                ' class="btn btn-sm btn-outline-secondary pt-0 pb-0">'
                '%s</button></p>' 
                % (nd.getVersionString(), ("default" if nd.getDefaultVersion() else "non-default"), 
                                          (nd.getInheritString() if len(nd.getInheritString()) > 0 else "none")
                ), file=f)

            print('<p class="card-text"><b>Description:</b> '
                '%s.</p>' % nd.getAttribute('doc'), file=f)

            if opts.nodegraph:

                print('<p class="card-text"><b></b>', file=f)

                mdoutput = ''
                ng = nd.getImplementation()
                if ng and ng.isA(mx.NodeGraph):
                    print('<details><summary><b>Node Graph</b>', file=f)
                    print(' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" '
                        ' class="bi bi-diagram-3 text-primary" viewBox="0 0 16 16">'
                        ' <path fill-rule="evenodd" d="M6 3.5A1.5 1.5 0 0 1 7.5 2h1A1.5 1.5 0 0 1 10 3.5v1A1.5 1.5 0 0 1 8.5 6v1H14a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-1 0V8h-5v.5a.5.5 0 0 1-1 0V8h-5v.5a.5.5 0 0 1-1 0v-1A.5.5 0 0 1 2 7h5.5V6A1.5 1.5 0 0 1 6 4.5v-1zM8.5 5a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1zM0 11.5A1.5 1.5 0 0 1 1.5 10h1A1.5 1.5 0 0 1 4 11.5v1A1.5 1.5 0 0 1 2.5 14h-1A1.5 1.5 0 0 1 0 12.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zm4.5.5A1.5 1.5 0 0 1 7.5 10h1a1.5 1.5 0 0 1 1.5 1.5v1A1.5 1.5 0 0 1 8.5 14h-1A1.5 1.5 0 0 1 6 12.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zm4.5.5a1.5 1.5 0 0 1 1.5-1.5h1a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1-1.5 1.5h-1a1.5 1.5 0 0 1-1.5-1.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1z"/>'
                        ' </svg>', file=f)
                    print('</summary>', file=f) 
                    outputList = ng.getOutputs()
                    mdoutput = graphio.write(ng, outputList)

                    #print('<li> <em>Nodegraph</em>: %s' % ng.getName())
                    if mdoutput:
                        print('<button id="%s_mrender" class="mrender btn btn-outline-primary">Draw Graph</button>' % nd.getName(), file=f)
                        print('<pre><code class="language-mermaid">', file=f)
                        # Output graph
                        print('<div id="%s_mrender_mermaid_output" class="mermaid" hidden>' % nd.getName(), file=f)
                        print('</div>', file=f)
                        # Input text
                        print('<div id="%s_mrender_mermaid_input" class="mermaid" hidden>' % nd.getName(), file=f)
                        print(mdoutput, file=f)
                        print('\n', file=f)
                        print('</div></code></pre>\n', file=f) 
                else:
                    print('<details><summary><b>Code Implementation</b>', file=f)
                    print('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-code-square" viewBox="0 0 16 16">'
                    ' <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>'
                    ' <path d="M6.854 4.646a.5.5 0 0 1 0 .708L4.207 8l2.647 2.646a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 0 1 .708 0zm2.292 0a.5.5 0 0 0 0 .708L11.793 8l-2.647 2.646a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708 0z"/>'
                    ' </svg>', file=f)                   
                    print('</summary>', file=f)
                    print('Non-graph', file=f)

                print('</details>', file=f)
                print('</p>', file=f)  

            print('<p class="card-text"><b>Parameters:</b></p>', file=f)

            # - Print buttons
            print('<ul class="nav nav-pills" role="tablist">', file=f)
            inputList = nd.getActiveInputs() if opts.showInherited  else nd.getInputs()            
            tokenList = nd.getActiveTokens() if opts.showInherited  else nd.getTokens()
            outputList = nd.getActiveOutputs() if opts.showInherited  else nd.getOutputs()
            totalList = inputList + tokenList + outputList
            makeactive = True
            for port in totalList:

                portName = port.getName()
                button_label = portName
                if port.isA(mx.Output): 
                    button_label = "<b>" + portName + "</b>"
                portid = nd.getName() + "_" + port.getName()
                print('<li class="nav-item" role="presentation">'
                    ' <button class="nav-link %s" '
                    ' data-bs-toggle="pill" data-bs-target="#pills-%s"'
                    ' type="button" role="tab" aria-controls="pills-%s"'
                    ' aria-selected="true">%s</button>'
                    '</li>' % ("active" if makeactive else "", portid, portid, button_label), file=f)
                makeactive = False
            print('</ul>', file=f)
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
                    print('  <label class="col-sm-2 col-form-label col-form-label-sm">Description:</label>', file=f)
                    print('    <div class="col-sm-8">', file=f)
                    print('      <textarea class="form-control form-control-sm" rows="3"', file=f)
                    print('        style="resize: none;" disabled>%s </textarea>' % portdoc, file=f)
                    print('    </div>', file=f)
                    print('  </div>', file=f)
                    #print('  <br>')

                # Type / Uniform
                portType = port.getType()
                print('  <div class="form-group row g-2">', file=f)
                print('  <label class="col-sm-2 col-form-label col-form-label-sm">Type:</label>', file=f)
                print('   <div class="col-sm-2">', file=f)
                #print('     <button type="button" class="btn btn-sm btn-outline-secondary pt-0 pb-0">%s</button>'
                #                % portType)
                print('     <input type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                % portType, file=f)
                print('   </div>', file=f)
                if port.getAttribute('uniform'):                                
                    print('   <div class="col-sm-2">', file=f)
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
                    print('<label class="col-sm-2 col-form-label col-form-label-sm">Unit Type / Unit: </label>', file=f)
                    print(' <div class="col-sm-2">', file=f)
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
                    print('          class="col-sm-2 col-form-label col-form-label-sm">Geometry Input: </label>', file=f)
                    print('      <div class="col-sm-2">', file=f)
                    print('          <input type="text" class="form-control form-control-sm" value="%s" disabled>' % defaultgeomprop, file=f)
                    print('      </div>', file=f) 
                    print('  </div>', file=f)                    

                # Default Value
                val = port.getValue()
                valstr = port.getValueString()
                portType = port.getType()
                valueLabel = "Value: "

                # - Special handlig of default value on Output Elements
                if port.isA(mx.Output): 
                    valstr = port.getAttribute('default')
                    if len(valstr) > 0: 
                        val = mx.Value.createValueFromStrings(valstr, portType)
                        if not val:
                            valstr = ""
                        else:
                            valstr = val.getValueString()
                            val = val.getData()
                            valueLabel = "Disabled Value :"
                    else:
                        # This is a connection so make the type a string
                        if port.hasAttribute('defaultinput'):
                            valstr = port.getAttribute('defaultinput')
                            val = valstr
                            portType = 'string'
                            valueLabel = "Disabled Value :"

                # - Regular handling of value on Input Elements
                haveval = len(valstr) > 0 or portType == 'string' or portType == 'filename'
                valueSize = 1
                if haveval:
                    if (portType == 'boolean'):
                        print('  <div class="form-group row g-1">', file=f)
                        print('      <label', file=f)
                        print('          class="col-sm-2 col-form-label col-form-label-sm">%s</label>' % valueLabel, file=f)
                        print('      <div class="col-sm-2">', file=f)
                        print('          <input type="text" class="form-control form-control-sm" value="%s" disabled>' % valstr, file=f)
                        print('      </div>', file=f)
                        print('  </div>', file=f)

                    elif (portType == 'string' or portType == 'filename'):
                        print('  <div class="form-group row g-1">', file=f)
                        print('      <label', file=f)
                        print('          class="col-sm-2 col-form-label col-form-label-sm">%s</label>' % valueLabel, file=f)
                        print('      <div class="col-sm-2">', file=f)
                        print('          <input type="text" class="form-control form-control-sm" value="%s" disabled>' % val, file=f)
                        print('      </div>', file=f)
                        print('  </div>', file=f)

                    elif (portType == 'float' or portType == 'integer'):
                        print('  <div class="form-group row g-1">', file=f)
                        print('      <label', file=f)
                        print('          class="col-sm-2 col-form-label col-form-label-sm">%s </label>' % valueLabel, file=f)
                        print('      <div class="col-sm-2">', file=f)
                        print('          <input type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                            % (val if haveval else -1), file=f)
                        print('      </div>', file=f)
                        print('  </div>', file=f)

                    elif (portType == 'vector2' 
                        or portType == 'vector3' 
                        or portType == 'vector4' 
                        or portType == 'color3' 
                        or portType == 'color4'):

                        print('  <div class="form-group row g-1">', file=f)
                        print('      <label class="col-sm-2 col-form-label col-form-label-sm">%s</label>' % valueLabel, file=f)
                        print('      <div class="col-sm-2">', file=f)
                        print('          <input type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                        % val[0] if haveval else -1, file=f)
                        print('      </div>', file=f)
                        print('      <div class="col-sm-2">', file=f)
                        print('          <input type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                        % val[1] if haveval else -1, file=f)
                        print('      </div>', file=f)

                        valueSize = 2

                        if portType != 'vector2':
                            print('      <div class="col-sm-2">', file=f)
                            print('          <input type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                            % val[2] if haveval else -1, file=f)
                            print('      </div>', file=f)
                            valueSize = 3

                        if portType == 'vector4' or portType == 'color4':
                            print('      <div class="col-sm-2">', file=f)
                            print('          <input type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                            % val[3] if haveval else -1, file=f)
                            print('      </div>', file=f)
                            valueSize = 4
                        
                        if portType == 'color3':
                            hexval = [int(255*val[0]), int(255*val[1]), int(255*val[2])]
                            #print('      <div class="col-sm-2">', file=f)
                            #print('          <input type="text" class="form-control form-control-s value="%02x%02x%02x" disabled>' 
                            #            % (hexval[0], hexval[1], hexval[2]), file=f)                                        
                            #print('      </div>', file=f)                        
                            colorspace = port.getColorSpace()
                            if len(colorspace) > 0:
                                print('   <div class="col-sm-2">', file=f)
                                print('     <input type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                                % colorspace, file=f)
                                print('   </div>', file=f)
                            if colorspace != "none":
                                print('      <div class="col-sm-1">', file=f)
                                print('          <input type="color" value="#%02x%02x%02x" disabled>' % (hexval[0], hexval[1], hexval[2]), file=f)                                        
                                print('      </div>', file=f)

                        elif portType == 'color4' :
                            hexval = [int(255*val[0]), int(255*val[1]), int(255*val[2])]
                            #print('      <div class="col-sm-1">', file=f)
                            #print('          <input type="text" class="form-control form-control-sm" value="%02x%02x%02x" disabled>' 
                            #            % (hexval[0], hexval[1], hexval[2]), file=f)                                        
                            #print('      </div>', file=f)          
                            colorspace = port.getColorSpace()
                            if len(colorspace) > 0:
                                print('   <div class="col-sm-1">', file=f)
                                print('     <input type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                                % colorspace, file=f)
                                print('   </div>', file=f)
                            if colorspace != "none":
                                print('      <div class="col-sm-1">', file=f)
                                print('          <input type="color" value="#%02x%02x%02x" disabled>' % (hexval[0], hexval[1], hexval[2]), file=f)                                        
                                print('      </div>', file=f)
                            valueSize = 4

                        print('  </div>', file=f)

                # Enumeration
                portenum = port.getAttribute('enum') 
                if (len(portenum) > 0):
                    print('  <div class="form-group row g-1">', file=f)
                    print('      <label', file=f)
                    print('          class="col-sm-2 col-form-label col-form-label-sm">Possible Values: </label>', file=f)

                    enumlist = portenum.split(',')
                    if len(enumlist) == 0:
                        enumlist = portenum.split(', ')
                    enumlistSize = len(enumlist)
                    print('      <div class="col-sm-2">', file=f)
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
                                print('      <div class="col-sm-4">', file=f)
                            else:
                                print('      <div class="col-sm-2">', file=f)
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
                    print('<label class="col-sm-2 col-form-label col-form-label-sm">UI Name / Folder / Advanced:</label>', file=f)
                    print(' <div class="col-sm-2">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIName), file=f)
                    print(' </div>', file=f)
                    print(' <div class="col-sm-2">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIGroup), file=f)
                    print(' </div>', file=f)
                    print(' <div class="col-sm-2">', file=f)
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
                    print('<label class="col-sm-2 col-form-label col-form-label-sm">UI Min / Max / Step: </label>', file=f)
                    print(' <div class="col-sm-2">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIMin), file=f)
                    print(' </div>', file=f)
                    print(' <div class="col-sm-2">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIMax), file=f)
                    print(' </div>', file=f)
                    print(' <div class="col-sm-2">', file=f)
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIStep), file=f)
                    print(' </div>', file=f)
                    print('</div>', file=f)

                print(' </div>', file=f)
                print('</div>', file=f)

                makeactive = False

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
                buf = filedict[nodeString]
                printNodeDefFooter(buf)
                printFooter(opts, buf)
                f = open(outputPath + "/" + nodeString + '.html', 'w')
                buf.seek(0)
                shutil.copyfileobj(buf, f)            
                print('Wrote file: ' + outputPath + "/" + nodeString + '.html')
                f.close()
        else:
            # Write al buffers to root file
            f = rootfile
            for nodeString in filedict.keys():
                buf = filedict[nodeString]
                print(buf.getvalue(), file=f)
            printNodeDefFooter(f)
            printFooter(opts, f)
            f.close()

    # Markdown output
    elif opts.documentType == 'md':
        for nd in doc.getNodeDefs():
            nodeString = nd.getNodeString()
            if currentNodeString != nodeString:
                print('### Node: *%s*' % nodeString, file=f)
                currentNodeString = nodeString
            print('<details><summary>%s</summary>' % nd.getName(), file=f)
            print('<p>', file=f)
            print(' ', file=f)
            print('* *Nodedef*: %s' % nd.getName(), file=f)
            print('* *Type*: %s' % nd.getType(), file=f)
            print('* *Node Group*: %s' % ( nd.getNodeGroup() if len(nd.getNodeGroup()) else "none"), file=f)
            implversion = nd.getVersionString()
            if len(implversion) == 0:
                implversion = "1.0"
            print('* *Version*: %s. Is default: %s' % (implversion, nd.getDefaultVersion()), file=f)
            if len(nd.getInheritString()) > 0:
                print('- *Inherits From*: %s' % nd.getInheritString(), file=f)
            docstring = nd.getAttribute('doc')
            if not docstring:
                docstring = "UNDOCUMENTED"
            print('* *Doc*: %s' % docstring)
            if opts.nodegraph:
                mdoutput = ''
                ng = nd.getImplementation()
                if ng and ng.isA(mx.NodeGraph):
                    outputList = ng.getOutputs()
                    mdoutput = graphio.write(ng, outputList)
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
                print('| ' + " | ".join(infos) + ' |')

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
                mx.readFromXmlFile(doc, inputFilename, mx.FileSearchPath(), readOptions)
            except mx.ExceptionFileMissing as err:
                print(err)
    else:
        try:
            mx.readFromXmlFile(doc, rootPath, mx.FileSearchPath(), readOptions)
        except mx.ExceptionFileMissing as err:
            print(err)
            readDoc = False

    return readDoc


def printHeader(opts,f):
    if opts.documentType == "html":

        headerfile = open('header.html', 'r')
        headerines = headerfile.readlines()
        for line in headerines:
            print('%s' % line, end = '', file=f)
        headerfile.close()

        print('<body class="min-vh-100">', file=f)

        print('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"'
        ' integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"'
        ' crossorigin="anonymous"></script>', file=f)

        # mermaid
        print('<script src="https://unpkg.com/mermaid/dist/mermaid.min.js"></script> ', file=f)
        print('<script>'
        ' mermaid.initialize({'
            ' startOnLoad: false,'
            ' theme: document.body.classList.contains("vscode-dark") || document.body.classList.contains("vscode-high-contras")'
            ' ? "dark"'
            ' : "forest"});'
        ' </script>', file=f)

        # Load in top menu
        print('', file=f)
        topfile = open('top.html', 'r')
        toplines = topfile.readlines()
        for line in toplines:
            print('%s' % line, end = '', file=f)
        topfile.close()
        
        # Add in container 
        # 
        print('<div class="container-fluid ">', file=f)
        print(' <div class="row flex-nowrap">', file=f)                     

def printFooter(opts, f):
    if opts.documentType == "html":
        print("<script>", file=f)
        print('  var searchInput = document.getElementById("searchTOC")', file=f)
        print('  searchInput.addEventListener("keypress", filterOnEnter);', file=f)
        print('  var renderButtons = document.querySelectorAll(".mrender");', file=f)
        print('  renderButtons.forEach((renderButton) => { renderButton.addEventListener("click", renderMermaid); });', file=f)
        print("</script>", file=f)
        print('</body>', file=f)
        print('</html>', file=f)

def main():
    parser = argparse.ArgumentParser(description="Print documentation for each nodedef in the given document.")
    parser.add_argument(dest="inputFilename", help="Path of the input MaterialX document or folder.")
    parser.add_argument('--docType', dest='documentType', default='md', help='Document type. Default is "md" (Markdown). Specify "html" for HTML output')
    parser.add_argument('--showInherited', default=False, action='store_true', help='Show inherited inputs. Default is False')
    parser.add_argument('--nodegraph', default=False, action='store_true', help='Show nodegraph implementation if any. Default is False')
    parser.add_argument('--printIndex', default=False, action='store_true', help="Print nodedef index. Default is False")
    parser.add_argument('--outputPath', default="_doc_dump", help="Output path. Default is the current path")
    parser.add_argument('--outputFile', default="root", help="Root output file name. Default is 'root.<docType>'")
    parser.add_argument('--separateFiles', default=False, help="Output separate files. Default is False")

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

    nodedict = getNodeDictionary(doc)
    #printNodeDictionary(nodedict, opts, f)
    printNodeDefs(doc, opts, nodedict, f) 

if __name__ == '__main__':
    main()
