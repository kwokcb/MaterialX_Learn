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
html_logo = "_static/logo3d_2_small.png"

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
#}

#html_theme_options = {

    "footer_icons": [

        {
            "name": "GitHub",
            "url": "https://github.com/kwokcb/MaterialX_Learn",
            "html": """
                <svg stroke="currentColor" fill="currentColor"
                     stroke-width="0" viewBox="0 0 16 16">
                    <path d="M8 0C3.58 0 0 3.58 0 8
                    c0 3.54 2.29 6.53 5.47 7.59
                    .4.07.55-.17.55-.38
                    0-.19-.01-.82-.01-1.49
                    -2.01.37-2.53-.49-2.69-.94
                    -.09-.23-.48-.94-.82-1.13
                    -.28-.15-.68-.52-.01-.53
                    .63-.01 1.08.58 1.23.82
                    .72 1.21 1.87.87 2.33.66
                    .07-.52.28-.87.51-1.07
                    -1.78-.2-3.64-.89-3.64-3.95
                    0-.87.31-1.59.82-2.15
                    -.08-.2-.36-1.02.08-2.12
                    0 0 .67-.21 2.2.82
                    .64-.18 1.32-.27 2-.27
                    .68 0 1.36.09 2 .27
                    1.53-1.04 2.2-.82 2.2-.82
                    .44 1.1.16 1.92.08 2.12
                    .51.56.82 1.27.82 2.15
                    0 3.07-1.87 3.75-3.65 3.95
                    .29.25.54.73.54 1.48
                    0 1.07-.01 1.93-.01 2.2
                    0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8
                    c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },

        {
            "name": "MaterialX Website",
            "url": "https://materialx.org",
            "html": """
                <img src="https://materialx.org/images/MaterialXLogoSmallA.png" alt="MaterialX" style="width: 20px; height: 20px;"/>
            """,
            "class": "",
        },
    ],
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
