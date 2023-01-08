#!/usr/bin/env python
'''
Print markdown documentation for each nodedef in the given document or documents in a folder
'''

import sys, os, argparse
import MaterialX as mx

class libraryHtml:
    def writeHeader():
        print('')

    

    def writeFooter():
        print('')

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

def printNodeDictionary(nodegroupdict, opts):
    if opts.documentType == "html":
        printNodeDictionaryHTML(nodegroupdict, opts)
    else:
        printNodeDictionaryMD(nodegroupdict, opts)

# Print out dictionary in Markdown format
def printNodeDictionaryMD(nodegroupdict, opts):
    for ng in nodegroupdict:
        if opts.documentType == "html":
            print('<h3>Node Group: ' + ng + '</h3>')
        elif opts.documentType == 'md':
            print('### Node Group: ' + ng)
        else:
            print('/// @defgroup ' + ng + " Group: " + ng)
            print('///@{')

        groupString = ""
        for n in nodegroupdict[ng]:
            groupString += '[' + n + '](#' + n + ') '
        print('* ' + groupString)

        print('---------')
    else:
        print(' ')

def printNodeDictionaryHTML(nodegroupdict, opts):

    #print('<p>')

    print('<form class="d-flex" role="search">')
    print(' <input id="searchTOC" class="form-control me-2" type="text" placeholder="Search value"'
            ' aria-label="Search">')
    print('    <div class="btn btn-outline-primary" onclick="return filterTOC()">Filter</div>')
    print('</form>')

    print('    <button class="btn btn-outline-primary border-0" type="button" data-bs-toggle="collapse"'
          ' data-bs-target="#nodeGroupIndex" aria-expanded="false"'
          ' aria-controls="nodeGroupIndex">'
          ' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right-fill" viewBox="0 0 16 16">'
          ' <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>'
          ' </svg>'                                        
          ' Node Groups'
        ' </button>'
    #' </p>'
    )
    print('<div class="collapse show" id="nodeGroupIndex">')

    # Add node groups
    for ng in nodegroupdict:
        print('<div class="ps-3">')
        print('<button class="btn btn-outline-primary border-0 py-0" type="button"'
              ' data-bs-toggle="collapse" data-bs-target="#collapse_%s"'
              ' aria-expanded="false" aria-controls="collapse_%s">'
                ' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right-fill" viewBox="0 0 16 16">'
                ' <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>'
                ' </svg>'                                        
              ' %s'
              ' </button>' % (ng, ng, ng))
        print('</div>')

        # Add items per node group
        print('<div class="collapse ps-5" id="collapse_%s">' % ng)
        print('<div class="d-grid gap-0 col-6">')
        nl = nodegroupdict[ng]
        for n in nl:
            print('<a class="idx text-left btn btn-outline-primary border-0 py-0" type="button" href="#%s">%s</a>' % (n, n))
        print('</div>')
        print('</div>')

    print('</div>')

    for x in range(0, 20):
        print('<p>&nbsp</p>')

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

# Print the document for node definitions in a file
def printNodeDefs(doc, opts):

    currentNodeString = ""

    graphio = mx.GraphIORegistry.create()
    graphio.addGraphIO(mx.MermaidGraphIO.create())

    for nd in doc.getNodeDefs():

        # HTML output
        if opts.documentType == 'html':
            nodeString = nd.getNodeString()
            if currentNodeString != nodeString:
                print("<br>")
                print('<b><a id="%s" class="m-4 mb-0">' % nodeString)
                print('Node: %s' % nodeString)
                print('</a></b>')
                currentNodeString = nodeString  

            # Implementation name    
            print('<details>'
                    '<summary class="card-header-sm rounded bg-opacity-50 m-4 py-0 p-3 mb-0 mt-1">'
                    '%s</summary>' % nd.getName())
            
            # Implementation Details            
            print('<div class="m-4 mt-0">')
            print('<div class="row">')
            print('<div class="col-12">')
            print('<div class="card border-primary border mb-4">')
            print('<div class="card-body">')

            # Preview image
            print('<p class="card-text">'
                '<img src="images/Default_osl.png" '
                'class="rounded float-left" alt="..." '
                'style="width: 128px; max-width: 50;"></p>')           

            # Type
            print('<p class="card-text"><b>Type </b>'
                ' <button type="button"'
                ' class="btn btn-sm btn-outline-secondary pt-0 pb-0">'
                ' %s</button></p>' % nd.getType())
            
            # Group
            if len(nd.getNodeGroup()):
                print('<p class="card-text"><b>Node Group </b>'
                    ' <button type="button"'
                    ' class="btn btn-sm btn-outline-secondary pt-0 pb-0">'
                    '%s</button>'
                    '</p>' % nd.getNodeGroup())

            print('<p class="card-text">'
                ' <b>Version</b>%s (%s).'
                ' <b>Inherits From </b><button type="button"'
                ' class="btn btn-sm btn-outline-secondary pt-0 pb-0">'
                '%s</button></p>' 
                % (nd.getVersionString(), ("default" if nd.getDefaultVersion() else "non-default"), 
                                          (nd.getInheritString() if len(nd.getInheritString()) > 0 else "none")
                ))

            print('<p class="card-text"><b>Description:</b> '
                '%s.</p>' % nd.getAttribute('doc'))

            #print('<ul>')
            #print('<li> <em>NodeDef</em>: %s' % nd.getName())
            #print('<li> <em>Type</em>: %s' % nd.getType())
            #if len(nd.getNodeGroup()) > 0:
            #    print('<li> <em>Node Group</em>: %s' % nd.getNodeGroup())
            #if len(nd.getVersionString()) > 0:
            #    print('<li> <em>Version</em>: %s. Is default: %s' % (nd.getVersionString(), nd.getDefaultVersion()))
            #if len(nd.getInheritString()) > 0:
            #    print('<li> <em>Inherits From</em>: %s' % nd.getInheritString())
            #print('<li> <em>Doc</em>: %s\n' % nd.getAttribute('doc'))
            if opts.nodegraph:

                print('<p class="card-text"><b></b>')

                mdoutput = ''
                ng = nd.getImplementation()
                if ng and ng.isA(mx.NodeGraph):
                    print('<details><summary><b>Node Graph</b>')
                    print(' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" '
                        ' class="bi bi-diagram-3 text-primary" viewBox="0 0 16 16">'
                        ' <path fill-rule="evenodd" d="M6 3.5A1.5 1.5 0 0 1 7.5 2h1A1.5 1.5 0 0 1 10 3.5v1A1.5 1.5 0 0 1 8.5 6v1H14a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-1 0V8h-5v.5a.5.5 0 0 1-1 0V8h-5v.5a.5.5 0 0 1-1 0v-1A.5.5 0 0 1 2 7h5.5V6A1.5 1.5 0 0 1 6 4.5v-1zM8.5 5a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1zM0 11.5A1.5 1.5 0 0 1 1.5 10h1A1.5 1.5 0 0 1 4 11.5v1A1.5 1.5 0 0 1 2.5 14h-1A1.5 1.5 0 0 1 0 12.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zm4.5.5A1.5 1.5 0 0 1 7.5 10h1a1.5 1.5 0 0 1 1.5 1.5v1A1.5 1.5 0 0 1 8.5 14h-1A1.5 1.5 0 0 1 6 12.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zm4.5.5a1.5 1.5 0 0 1 1.5-1.5h1a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1-1.5 1.5h-1a1.5 1.5 0 0 1-1.5-1.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1z"/>'
                        ' </svg>')
                    print('</summary>') 
                    outputList = ng.getOutputs()
                    # Don't want subgraph as the implemention is a subgraph
                    graphOptions = mx.GraphIOGenOptions()
                    graphOptions.setWriteSubgraphs(False)
                    graphOptions.setOrientation(mx.GraphOrientation.LEFT_RIGHT)
                    mdoutput = graphio.write('md', ng, outputList, graphOptions)

                    #print('<li> <em>Nodegraph</em>: %s' % ng.getName())
                    if mdoutput:
                        print('<button id="%s_mrender" class="mrender btn btn-outline-primary">Draw Graph</button>' % nd.getName())
                        print('<pre><code class="language-mermaid">')
                        # Output graph
                        print('<div id="%s_mrender_mermaid_output" class="mermaid" hidden>' % nd.getName())
                        print('</div>')
                        # Input text
                        print('<div id="%s_mrender_mermaid_input" class="mermaid" hidden>' % nd.getName())
                        print(mdoutput)
                        print('\n')
                        print('</div></code></pre>\n') 
                else:
                    print('<details><summary><b>Code Implementation</b>')
                    print('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-code-square" viewBox="0 0 16 16">'
                    ' <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>'
                    ' <path d="M6.854 4.646a.5.5 0 0 1 0 .708L4.207 8l2.647 2.646a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 0 1 .708 0zm2.292 0a.5.5 0 0 0 0 .708L11.793 8l-2.647 2.646a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708 0z"/>'
                    ' </svg>')                   
                    print('</summary>')
                    print('Non-graph')

                print('</details>')
                print('</p>')  

            print('<p class="card-text"><b>Parameters:</b></p>')

            # - Print buttons
            print('<ul class="nav nav-pills" id="pills-tab" role="tablist">')
            inputList = nd.getActiveInputs() if opts.showInherited  else nd.getInputs()            
            tokenList = nd.getActiveTokens() if opts.showInherited  else nd.getTokens()
            outputList = nd.getActiveOutputs() if opts.showInherited  else nd.getOutputs()
            totalList = inputList + tokenList + outputList
            makeactive = True
            for port in totalList:

                portName = port.getName()
                portid = nd.getName() + "_" + port.getName()
                print('<li class="nav-item" role="presentation">'
                    ' <button class="nav-link %s" id="pills-%s-tab"'
                    ' data-bs-toggle="pill" data-bs-target="#pills-%s"'
                    ' type="button" role="tab" aria-controls="pills-%s"'
                    ' aria-selected="true">%s</button>'
                    '</li>' % ("active" if makeactive else "", portid, portid, portid, portName))
                makeactive = False
            print('</ul>')
            print('<br>')
                    
            makeactive = True
            for port in totalList:
                # - Content per parameter
                portid = nd.getName() + "_" + port.getName()
                print('<div class="tab-content" id="pills-tabContent">')
                print(' <div class="tab-pane %s" id="pills-%s"' % ("show active" if makeactive else "", portid))
                print('  role="tabpanel" aria-labelledby="pills-%s-tab" tabindex="0">' % portid)

                # Description
                portdoc = port.getAttribute('doc')
                if len(portdoc) > 0:
                    print('  <div class="form-group row g-2">')
                    print('  <label class="col-sm-2 col-form-label col-form-label-sm">Description:</label>')
                    print('    <div class="col-sm-8">')
                    print('      <textarea class="form-control form-control-sm" id="form_description" rows="3"')
                    print('        style="resize: none;" disabled>%s </textarea>' % portdoc)
                    print('    </div>')
                    print('  </div>')
                    #print('  <br>')

                # Type / Uniform
                portType = port.getType()
                print('  <div class="form-group row g-2">')
                print('  <label class="col-sm-2 col-form-label col-form-label-sm">Type:</label>')
                print('   <div class="col-sm-2">')
                #print('     <button type="button" class="btn btn-sm btn-outline-secondary pt-0 pb-0">%s</button>'
                #                % portType)
                print('     <input type="button" class="form-control form-control-sm btn btn-sm btn-outline-secondary pt-0 pb-0" value="%s">'
                                % portType)
                print('   </div>')
                if port.getAttribute('uniform'):                                
                    print('   <div class="col-sm-2">')
                    print('     <label>Uniform</label>')
                    print('     <input type="checkbox" class="form-check-input form-check-sm" disabled %s>' 
                                    % ("checked" if port.getAttribute('uniform') else ""))
                    print('   </div>')
                print('  </div>')

                # Unit type / Unit
                portUnit = port.getAttribute('unit')
                portUnitType = port.getAttribute('unittype')
                if len(portUnit) > 0 or len(portUnitType):
                    print('<div class="form-group row g-1">')
                    print('<label class="col-sm-2 col-form-label col-form-label-sm">Unit Type / Unit: </label>')
                    print(' <div class="col-sm-2">')
                    print('   <button type="button" class="btn btn-sm btn-outline-secondary pt-0 pb-0">%s</button>'
                                % (str(portUnitType) if len(portUnitType) else "none"))
                    print('   <button type="button" class="btn btn-sm btn-outline-secondary pt-0 pb-0">%s</button>'
                                % (str(portUnit) if len(portUnit) else "none"))
                    print(' </div>')
                    print('</div>')                    

                # Default Geom Property
                defaultgeomprop = port.getAttribute('defaultgeomprop')
                if len(defaultgeomprop) > 0:
                    print('  <div class="form-group row g-1">')
                    print('      <label')
                    print('          class="col-sm-2 col-form-label col-form-label-sm">Default Geometry Property: </label>')
                    print('      <div class="col-sm-2">')
                    print('          <input type="text" class="form-control form-control-sm" value="%s" disabled>' % defaultgeomprop)
                    print('      </div>') 
                    print('  </div>')                    

                # Default Value
                val = port.getValue()
                valstr = port.getValueString()

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

                # - Regular handling of value on Input Elements
                haveval = len(valstr) > 0
                if haveval:
                    portType = port.getType()
                    if (portType == 'boolean'):
                        print('  <div class="form-group row g-1">')
                        print('      <label')
                        print('          class="col-sm-2 col-form-label col-form-label-sm">Value: </label>')
                        #print('      <div class="col-sm-1">')
                        print('      <div class="col-sm-2">')
                        print('          <input type="text" class="form-control form-control-sm" value="%s" disabled>' % valstr)
                        print('      </div>')
                        #print('          <input type="checkbox" class="form-check-input form-check-sm" %s disabled>' 
                        #                    % ("checked" if haveval else ""))
                        #print('      </div>')
                        print('  </div>')

                    elif (portType == 'string'):
                        print('  <div class="form-group row g-1">')
                        print('      <label')
                        print('          class="col-sm-2 col-form-label col-form-label-sm">Value: </label>')
                        print('      <div class="col-sm-2">')
                        print('          <input type="text" class="form-control form-control-sm" value="%s" disabled>' % val)
                        print('      </div>')
                        print('  </div>')

                    elif (portType == 'float' or portType == 'integer'):
                        print('  <div class="form-group row g-1">')
                        print('      <label')
                        print('          class="col-sm-2 col-form-label col-form-label-sm">Value: </label>')
                        print('      <div class="col-sm-2">')
                        print('          <input type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                            % (val if haveval else -1))
                        print('      </div>')
                        print('  </div>')

                    elif (portType == 'vector2' 
                        or portType == 'vector3' 
                        or portType == 'vector4' 
                        or portType == 'color3' 
                        or portType == 'color4'):

                        print('  <div class="form-group row g-1">')
                        print('      <label')
                        print('          class="col-sm-2 col-form-label col-form-label-sm">')
                        print('          Value: </label>')
                        print('      <div class="col-sm-2">')
                        print('          <input type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                        % val[0] if haveval else -1)
                        print('      </div>')
                        print('      <div class="col-sm-2">')
                        print('          <input type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                        % val[1] if haveval else -1)
                        print('      </div>')

                        if portType != 'vector2':
                            print('      <div class="col-sm-2">')
                            print('          <input type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                            % val[2] if haveval else -1)
                            print('      </div>')

                        if portType == 'vector4' or portType == 'color4':
                            print('      <div class="col-sm-2">')
                            print('          <input type="number" class="form-control form-control-sm" value="%g" disabled>' 
                                            % val[3] if haveval else -1)
                            print('      </div>')
                        
                        if portType == 'color3':
                            hexval = [int(255*val[0]), int(255*val[1]), int(255*val[2])]
                            print('      <div class="col-sm-2">')
                            print('          <input type="text" class="form-control form-control-sm" value="#%02x%02x%02x" disabled>' 
                                        % (hexval[0], hexval[1], hexval[2]))                                        
                            print('      </div>')                        
                            print('      <div class="col-sm-2">')
                            print('          <input type="color" value="#%02x%02x%02x" disabled>' % (hexval[0], hexval[1], hexval[2]))                                        
                            print('      </div>')


                        elif portType == 'color4':
                            hexval = [int(255*val[0]), int(255*val[1]), int(255*val[2])]
                            print('      <div class="col-sm-1">')
                            print('          <input type="text" class="form-control form-control-sm" value="#%02x%02x%02x" disabled>' 
                                        % (hexval[0], hexval[1], hexval[2]))                                        
                            print('      </div>')                        
                            print('      <div class="col-sm-1">')
                            print('          <input type="color" value="#%02x%02x%02x" disabled>' % (hexval[0], hexval[1], hexval[2]))                                        
                            print('      </div>')

                        print('  </div>')

                # Enumeration
                portenum = port.getAttribute('enum') 
                if (len(portenum) > 0):
                    print('  <div class="form-group row g-1">')
                    print('      <label')
                    print('          class="col-sm-2 col-form-label col-form-label-sm">Possible Values: </label>')

                    enumlist = portenum.split(',')
                    if len(enumlist) == 0:
                        enumlist = portenum.split(', ')
                    enumlistSize = len(enumlist)
                    print('      <div class="col-sm-2">')
                    print('        <select class="form-select form-select-sm" style="font-size:90%%" size="%d" disabled>'
                        % enumlistSize)
                    for enumopt in enumlist:
                        print('          <option>%s</option>' % enumopt)
                    print('       </select>')
                    print('      </div>')                            
                    
                    portenumValues = port.getAttribute('enumvalues')
                    if len(portenumValues) > 0:
                        enumValuelist = portenumValues.split(',')
                        if len(enumValuelist) == 0:
                            enumValuelist = portenumValues.split(', ')
                        enumValuelistSize = len(enumValuelist)
                        if enumValuelistSize > 0:
                            print('      <div class="col-sm-2">')
                            print('        <select class="form-select form-select-sm" style="font-size:90%%" size="%d" disabled>'
                                % enumValuelistSize)
                            for enumValueOpt in enumValuelist:
                                print('          <option>%s</option>' % enumValueOpt)
                            print('        </select>')
                            print('       </div>')                            
                    
                    print('  </div>')
                        
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

                    print('<div class="form-group row g-1">')
                    print('<label class="col-sm-2 col-form-label col-form-label-sm">UI Name/Folder/Advanced:</label>')
                    print(' <div class="col-sm-2">')
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIName))
                    print(' </div>')
                    print(' <div class="col-sm-2">')
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIGroup))
                    print(' </div>')
                    print(' <div class="col-sm-2">')
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIAdvanced))
                    print(' </div>')
                    print('</div>')

                # - min / max / step
                portUIMin = port.getAttribute('uimin')
                portUIMax = port.getAttribute('uimax')
                portUIStep = port.getAttribute('uistep')
                if len(portUIMin) > 0 or len(portUIMax) > 0 or len(portUIStep) > 0: 
                    print('<div class="form-group row g-1">')
                    print('<label class="col-sm-2 col-form-label col-form-label-sm">UI Min/Max/Step: </label>')
                    print(' <div class="col-sm-2">')
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIMin))
                    print(' </div>')
                    print(' <div class="col-sm-2">')
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIMax))
                    print(' </div>')
                    print(' <div class="col-sm-2">')
                    print('  <input type="text" class="form-control form-control-sm" value="%s" disabled>'
                                % str(portUIStep))
                    print(' </div>')
                    print('</div>')

                print(' </div>')
                print('</div>')

                makeactive = False

            print('</div>')
            print('</div>')
            print('</div>')

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
            print('</div>')
            print('</details>')

            # Parameter Information


        # Markdown output
        elif opts.documentType == 'md':
            nodeString = nd.getNodeString()
            if currentNodeString != nodeString:
                print('### Node: *%s*' % nodeString)
                currentNodeString = nodeString
            print('<details><summary>%s</summary>' % nd.getName())
            print('<p>')
            print(' ')
            print('* *Nodedef*: %s' % nd.getName())
            print('* *Type*: %s' % nd.getType())
            print('* *Node Group*: %s' % ( nd.getNodeGroup() if len(nd.getNodeGroup()) else "none"))
            implversion = nd.getVersionString()
            if len(implversion) == 0:
                implversion = "1.0"
            print('* *Version*: %s. Is default: %s' % (implversion, nd.getDefaultVersion()))
            if len(nd.getInheritString()) > 0:
                print('- *Inherits From*: %s' % nd.getInheritString())
            docstring = nd.getAttribute('doc')
            if not docstring:
                docstring = "UNDOCUMENTED"
            print('* *Doc*: %s' % docstring)
            if opts.nodegraph:
                mdoutput = ''
                ng = nd.getImplementation()
                if ng and ng.isA(mx.NodeGraph):
                    outputList = ng.getOutputs()
                    # Don't want subgraph as the implemention is a subgraph
                    graphOptions = mx.GraphIOGenOptions()
                    graphOptions.setWriteSubgraphs(False)
                    graphOptions.setOrientation(mx.GraphOrientation.LEFT_RIGHT)
                    mdoutput = graphio.write('md', ng, outputList, graphOptions)
                    print('* *Nodegraph*: %s' % ng.getName())
                    if mdoutput:
                        print('\n')
                        print('```mermaid')
                        print(mdoutput)
                        print('```')
                    else:
                        print('None')
                else:
                    print('* *Implementation*: Non-graph')
            
            print(' \n')
            print('| ' + ' | '.join(HEADERS) + ' |')
            print('|' + ' ---- |' * len(HEADERS) + '')
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

            print('</p></details>')
            print(' ')

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


def printHeader(opts):
    if opts.documentType == "html":
        print('<html>')
        print('<head>')

        # bootstrap
        print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"'
        ' integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">')
            
        print('<style>')
        print(' body { font-size: 90%; }')
        print(' .col-form-label-sm { font-size: 90%; }')
        print(' .form-control { font-size: 90%; }')
        print(' .card-body { font-size: 80%; } ')
        print(' .btn { font-size: 90%; }')
        print(' .nav-link { font-size: 100%; }')
        print(' a{ text-decoration: none; } ')
        print(' a:hover { text-decoration: none; cursor: pointer;}')
        print(' .text-left { text-align: left !important; }')
        print(' .greyhover { text-decoration: none; }')
        print(' .greyhover:hover { text-decoration: none; cursor: pointer; background: rgb(239, 239, 239); }')
        #print('.form-control { border: 0; }')
        print('</style>')

        # Add in mermaid support
        #if opts.nodegraph:
        #    print('<script src="https://unpkg.com/mermaid/dist/mermaid.min.js"></script>')
        #    print('<script>')
        #    print('mermaid.initialize({ startOnLoad: true, theme: document.body.classList.contains("vscode-dark") || document.body.classList.contains("vscode-high-contrast") ? "dark" : "default" });')
        #    print('</script>')        
        #print('table, th, td {')
        #print('   border-bottom: 1px solid; border-collapse: collapse; padding: 10px;')
        #print('}')
        #print('</style></head>')
        print('</head>')
        print('<body class="min-vh-100">')

        print('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"'
        ' integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"'
        ' crossorigin="anonymous"></script>')

        # mermaid
        print('<script src="https://unpkg.com/mermaid/dist/mermaid.min.js"></script> ')
        print('<script>'
        ' mermaid.initialize({'
            ' startOnLoad: false,'
            ' theme: document.body.classList.contains("vscode-dark") || document.body.classList.contains("vscode-high-contras")'
            ' ? "dark"'
            ' : "default"});'
        ' </script>')

        # Load in top menu
        print('')
        topfile = open('D:/Health/modelAssets/nodeLibrary/top.html', 'r')
        toplines = topfile.readlines()
        for line in toplines:
            print('%s' % line, end = '')

        # Add in container 
        # 
        print('<div class="container-fluid ">')
        print(' <div class="row flex-nowrap">')                     

def printFooter(opts):
    if opts.documentType == "html":
        print("<script>")
        print('  var searchInput = document.getElementById("searchTOC")')
        print('  searchInput.addEventListener("keypress", filterOnEnter);')
        print('  var renderButtons = document.querySelectorAll(".mrender");')
        print('  renderButtons.forEach((renderButton) => { renderButton.addEventListener("click", renderMermaid); });')
        print("</script>")
        print('</body>')
        print('</html>')

def main():
    parser = argparse.ArgumentParser(description="Print documentation for each nodedef in the given document.")
    parser.add_argument(dest="inputFilename", help="Path of the input MaterialX document or folder.")
    parser.add_argument('--docType', dest='documentType', default='md', help='Document type. Default is "md" (Markdown). Specify "html" for HTML output')
    parser.add_argument('--showInherited', default=False, action='store_true', help='Show inherited inputs. Default is False')
    parser.add_argument('--nodegraph', default=False, action='store_true', help='Show nodegraph implementation if any. Default is False')
    parser.add_argument('--printIndex', default=False, action='store_true', help="Print nodedef index. Default is False")

    opts = parser.parse_args()

    printHeader(opts)

    rootPath = opts.inputFilename;
    doc = mx.createDocument()
    readDocuments(rootPath, doc)    

    # Add in left column
    if opts.documentType == "html":
        print('   <div class="col-auto px-0">')
        print('     <div class="row vh-100 overflow-auto">')
        print('       <div class="col-12 pt-2 pl-2">')
        print('         <div class="container-md">')
        print('           <div id="sidebar" class="collapse show collapse-horizontal">')   

    nodedict = getNodeDictionary(doc)
    printNodeDictionary(nodedict, opts)

    if opts.documentType == "html":
        print('           </div>')
        print('         </div>')
        print('       </div>')
        print('     </div>')
        print('   </div>')

    # Add in right colunn
    if opts.documentType == "html":
        print('   <div class="col ps-md-2 pt-2">')
        print('       <div class="row vh-100 overflow-auto">')
        print('           <div class="col-12 pt-2 pl-2">')
        print('               <div class="container-md">')

    printNodeDefs(doc, opts) 

    if opts.documentType == "html":
        print('               </div>')
        print('           </div>')
        print('       </div>')
        print('   </div>')

    printFooter(opts) 

if __name__ == '__main__':
    main()
