# MaterialX Utilities Collection

This package `mtlxutils` contains a collection of the utilities explained and used for Python tutorials. The minimum
MaterialX package version is `1.38.7`.

This includes:

* mxbase : Utility for minimum version checking.
* mxfile : File utilities including: creating "working" documents, loading in default libraries, library write filter predicate, and write to file / string wrappers. Used by various notebooks. Logic described in the [Basics notebook](../mtlx_basics_notebook.ipynb)
* mxodegraph : Node and nodegraph creation as explained in the [Nodegraph notebook](../mtlx_graphs_notebook.ipynb)
* mxtraversal : Nodegraph introspection and sample usage to create `Mermaid` graphs as explained in the [Traversal noetbook](../mtlx_traversal_notebook.ipynb) 
* mxusd : MaterialX / Usd graphing mapping utilities as explained in the [MaterialX / Usd notebook](../mtlx_usd_notebook.ipynb). Note that 
the Usd / MaterialX conversion logic is not included here as `UsdMtlx` from the the official Usd release should be used.

Additional utilities can be extracted from the notebooks if they are not available here.

> Note that a shader generation utility (`generateshader.py`) is part of the core distribution so is not included here.
