//
// Utilities for each library document including indexing filtering and
// Mermaid graph rendering and copying.
//

//
// Perform indexing filtering 
//
function filterTOC() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("searchTOC");
    if (!input)
        return
    filter = input.value;
    console.log("Look for: ", filter)
    li = document.querySelectorAll('.idx');
    for (i = 0; i < li.length; i++) {
        a = li[i];
        if (a.innerHTML.match(filter)) {
            if (filter.length > 0) {

                // Recursively expand parents
                var parent = a.parentElement
                while (parent) {
                    if (parent.className && parent.classList.contains("collapse")) {
                        //console.log("Show: ", parent)
                        parent.classList.add("show");
                    }
                    parent = parent.parentElement;
                }
            }
            a.style.display = "";
        }
        else {
            if (filter.length > 0)
                a.style.display = "none";
            else
                a.style.display = "";
        }
    }
}

// Perform indexing filtering on ENTER being pressing
// in filter field
function filterOnEnter(event) {
    if (event.code === 'Enter') {
        event.preventDefault();
        filterTOC();
    }
};

//
// Utility to render a Mermaid element
//
function renderMermaid(event) {
    buttonId = event.target.id;

    var mermaidinput = document.getElementById(buttonId + "_mermaid_input");
    var mermaidoutput = document.getElementById(buttonId + "_mermaid_output");
    if (mermaidinput && mermaidoutput) {
        const code = mermaidinput.textContent;
        let generateDiagram = function (code) {
            mermaidoutput.innerHTML = code;
            mermaidoutput.hidden = false;
        };
        mermaid.render(buttonId + "_mermaid_output_rendered", code, generateDiagram);

        var button = document.getElementById(event.target.id);
        button.hidden = true;
        button.remove;
    }
}

//
// Utility to copy the text from a Mermaid element
//
function copyMermaid(event) {
    buttonId = event.target.id;
    inputId = buttonId.replace('mrcopy', 'mrender')
    var mermaidinput = document.getElementById(inputId + "_mermaid_input");
    var text_to_copy = mermaidinput.innerHTML;
    text_to_copy = text_to_copy.replace(/&gt;/g, ">")
    text_to_copy = text_to_copy.replace(/&lt;/g, "<")
    //console.log(text_to_copy)
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text_to_copy).then(
            function () {
                //console.log(text_to_copy)
                document.getElementById(buttonId).textContent = "Copied";
                setTimeout(function () { document.getElementById(buttonId).textContent = "Copy Graph"; }, 2500);

            })
            .catch(
                function () {
                    document.getElementById(buttonId).textContent = "Failed to copy graph";
                    setTimeout(function () { document.getElementById(buttonId).textContent = "Copy Graph"; }, 2500);
                });
    }
}

// Toggle to handle when an indexing area is expanded or collapsed
// For now just changes the icon shown
function toggleIndexArea(event) {
    var img = event.target.firstElementChild;
    var imgsrc = event.target.innerHTML;
    if (event.target.getAttribute('aria-expanded') == "true") {
        event.target.innerHTML = imgsrc.replace('right', 'down');
    } else {
        event.target.innerHTML = imgsrc.replace('down', 'right');
    }
    //console.log(event.target.innerHTML)
}
