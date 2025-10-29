#from IPython.display import Markdown, display
import MaterialX as mx
import pkgutil
import importlib
import types

def import_modules():
    print('Scanning for MaterialX modules...')
    module_list = []
    for module_info in pkgutil.iter_modules(importlib.import_module('MaterialX').__path__):
        print('Found module:', module_info.name)
        module_list.append(module_info.name)
    print("Found MaterialX modules:", module_list)

    imported_modules = {}  # Store successfully imported modules

    for mod in module_list:
        try:
            imported = __import__('MaterialX.' + mod, fromlist=[''])
            imported_modules[mod] = imported  # Save for later use
            print(f"Imported MaterialX.{mod}")
        except Exception as e:
            print(f"Could not import MaterialX.{mod}: {e}")
    return imported_modules


def create_html(title, body):
    # Create html header
    # Include usage of bootstratp 5.3.2
    result = "<html>\n"
    result += "<head>\n"
    result += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">\n'
    result += f"<title>{title}</title>\n"
    result += "</head>\n"
    result += "<body data-bs-theme='dark' style='font-size: small;'>\n"
    result += "<div class='container-fluid p-4'>\n"    
    result += f"<h2>{title}</h2>\n"
    result += f"{body}\n"
    result += "<div></body>\n"
    result += "</html>\n"

    return result

def export_documentation(imported_modules):
    total_md = []

    print("Generating documentation...")
    for mod_name, mod in imported_modules.items():
        if mod_name.startswith('_'):
            continue
        md = []
        md.append(f"<h3>Module: MaterialX.{mod_name}</h3>")
        items = dir(mod)
        functions = []
        classes = []
        class_methods = {}
        class_non_methods = {}
        class_docs = {}
        function_docs = {}
        rest = []
        for name in items:
            if name.startswith('_'):
                continue
            obj = getattr(mod, name, None)
            if callable(obj):
                # Check classes
                if isinstance(obj, type):
                    classes.append(name)
                    class_docs[name] = obj.__doc__.split('\n')[0] if hasattr(obj, '__doc__') and obj.__doc__ else ''
                    # Get methods for this class
                    cls_obj = obj
                    method_names = [m for m in dir(cls_obj) if not m.startswith('_') and callable(getattr(cls_obj, m, None))]
                    nonmethod_names = [m for m in dir(cls_obj) if not m.startswith('_') and not callable(getattr(cls_obj, m, None))]
                    if nonmethod_names:
                        #print(f"Class {name} non-methods: {nonmethod_names}")
                        class_non_methods[name] = nonmethod_names
                    method_docs = {}
                    for m in method_names:
                        method_obj = getattr(cls_obj, m, None)
                        method_docs[m] = method_obj.__doc__.split('\n')[0] if hasattr(method_obj, '__doc__') and method_obj.__doc__ else ''
                    if method_names:
                        class_methods[name] = (method_names, method_docs)

                # Check functions
                else:
                    functions.append(name)
                    function_docs[name] = obj.__doc__.split('\n')[0] if hasattr(obj, '__doc__') and obj.__doc__ else ''
            else:
                # Is it a constant or other variable? Test if it's a global module variable defined inside the module
                # Skip imported modules (e.g. os, sys, warnings)
                if isinstance(obj, types.ModuleType):
                    continue
                # If the object has an owner module and it's not this module, and it's not a constant-like name, skip it
                owner = getattr(obj, "__module__", None)
                if owner not in (None, mod.__name__) and not name.isupper():
                    continue
                #print("res:", name)
                rest.append(name)

        if classes:
            md.append("<details open><summary>Classes</summary>\n")
            md.append("<div class='container-fluid rounded-4 border p-2 my-2' style='max-height: 200px; overflow-y: auto;'>")
            for cls_name in classes:
                
                # Row per class
                md.append("<div class='row px-2'>")
                doc = class_docs.get(cls_name, '')
                if doc:
                    doc = f": {doc}"
                
                # Class name column
                md.append(f"<div class='col-sm-3'><code>{cls_name}</code>{doc}</div>")
                
                # Class methods and members column
                md.append("<div class='col-sm'>")
                if cls_name in class_methods:
                    method_names, method_docs = class_methods[cls_name]
                    md.append(f"    <details><summary>Methods</summary><ul>")
                    #md.append(f"    - Methods of **{cls_name}**:")
                    for m in method_names:
                        md.append(f"        <li> <code>{m}</code>: {method_docs.get(m, '')}")
                    md.append("    </ul></details>")
                #else:
                #    md.append("    No public methods.")

                if cls_name in class_non_methods:
                    nonmethod_names = class_non_methods[cls_name]
                    md.append(f"    <details><summary>Attributes</summary><ul>")
                    for nm in nonmethod_names:
                        md.append(f"        <li> <code>{nm}</code>")
                    md.append("    </ul></details>")
                
                md.append("</div>") # Close class methods column
                
                md.append("</div>")  # Close row
            md.append("</div>")
            md.append("</details>")

        if functions:
            md.append("<details open><summary>Functions</summary>")
            md.append("<div class='container-fluid rounded-4 border p-2 my-2' style='max-height: 200px; overflow-y: auto;'>")
            for func_name in functions:
                # Row per function
                md.append("<div class='row px-2'>")
                doc = function_docs.get(func_name, '')
                # Replace func_name in code with <code>func_name</code>
                doc = doc.replace(func_name, f"<code>{func_name}</code> ")
                md.append(f"<div class='col-sm-3'><code>{func_name}</code></div>")
                md.append(f"<div class='col'>{doc}</div>")
                md.append("</div>")
            md.append("</div>")
            md.append("</details>")

        if rest:
            md.append("<details><summary>Globals</summary>")
            md.append("<ul>")
            for name in rest:
                md.append(f"<li> <code>{name}</code>")
            md.append("</ul>")
            md.append("</details>")

        md.append("<hr/>")

        total_md.extend(md)

    return total_md

def write_to_file(total_md):
    version = mx.getVersionString()

    version_safe = mx.createValidName(version)
    filename = f"Python_{version_safe}_documentation.md"
    print("Write Markdown docs to file:", filename)
    with open(filename, "w", encoding="utf-8") as f:
        f.write('\n'.join(total_md))

    html = create_html(f"MaterialX {version} Python Documentation", '\n'.join(total_md))
    filename = f"Python_{version_safe}_documentation.html"
    print("Write HTML docs to file:", filename)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    imported_modules = import_modules()
    total_md = export_documentation(imported_modules)
    write_to_file(total_md)

if __name__ == "__main__":
    main()