## MaterialX Python Utilities

The Python package <a href="https://github.com/kwokcb/MaterialX_Learn/tree/main/pymaterialx/mtlxutils/" target="_blank">mtlxutils</a>
contains a collection of the utilities

This package is used in [Python command line
utilities](https://github.com/kwokcb/MaterialX_Learn/tree/main/pymaterialx) which can be of general use. A number of these are used in the *Github* actions workflow used to build this site as outlined in the
[Implementation](implementation.html) page.

-   **genMaterialsFromDefs.py** : For creation of nodegraphs based on definitions (nodedefs). "Sampling" of node outputs is accomplished by using new "convert" nodes introduced in 1.38.7 and forward.
-   **renderDocuments.py** : For rendering of renderable nodes in documents. This is used to render the graphs created by `genMaterialsFromDefs`. The renderer is the same as used for render unit testing for GLSL code generated shaders. The content can be found in the [resources folder](https://github.com/kwokcb/MaterialX_Learn/tree/main/resources/mtlx/nodedef_materials)
-   **generateMermaidGraph.py** : For creation Mermaid graphs from MaterialX node graphs. A variant of this (which includes additional node coloring) is used to generate the node reference documentation.
-   **createDefinitions.py** : For creation of definitions from node graphs.
-   **usd2Mtlx.py** : For converting to and from Usd / MaterialX node graphs.

Note: Additional package enhancements and command like utilities will be exposed over time once they are factored out into reusable modules. This includes the Python script used to generate all the node reference
documentation.

The minimum MaterialX package version is `1.38.8`.

The package and utilities are used (and explained) within the various Python [tutorials](https://kwokcb.github.io/MaterialX_Learn/documents/jupyter_example.html)

## Core Utilities

-   `mxbase` : Utility for minimum version checking.
-   `mxfile` : File utilities including: creating "working" documents, loading in default libraries, library write filter predicate, and write to file / string wrappers. Used by various notebooks. Logic described in the [Basics notebook](https://github.com/kwokcb/MaterialX_Learn/tree/main/pymaterialx/mtlx_basics_notebook.ipynb)
-   `mxodegraph` : Node and nodegraph creation as explained in the [Nodegraph notebook](https://github.com/kwokcb/MaterialX_Learn/tree/main/pymaterialx/mtlx_graphs_notebook.ipynb)
-   `mxtraversal` : Nodegraph introspection and sample usage to create `Mermaid` graphs as explained in the [Traversal notetbook](https://github.com/kwokcb/MaterialX_Learn/tree/main/pymaterialx/mtlx_traversal_notebook.ipynb)
-   `mxshadergen` : Utilities for shader generation as explained in the [Shader Generation Notebook](https://github.com/kwokcb/MaterialX_Learn/blob/main/pymaterialx/mtlx_shadergen_notebook.ipynb)
-   `mxrenderer` : Utilities for rendering with a default GLSL renderer as covered in the [Rendering Notebook](https://github.com/kwokcb/MaterialX_Learn/blob/main/pymaterialx/mtlx_render_notebook.ipynb)

## Supplemental Utilities

-   `mxusd` : MaterialX / Usd graphing mapping utilities as explained in the [MaterialX / Usd notebook](https://github.com/kwokcb/MaterialX_Learn/tree/main/pymaterialx/mtlx_usd_notebook.ipynb).
    Note that the Usd / MaterialX conversion logic is not included here as `UsdMtlx` from the the official Usd release should be used.
