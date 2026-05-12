import pkgutil
import os

# Output directory for .md files
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Try to import the top-level MaterialX package
try:
    import MaterialX
except ImportError:
    print("MaterialX package not found. Please ensure it is installed and available in PYTHONPATH.")
    raise SystemExit(1)

# Find all submodules in MaterialX
submodules = [name for _, name, _ in pkgutil.iter_modules(MaterialX.__path__)]

# Always include top-level module
modules = ["MaterialX"] + [f"MaterialX.{name}" for name in submodules]

# Modules to skip
SKIP_MODULES = {
    "MaterialX._scripts",
}

# --------------------------------------------------------------------------
# Generate per-module markdown files
# --------------------------------------------------------------------------

for modname in modules:

    if modname in SKIP_MODULES:
        continue

    print(f"> Processing module: {modname}")

    short_name = modname.split(".")[-1]
    md_filename = os.path.join(OUTPUT_DIR, f"{short_name}.md")

    with open(md_filename, "w", encoding="utf-8") as f:

        # Title
        f.write(f"# {short_name}\n\n")

        # Optional inheritance diagram
        f.write("```{eval-rst}\n")
        f.write(f".. inheritance-diagram:: {modname}\n")
        f.write("   :parts: 1\n")
        f.write("   :top-classes: object\n")
        f.write("```\n\n")

        # Automodule directive
        f.write("```{eval-rst}\n")
        f.write(f".. automodule:: {modname}\n")
        f.write("   :members:\n")
        f.write("   :undoc-members:\n")
        f.write("   :show-inheritance:\n")
        f.write("```\n")

    print(f">> Wrote {md_filename}")

# --------------------------------------------------------------------------
# Generate modules.md table of contents
# --------------------------------------------------------------------------

modules_md = os.path.join(OUTPUT_DIR, "modules.md")

with open(modules_md, "w", encoding="utf-8") as f:

    f.write("# MaterialX Python Modules\n\n")

    f.write("```{toctree}\n")
    f.write(":maxdepth: 1\n\n")

    for modname in modules[1:]:

        if modname in SKIP_MODULES:
            continue

        short_name = modname.split(".")[-1]
        f.write(f"{short_name}\n")

    f.write("```\n")

print(f"> Wrote {modules_md}")


# --------------------------------------------------------------------------
# Generate api.md with all modules in one file
# --------------------------------------------------------------------------

build_api_md = False

if build_api_md:

    api_md = os.path.join(OUTPUT_DIR, "api.md")

    with open(api_md, "w", encoding="utf-8") as f:

        f.write("# MaterialX Python API Reference\n\n")

        for modname in modules:

            if modname in SKIP_MODULES:
                continue

            short_name = modname.split(".")[-1]

            # Section title
            f.write(f"## {short_name}\n\n")

            # Inheritance diagram
            f.write("```{eval-rst}\n")
            f.write(f".. inheritance-diagram:: {modname}\n")
            f.write("   :parts: 1\n")
            f.write("   :top-classes: object\n")
            f.write("```\n\n")

            # Automodule
            f.write("```{eval-rst}\n")
            f.write(f".. automodule:: {modname}\n")
            f.write("   :members:\n")
            f.write("   :undoc-members:\n")
            f.write("   :show-inheritance:\n")
            f.write("```\n\n")

    print(f"> Wrote {api_md}")