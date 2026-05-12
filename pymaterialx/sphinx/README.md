### Build Instructions

To build the documentation, you will need to have `Sphinx` and `MaterialX` installed.  In addition a number of Sphinx extensions are used. All packages
are listed in the `requirements.txt` file. You can install them using pip:

```bash
pip install -r requirements.txt
```

The shell script `setup.sh` includes setting up a Python virtual environment and installing the required packages. You can run it using:

```bash
source setup.sh setup
```

Once the environment is setup, the `build_it.sh` script can be used to build the documentation. It will generate RST files used by Sphinx and then generate the HTML documentation. You can run it using:

```bash
source build_it.sh
```

The environment can be cleanuped up using:

```bash
source setup.sh cleanup
```

#### Acknowledgments

MaterialX is developed and maintained by the `Academy Software Foundation` and its contributors. All content was created by the contributors to the MaterialX project.



