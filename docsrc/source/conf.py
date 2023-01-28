#!/usr/bin/env python3
# isort: skip_file
# -*- coding: utf-8 -*-
#
# documentation build configuration file, created by
# sphinx-quickstart on Sat Aug  3 16:59:37 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import datetime
import warnings

sys.path.insert(0, os.path.abspath('../..'))
import conf
import version as vs
from docsrc.directives.auto_summary import AutoSummaryNameOnly


_package_version = vs.get_version()

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx_autodoc_typehints',
    'sphinx_paramlinks',
    'sphinx_material',
    'sphinx_gallery.gen_gallery',
    'sphinx_copybutton',
    'myst_parser',
]

# Options for sphinx_autodoc_typehints
set_type_checking_flag = False

# Options for sphinx.ext.autosummary
autodoc_default_flags = ['members']
autosummary_generate = True
# List any packages that should be mocked here
autodoc_mock_imports = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = conf.PACKAGE_NAME
copyright = f'{datetime.datetime.now().year}, Nick DeRobertis'
author = "Nick DeRobertis"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = _package_version
# The full version, including alpha/beta/rc tags.
release = _package_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Base URL for sitemap
html_baseurl = "https://nickderobertis.github.io/py-finstmt" + '/'

sphinx_gallery_conf = {
    'examples_dirs': '../../_examples',   # path to your example scripts
    'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
    'filename_pattern': '/',  # re to match examples .py files that should be run to generate output. Set as / for all
    'reference_url': {
        # The module you locally document uses None
        'sphinx_gallery': None,
    },
    'binder': {
         # Required keys
         'org': "nickderobertis",
         'repo': "py-finstmt",
         'branch': 'gh-pages',  # Can be any branch, tag, or commit hash. Use a branch that hosts your docs.
         'binderhub_url': 'https://mybinder.org',  # Any URL of a binderhub deployment. Must be full URL (e.g. https://mybinder.org).
         'dependencies': './binder/requirements.txt',
         # Optional keys
         # 'filepath_prefix': '<prefix>', # A prefix to prepend to any filepaths in Binder links.
         # 'notebooks_dir': '<notebooks-directory-name>', # Jupyter notebooks for Binder will be copied to this directory (relative to built documentation root).
         'use_jupyter_lab': True, # Whether Binder links should start Jupyter Lab instead of the Jupyter Notebook interface.
     }
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'matplotlib': ('https://matplotlib.org', None)
}

# Remove matplotlib agg warnings from generated doc when using plt.show
warnings.filterwarnings("ignore", category=UserWarning,
                        message='Matplotlib is currently using agg, which is a'
                                ' non-GUI backend, so cannot show the figure.')

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = dict(
    nav_title=project,
    base_url="https://nickderobertis.github.io/py-finstmt",
    color_primary='indigo',
    color_accent='deep-purple',
    logo_icon='&#xe869',
    repo_url="https://github.com/nickderobertis/py-finstmt",
    repo_name="py-finstmt",
    globaltoc_depth=3,
)
if conf.GOOGLE_ANALYTICS_TRACKING_ID:
    html_theme_options['google_analytics_account'] = conf.GOOGLE_ANALYTICS_TRACKING_ID

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        "logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"
    ]
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#

# Uncomment the following line once logo url is set in main conf.py
# html_logo = str(pathlib.Path('_static') / 'images' / 'logo.svg')


# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#

# Uncomment the following line once logo url is set in main conf.py
# html_favicon = str(pathlib.Path('_static') / 'images' / 'logo.svg')


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'helpdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, f'{conf.PACKAGE_NAME}.tex', f'{conf.PACKAGE_NAME} Documentation',
     "Nick DeRobertis", 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, conf.PACKAGE_NAME, f'{conf.PACKAGE_NAME} Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, conf.PACKAGE_NAME, f'{conf.PACKAGE_NAME} Documentation',
     author, conf.PACKAGE_NAME, "Contains classes to work with financial statement data. Can calculate free cash flows and help project financial statements.",
     'Miscellaneous'),
]


def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)
    app.add_directive('autosummarynameonly', AutoSummaryNameOnly)