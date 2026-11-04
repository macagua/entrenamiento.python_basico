# Sphinx Python Documentation Skill

> **Quick Reference Guide**

## Overview

Generate professional Python documentation with Sphinx. Automatic API docs from docstrings, multiple output formats, and Read the Docs integration.

**Version**: 1.0.0
**Category**: Documentation
**Platforms**: Linux, macOS, Windows

## Quick Start

### 1. Installation

```bash
pip install sphinx sphinx-rtd-theme sphinx-autodoc-typehints
```

### 2. Initialize Project

```bash
sphinx-quickstart docs
```

### 3. Configure (conf.py)

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
]

html_theme = 'sphinx_rtd_theme'

autodoc_default_options = {
    'members': True,
    'show-inheritance': True,
}
```

### 4. Generate API Docs

```bash
sphinx-apidoc -o docs/source/api src/mypackage -f -e
```

### 5. Build Documentation

```bash
sphinx-build -b html docs/source docs/build/html
```

## Key Features

- **Autodoc** - Extract documentation from Python docstrings
- **Napoleon** - Google and NumPy docstring support
- **Intersphinx** - Cross-reference external documentation
- **Multiple Formats** - HTML, PDF, ePub, man pages
- **MyST** - Write docs in Markdown
- **Read the Docs** - Easy cloud deployment

## Docstring Style

```python
def process(data: list, validate: bool = True) -> dict:
    """
    Process input data.

    Args:
        data: Input data to process.
        validate: Enable validation. Defaults to True.

    Returns:
        Dictionary with processed results.

    Raises:
        ValueError: If data is empty.
    """
    pass
```

## When to Use

**USE for**: Python API docs, library documentation, scientific papers
**AVOID for**: Simple project docs (use MkDocs), non-Python projects

## Output Formats

| Format | Command |
|--------|---------|
| HTML | `sphinx-build -b html source build/html` |
| PDF | `sphinx-build -b latex source build/latex && make` |
| ePub | `sphinx-build -b epub source build/epub` |

## Files

```
sphinx/
├── SKILL.md      # Full documentation (900+ lines)
└── README.md     # This quick reference
```

## Related Skills

- **mkdocs** - Simple project documentation
- **pandoc** - Document format conversion
- **docusaurus** - React-based documentation

## Resources

- [Sphinx Docs](https://www.sphinx-doc.org/)
- [Read the Docs](https://docs.readthedocs.io/)
- [Napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)

---

See `SKILL.md` for complete autodoc configuration, custom extensions, and deployment workflows.
