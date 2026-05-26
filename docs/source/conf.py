# conf.py — Sphinx configuration for fmcw-thz-radar-sim documentation
# Author: Luis Viveros · May 2026

import os

project   = "fmcw-thz-radar-sim"
copyright = "2026, Luis Viveros"
author    = "Luis Viveros"
release   = "0.2.0"
version   = "0.2"

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "myst_parser",
]

# ── ReadTheDocs theme ─────────────────────────────────────────────────────────
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "logo_only":                    False,
    "display_version":              True,
    "prev_next_buttons_location":   "bottom",
    "style_external_links":         True,
    "collapse_navigation":          False,
    "sticky_navigation":            True,
    "navigation_depth":             4,
    "includehidden":                True,
    "titles_only":                  False,
}
html_static_path     = ["_static"]
html_css_files       = ["custom.css"]
html_show_sphinx     = False
html_show_sourcelink = False

# ── General ───────────────────────────────────────────────────────────────────
master_doc       = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix    = {".rst": "restructuredtext", ".md": "markdown"}
templates_path   = ["_templates"]
pygments_style   = "monokai"

# ── MathJax ───────────────────────────────────────────────────────────────────
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# ── Intersphinx ───────────────────────────────────────────────────────────────
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# ── Copy button ───────────────────────────────────────────────────────────────
copybutton_prompt_text = r"^\$ |>>> "
copybutton_prompt_is_regexp = True
