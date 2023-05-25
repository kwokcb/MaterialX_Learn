# Python MaterialX Workspace

This folder can be used as a workspace for running MaterialX via Python. 

There are various example `(.ipynb)` files which correspond to
tutorials (Jupyter notebooks) on the learning site. The corresponding html and python files are generated from those notebooks. MaterialX and other support file types are included.

The files are targeted for usage with Visual Studio Code with appropriate extensions installed to run in a Python virtual environment. Other editors can be used as desired. These notebooks can be used as is or published to something like a `Github Codespaces` or `Google Colab`. 

The notebooks are not "published" as yet due to lack of a `PyPi` package for MaterialX (note that at time of writing this is in the works).

Dependent packages used in the notebooks are not installed within the notebooks. They can be installed from `PyPi` as needed (e.g, Usd and Blender packages) 

All notebooks currently have been tested with Python 3.10 and 3.9.

## Support Files

* Utilities used for tutorials are packaged in the [mtlxutils](mtlxutils) folder.
* Data files used for tutorials are in the [data](data) folder.
* As of MaterialX 1.38.7 definition libraries are part of the Python package. 
* The [videos](vidoes) folder will contain videos for tutorials. Currently a Python / Visual Studio code setup video is included.

## Additional Utilities

Some stand-alone utilities are available which package up notebook logic, or additional logic. This includes:

* usd_mtlx.py : Usd to MaterialX sample converter. Logic used in the [Usd / MaterialX notebookx](./mtlx_usd_notebook.ipynb)
* blender_mtlx.py : Blender material to MaterialX / GLTF converter. Logic for bespoke conversion as shown in the [Blender notebook](./blender_export_mtlx_noui.ipynb)

As with notebooks, additional utilities will be made available over time, if not added as part of the core MaterialX distribution. This includes scripts used to generate the site's contents such as the definition reference library. 


