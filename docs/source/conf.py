# conf.py — thz-fmcw-dsp DSP reference
# Author: Luis Viveros · May 2026

project   = "thz-fmcw-dsp"
copyright = "2026, Luis Viveros"
author    = "Luis Viveros"
release   = "1.0"
version   = "1.0"

extensions = [
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
    "myst_parser",
]

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "logo_only":                    False,
    "display_version":              True,
    "prev_next_buttons_location":   "bottom",
    "style_external_links":         True,
    "collapse_navigation":          False,
    "sticky_navigation":            True,
    "navigation_depth":             4,
}
html_static_path     = ["_static"]
html_css_files       = ["custom.css"]
html_show_sphinx     = False
html_show_sourcelink = False

master_doc       = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix    = {".rst": "restructuredtext", ".md": "markdown"}
templates_path   = ["_templates"]
pygments_style   = "monokai"

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

copybutton_prompt_text = r"^\$ |>>> "
copybutton_prompt_is_regexp = True
