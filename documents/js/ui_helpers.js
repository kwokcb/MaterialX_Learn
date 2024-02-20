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

    // Setup mermarid display mode
    mermaid.initialize({
        startOnLoad: false,
        theme: prefersDarkMode ? 'dark' : 'base',
        themeVariables: {
            'primaryColor': prefersDarkMode ? '#1F1F1F' : '#F1F1F1',
            'primaryBorderColor': prefersDarkMode ? '#FFFFFF' : '#000000',
            'background': prefersDarkMode ? '#000000' : '#FFFFFF',
            'secondaryColor': prefersDarkMode ? '#111100' : '#EEEEFF',
            'tertiaryColor': prefersDarkMode ? '#111111' : '#EEEEEE'
        }
    });
}

setupTheme();

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
