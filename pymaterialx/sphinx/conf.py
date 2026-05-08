# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'MaterialX 1.39.5 Python API'
copyright = '2026, MaterialX Authors'
author = 'MaterialX Authors'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

autodoc_typehints = 'description'

# -- Options for autodoc -----------------------------------------------------
autodoc_mock_imports = []

# -- Options for HTML output -------------------------------------------------
#html_theme = sphinx_rtd_dark_mode' 
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    "style_external_links": True,
    "style_nav_header_background": "#222",
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False
#    "dark_mode": True,
}

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.inheritance_diagram',
    'sphinx_rtd_dark_mode'
]

# -- Graphviz and inheritance-diagram settings ------------------------------
# Use SVG for high-quality, scalable diagrams
graphviz_output_format = 'svg'
graphviz_dot_args = ['-Gdpi=200']
inheritance_graph_attrs = dict(dpi='200')

# -- MaterialX autodoc settings ----------------------------------------------
# Use the installed MaterialX package (not local source)
import importlib.util
spec = importlib.util.find_spec('MaterialX')
if spec is not None and spec.submodule_search_locations:
    sys.path.insert(0, spec.submodule_search_locations[0])
