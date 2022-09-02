# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('sphinxext'))


# -- Project information -----------------------------------------------------

project_namecode = u'entrenamiento.python_basico'
project_short_name = u'programación en Python - Nivel básico'
project = project_short_name[0].capitalize() + project_short_name[1:39]
project_name = project_namecode.replace(".", "")
project_details = u'Materiales del entrenamiento de {0}'.format(project_short_name)
publisher = u'Covantec R.L.'
years= u'2014 - 2019'
copyright = u'{0}, {1}'.format(years, publisher)
author = u'Leonardo J. Caballero G.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version
version = u'0.2'
# The full version, including alpha/beta/rc tags
release = u'0.2'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive'
]

# Options for the linkcheck builder
# Ignore localhost
linkcheck_ignore = [
    r'http://localhost:\d+/',
    r'http://localhost:8080\d+/',
    r'http://localhost:8080',
    r'http://127.0.0.1:8080',
    r'http://whatever.herokuapp.com',
    r'http://example.com/news',
    r'http://example.com\d+/',
]
linkcheck_anchors = False
linkcheck_timeout = 30

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = u'es'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%d de %B de %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['index_latex.rst']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# A string of reStructuredText that will be included at the end of every 
# source file that is read. 
rst_epilog = """
.. _`CodigoFacilito.com`: https://codigofacilito.com/
.. |psf| replace:: Python Software Foundation
"""

# If true, figures, tables and code-blocks are automatically numbered if 
# they have a caption.
numfig = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
  'logo_name': True,
  'description': 'Nivel basico',
  'github_user': 'Covantec',
  'github_repo': 'entrenamiento.python_basico',
  'github_banner': True,
  'github_type': 'follow',
  'github_count': False,
  'show_powered_by': False,
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project_details

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = project_short_name[0].capitalize() + project_short_name[1:39]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_images/covantec_logo_html.jpg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_images', '_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d de %B de %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = '{0}doc'.format(project_name)


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # "inputenc" package inclusion, default '\\usepackage[utf8]{inputenc}'.
    'inputenc': r'''
    \usepackage[utf8]{inputenc}
    ''',

    # "fontenc" package inclusion, default '\\usepackage[T1]{fontenc}'.
    # 'fontenc': r'''
    # \usepackage[T1]{fontenc}
    # ''',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
    \usepackage{pmboxdraw}
    \authoraddress{
      \strong{Covantec R.L., Santa Cruz de Mara, Mara, Zulia. 4046.}\\
      \strong{Telf.} +58-414-979.80.83 / +58-426-771.35.73 / +58-262-879.18.80\\
      \strong{Contactos:} \email{covantec.ve@outlook.com} - 
      \url{https://github.com/Covantec/}
    }
    \let\Verbatim=\OriginalVerbatim
    \let\endVerbatim=\endOriginalVerbatim
    ''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',

    # Additional footer content (before the indices), default empty.
    # 'footer': 'Asociación Cooperativa Vanguardista Tecnológica - Covantec R.L.'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, project_name + ".tex", project_details, author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_images/covantec_logo_pdf.jpg'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# Documents to append as an appendix to all manuals.
latex_appendices = ['esquema', 'lecturas', 'apendices/operadores', 'apendices/anexos', 'glosario', 'licencia']

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [
#     (master_doc, project_name, project_details,
#      [author], 1)
# ]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, project_name, project_details, author,
   project_name, project_details,
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = ['apendices/operadores', 'glosario','licencia']

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project_details
epub_author = author
epub_publisher = publisher
epub_copyright = u'{0}, {1}'.format(years, author)

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
epub_language = language

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#
# epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#
# epub_tocdepth = 3

# Allow duplicate toc entries.
#
# epub_tocdup = True


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
# Add mappings
# https://kev.inburke.com/kevin/sphinx-interlinks/
intersphinx_mapping = {
#    'urllib3': ('http://urllib3.readthedocs.org/en/latest', None),
#    'python3': ('https://docs.python.org/3.7/', None)
    'python2': ('https://docs.python.org/2.7/', None)
}
intersphinx_timeout = 120

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# If true, ....
todo_emit_warnings = False

# -- Options for main setup --------------------------------------------------

# def setup(app):
#     from sphinx.util.texescape import tex_replacements
#    print tex_replacements
#    tex_replacements.append((u"’", u"'"))
#    tex_replacements.remove((u"’", r"'"))
#    tex_replacements.remove(('─', r'-'))
#    tex_replacements.remove(('│', r'\textbar{}'))
