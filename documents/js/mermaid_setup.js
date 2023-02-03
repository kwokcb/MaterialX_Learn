//
// Special code to dynamically render Mermaid graphs. 
//
// The issue is that hidden (under a Bootstrap card tab)
// graphs do not render properly if done at initialization time. Instead
// graphs are rendered when the tab is made active by finding the
// associated card area's graphs and rendering them. If the area's graphs
// have already been rendered (i.e. there is a SVG child), then rendering
// is skipped.
//
// Note that only those buttons with class 'top-toggle' will be examined
//
// This code can be removed if / when hidden Mermaid graphs are handled properly
// (e.g. if Bootstrap actually hides and shows contents via an attribute change)
//

// Initialize mermaid but don't render immediately. Use logic below to dynamically render
mermaid.initialize({ startOnLoad: false, theme: document.body.classList.contains("vscode-dark") || document.body.classList.contains("vscode-high-contras") ? "dark" : "forest" });

// Render all mermaid graph children defined by an aria control (callback)
function renderAriaMermaidEvent(event) {
    let tab = event.target;
    renderAriaMermaid(tab);
}

// Render all mermaid graph children defined by an aria control
function renderAriaMermaid(tab) {
    let area = tab.getAttribute('aria-controls');
    let areaNode = document.getElementById(area);

    let graphs = document.querySelectorAll('.mermaid');
    for (let graph of graphs) {
        let svgs = graph.getElementsByTagName('svg')

        // Skip already rendered graphs
        if (svgs.length > 0) {
            continue;
        }

        if (areaNode.contains(graph)) {
            let html = graph.textContent;
            let id = 'graph-' + Math.floor(Math.random() * Math.floor(1000));
            mermaid.mermaidAPI.render(id, html, content => {
                graph.innerHTML = content;
            });

        }
    }
}

// Scan for aria tabs and render shown graphs
// and add an event handle to when other tabs are selected.
function monitor_mermaid_tabs() {
    let tabs = document.querySelectorAll('.top-toggle');
    console.log('Monitor tabs:', tabs);
    for (let tab of tabs) {
        if (tab.classList.contains('active')) {
            renderAriaMermaid(tab);
        }
        else {
            addEventListener("click", renderAriaMermaidEvent)
        }
    }
}
