To riff a bit on Python environment. I'd like to put this out for feedback for what`
is a 'recommended' workflow for MaterialX Python package usage.

## 1 MaterialX Python Setup

If working from within an integrated environment with an existing Python package. e.g. a Usd integration or Blender distribution, use this package for compatibility reasons.

If there is no package or coding something that can use a different / newer MaterialX version:

1. Determine if you need to work with more than one Python version or a specific Python version. 
If so create a [virtual environment] (https://docs.python.org/3/library/venv.html) for each. 

   - *This is useful for development setups, or just in general to avoid polluting other projects or the system.*

   - For those using `VSCode` this is easy to set up. github `codespace` environments also support this. For both, you can choose the Python Interpreter version to use as well.

2. Install the desired MaterialX package using `pip install` (e.g. from the PyPi repository, via a downloaded package from the MaterialX github site, or a locally built package). 

## 2 MaterialX Python Data Libraries

### 2.1 Import MaterialX 
Packages can be referenced as needed. E.g.
```python
# Core, File I/O 
import MaterialX as mx

# Shader Generation
import MaterialX.PyMaterialXGenShader as mx_gen_shader
import MaterialX.PyMaterialXGenGlsl as mx_gen_glsl
import MaterialX.PyMaterialXGenOsl as mx_gen_osl
import MaterialX.PyMaterialXGenMdl as mx_gen_mdl
import MaterialX.PyMaterialXGenMsl as mx_gen_msl

# Rendering
from MaterialX import PyMaterialXRender as mx_render
from MaterialX import PyMaterialXRenderGlsl as mx_render_glsl
if platform == "darwin":
    from MaterialX import PyMaterialXGenMsl as ms_gen_msl
    from MaterialX import PyMaterialXRenderMsl as mx_render_msl
```

### 2.2 Version Checking
For version compatibility, check the MaterialX version using:
```python
major, minor, patch = mx.getVersionIntegers()
```
Note that this gives you the 3 integers: major, minor and patch. Use this to perform feature checking. Don't use the document version as this does
not include the patch version.

### 2.3 Accessing Package Location
In general, `sys.exec_prefix` can be used to find the root of where the Python packages are installed (under `libs/site-packages/`).
This can be used to access where `/MaterialX` reside. `sys.exec_prefix` will resolve properly whether using a virtual environment or not. 

If working in an existing environment it should hopefully have overridden this location (e.g. Blender does so you end up pointing to `C:\Program Files\Blender Foundation\Blender 3 5\3.5\python\lib\site-packages\MaterialX` for the 3.5 install of Blender).

### 2.4 Loading Libraries from Package Location (1.38.7)
MaterialX packages from 1.38.7 onward include standard data libraries within the package. Convenience functions `getDefaultDataSearchPath()` and `getDefaultDataLibraryFolders()` can be used in conjunction with `loadLibraries` to load in these libraries:
 
 ```python
 # Points to here the package resides
 searchPath = mx.getDefaultDataSearchPath()
 # Load libraries relative to this location
 mx.loadLibraries(mx.getDefaultDataLibraryFolders(), searchPath, doc)
 ```
 `sys.exec_prefix` can still be used if desired to find the same information.

### 2.5 Custom Libraries
Custom definitions (`nodedef`s) can be loaded via `loadLibraries`. It is up to the user / integration as to where these resides but it seems that it would be useful if they can be found under `sys.exec_prefix` which would be the case if included as part of a Python package.


