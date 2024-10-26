# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ejemplo1'
copyright = '2024, nerea mr'
author = 'nerea mr'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# estas dos líneas siguientes de código son librerías necesarias de python para documentar, sin ellos, la siguiente línea no podría usarse
import os
import sys
# esta línea de código es para indicarle a sphinx dónde buscar los documentos para documentar
sys.path.insert(0, os.path.abspath('..'))

# esta extensión va a permitir la generación de documentación a partir de los docstrings
extensions = ['sphinx.ext.autodoc']