

export function initializeNodeEditor(materialFilename, geometryFilename, theRenderer) {

    // Customize what icon to show based on nodedef name prefix or nodegroup
    // Note that this is just a heuristic based on current nodegroup and naming 
    // convention. Default is "mtlx" for MaterialX nodes.
    var my_icon_map = {
        "gltf": "./Images/gltf_logo.webp",
        "usd": "./Images/openusd_logo.webp",
        "open_pbr": "./Images/openpbr_logo.webp",
        "houdini": "./Images/houdini_icon.webp",
        "maya": "./Images/maya_surfaces.webp",
        "_default_": "./Images/materialx_logo.webp",
        "_default_graph_": "./Images/nodegraph_white.svg"
    };

    function uriExists(uri) {
        // Add try / catch block to handle network errors        
        return fetch(uri)
            .then(response => {
                if (response.ok) {
                    return true;
                } else {
                    return false;
                }
            })
            .catch(error => {
                console.log('Error checking URI:', error);
                return false;
            });
    }

    if (theRenderer) {
        var viewer = theRenderer.initializeViewer(materialFilename, geometryFilename);
        console.log('Setup viewer:', viewer);
    }
    else {
        let preview_panel = document.getElementById("preview_panel");
        // Hide preview_panel DOM element
        if (preview_panel)
            preview_panel.style.display = 'none';
    }

    var canvas = document.getElementById('mygraphcanvas');
    var cmeditor = setupXMLSyntax();
    var cmeditor2 = setupJavascriptSyntax();
    var ui = {
        console_area: document.getElementById('console_area'),
        nodeTypesList: document.getElementById('nodeTypesList'),
        mtlxdoc: cmeditor,
        mtlxlib: cmeditor2,
        mtlxdoc_colorspace: null, // document.getElementById('mtlxdoc_colorspace'),
        propertypanel_content: document.getElementById('propertypanel_content'),
        propertypanel_icon: document.getElementById('propertypanel_icon'),
        icon_map: my_icon_map,
    };
    var editor = new MxShadingGraphEditor();
    editor.initialize(false, canvas, ui, materialFilename);

    function addUIHandlers() {
        // Add event listener to save canvas as image when button is clicked
        var saveCanvasButton = document.getElementById('captureGraph');
        saveCanvasButton.addEventListener('click', function () {
            var canvas = document.getElementById('mygraphcanvas');
            var dataURL = canvas.toDataURL('image/png');
            var link = document.createElement('a');
            link.href = dataURL;
            link.download = 'graph_capture.png';
            link.click();
        });

        // TODO: Make this a user option
        var auto_arrange_size = 80;

        // Add load materialx graph event listener
        var loadMaterialXDocumentFromFile = document.getElementById('loadMaterialXDocumentFromFile');
        loadMaterialXDocumentFromFile.addEventListener('click', function () {
            editor.loadGraphFromFile('mtlx', auto_arrange_size);
        });

        // Add load materialx graph from text event listener
        var texAreaNumber = 0;
        var loadMaterialXDocumentFromText = document.getElementById('loadMaterialXDocumentFromText');
        loadMaterialXDocumentFromText.addEventListener('click', function () {
            var mtlxdoc = document.getElementById('mtlxdoc').value;
            // Generate a name for the graph
            if (mtlxdoc.length > 0) {
                var name = 'MaterialXGraph' + texAreaNumber++;
                editor.loadGraphFromString('mtlx', mtlxdoc, name, auto_arrange_size);
            }
        });

        // Add load definitions event listener
        var loadMaterialXDefinitions = document.getElementById('loadMaterialXDefinitions');
        loadMaterialXDefinitions.addEventListener('click', function () {
            editor.loadDefinitionsFromFile('mtlx');
        });

        // Add clear graph event listener
        var clearGraphButton = document.getElementById('clearGraph');
        clearGraphButton.addEventListener('click', function () {
            editor.clearGraph();
        });

        // Add save materialx graph event listener
        var saveMaterialXGraph = document.getElementById('saveMaterialXGraph');
        saveMaterialXGraph.addEventListener('click', function () {
            var saveCustomLibs = document.getElementById('saveCustomLibs').checked;
            var saveNodePositions = document.getElementById('saveNodePositions').checked;
            editor.saveGraphToFile('mtlx', saveCustomLibs, saveNodePositions);
        });

        // Add save materialx graph text event listener
        var saveMaterialXGraphText = document.getElementById('saveMaterialXGraphText');
        saveMaterialXGraphText.addEventListener('click', function () {
            saveToStringUI();
        });

        // Add open subgraph event handler
        var openSubgraph = document.getElementById('openSubgraph');
        openSubgraph.addEventListener('click', function () {
            editor.openSubgraph();
        });

        // Add close subgraph event handler
        var closeSubgraph = document.getElementById('closeSubgraph');
        closeSubgraph.addEventListener('click', function () {
            editor.closeSubgraph();
        });


        // Add reset view event handler
        var resetView = document.getElementById('resetView');
        resetView.addEventListener('click', function () {
            editor.resetView();
        });

        // Add arrange graph event listener
        var arrangeGraphButton = document.getElementById('arrangeGraph');
        arrangeGraphButton.addEventListener('click', function () {
            editor.arrangeGraph();
        });

        // Add center node event listener
        var centerNodeButton = document.getElementById('centerNode');
        centerNodeButton.addEventListener('click', function () {
            editor.centerNode();
        });

        // Add collapse/expand nodes event listener
        var collapseNodesButton = document.getElementById('collapseNodes');
        collapseNodesButton.addEventListener('click', function () {
            editor.collapseExpandNodes(true);
        });
        var expandNodesButton = document.getElementById('expandNodes');
        expandNodesButton.addEventListener('click', function () {
            editor.collapseExpandNodes(false);
        });

        // Add copy selected event listener
        var copySelectedButton = document.getElementById('copySelected');
        copySelectedButton.addEventListener('click', function () {
            editor.copyToClipboard();
        });

        // Add paste selected event listener
        var pasteSelectedButton = document.getElementById('pasteSelected');
        pasteSelectedButton.addEventListener('click', function () {
            editor.pasteFromClipboard();
        });

        // Add create subgraph event listener
        var createNodeGraphButton = document.getElementById('createNodeGraph');
        createNodeGraphButton.addEventListener('click', function () {
            editor.createNodeGraph();
        });

        // Add extract subgraph event listener
        var extractNodeGraphButton = document.getElementById('extractNodeGraph');
        extractNodeGraphButton.addEventListener('click', function () {
            editor.extractNodeGraph();
        });

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
        var xmltograph = document.getElementById('xmltograph');
        xmltograph.addEventListener('click', function () {
            var name = 'MaterialXGraph' + texAreaNumber++;
            var mtlxdoc = document.getElementById('mtlxdoc').value;
            editor.loadGraphFromString('mtlx', mtlxdoc, 'MaterialXGraph', auto_arrange_size);
        });

        /* function updateRenderableItemUI(renderableItems) {
            let renderableItemSelect = document.getElementById('renderableItem');
            // Remove any previous children
            while (renderableItemSelect.firstChild) {
                renderableItemSelect.removeChild(renderableItemSelect.firstChild);
            }
            for (let i = 0; i < renderableItems.length; i++) {
                let item = renderableItems[i];
                let option = document.createElement('option');
                option.value = i;
                option.text = item; // item.getNamePath();
                renderableItemSelect.appendChild(option);
            }
        } */

        function updateRenderableItemUI()
        {
            let renderableItems = editor.findRenderableItems();

            // Update selection for renderables
            let renderableItemSelect = document.getElementById('renderableItem');
            while (renderableItemSelect.firstChild) {
                renderableItemSelect.removeChild(renderableItemSelect.firstChild);
            }
            for (let i = 0; i < renderableItems.length; i++) {
                let item = renderableItems[i];
                let option = document.createElement('option');
                option.value = item;
                let uiitem = item;
                // Truncate the name so it will fit into UI.
                if (uiitem.length > 12)
                    uiitem = uiitem.substring(0, 12) + '...';
                option.text = uiitem; 
                renderableItemSelect.appendChild(option);
            }          
        }

        function saveToStringUI() {
            var saveCustomLibs = document.getElementById('saveCustomLibs').checked;
            var saveNodePositions = document.getElementById('saveNodePositions').checked;
            var result = editor.saveGraphToString('mtlx', saveCustomLibs, saveNodePositions);
            cmeditor.setValue(result);

            if (theRenderer) {
                theRenderer.updateMaterialFromText(result);
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

        var graphtoxml2 = document.getElementById('graphtoxml2');
        if (graphtoxml2) {
            graphtoxml2.addEventListener('click', function () {
                saveToStringUI();
            });
        }

        // Handle turntabe option
        let turntableEnabledUI = document.getElementById('turntableEnabled');
        if (turntableEnabledUI) {
            turntableEnabledUI.addEventListener('click', (e) => {
                // Toggle inverting the button colors no toggling danger
                turntableEnabledUI.classList.toggle('btn-secondary');
                if (theRenderer)
                    theRenderer.toggleTurntable();
            });
        }

        // Handle render disabled option
        let disableRenderingUI = document.getElementById('disableRendering');
        if (disableRenderingUI) {
            disableRenderingUI.addEventListener('click', (e) => {
                // Toggle inverting the button colors
                disableRenderingUI.classList.toggle('btn-danger');
                if (theRenderer)
                    theRenderer.toggleRendering();
            });
        }

        // Handle background display option
        let toggleBackgroundTextureUI = document.getElementById('toggleBackgroundTexture');
        if (toggleBackgroundTextureUI) {
            toggleBackgroundTextureUI.addEventListener('click', (e) => {
                toggleBackgroundTextureUI.classList.toggle('btn-secondary');
                if (theRenderer)
                    theRenderer.toggleBackgroundTexture();
            });
        }
        // Handle reset camera option
        let resetCameraUI = document.getElementById('resetCamera');
        if (resetCameraUI) {
            resetCameraUI.addEventListener('click', (e) => {
                if (theRenderer)
                    theRenderer.resetCamera();
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
                        if (theRenderer)
                            theRenderer.setRenderGeometry(fileURL);
                        console.log('Change geometry to:', fileURL);
                    }
                }
                fileInput.click();
            }
            else {
                // Convert to lowercase and remove spaces
                var geometryURL = uiItem.toLowerCase().replace(/\s/g, '');
                var geometryPath = 'Geometry/' + geometryURL + '.glb';
                console.log('Change geometry to:', geometryPath);
                if (theRenderer)
                    theRenderer.setRenderGeometry(geometryPath);
            }
        }

        // Handle geometry item changed
        let geometryItemSelect = document.getElementById('loadGeometry');
        if (geometryItemSelect) {
            // Add event handler for selection
            geometryItemSelect.addEventListener('change', (e) => {
                loadFromMenu(e);
                if (e.target.value == '_loadFromFile_')
                    e.target.value = 'Custom Geometry'
            });
        }

        // Handle material selection change
        let renderableItemSelect = document.getElementById('renderableItem');
        if (renderableItemSelect) {
            renderableItemSelect.addEventListener('change', (e) => {
                let index = e.target.value;
                if (theRenderer)
                    theRenderer.setRenderMaterial(index);
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
                editor.setDirty();
            }
        });

        // Start observing the canvas container
        observer.observe(colContainer);

    }

    function setupJavascriptSyntax() {
        // Initialize CodeMirror for JS syntax highlighting
        const elem = document.getElementById('mtlxlib');
        if (!elem) {
            return;
        }
        var cmeditor = CodeMirror.fromTextArea(elem, {
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
        var cmeditor = CodeMirror.fromTextArea(materialXTextArea, {
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
