# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Capital One Card Login Guide'
author = 'Capital One Help Blog'
copyright = '2025, Capital One Help'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_allow_unsafe = True  # Allow raw HTML in .rst or .md files

# -- HTML output settings ----------------------------------------------------

# Choose a theme
html_theme = 'alabaster'  # You can change to 'furo' or 'sphinx_rtd_theme' if available

# Website tab title and headline
html_title = "How to Log in and Activate Your Capital One Card"
html_short_title = "Capital One Card Guide"

# Optional favicon
html_favicon = 'favicon.ico'

# Hide "View page source" link on docs
html_show_sourcelink = False

# Theme customization (only applies to some themes like alabaster)
html_theme_options = {
    'description': "Step-by-step Capital One card login and activation guide with FAQs and user experience.",
    'show_powered_by': False,
    'sidebar_width': '240px',
    'page_width': '1024px',
}

# Uncomment below if you have a static folder (e.g., custom CSS, logos)
# html_static_path = ['_static']
