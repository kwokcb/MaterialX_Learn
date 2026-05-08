import pkgutil
import importlib
import os

# Output directory for .rst files (assume script is run from sphinx/)
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Try to import the top-level MaterialX package
try:
    import MaterialX
except ImportError:
    print("MaterialX package not found. Please ensure it is installed and available in PYTHONPATH.")
    exit(1)

# Find all submodules in MaterialX
submodules = [name for _, name, _ in pkgutil.iter_modules(MaterialX.__path__)]

# Always include the top-level MaterialX
modules = ["MaterialX"] + [f"MaterialX.{name}" for name in submodules]

for modname in modules:
    rst_filename = os.path.join(OUTPUT_DIR, modname.split('.')[-1] + ".rst")
    with open(rst_filename, "w") as f:
        title = f"{modname} Module"
        f.write(title + "\n" + "=" * len(title) + "\n\n")
        f.write(f".. automodule:: {modname}\n")
        f.write("    :members:\n")
        f.write("    :undoc-members:\n")
        f.write("    :show-inheritance:\n")
        f.write("    :inherited-members:\n")
    print(f"Wrote {rst_filename}")

# Optionally, generate a modules.rst toctree
modules_rst = os.path.join(OUTPUT_DIR, "modules.rst")
with open(modules_rst, "w") as f:
    f.write("MaterialX Python Modules\n=======================\n\n.. toctree::\n   :maxdepth: 1\n\n")
    for modname in modules[1:]:
        f.write(f"   {modname.split('.')[-1]}\n")
print(f"Wrote {modules_rst}")

# Also generate api.rst with all modules in a single file
api_rst = os.path.join(OUTPUT_DIR, "api.rst")
with open(api_rst, "w") as f:
    f.write("MaterialX Python API Reference\n=============================\n\n")
    for modname in modules:
        f.write(f".. automodule:: {modname}\n")
        f.write("    :members:\n")
        f.write("    :undoc-members:\n")
        f.write("    :show-inheritance:\n")
        f.write("    :inherited-members:\n\n")
print(f"Wrote {api_rst}")
