// UI helpers.

function setupTheme() {
    const body = document.body;
    // Check if the user has a preferred color scheme
    const prefersDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (document.body.classList.contains('vscode-dark') || document.body.classList.contains('vscode-high-contrast'))
        prefersDarkMode = true

    // Set the initial theme based on user preferences
    if (prefersDarkMode) {
        body.setAttribute('data-bs-theme', 'dark');
    } else {
        body.setAttribute('data-bs-theme', 'light');
    }   
}

//setupTheme();

// Interaction for SVG display area
function setUpSVGInteraction(svgContainerId, svgContentId) {

    var svgContainer = document.getElementById(svgContainerId);
    var svgContent = document.getElementById(svgContentId);

    var state = {
        isPanning: false,
        startCoords: { x: 0, y: 0 },
        startViewBox: null
    };

    // Clear or set the style here. Clear max width so that the SVG can be scaled 
    // to fit the container.
    style = svgContent.getAttribute('style')
    //svgContent.setAttribute('style', 'max-width:2048px;')
    svgContent.setAttribute('style', '')

    // Handle start of panning
    function handleMouseDown(event) {
        if (event.button !== 0)
            return;

        event.preventDefault();
        state.isPanning = true;
        state.startCoords.x = event.clientX;
        state.startCoords.y = event.clientY;
        state.startViewBox = svgContent.getAttribute('viewBox');
    }

    // Handle panning
    function handleMouseMove(event) {
        if (!state.isPanning)
            return;

        event.preventDefault();
        var dx = event.clientX - state.startCoords.x;
        var dy = event.clientY - state.startCoords.y;
        var viewBox = state.startViewBox.split(' ');

        viewBox[0] -= dx;
        viewBox[1] -= dy;

        svgContent.setAttribute('viewBox', viewBox.join(' '));
    }

    // Handle stop of panning
    function handleMouseUp(event) {
        if (event.button !== 0)
            return;

        event.preventDefault();
        state.isPanning = false;
    }

    // Handle zooming
    function handleWheel(event) {
        event.preventDefault();

        var delta = Math.max(-1, Math.min(1, (event.deltaY || -event.detail)));
        var viewBox = svgContent.getAttribute('viewBox').split(' ');

        var scaleFactor = delta > 0 ? 1.1 : 0.9;

        var containerWidth = svgContainer.offsetWidth;
        var containerHeight = svgContainer.offsetHeight;

        var center = {
            x: containerWidth / 2,
            y: containerHeight / 2
        };

        var oldWidth = parseFloat(viewBox[2]);
        var oldHeight = parseFloat(viewBox[3]);
        var newWidth = oldWidth / scaleFactor;
        var newHeight = oldHeight / scaleFactor;

        var deltaX = (oldWidth - newWidth) * (center.x / containerWidth);
        var deltaY = (oldHeight - newHeight) * (center.y / containerHeight);

        var newX = parseFloat(viewBox[0]) + deltaX;
        var newY = parseFloat(viewBox[1]) + deltaY;

        viewBox[0] = newX;
        viewBox[1] = newY;
        viewBox[2] = newWidth;
        viewBox[3] = newHeight;

        svgContent.setAttribute('viewBox', viewBox.join(' '));
    }

    // Set up event handling
    svgContainer.addEventListener('mousedown', handleMouseDown);
    svgContainer.addEventListener('mousemove', handleMouseMove);
    svgContainer.addEventListener('mouseup', handleMouseUp);
    svgContainer.addEventListener('mouseleave', handleMouseUp);
    svgContainer.addEventListener('wheel', handleWheel);
};

function copyContentToClipboard(button) {
    var targetId = button.getAttribute('data-target');
    var element = document.getElementById(targetId);

    if (!element) {
        console.error('Element not found');
        return;
    }

    var textToCopy = element.value;

    navigator.clipboard.writeText(textToCopy).then(function() {
        // Provide some visual feedback
        //button.classList.add('invert');
        //setTimeout(function() {
        //    button.classList.remove('invert');
        //}, 500);
    }).catch(function(err) {
        console.error('Could not copy text: ', err);
    });
}

function pasteContentFromClipboard(button) {
    var targetId = button.getAttribute('data-target');
    var element = document.getElementById(targetId);

    navigator.clipboard.readText().then(function(text) {
        if (element) {
            console.log('Pasting text: ', text);
            element.value = text;
        }
    }).catch(function(err) {
        console.error('Could not paste text: ', err);
    });
}

function addCopyHandler(copyButton)
{
    if (copyButton)
    {
        //console.log('Adding copy handler for button: ', copyButton.id, copyButton.getAttribute('data-target'));
        copyButton.addEventListener('click', function() {
            copyContentToClipboard(copyButton);
        });
    }
}

function addPasteHandler(pasteButton)
{
    if (pasteButton)
    {
        //console.log('Adding paste handler for button: ', pasteButton.id, pasteButton.getAttribute('data-target'));
        pasteButton.addEventListener('click', function() {
            pasteContentFromClipboard(pasteButton);
        });
    }
}

function pasteContentFromClipboard(button, setterFunction) {

    navigator.clipboard.readText().then(function(text) {
        setterFunction.setValue(text);
    }).catch(function(err) {
        console.error('Could not paste text: ', err);
    });
}


function addPasteHandler(pasteButton, setterFunction)
{
    if (pasteButton)
    {
        //console.log('Adding paste handler for button: ', pasteButton.id, pasteButton.getAttribute('data-target'));
        pasteButton.addEventListener('click', function() {
            pasteContentFromClipboard(pasteButton, setterFunction);
        });
    }
}

function addCopyHandlers()
{
    const darkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (document.body.classList.contains('vscode-dark') || document.body.classList.contains('vscode-high-contrast'))
        darkMode = true

    var copyButtons = document.getElementsByClassName('copy-button');
    for (var i = 0; i < copyButtons.length; i++)
    {
        var copyButton = copyButtons[i];
        //console.log('Setting copy button theme: ', darkMode ? 'dark' : 'light');
        var childImg = copyButton.getElementsByTagName('img')[0];
        if (childImg)
            if (darkMode)
                childImg.classList.add('inverted-svg')
            else
                childImg.classList.remove('inverted-svg')
        copyButton.setAttribute('data-bs-theme', darkMode ? 'dark' : 'light');
        addCopyHandler(copyButton);
    }

    var invertButtons = document.getElementsByClassName('invert-button');
    for (var i = 0; i < invertButtons.length; i++)
    {
        var invertButton = invertButtons[i];
        var childImg = invertButton.getElementsByTagName('img')[0];
        if (childImg)
            //console.log('Setting invert button theme: ', invertButton.id, darkMode ? 'dark' : 'light');
            if (darkMode)
                childImg.classList.add('inverted-svg')
    }        
}

function addPasteHandlers()
{

    const darkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (document.body.classList.contains('vscode-dark') || document.body.classList.contains('vscode-high-contrast'))
        darkMode = true

    var pasteButtons = document.getElementsByClassName('paste-button');
    for (var i = 0; i < pasteButtons.length; i++)
    {
        var pasteButton = pasteButtons[i];
        //console.log('Setting paste button theme: ', darkMode ? 'dark' : 'light');
        var childImg = pasteButton.getElementsByTagName('img')[0];
        if (childImg)
            if (darkMode)
                childImg.classList.add('inverted-svg')
        pasteButton.setAttribute('data-bs-theme', darkMode ? 'dark' : 'light');
        addPasteHandler(pasteButton);
    }
}
