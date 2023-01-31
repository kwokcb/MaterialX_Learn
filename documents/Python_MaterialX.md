## Python MaterialX in Visual Studio Code 

A simple environment can be set up to test using the Python MaterialX API
within Visual Studio Code.

### Virtual Environment Setup

First a virtual environment can be set up to run Python, following the instructions found [here](https://code.visualstudio.com/docs/python/environments).

`Ctrl+Shift+P` can be used to run the command `Python: Create Environment`.
Choose to create a virtial environment vs a `Conda` environment, as well as pick the appropriate Pythong interpreter 
to use based on the version of Python used for the MaterialX modules.

A `.venv` folder will be created locally for the environment created.
Within there various Python packages can be added or removed as needed.
To this the MaterialX modules can be added.

### Adding MaterialX Modules

We will use a simple example file called `hello_materialx.py` to continue with.
Add this file to you workspace and attempt to run it. 

Running this file will return an error if the MaterialX modules are not added yet. 
```
import MaterialX as mx
ModuleNotFoundError: No module named 'MaterialX'
```

At the time of righting MaterialX is not available via `pip` (PySide), so must be installed
manually. The easiest way to do this is to go where MaterialX is installed and run the local
setup from within the workspace terminal. For example go to:
```
<install location>/python
```
and run the setup script
```
python setup.py install
```
This will add the MaterialX modules to the virtual environment under `.venv/Lib/site-packages`. The modules installed will depend on the ones found in the installation area.

<img src="./images/VSCode_PythonModules.png" style="width: 20%">

Other dependent packages can be added using `pip` or other means as necessary.

### Test Example

In general the "minimum" number of modules wil be loaded by importing the `MaterialX` module. This includes code functionality as well as file I/O.

At a minimum a document must be created as all operations are based on documents or document contents.

Thus to test that the environment works properly the test example creates a document checks the version of MaterialX.
```python
doc = mx.createDocument()
print('Hello MaterialX (Version %s)' % doc.getVersionString())    
```

### Minimal "Useful" Example

To do any useful operations, at least the standard libraries that come
with the installation need to be loadeded in. The `load_libraries.py`
file contains this minimal setup.
```python
# Assuming we are running from the install localtion for MaterialX
# This will loade in all files found under the `libraries` folder
# into a document called `stdlib`    
libraryPath = mx.FilePath('libraries')
stdlib = mx.createDocument()
searchPath = mx.FileSearchPath()
libFiles = mx.loadLibraries([ libraryPath ], searchPath, stdlib)

# Create main document and import the library document
doc = mx.createDocument()
doc.importLibrary(stdlib)
```
Note that the "standard" libraries are in the `libraries` folder in 
the installation location. The key interfaces used are:
* the `loadLibraries` utility to create a library document.
* the Document `importLibrary` method to import the libraries into
a working / main document.



