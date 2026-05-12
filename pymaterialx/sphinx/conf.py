# -- Path setup --------------------------------------------------------------

import os
import sys
import importlib.util

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'MaterialX 1.39.5 Python API'
copyright = '2026, MaterialX Authors'
author = 'MaterialX Authors'

# -- General configuration ---------------------------------------------------

extensions = [
    # Core Sphinx
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.inheritance_diagram',

    # Better typing support
    'sphinx_autodoc_typehints',

    # Modern UI enhancements
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_togglebutton',

    # Mermaid diagrams
    'sphinxcontrib.mermaid',

    # Markdown support
    'myst_parser',
]

# -- Autodoc configuration ---------------------------------------------------

autodoc_typehints = 'description'

autodoc_member_order = 'groupwise'

autoclass_content = 'both'

autodoc_inherit_docstrings = True

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'inherited-members': True,
}

# Mock imports if needed
autodoc_mock_imports = []

# -- Napoleon settings -------------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True

napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True

# -- Inheritance diagram settings --------------------------------------------
graphviz_output_format = 'svg'

# Higher DPI for sharper rendering
graphviz_dot_args = ['-Gdpi=200']

inheritance_graph_attrs = dict(
    rankdir="LR",
    fontsize=12,
    ratio='compress'
)

inheritance_node_attrs = dict(
    shape='box',
    fontsize=10,
    height=0.4,
    fontname='Arial'
)

# -- Mermaid configuration ---------------------------------------------------

mermaid_version = "10.9.0"

mermaid_init_js = """
mermaid.initialize({
    startOnLoad: true,
    theme: "default",
    securityLevel: "loose",
    flowchart: {
        useMaxWidth: true,
        htmlLabels: true
    }
});
"""

# -- MyST Markdown configuration ---------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    #"linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# -- Templates ---------------------------------------------------------------

templates_path = ['_templates']

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]

# -- HTML output -------------------------------------------------------------

html_theme = 'furo'

html_title = project

html_show_sphinx = False

html_copy_source = False

html_show_sourcelink = True

html_static_path = ['_static']

html_css_files = [
    #'custom.css', -disable until really needed. Can break responsiveness.
]

html_favicon = "_static/logo3d_2_small.png"

html_theme_options = {
    # Keyboard navigation
    "navigation_with_keys": True,

    # GitHub integration
    #"source_repository": "https://github.com/AcademySoftwareFoundation/MaterialX/",
    #"source_branch": "main",
    #"source_directory": "docs/",

    # Light mode colors
    "light_css_variables": {
        "color-brand-primary": "#2563eb",
        "color-brand-content": "#2563eb",
    },

    # Dark mode colors
    "dark_css_variables": {
        "color-brand-primary": "#60a5fa",
        "color-brand-content": "#93c5fd",
    },
}

# -- Syntax highlighting -----------------------------------------------------

#pygments_style = "sphinx"
#pygments_dark_style = "monokai"
pygments_style = "vs"
pygments_dark_style = "native"

# -- Copybutton configuration ------------------------------------------------

copybutton_prompt_text = r">>> |\.\.\. "
copybutton_prompt_is_regexp = True

# -- Exclusion of certain modules from documentation --------------------------------
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',

    # Ignore virtual environments
    'venv',
    'venv/**',

    # Ignore Python cache
    '**/__pycache__',

    # Ignore installed packages
    '**/site-packages/**',

    # Ignore dist-info metadata
    '**/*.dist-info/**',
]

# -- MaterialX autodoc setup -------------------------------------------------

# Use installed MaterialX package instead of local source tree
spec = importlib.util.find_spec('MaterialX')

if spec is not None and spec.submodule_search_locations:
    sys.path.insert(0, spec.submodule_search_locations[0])
