# Python MaterialX Workspace

This folder can be used as a workspace for using MaterialX via Python. There are various example `(.ipynb)` files which correspond to
tutorials (Jupyter notebooks) on the learning site. The corresponding html and python files are generated from those notebooks.
MaterialX and other support files are included as well.

The files are targeted for usage with Visual Studio code with appropriate plug-ins installed to run in a Python virtual environment but other
editors can be used as desired. These can be used as is or published to something like a github codespace or Google Colab. 

The notebooks are not "published" as yet due to lack of a PyPi package for MaterialX (note that at time of writing this is in the works).
Dependent packages currently available such as
Usd can be installed as needed with the target
Python version being 3.9 and above.

* Utilities used for tutorials are packaged in the [mtlxutils](mtlxutils/README.md) folder.
* Data files used for tutorials are in the [data](data) folder.
* MaterialX code is in the [libraries](libraries) folder. The appropriate version can be placed here as desired.


