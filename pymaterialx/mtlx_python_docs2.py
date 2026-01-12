'''
MaterialX Python API Documentation Generator
Generates Markdown and HTML documentation based on installed MaterialX Python modules.
''' 
try:
    import MaterialX as mx
except ImportError:
    raise ImportError("MaterialX module not found. Please ensure MaterialX is installed and accessible in your Python environment.")

import pkgutil
import importlib
import types
import argparse
import os
import json

class PythonDocumentationGenerator:

    def import_modules(self) -> dict:
        print('Scanning for MaterialX modules...')
        module_list = []
        ignore_list = ['_scripts', 'datatype']
        for module_info in pkgutil.iter_modules(importlib.import_module('MaterialX').__path__):    
            if module_info.name not in ignore_list:        
                module_list.append(module_info.name)
        print(f"Found {len(module_list)} MaterialX modules:", module_list)

        imported_modules = {}
        imported_module_names = []
        failed_to_import_module_names = []
        for mod in module_list:
            try:
                imported = __import__('MaterialX.' + mod, fromlist=[''])
                imported_modules[mod] = imported
                imported_module_names.append(mod)
            except Exception as e:
                failed_to_import_module_names.append(mod)
    
        print(f'Imported modules: {len(imported_module_names)}')
        num_failed = len(failed_to_import_module_names)
        if num_failed> 0:
            print(f'WARNING : Failed to import {failed_to_import_module_names}')
        return imported_modules

    def build_structure(self, imported_modules):
        """Build structured data representation of modules, classes, functions, and globals."""
        structure = {}

        for mod_name, mod in imported_modules.items():
            if mod_name.startswith('_'):
                continue

            mod_info = {"classes": {}, "functions": {}, "globals": {}}
            for name in dir(mod):
                if name.startswith('_'):
                    continue
                obj = getattr(mod, name, None)

                is_python_defined = callable(obj) and getattr(obj, '__module__', None) == mod.__name__
                if is_python_defined:

                    if isinstance(obj, type):  # class
                        cls_info = {
                            "doc": (obj.__doc__ or '').strip(),
                            "methods": {},
                            "attributes": [],
                            "bases": []
                        }

                        bases = []
                        for base in getattr(obj, "__mro__", [])[1:]:  # skip the class itself
                            base_name = getattr(base, "__name__", str(base))
                            if "pybind" not in base_name and base_name != "object" and base_name not in bases:
                                bases.append(base_name)
                        cls_info["bases"] = bases
                        
                        for m, attr in obj.__dict__.items():
                            if m.startswith('_'):
                                continue
                            # unwrap staticmethod/classmethod
                            if isinstance(attr, (staticmethod, classmethod)):
                                attr = attr.__func__
                            if callable(attr):
                                import re
                                
                                doc = attr.__doc__ or ''
                                lines = doc.splitlines()
                                #for l in lines:
                                #    print(l)
                                if lines and lines[0].startswith(attr.__name__ + '(*args'):
                                    doc = '\n'.join(lines[1:]).strip()
                                
                                # Add newline before numbered overloads
                                doc = re.sub(r'(?<!^)(\d+\.)', r'<br>\1', doc)
                                
                                # Replace newlines with <br> for HTML display
                                doc = doc.replace('\n\n', '<br>')
                                doc = doc.replace('\n', '<br>')
                                doc = doc + '<br>'
                                
                                cls_info["methods"][m] = lines

                            else:
                                value = getattr(obj, m, None)
                                value = repr(value)
                                if '<' in value:
                                    value = "(property)"
                                value = value.replace('<', '(').replace('>', ')')
                                cls_info["attributes"].append((m, value))
                                #cls_info["attributes"].append(m)

                        mod_info["classes"][name] = cls_info
                    else:  # function
                        mod_info["functions"][name] = (obj.__doc__ or '').strip()
                else:
                    if isinstance(obj, types.ModuleType):
                        continue
                    if (mod_name == 'main'):
                        continue

                    owner = getattr(obj, "__module__", None)
                    if owner not in (None, mod.__name__) and not name.isupper():
                        continue
                    # Find value of global variable
                    value = getattr(mod, name, '')
                    if value:
                        name_value = repr(value)
                        # replace non-XML safe characters
                        name_value = name_value.replace('<', '(').replace('>', ')')
                    else:
                        name_value = ''
                    mod_info["globals"][name] = name_value

            structure[mod_name] = mod_info
        return structure

    def escape_html(self, text):
        if not text:
            return ''
        return (text.replace('&', '&amp;')
                    .replace('<', '&lt;')
                    .replace('>', '&gt;')
                    .replace('"', '&quot;')
                    .replace("'", '&#39;')
                    .replace('\n', '<br>'))

    def generate_markdown(self, structure):
        md = []
        mod_number = 1
        for mod_name, mod_info in structure.items():
            md.append(f"## {mod_number}. Module: MaterialX.{mod_name}\n")
            mod_number += 1

            if mod_info["classes"]:
                md.append("### Classes\n")
                class_number = 1
                for cls_name, cls_info in mod_info["classes"].items():
                    #md.append(f"- **{cls_name}**: {cls_info['doc']}\n")
                    #if cls_info.get("bases"):
                    #    md.append(f"  - Inherits from: {', '.join(cls_info['bases'])}\n")
                    # Add an HTML anchor for this class so we can link to it
                    anchor = f"materialx-{mod_name.lower()}-{cls_name.lower()}"
                    md.append(f"<hr><h4>{class_number}. <a id='{anchor}'>{cls_name}</a></h4>\n")
                    md.append(f"{cls_info['doc']}\n")
                    class_number += 1

                    # Add linked base classes
                    if cls_info.get("bases"):
                        linked_bases = []
                        for base in cls_info["bases"]:
                            # Search all modules for the base to link properly
                            base_anchor = f"#{'materialx-' + mod_name.lower() + '-' + base.lower()}"
                            linked_bases.append(f"[{base}]({base_anchor})")
                        md.append(f'##### Inheritance')
                        for lb in linked_bases:
                            md.append(f"- {lb}")                        

                    if cls_info["methods"]:
                        md.append(f"##### Methods\n")
                        for m, doc in cls_info["methods"].items():
                            doc_string = "\n        ".join(doc)
                            doc_string = self.escape_html(doc_string)
                            md.append(f"- **`{m}`**: {doc_string}\n")
                    if cls_info["attributes"]:
                        md.append(f"##### Attributes\n")
                        for name, value in cls_info["attributes"]:
                            md.append(f"- `{name}` = {value}")
                        #attrs = [f"{name} = {value}" for name, value in cls_info["attributes"]]
                        #md.append(f"  - Attributes: {', '.join(attrs)}\n")

            if mod_info["functions"]:
                md.append("\n### Functions\n")
                for fn, doc in mod_info["functions"].items():
                    md.append(f"- `{fn}`: {doc}\n")

            if mod_info["globals"]:
                md.append("\n### Globals\n")
                for g in mod_info["globals"]:
                    md.append(f"- `{g}`")
                    if mod_info["globals"][g]:
                        md.append(f" = {mod_info['globals'][g]}")
                #md.append("\n")

            md.append("\n---\n")
        return "\n".join(md)

    def generate_html(self, structure, title):
        html = []
        html.append("<html><head>")
        html.append('<meta charset="utf-8">')
        html.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
        html.append(f"<title>{title}</title>")
        html.append('<link href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">')
        html.append('<!--StyleStart-->')
        html.append("<style>")
        html.append("""
        pre { white-space: pre-wrap; }
        a { cursor: pointer; }
        """)
        html.append("</style>")
        html.append('<!--StyleEnd-->')
        html.append("</head><body data-bs-theme='dark'>")
        html.append("<!--Start-->")
        # Simple header row inside content to avoid conflicting site nav
        html.append("<div class='rounded-4 container-fluid py-2 bg-primary bg-gradient sticky-top'>")
        html.append("  <div class='d-flex align-items-center gap-2'>")
        html.append("    <button class='btn btn-outline-light' type='button' data-bs-toggle='offcanvas' data-bs-target='#mxdoc-sidebar' aria-controls='mxdoc-sidebar'>Index</button>")
        html.append(f"    <span class='h5 mb-0'>{title}</span>")
        html.append("  </div>")
        html.append("</div>")

        # Offcanvas sidebar index
        html.append("<div class='offcanvas offcanvas-start text-bg-dark' tabindex='-1' id='mxdoc-sidebar' aria-labelledby='mxdoc-sidebarLabel'>")
        html.append("  <div class='offcanvas-header'>")
        html.append("    <h5 class='offcanvas-title' id='mxdoc-sidebarLabel'>Python Modules</h5>")
        html.append("    <button type='button' class='btn-close btn-close-white' data-bs-dismiss='offcanvas' aria-label='Close'></button>")
        html.append("  </div>")
        html.append("  <div class='offcanvas-body'>")
        html.append('    <input type="text" id="mxdoc-search" class="form-control mb-2" placeholder="Filter...">')
        html.append("    <ul class='list-unstyled' style=\"font-size: small;\" id='mxdoc-index'>")

        # Sidebar tree
        for mod_name, mod_info in structure.items():
            html.append(f"<li><strong>{mod_name}</strong><ul>")
            if mod_info["classes"]:
                html.append("<li>Classes<ul>")
                for cls in mod_info["classes"]:
                    html.append(f"<li><a class='link-info link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover list-group-item-action' data-bs-dismiss='offcanvas' role='button' data-type='class' data-module='{mod_name}' data-name='{cls}'>{cls}</a></li>")
                html.append("</ul></li>")
            if mod_info["functions"]:
                html.append("<li>Functions<ul>")
                for fn in mod_info["functions"]:
                    html.append(f"<li><a class='link-warning link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover list-group-item-action' data-bs-dismiss='offcanvas' role='button' data-type='function' data-module='{mod_name}' data-name='{fn}'>{fn}</a></li>")
                html.append("</ul></li>")
            if mod_info["globals"]:
                html.append("<li>Globals<ul>")
                for g in mod_info["globals"]:
                    html.append(f"<li><a class='link-success link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover list-group-item-action' data-bs-dismiss='offcanvas' role='button' data-type='global' data-module='{mod_name}' data-name='{g}'>{g}</a></li>")
                html.append("</ul></li>")
            html.append("</ul></li>")
        html.append("    </ul>")
        html.append("  </div>")
        html.append("</div>")

        # Main content area
        html.append("<p><main style=\"font-size: small;\" class='border rounded-4 container-fluid py-3' id='mxdoc-content'><p>Select interface item from index.</p></main>")

        # Conditionally load Bootstrap bundle only if not present to avoid conflicts when embedded
        html.append("<script>(function(){if(!window.bootstrap){var s=document.createElement('script');s.src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js';s.crossOrigin='anonymous';document.head.appendChild(s);}})();</script>")

        html.append("<script>")
        html.append("const data = " + json.dumps(structure) + ";")
        html.append(r"""

        // Handle clicks on base class links
        document.addEventListener('click', function(e) {
            if (e.target && e.target.classList.contains('mxdoc-base')) {
                e.preventDefault();
                const baseName = e.target.dataset.basename;

                // Search for the base class in all modules
                for (const [moduleName, module] of Object.entries(data)) {
                    if (module.classes && module.classes[baseName]) {
                        // Simulate selecting this class
                        const cls = module.classes[baseName];
                        let html = `<h3>${moduleName}.${baseName}</h3>`;
                        html += `<h4>Class</h4><p>${cls.doc}</p>`;
                        if (cls.bases && cls.bases.length) {
                            html += `<h5>Inherits from</h5><ul>`;
                            for (const base of cls.bases) {
                                html += `<li><a href="#" class="link-info mxdoc-base" data-basename="${base}">${base}</a></li>`;
                            }
                            html += `</ul>`;
                        }
                        if (Object.keys(cls.methods).length) {
                            html += '<h5>Methods</h5><ul>';
                            for (const [m, doc] of Object.entries(cls.methods)) {
                                doc_string = doc.join('<br>');
                                html += `<li><code>${m}</code>: <pre>${doc_string}</pre></li>`;
                            }
                            html += '</ul>';
                        }
                        if (cls.attributes.length) {
                            html += '<h5>Attributes</h5><ul>';
                            for (const a of cls.attributes) {
                                if (!a[1]) {
                                    a[1] = '';
                                } else {
                                    a[1] = ' = ' + escapeHtml_2(a[1]);}
                                html += `<li><code>${a[0]}</code><i>${a[1]}</i></li>`;
                            }
                            html += '</ul>';
                        }

                        document.getElementById('mxdoc-content').innerHTML = html;
                        return; // Stop after first found
                    }
                }
            }
        });


    function escapeHtml(text) {
        if (!text) return '';
        return text.replace(/&(?!amp;)/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#39;')
                .replace(/&lt;br&gt;/g, '<br>');
    }

    function escapeHtml_2(text) {
        if (!text) return '';
        return text.replace(/[&<>"']/g, function(m) {
            return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m];
        });
    }

    // Click to show content and auto-hide offcanvas
    // Scope listeners to our offcanvas only to avoid affecting site menus
    document.querySelectorAll('#mxdoc-sidebar a[data-type]').forEach(el => {
        el.addEventListener('click', () => {
            const module = el.dataset.module;
            const name = el.dataset.name;
            const type = el.dataset.type;
            const mod = data[module];
            let html = `<h3>${module}.${name}</h3>`;
            //if (type === 'class') {
            if (type === 'class') {
                const cls = mod.classes[name];
                html += `<h5>Class</h5><p>${cls.doc}</p>`;
                    
                if (cls.bases && cls.bases.length) {
                    html += `<h6>Inherits from</h6><ul>`;
                    for (const base of cls.bases) {
                        // Create a clickable link for base class
                        html += `<li><a href="#" class="link-info mxdoc-base" data-basename="${base}">${base}</a></li>`;
                    }
                    html += `</ul>`;
                }

                //if (cls.bases && cls.bases.length) {
                //    html += `<h5>Inherits from</h5><p>${cls.bases.join('-> ')}</p>`;
                //}                    

                //const cls = mod.classes[name];
                //html += `<h5>Class</h5><p>${cls.doc}</p>`;
                if (Object.keys(cls.methods).length) {
                    html += '<h6>Methods</h6><ul>';
                    for (const [m, doc] of Object.entries(cls.methods)) {
                        for (let i = 0; i < doc.length; i++) {
                            doc[i] = doc[i] + "";
                        }
                        doc_string = doc.join('<br>');
                        html += `<li><code>${m}</code>: <pre>${doc_string}</pre></li>`;
                    }
                    html += '</ul>';
                }
                if (cls.attributes.length) {
                    html += '<h6>Attributes</h6><ul>';
                    for (const a of cls.attributes) {
                        if (!a[1]) {
                            a[1] = '';
                        } else {
                            a[1] = ' = ' + escapeHtml_2(a[1]);}
                        html += `<li><code>${a[0]}</code><i>${a[1]}</i></li>`;
                    }
                    html += '</ul>';
                }
            } else if (type === 'function') {
                const fn = mod.functions[name];
                html += `<h5>Function</h5><pre>${escapeHtml(fn)}</pre>`;
            } else if (type === 'global') {
                const g = mod.globals[name];
                if (g) {
                    html += `<p>Global : ${name} = ${escapeHtml_2(g)}</p>`;
                } else {    
                    html += `<p>Global : ${name}</p>`;
                }
            }
            document.getElementById('mxdoc-content').innerHTML = html;

            // Auto-close the offcanvas if open
            const sidebar = document.getElementById('mxdoc-sidebar');
            if (sidebar && window.bootstrap) {
                const oc = bootstrap.Offcanvas.getOrCreateInstance(sidebar);
                oc.hide();
            }
        });
    });

    // Sidebar search filter
    document.getElementById('mxdoc-search').addEventListener('keyup', function() {
        const filter = this.value.toLowerCase();
        document.querySelectorAll('#mxdoc-index li').forEach(li => {
            const text = li.textContent.toLowerCase();
            li.style.display = text.includes(filter) ? '' : 'none';
        });
    });
        """)
        html.append("</script>")
        html.append("<!--End-->")
        html.append("</body></html>")
        return "\n".join(html)
   
    def write_to_file(self, structure, output_folder):
        version = mx.getVersionString()
        version_safe = mx.createValidName(version)

        print("Generating Markdown...")
        md_filename = os.path.join(output_folder, f"Python_{version_safe}_documentation.md")
        md_content = self.generate_markdown(structure)

        print("Generating HTML...")
        html_filename = os.path.join(output_folder, f"Python_{version_safe}_documentation.html")
        html_content = self.generate_html(structure, f"MaterialX {version} Python Documentation")

        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(md_content)
        print("Wrote:", md_filename)
        with open(html_filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print("Wrote:", html_filename)

def main():
    parser = argparse.ArgumentParser(description='Generate MaterialX Python API documentation.')
    parser.add_argument('-o', '--output', dest='output_folder', help='Path to output files.')
    args = parser.parse_args()

    output_folder = args.output_folder if args.output_folder else "."
    os.makedirs(output_folder, exist_ok=True)

    doc_generator = PythonDocumentationGenerator()
    imported_modules = doc_generator.import_modules()
    structure = doc_generator.build_structure(imported_modules)
    doc_generator.write_to_file(structure, output_folder)


if __name__ == "__main__":
    main()
