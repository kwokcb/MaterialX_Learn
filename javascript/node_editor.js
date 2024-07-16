/*
    Interface setup for MaterialX node editor. This script sets up the UI and event handlers for 
    the node editor. It also initializes the CodeMirror instances for syntax highlighting of 
    MaterialX documents and JavaScript code.
    
    The node editor is initialized with the specified MaterialX document and geometry file.
    An optional renderer can be used to display the material and geometry in a viewer.
*/

/**
 * @function initializeNodeEditor
 * @description Function to initialize the MaterialX node editor
 * @param {String} materialFilename - The filename of the MaterialX document to load
 * @param {String} geometryId - The id of the geometry to load
 * @param {Object} customRenderer - The custom renderer object to use for rendering
 * @param {Object} user_icon_map - The object containing the user icon map. Optional.
 * @param {Object} sampleFiles - The object containing the sample files. Optional.
 * @param {Boolean} readOnly - Flag to indicate if the editor is read-only. Optional.
 * @returns {void}
 */
export function initializeNodeEditor(materialFilename, geometryId, customRenderer, user_icon_map = null, sampleFiles = null,
                                    readOnly = false)
{
    let my_icon_map = {
        "_default_": "./Icons/materialx_logo.webp",
        "_default_graph_": "./Icons/nodegraph_white.svg"
    };

    let geometryValues = ['teapot', 'shaderball', 'sphere', 'plane', 'cube', 'cylinder', 'twist', '_loadFromFile_']

    if (user_icon_map) {
        // add items in user icon map. Overwrite any existing items
        for (var key in user_icon_map) {
            my_icon_map[key] = user_icon_map[key];
        }
    }

    // Check if URI exists
    function uriExists(uri) {
        return fetch(uri)
            .then(response => {
                if (response.ok) {
                    return Promise.resolve(true);
                } else {
                    return Promise.resolve(false);
                }
            })
            .catch(error => {
                console.log('Error checking URI:', error);
                return Promise.resolve(false);
            });
    }    

    // Renderable item UI updater
    function renderableItemUpdater(renderableItems) 
    {
        let renderableItemSelect = document.getElementById('renderableItem');
        if (renderableItemSelect) {

            const TRUNCATION_LENGTH = 12;
    
            while (renderableItemSelect.firstChild) {
                renderableItemSelect.removeChild(renderableItemSelect.firstChild);
            }
            for (let i = 0; i < renderableItems.length; i++) {
                let item = renderableItems[i];
                let option = document.createElement('option');
                option.value = item;
                let uiItem = item;
                // Truncate the name so it will fit into UI.
                if (uiItem.length > 10)
                    uiItem = uiItem.substring(0, 10) + '...';
                option.text = uiItem; 
                renderableItemSelect.appendChild(option);
            }                             
        }    
    }

    // Logger
    // TODO: Pass in a logger object instead of looking for a DOM element.
    function consoleLog(text, severity, clear = null) 
    {
        if (severity === 2) {
            text = '> Error: ' + text
        }
        else if (severity === 1) {
            text = '> Warning: ' + text
        }
        else {
            if (text.length)
                text = '> ' + text;
        }

        let console_area = document.getElementById('console_area');
        if (console_area)
        {
            if (clear) { 
                console_area.value = text + '\n';
            }
            else 
            {
                console_area.value = console_area.value + text + '\n';
            }
            // Scroll to latest entry.
            console_area.scrollTop = console_area.scrollHeight;
        }
        else {
            console.log(text);
        }        
    }

    /* function createMenuStructure(obj) {
        let items = [];
        for (let key in obj) {
            if (typeof obj[key] === 'object' && !Array.isArray(obj[key])) {
                // It's a nested object, create a submenu
                let subItems = createMenuStructure(obj[key]); // Recursively handle nested objects
                items.push(createSubMenu(key, subItems));
            } else {
                items.push(createMenuItem(key, obj[key]));
            }
            console.log('<<< END SCAN');
        }
        return items;
    } */


    /** 
     * Create a menu item for the library dropdown
     * @param {String} text - The text to display for the menu item
     * @param {String} filename - The filename to load when the menu item is clicked
     * @returns {HTMLElement} - The menu item element
     */
    function createMenuItem(text, filename) {
        let menuItem = document.createElement('li');
        menuItem.className = 'dropdown-item';
        menuItem.innerText = text;
        menuItem.onclick = function() {
            console.log('Load library file:', filename);
            MxShadingGraphEditor.theEditor.handler.loadLibraryDocument(MxShadingGraphEditor.theEditor, filename);
            // Collapse the dropdown menu
            let dropdownMenu = document.getElementById('libraryDropdown');
            dropdownMenu.classList.remove('show');            
        };
        return menuItem;
    }

    /** 
     * Create a submenu for the library dropdown
     * @param {String} title - The title of the submenu
     * @param {Boolean} auto_close - Make the submenu appear if not top level
     * @returns {HTMLElement} - The submenu element
     */
    function createSubMenu(title, auto_close = false) {

        let li = document.createElement('li');
        li.className = "dropend dropdown";
        li.id = key;

        let subMenu = document.createElement('a');
        subMenu.className = "dropdown-item dropdown-toggle";
        subMenu.setAttribute('data-bs-toggle',"dropdown");
        if (auto_close) 
        {
            subMenu.setAttribute('data-bs-auto-close','outside');
        }
        subMenu.setAttribute('aria-expanded', 'false');
        subMenu.setAttribute('aria-haspopup', 'true');
        subMenu.innerHTML = title;
        li.appendChild(subMenu);        

        return li;
    }

    /** 
     * Create the library menu structure
     * @param {Object} sampleFiles - The object containing the library structure
     * @param {HTMLElement} libraryDropdown - The dropdown menu element
     * @returns {void}
     */
    function createLibraryMenu(sampleFiles, libraryDropdown)
    {
        for (let key in sampleFiles) 
        {
            //  Create top level menus
            let li = createSubMenu(key, true);
            libraryDropdown.appendChild(li);

            let value = sampleFiles[key];

            // Add items to the submenu
            if (typeof value === 'string') 
            {
                let value = sampleFiles[key];
                li.appendChild(createMenuItem(key, value));
            }                
            else if (typeof value === 'object') {

                let subMenuList = document.createElement('ul');
                subMenuList.className = 'dropdown-menu';
                subMenuList.id = key;

                for (key in value) {
                
                    // Check if value is a string
                    if (typeof value[key] === 'string') {
                        subMenuList.appendChild(createMenuItem(key, value[key]));
                    }

                    else if (typeof value[key] === 'object') {

                        //  Create sub level menus
                        let sli = createSubMenu(key, false);
                        subMenuList.appendChild(sli);

                        let ssubMenuList = document.createElement('ul');
                        ssubMenuList.className = 'dropdown-menu';
                        for (let skey in value[key]) {
                            ssubMenuList.appendChild(createMenuItem(skey, (value[key])[skey]));
                        }
                        sli.appendChild(ssubMenuList);                        
                    }
                }

                li.appendChild(subMenuList);
            } 

        }        
    }

    // Build material library menu UI
    if (sampleFiles && libraryDropdown) 
    {
        createLibraryMenu(sampleFiles, libraryDropdown);
    }
    
    // Update selected geometry menu UI
    let selectGeometryUI = false;
    if (customRenderer) {

        let geometryURL = geometryId;
        if (geometryId.length > 0 && geometryValues.includes(geometryId)) {
            geometryURL = 'Geometry/' + geometryId + '.glb';
            selectGeometryUI = true;
        }
        var viewer = customRenderer.initialize(materialFilename, geometryURL, readOnly);
        console.log('Setup renderer:', viewer);
    }
    else {
        let preview_panel = document.getElementById("preview_panel");
        // Hide preview_panel DOM element
        if (preview_panel)
            preview_panel.style.display = 'none';
    }

    // TODO: Pass in a ui function instead of looking for a DOM element.
    /** 
     * Display the node types in the UI
     * @param {Object} nodeTypes - The object containing the node types
     * @returns {void}
     */
    function displayNodeTypes(nodeTypes) 
    {
        // Get the list container
        var nodeList = document.getElementById('nodeTypesList');
        if (!nodeList) {
            return;
        }
        
        // Clear all children of nodeList
        while (nodeList.firstChild) {
            nodeList.removeChild(nodeList.firstChild);
        }

        // Iterate over the node types and add them to the list        
        for (var typeName in nodeTypes) {            

            var rowItem = document.createElement("tr");

            var cellItem = document.createElement("td");
            cellItem.textContent = typeName;
            rowItem.appendChild(cellItem);

            cellItem = document.createElement("td");
            var nodeDefString = '<None>';
            var nodeDefName = nodeTypes[typeName].nodedef_name;
            var nodeDefNode = nodeTypes[typeName].nodedef_node
            var nodeDefHref = nodeTypes[typeName].nodedef_href;
            if (nodeDefName) {
                if (nodeDefNode)
                {
                    var link = document.createElement("a");
                    link.target = "_blank";
                    link.href = nodeDefHref;
                    link.textContent = nodeDefNode + " ( " + nodeDefName + " )";
                    cellItem.appendChild(link);
                }
                else
                {
                    cellItem.textContent = nodeDefName;                
                }
            }
            else {
                cellItem.textContent = nodeDefString;
            }
            rowItem.appendChild(cellItem);

            nodeList.appendChild(rowItem);
        }
    }

    // Set up syntax highlighting for text areas
    var cmeditor = setupXMLSyntax();
    var cmeditor2 = setupJavascriptSyntax();
    var cmeditor3 = setupGLTFSyntax();

    /** 
     * Update xml document text display
     * @param {String} contents - The contents of the document
     * @returns {void}
     */
    function docDisplayUpdater(contents) {
        if (cmeditor)
            cmeditor.setValue(contents);
    } 

    /** 
     * Update gltf document text display
     * @param {String} contents - The contents of the document
     * @returns {void}
     */
    function gltfDisplayUpdater(contents) {
        if (!contents || contents.length == 0)
        {
            contents = '{}';
        }
        if (cmeditor3)
            cmeditor3.setValue(contents);
        else
            console.log(contents);
    }

    /** 
     * Update javascript definitions display
     * @param {String} contents - The contents of the document
     * @returns {void}
     */
    function jsDefinitionsDisplayUpdater(contents) {
        if (cmeditor2)
            cmeditor2.setValue(contents);
    } 

    // Set up graphing UI
    var canvas = document.getElementById('mygraphcanvas');
    var ui = {
        consoleLogger: consoleLog, 
        nodeTypesListUpdater: displayNodeTypes,
        renderableItemUpdater: renderableItemUpdater,
        documentDisplayUpdater: docDisplayUpdater,
        gltfDocumentDisplayUpdater: gltfDisplayUpdater,
        definitionsDisplayUpdater: jsDefinitionsDisplayUpdater,
        propertypanel_content: document.getElementById('propertypanel_content'),
        propertypanel_icon: document.getElementById('propertypanel_icon'),
        icon_map: my_icon_map,
    };
    var editor = new MxShadingGraphEditor();    

    function toggleRequireUpdateUI()
    {
        let graphtoxml2 = document.getElementById('graphtoxml2');
        if (graphtoxml2) {
            graphtoxml2.classList.remove('btn-outline-secondary');
            graphtoxml2.classList.add('btn-outline-warning');
        }
    }

    /**
     * Custom monitor class for MaterialX graph
     * Allows updates to be passed to any renderer used.
     * @extends MxGraphMonitor
     * @class
     * @memberof MxShadingGraphEditor
     * @param {String} name - The name of the monitor
     * @returns {void}
     * @constructor
     * @example
     * var monitor = new MxMaterialXMonitor('Custom MaterialX Graph Monitor');
     * monitor.setRenderer(customRenderer);
     * editor.initialize(canvas, ui, monitor, materialFilename);
     * @see {@link MxGraphMonitor}
     * @see {@link MxShadingGraphEditor}
     * @see {@link MxMaterialXMonitor}     * 
     */
    class MxMaterialXMonitor extends MxGraphMonitor {
        constructor(name) {
            super(name);    

            this.onDocumentChange = function(attribute, value, prevValue)
            {
                if (!this.monitoring)
                    {
                        return;
                    }
    
                    if (this.renderer)
                        toggleRequireUpdateUI();
                    if (this.debug) {
                        this.debugMessage('Monitor> Document attribute "' + attribute + '" changed from: ' + prevValue + ' to: ' + value, '');
                    }            
            }

            this.onConnectionChange= function(node, parentGraph)
            {
                if (!this.monitoring)
                {
                    return;
                }

                if (this.renderer)
                    toggleRequireUpdateUI();
                if (this.debug) {
                    this.debugMessage('Monitor> Connection change: ', this.getPath(node, parentGraph));
                }    
            }

            this.onNodeRemoved = function(node, parentGraph)
            {
                if (!this.monitoring)
                {
                    return;
                }
        
                if (this.renderer)
                    toggleRequireUpdateUI();
                if (this.debug) {
                    this.debugMessage('Monitor> Node removed: ', this.getPath(node, parentGraph));
                }
            }
    
            this.onNodeRenamed = function(node, newName)
            {
                if (!this.monitoring)
                {
                    return;
                }    
    
                if (this.renderer)
                    toggleRequireUpdateUI();

                if (this.debug) {
                    let parentPath = this.getParentPath(node);
                    let path = parentPath + node.title;
                    let newpath = parentPath + newName;
                    this.debugMessage('Monitor> Node renamed: ', path + ' to: ' + newpath);
                }    
            }

            this.onPropertyInfoChanged = function(nodeName, propertyName, propertyInfoName, newValue, previousValue, node)
            {
                if (!this.monitoring)
                    {
                        return;
                    }    
        
                if (this.renderer)
                    toggleRequireUpdateUI();

                if (this.debug) {
                    let path = this.getParentPath(node) + nodeName;
                    console.log('Monitor> Property Info changed:', path, '. Property: ' + propertyName + 
                        '. Property Info: ' + propertyInfoName +
                    '. Value: ' + newValue + '. Previous Value: ' + previousValue, '. Category:', node.nodedef_node);
                }                    
            }

            this.onPropertyChanged  = function (nodeName, propertyName, newValue, previousValue, node)
            {
                if (!this.monitoring)
                {
                    return;
                }
        
                let path = this.getParentPath(node) + nodeName;

                if (this.renderer)
                {
                    if (typeof newValue == 'string')
                    {
                        toggleRequireUpdateUI();
                        if (this.debug) 
                        {
                            console.log('Renderer> Build required for string change:', path, '. Property: ' + propertyName + 
                            '. Value: ' + newValue + '. Previous Value: ' + previousValue + '. Node: ' + node.nodedef_node);
                        }    
                    }
                    else 
                    {
                        if (node.nodedef_node != 'input')
                            path = path + '/' + propertyName;
                        this.renderer.updateShader(path, newValue);
                    }
                }
                else
                {
                    if (this.debug) 
                    {
                        console.log('Monitor> Property changed:', path, '. Property: ' + propertyName + 
                        '. Value: ' + newValue + '. Previous Value: ' + previousValue + '. Node: ' + node.nodedef_node);
                    }    
                }
            }        
        }
    }    

    let monitor = new MxMaterialXMonitor('Custom MaterialX Graph Monitor');
    monitor.setRenderer(customRenderer);
    editor.initialize(canvas, ui, monitor, materialFilename, readOnly);

    /**
     * Add event handlers for UI elements
     * @returns {void}
     */
    function addUIHandlers() {
        // Add event listener to save canvas as image when button is clicked
        var saveCanvasButton = document.getElementById('captureGraph');
        if (saveCanvasButton) {
        saveCanvasButton.addEventListener('click', function () {
            var canvas = document.getElementById('mygraphcanvas');
            var dataURL = canvas.toDataURL('image/png');
            var link = document.createElement('a');
            link.href = dataURL;
            link.download = 'graph_capture.png';
            link.click();
        }); }

        // TODO: Make this a user option
        var auto_arrange_size = 80;

        // Add load materialx graph event listener
        var loadMaterialXDocumentFromFile = document.getElementById('loadMaterialXDocumentFromFile');
        if (loadMaterialXDocumentFromFile)
        {
            loadMaterialXDocumentFromFile.addEventListener('click', function () {
                editor.loadGraphFromFile('mtlx', auto_arrange_size);
                toggleRequireUpdateUI();
            });
        }

        // Add load materialx graph from text event listener
        var texAreaNumber = 0;
        var loadMaterialXDocumentFromText = document.getElementById('loadMaterialXDocumentFromText');
        if (loadMaterialXDocumentFromText)
        {
            loadMaterialXDocumentFromText.addEventListener('click', function () {
                var mtlxdoc = document.getElementById('mtlxdoc').value;
                // Generate a name for the graph
                if (mtlxdoc.length > 0) {
                    var name = 'MaterialXGraph' + texAreaNumber++;
                    editor.loadGraphFromString('mtlx', mtlxdoc, name, auto_arrange_size);
                    toggleRequireUpdateUI();
                }
            });
        }

        // Add load definitions event listener
        var loadMaterialXDefinitions = document.getElementById('loadMaterialXDefinitions');
        if (loadMaterialXDefinitions)
        {
            loadMaterialXDefinitions.addEventListener('click', function () {
                editor.loadDefinitionsFromFile('mtlx');
            });
        }

        // Add clear graph event listener
        var clearGraphButton = document.getElementById('clearGraph');
        if (clearGraphButton)
        {
            clearGraphButton.addEventListener('click', function () {
                editor.clearGraph();
                toggleRequireUpdateUI();
            });
        }

        // Add save materialx graph event listener
        var saveMaterialXGraph = document.getElementById('saveMaterialXGraph');
        if (saveMaterialXGraph) {
            saveMaterialXGraph.addEventListener('click', function () {
                var sl = document.getElementById('writeCustomLibs').checked;
                var sp = document.getElementById('saveNodePositions').checked;
                var wo = true;
                var graphWriteOptions = { writeCustomLibs: sl, saveNodePositions: sp, writeOutputs : wo };
                editor.saveGraphToFile('mtlx', graphWriteOptions);
            });
        }

        // Add save materialx graph text event listener
        var saveMaterialXGraphText = document.getElementById('saveMaterialXGraphText');
        if (saveMaterialXGraphText)
        {
            saveMaterialXGraphText.addEventListener('click', function () {
                saveToStringUI();
            });
        }

        // Add open subgraph event handler
        var openSubgraph = document.getElementById('openSubgraph');
        if (openSubgraph)
        {
            openSubgraph.addEventListener('click', function () {
                editor.openSubgraph();
            });
        }

        // Add close subgraph event handler
        var closeSubgraph = document.getElementById('closeSubgraph');
        if (closeSubgraph) {
        closeSubgraph.addEventListener('click', function () {
            editor.closeSubgraph();
        });
        }

        // Add reset view event handler
        var resetView = document.getElementById('resetView');
        if (resetView)
        {
        resetView.addEventListener('click', function () {
            editor.resetView();
        });
        }

        // Add arrange graph event listener
        var arrangeGraphButton = document.getElementById('arrangeGraph');
        if (arrangeGraphButton) {
        arrangeGraphButton.addEventListener('click', function () {
            editor.arrangeGraph();
        }); }

        // Add center node event listener
        var centerNodeButton = document.getElementById('centerNode');
        if (centerNodeButton) {
        centerNodeButton.addEventListener('click', function () {
            editor.centerNode();
        }); }

        // Add collapse/expand nodes event listener
        var collapseNodesButton = document.getElementById('collapseNodes');
        if (collapseNodesButton) {
        collapseNodesButton.addEventListener('click', function () {
            editor.collapseExpandNodes(true);
        }); }
        var expandNodesButton = document.getElementById('expandNodes');
        if (expandNodesButton) {
        expandNodesButton.addEventListener('click', function () {
            editor.collapseExpandNodes(false);
        }); }

        // Add copy selected event listener
        var copySelectedButton = document.getElementById('copySelected');
        if (copySelectedButton) {
        copySelectedButton.addEventListener('click', function () {
            editor.copyToClipboard();
        }); }

        // Add paste selected event listener
        var pasteSelectedButton = document.getElementById('pasteSelected');
        if (pasteSelectedButton) {
        pasteSelectedButton.addEventListener('click', function () {
            editor.pasteFromClipboard();
        }); }

        // Add create subgraph event listener
        var createNodeGraphButton = document.getElementById('createNodeGraph');
        if (createNodeGraphButton) {
        createNodeGraphButton.addEventListener('click', function () {
            editor.createNodeGraph();
        }); }

        // Add extract subgraph event listener
        var extractNodeGraphButton = document.getElementById('extractNodeGraph');
        if (extractNodeGraphButton) {
        extractNodeGraphButton.addEventListener('click', function () {
            editor.extractNodeGraph();
        }); }

        /* 
        // Add load serialization event listener
        var loadSerialization = document.getElementById('loadSerialization');
        loadSerialization.addEventListener('click', function () {
            editor.loadSerialization();
        });
    
        // Add download graph event listener
        var downloadGraph = document.getElementById('downloadGraph');
        downloadGraph.addEventListener('click', function () {
            editor.saveSerialization();
        }); */

        // Add xml to graph event listener
        var xmlToGraph = document.getElementById('xmltograph');
        if (xmlToGraph) {
        xmlToGraph.addEventListener('click', function () {
            var name = 'MaterialXGraph' + texAreaNumber++;
            var mtlxdoc = document.getElementById('mtlxdoc').value;
            editor.loadGraphFromString('mtlx', mtlxdoc, 'MaterialXGraph', auto_arrange_size);
            toggleRequireUpdateUI();
        }); }
        
        function updateRenderableItemUI()
        {
            let renderableItems = editor.findRenderableItems();
            renderableItemUpdater(renderableItems);
        }

        function saveToStringUI() {
            var cl = document.getElementById('writeCustomLibs').checked;
            var sp = document.getElementById('saveNodePositions').checked;
            var wo  = true;
            var graphWriteOptions = { writeCustomLibs: cl, saveNodePositions: sp, writeOutputs: wo };
            console.log('Save with options: ', graphWriteOptions);
            var result = editor.saveGraphToString('mtlx', graphWriteOptions);
            
            cmeditor.setValue(result[0]);

            if (customRenderer) {
                customRenderer.setSourceColorSpace(editor.getSourceColorSpace());
                customRenderer.setTargetDistanceUnit(editor.getTargetDistanceUnit());
                customRenderer.updateMaterialFromText(result[0]);
                updateRenderableItemUI();
            }
        }

        // Add graph to xml event listener
        var graphtoxml = document.getElementById('graphtoxml');
        if (graphtoxml) {
            graphtoxml.addEventListener('click', function () {
                saveToStringUI();
            });
        }

        let graphtoxml2 = document.getElementById('graphtoxml2');
        if (graphtoxml2) {
            graphtoxml2.addEventListener('click', function () {
                saveToStringUI();
                graphtoxml2.classList.remove('btn-outline-warning');
                graphtoxml2.classList.add('btn-outline-secondary');
            });
        }

        // Add graph to gltf event listener
        var graphtogltf = document.getElementById('graphtogltf');
        if (graphtogltf) {
            graphtogltf.addEventListener('click', function () {
                var graphWriteOptions = { writeCustomLibs: false, saveNodePositions: false, writeOutputs: true };
                var result = editor.saveGraphToString('gltf', graphWriteOptions);
                gltfDisplayUpdater(result[0]);
                if (result[1])
                {
                    consoleLog(result[1], 1, false);
                }
            });
        }

        // Add gltf to graph listener
        var gltftograph = document.getElementById('gltftograph');
        if (gltftograph) {
            gltftograph.addEventListener('click', function () {
                var gltfdoc = document.getElementById('gltfgraph').value;
                if (gltfdoc.length > 0) {
                    editor.loadGraphFromString('gltf', gltfdoc, 'GLTFGraph', auto_arrange_size);
                    toggleRequireUpdateUI();
                }
            });
        }

        // Handle turntable option
        let turntableEnabledUI = document.getElementById('turntableEnabled');
        if (turntableEnabledUI) {
            turntableEnabledUI.addEventListener('click', (e) => {
                // Toggle inverting the button colors no toggling danger
                turntableEnabledUI.classList.toggle('btn-secondary');
                if (customRenderer)
                    customRenderer.toggleTurntable();
            });
        }

        // Handle render disabled option
        let disableRenderingUI = document.getElementById('disableRendering');
        if (disableRenderingUI) {
            disableRenderingUI.addEventListener('click', (e) => {
                // Toggle inverting the button colors
                disableRenderingUI.classList.toggle('btn-danger');
                if (customRenderer)
                    customRenderer.toggleRendering();
            });
        }

        // Handle background display option
        let toggleBackgroundTextureUI = document.getElementById('toggleBackgroundTexture');
        if (toggleBackgroundTextureUI) {
            toggleBackgroundTextureUI.addEventListener('click', (e) => {
                toggleBackgroundTextureUI.classList.toggle('btn-primary');
                if (customRenderer)
                    customRenderer.toggleBackgroundTexture();
            });
        }

        // Handle reset camera option
        let resetCameraUI = document.getElementById('resetCamera');
        if (resetCameraUI) {
            resetCameraUI.addEventListener('click', (e) => {
                if (customRenderer)
                {
                    customRenderer.resetCamera();
                }
            });
        }

        // Handle renderable geometry option
        function loadFromMenu(e) {
            var uiItem = e.target.value;
            if (uiItem == '_loadFromFile_') {
                // Create a file dialog to get the filename
                var fileInput = document.createElement('input');
                fileInput.type = 'file';
                fileInput.accept = '.glb';

                fileInput.onchange = function (event) {
                    var file = event.target.files[0];
                    if (file) {
                        var fileURL = URL.createObjectURL(file);
                        if (customRenderer)
                            customRenderer.setRenderGeometry(fileURL);
                        console.log('Change geometry to:', fileURL, 'from file:', file.name);
                    }
                }
                fileInput.click();
            }
            else {
                // Convert to lowercase and remove spaces
                var geometryURL = uiItem.toLowerCase().replace(/\s/g, '');
                var geometryPath = 'Geometry/' + geometryURL + '.glb';
                console.log('Change geometry to:', geometryPath);
                if (customRenderer)
                    customRenderer.setRenderGeometry(geometryPath);
            }
        }

        // Handle geometry item changed
        let geometryItemSelect = document.getElementById('loadGeometry');
        if (geometryItemSelect) {

            // Add built-in geometry options
            var geometryItems = ['Teapot', 'Shader Ball', 'Sphere', 'Plane', 'Cube', 'Cylinder', 'Twist', 'Custom...'];
            for (var i = 0; i < geometryItems.length; i++) {
                var option = document.createElement('option');
                option.value = geometryValues[i];
                option.text = geometryItems[i];
                geometryItemSelect.appendChild(option);
            }

            // Add event handler for selection
            geometryItemSelect.addEventListener('change', (e) => {
                loadFromMenu(e);
                if (e.target.value == '_loadFromFile_')
                    e.target.value = 'Custom Geometry'
            });

            // Set initial geometry.
            if (selectGeometryUI) {
                // Set the default geometry
                geometryItemSelect.value = geometryId;
            }
        }

        // Handle material selection change
        let renderableItemSelect = document.getElementById('renderableItem');
        if (renderableItemSelect) {
            renderableItemSelect.addEventListener('change', (e) => {
                let index = e.target.value;
                if (customRenderer)
                    customRenderer.setRenderMaterial(index);
            });
        }

        // Get the canvas element and its container
        var canvas = document.getElementById('mygraphcanvas');
        var canvasContainer = document.getElementById('canvasContainer');
        var colContainer = document.getElementById('colContainer');

        // Create a new ResizeObserver
        var observer = new ResizeObserver(function (entries) {
            for (var entry of entries) {
                // Get the new width and height of the column
                var newWidth = entry.contentRect.width;
                var newHeight = entry.contentRect.height;

                // Set the canvas size to match the column
                canvas.width = newWidth;
                canvas.height = newHeight;

                // Mark the editor as dirty to redraw the graph.
                console.log('Resized node graph canvas to:', newWidth, newHeight);
                editor.setDirty();
            }
        });

        // Start observing the canvas container
        observer.observe(colContainer);

    }

    function setupGLTFSyntax() {
        // Initialize CodeMirror for GLTF syntax highlighting
        let cmeditor = null;
        const gltfTextArea = document.getElementById('gltfgraph');
        if (gltfTextArea)
        {
            cmeditor = CodeMirror.fromTextArea(gltfTextArea, {
                mode: 'application/json',
                lineNumbers: true,
                dragDrop: false,
                theme: 'dracula'
            });

            // Optional: Set an initial value for the textarea
            const initialGLTF = '';
            gltfTextArea.value = initialGLTF;
            cmeditor.setValue(initialGLTF);

            // Update CodeMirror whenever the textarea content changes
            cmeditor.on('change', (e) => {
                gltfTextArea.value = cmeditor.getValue();
            });

            var pasteButton = document.getElementById('gltfgraph_paste');
            if (pasteButton)
                addPasteHandler(pasteButton, cmeditor);

        }
        return cmeditor;
    }

    function setupJavascriptSyntax() {
        // Initialize CodeMirror for JS syntax highlighting
        const elem = document.getElementById('mtlxlib');
        if (!elem) {
            return;
        }
        let cmeditor = CodeMirror.fromTextArea(elem, {
            mode: 'application/javascript',
            lineNumbers: true,
            dragDrop: false,
            theme: 'dracula',
            readOnly: true
        });

        elem.value = '';
        cmeditor.setValue('');

        // Update CodeMirror whenever the textarea content changes
        cmeditor.on('change', () => {
            elem.value = cmeditor.getValue();
        });

        return cmeditor;
    }


    function setupXMLSyntax() {
        // Initialize CodeMirror for XML syntax highlighting
        const materialXTextArea = document.getElementById('mtlxdoc');
        let cmeditor = CodeMirror.fromTextArea(materialXTextArea, {
            mode: 'application/xml',
            lineNumbers: true,
            dragDrop: true,
            theme: 'night'
        });

        // Optional: Set an initial value for the textarea
        const initialXML = '';
        materialXTextArea.value = initialXML;
        cmeditor.setValue(initialXML);

        // Update CodeMirror whenever the textarea content changes
        cmeditor.on('change', (e) => {
            materialXTextArea.value = cmeditor.getValue();
        });

        var pasteButton = document.getElementById('mtlxdoc_paste');
        if (pasteButton)
            addPasteHandler(pasteButton, cmeditor);

        return cmeditor;
    }

    addUIHandlers();
    addCopyHandlers();
}
