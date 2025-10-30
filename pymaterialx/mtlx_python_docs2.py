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
        for module_info in pkgutil.iter_modules(importlib.import_module('MaterialX').__path__):
            print('Found module:', module_info.name)
            module_list.append(module_info.name)
        print("Found MaterialX modules:", module_list)

        imported_modules = {}

        for mod in module_list:
            try:
                imported = __import__('MaterialX.' + mod, fromlist=[''])
                imported_modules[mod] = imported
                print(f"Imported MaterialX.{mod}")
            except Exception as e:
                print(f"Could not import MaterialX.{mod}: {e}")
        return imported_modules

    def build_structure(self, imported_modules):
        """Build structured data representation of modules, classes, functions, and globals."""
        structure = {}

        for mod_name, mod in imported_modules.items():
            if mod_name.startswith('_'):
                continue

            mod_info = {"classes": {}, "functions": {}, "globals": []}
            for name in dir(mod):
                if name.startswith('_'):
                    continue
                obj = getattr(mod, name, None)

                if callable(obj):
                    if isinstance(obj, type):  # class
                        cls_info = {
                            "doc": (obj.__doc__ or '').strip(),
                            "methods": {},
                            "attributes": []
                        }
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
                                if lines and lines[0].startswith(attr.__name__ + '(*args'):
                                    doc = '\n'.join(lines[1:]).strip()
                                
                                # Add newline before numbered overloads
                                doc = re.sub(r'(?<!^)(\d+\.)', r'<br>\1', doc)
                                
                                # Replace newlines with <br> for HTML display
                                #doc = doc.replace('\n', '<br>')
                                
                                cls_info["methods"][m] = doc

                                #cls_info["methods"][m] = doc                                
                                
                                #cls_info["methods"][m] = (attr.__doc__ or '').strip()
                            else:
                                cls_info["attributes"].append(m)

                        #for m, attr in obj.__dict__.items():
                        #    if m.startswith('_'):
                        #        continue
                        #    if callable(attr):
                        #        cls_info["methods"][m] = (attr.__doc__ or '').strip()
                        #    else:
                        #        cls_info["attributes"].append(m)                        
                        #for m in dir(obj):
                        #    if m.startswith('_'):
                        #        continue
                        #    attr = getattr(obj, m, None)
                        #    if callable(attr):
                        #        cls_info["methods"][m] = (attr.__doc__ or '').strip()
                        #    else:
                        #        cls_info["attributes"].append(m)
                        mod_info["classes"][name] = cls_info
                    else:  # function
                        mod_info["functions"][name] = (obj.__doc__ or '').strip()
                else:
                    if isinstance(obj, types.ModuleType):
                        continue
                    owner = getattr(obj, "__module__", None)
                    if owner not in (None, mod.__name__) and not name.isupper():
                        continue
                    mod_info["globals"].append(name)

            structure[mod_name] = mod_info
        return structure

    def generate_markdown(self, structure):
        md = []
        for mod_name, mod_info in structure.items():
            md.append(f"## Module: MaterialX.{mod_name}\n")

            if mod_info["classes"]:
                md.append("### Classes\n")
                for cls_name, cls_info in mod_info["classes"].items():
                    md.append(f"- **{cls_name}**: {cls_info['doc']}\n")
                    if cls_info["methods"]:
                        md.append(f"  - Methods:\n")
                        for m, doc in cls_info["methods"].items():
                            md.append(f"    - `{m}`: {doc}\n")
                    if cls_info["attributes"]:
                        md.append(f"  - Attributes: {', '.join(cls_info['attributes'])}\n")

            if mod_info["functions"]:
                md.append("### Functions\n")
                for fn, doc in mod_info["functions"].items():
                    md.append(f"- `{fn}`: {doc}\n")

            if mod_info["globals"]:
                md.append("### Globals\n")
                md.append(", ".join(mod_info["globals"]))
                md.append("\n")

            md.append("\n---\n")
        return "\n".join(md)

    def generate_html(self, structure, title):
        html = []
        html.append("<html><head>")
        html.append('<meta charset="utf-8">')
        html.append(f"<title>{title}</title>")
        html.append('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">')
        html.append('<!--StyleStart-->')
        html.append("<style>")
        html.append("""
        #sidebar { width: 300px; height: 100vh; overflow-y: auto; position: fixed; }
        #content { margin-left: 320px; padding: 1rem; }
        pre { white-space: pre-wrap; }
        a { cursor: pointer; }
        """)
        html.append("</style>")
        html.append('<!--StyleEnd-->')
        html.append("</head><body data-bs-theme='dark'>")

        html.append("<!--Start-->")
        html.append("<div id='sidebar' class='bg-dark text-light p-3'>")
        html.append("<h5>Python Modules</h5>")

        # Add search input
        html.append('<input type="text" id="searchBox" class="form-control mb-2" placeholder="Filter...">')

        html.append("<ul class='list-unstyled' id='indexList'>")

        # Sidebar tree
        for mod_name, mod_info in structure.items():
            html.append(f"<li><strong>{mod_name}</strong><ul>")
            if mod_info["classes"]:
                html.append("<li>Classes<ul>")
                for cls in mod_info["classes"]:
                    html.append(f"<li><a class='link-info link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover' data-type='class' data-module='{mod_name}' data-name='{cls}'>{cls}</a></li>")
                html.append("</ul></li>")
            if mod_info["functions"]:
                html.append("<li>Functions<ul>")
                for fn in mod_info["functions"]:
                    html.append(f"<li><a class='link-warning link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover' data-type='function' data-module='{mod_name}' data-name='{fn}'>{fn}</a></li>")
                html.append("</ul></li>")
            if mod_info["globals"]:
                html.append("<li>Globals<ul>")
                for g in mod_info["globals"]:
                    html.append(f"<li><a class='link-danger link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover' data-type='global' data-module='{mod_name}' data-name='{g}'>{g}</a></li>")
                html.append("</ul></li>")
            html.append("</ul></li>")
        html.append("</ul></div>")

        html.append("<div id='content'><h3>Select interface item from index.</h3></div>")

        html.append("<script>")
        html.append("const data = " + json.dumps(structure) + ";")
        html.append(r"""
                    
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

    // Click to show content
    document.querySelectorAll('a[data-type]').forEach(el => {
        el.addEventListener('click', () => {
            const module = el.dataset.module;
            const name = el.dataset.name;
            const type = el.dataset.type;
            const mod = data[module];
            let html = `<h3>${module} - ${name}</h3>`;
            if (type === 'class') {
                const cls = mod.classes[name];
                html += `<h4>Class</h4><p>${escapeHtml(cls.doc)}</p>`;
                if (Object.keys(cls.methods).length) {
                    html += '<h5>Methods</h5><ul>';
                    for (const [m, doc] of Object.entries(cls.methods)) {
                        html += `<li><code>${m}</code>: ${escapeHtml(doc)}</li>`;
                    }
                    html += '</ul>';
                }
                if (cls.attributes.length) {
                    html += '<h5>Attributes</h5><ul>';
                    for (const a of cls.attributes) {
                        html += `<li>${a}</li>`;
                    }
                    html += '</ul>';
                }
            } else if (type === 'function') {
                const fn = mod.functions[name];
                html += `<h4>Function</h4><pre>${escapeHtml(fn)}</pre>`;
            } else if (type === 'global') {
                html += `<h4>Global</h4><p>${name}</p>`;
            }
            document.getElementById('content').innerHTML = html;
        });
    });

    // Sidebar search filter
    document.getElementById('searchBox').addEventListener('keyup', function() {
        const filter = this.value.toLowerCase();
        document.querySelectorAll('#indexList li').forEach(li => {
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
        md_filename = os.path.join(output_folder, f"Python_{version_safe}_documentation.md")
        html_filename = os.path.join(output_folder, f"Python_{version_safe}_documentation.html")

        print("Writing Markdown...")
        md_content = self.generate_markdown(structure)
        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(md_content)

        print("Writing HTML...")
        html_content = self.generate_html(structure, f"MaterialX {version} Python Documentation")
        with open(html_filename, "w", encoding="utf-8") as f:
            f.write(html_content)

        print("Wrote:", md_filename)
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
