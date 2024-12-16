## Hosting Jupyter Notebooks

There are various ways to host Jupyter notebooks on a server. In this section we will only
cover two options:

1. [Github Codespaces](#1-hosting-using-github-codespaces)
2. [Google Colab](#2-hosting-using-google-colab)

At time of writing the recommended option is using `Github Codespaces`.

### 1. Hosting Using Github Codespaces

Github Codespaces is a feature available to all tiers of Github users for individuals and organizations.

(At time of writing). Codespaces are hosted on a `Linux` environment running `Ubuntu`. Also a default Python version is used as the interpreter (e.g. 3.10.8).

It is possible to change the interpreter inside the  [devcontainer.json](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces) 
file in the `.devcontainer` folder. It is also possible create a virtual environment and chose a Python version as the interpreter.

The current MaterialX package has been tested to run on this configuration, but **it is advisable to check other packages for compatibility**. 

This section will cover a small subset of functionality to get started. For more information please refer to the [Github Codespaces documentation](https://docs.github.com/en/codespaces/overview).

To run the notebooks on this site the simplest approaches are:

1. Fork the MaterialX Elements repository so that a codespace can be created on the fork. This will allow you to edit the notebooks and push changes back to your fork. 

2. Create your own repository and code space and copy over the notebooks of interest from the `pymaterialx` folder. Note that some notebooks use the utility scripts found in the `mtlxutils` folder. It is thus advisable to copy over this subfolder as well. 

#### 1.1 Sample Repository

An example Github repository with the notebooks and utility scripts can be found [here](https://github.com/kwokcb/MaterialX_Learn_Sample_Codespace)

- The [devcontainer.json](https://github.com/kwokcb/MaterialX_Learn_Sample_Codespace/blob/main/.devcontainer/devcontainer.json) file includes a startup command to install package dependencies from the [requirements.txt](https://github.com/kwokcb/MaterialX_Learn_Sample_Codespace/blob/main/requirements.txt).

- This file includes minimally the IPython and MaterialX packages. 

#### 1.2 Adding a Codespace

To add a codespace to your repository, click on the `Code` button and select `New Codespace` from the dropdown menu.

Below is an example of a codespace creation for the sample repository using `main` branch. 
    
<img width="30%" src="images/create_codespace_github.png">

By default a "randomly" named new codespace is created with default options. It is possible to also create with custom options by using the "..." button. The codespace can be renamed after creation.

Also by default a `Visual Studio Code for Web` is used as the editor. This can be modified from your Github Settings for `CodeSpaces`

<img width="60%" src="images/create_codespace_github_editor_prefs.png">


#### 1.3 Using a Codespace

<img width="100%" src="images/create_codespace_github_2.png">

If using the Visual Studio Code for Web editor, the editor is pretty well the same as the desktop version.

From here it is possible to modify, add / remove content as desired, and push changes back to the repository.

It is possible to sync the the Web editor with the desktop editor as desired. Additional extensions can be installed as desired. For example for the JSON notebook the `JSONcrack` extension was installed.

<img width="100%" src="images/codespace_extension.png">

#### 1.4 Python Packages

Some Python packages are pre-installed in the codespace.
To check what is already available the terminal window can be opened and the `pip list` command can be used.

<img width="100%" src="images/codespace_packages.png">

If additional Python packages are required they can be installed inside a notebook, or in a terminal window. For example the `OpenUsd` package can be installed using: `pip install usd-core`.

<img width="100%" src="images/codespace_usd_install.png">

If the package is general to many notebooks  the `requirements.txt`` file can be modified and the codespace restarted.

As the MaterialX Package is loaded on startup, notebooks using this package can be run without any additional installation.

#### 1.5 GPU Rendering

At time of writing it does not seem possible to render images using a GPU, though this has not been investigated in detail. As the "rendering notebook" uses OpenGL on Linux, it the rendering of images using notebook is not currently possible in a Codespace environment. It is unknown if MSL will work as a Apple OS environment is not available.

### 2. Hosting Using Google Colab

Unlike codespaces, an entire environment setup does not seem possible with performing a number extra steps. This is especially true if there is dependent resources required and to share the notebook.

#### 2.1 Browser Access

A quick way to examine any notebook is to use the <a href="https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo" target="_blank">Open in Colab Chrome extension</a>. 

This option however fails to work well for execution when context data or utility scripts are required as only that file is available.

#### 2.2 Github Repository Usage

It is possible to access both private and public Github repositories using Colab via <a href="https://colab.research.google.com/github/" target="_blank">this browser link</a>.

<img src="./images/colab_github_notebook_access.png" width="60%">

To use the repo with extra steps for authentication the repo containing the notebooks can be `clone`d into the Colab environment. This is done by running the following Colab cell:

```python
# Clone the repo
!git clone <address of Github repository>
```

For this example the repository is `https://github.com/kwokcb/MaterialX_Learn_Sample_Codespace`, and the notebook is `mtlx_json_nootbook.ipynb`. 

This is also "safe" in the sense that a user of this notebook is not able to save back to the original repository.

After this is done, the current folder can be changed to the root where the notebook resides in order to execute it using the following cell:

```python
# Set the current folder to point to the appropriate folder.
import os
os.chdir('MaterialX_Learn_Sample_Codespace/notebooks') 
```

where `MaterialX_Learn_Sample_Codespace/notebooks` is the path folder containing the notebook.

Below is a snapshot of the loaded notebook after the clone and folder change is executed.
<img src="images/colable_github_setup.png" width="100%">

Note that notebooks in the learning site may require: 
1. Python utilities found in the `mtlxutils` sub-folder 
2. Resource files found in the `data` sub-folder

##### 2.2.1 Github File Access Via URI

It is possible to access individual files from Github if the URI is known. Note that the MaterialX file access API does not directly support network access and thus something like the `urlib` module must be used.

For an example of this see the 
<a href="../pymaterialx/mtlx_basics_notebook.html" target="_blank">Basics notebook</a>

#### 2.3 Google Drive Usage

If sharing is **not** required and "write" privileges make be required then the notebook and dpendendt files can also be uploaded to `Google Drive` and opened in Colab from there. 

Below is an example of same repository copied to Google Drive and opened from there.

<img src="./images/google_drive_colab.png" width="60%">

To use the notebook Google Drive must be explicitly mounted using the following cell:

```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')
```

The current folder can then be changed to location of the notebook.

#### 2.4 Installing Package Dependencies

At time of writing there unfortunately appears to be nothing equivalent in `Colab` to the "dev container" setup found in `Codespace`s.

Thus it is necessary to install the `MaterialX`` or any other package dependencies from within each notebook. For example to use MaterialX the follow cell can be added to the notebook:

```python
# Install MaterialX from PyPi
!pip install MaterialX
```









