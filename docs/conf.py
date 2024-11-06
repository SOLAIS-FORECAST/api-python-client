# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

import toml

sys.path.insert(0, os.path.abspath(".."))


def get_project_info():
    with open(os.path.abspath(os.path.join("..", "pyproject.toml")), "r") as file:
        pyproject_data = toml.load(file)
    project_info = pyproject_data.get("project")
    return project_info


project_info = get_project_info()
print(project_info)
project = project_info.get("name", "calibsunapi")
author = project_info.get("authors")[0]["name"]
release = project_info.get("version", "0.0.1")
copyright = "2024, Calibsun"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
