# sphinx-markdown-checkbox

Inspired by [sphinx-markdown-tables](https://github.com/ryanfox/sphinx-markdown-tables), 
this project renders markdown checkboxes as HTML using [pycmarkgfm](https://github.com/zopieux/pycmarkgfm),
because [Recommonmark](https://github.com/rtfd/recommonmark) does not support markdown checkboxes.

## Installation

    pip install sphinx-markdown-checkbox

## Usage

### If you have installed recommonmark
Add `sphinx_markdown_checkbox` to `extensions` in `conf.py`, like so:

    extensions = [
        'sphinx_markdown_checkbox',
    ]

### Otherwise
Sphinx needs to be configured to use markdown. First, you need `recommonmark`:

    pip install recommonmark

In `conf.py`, configure `source_parsers` and `source_suffix`:

    source_parsers = {
        '.md': 'recommonmark.parser.CommonMarkParser',
    }

    source_suffix = ['.rst', '.md']

Once Sphinx is configured appropriately, add `sphinx_markdown_checkbox` to `extensions`, like so:

    extensions = [
        'sphinx_markdown_checkbox',
    ]

For more information on Sphinx and markdown, see the
[Sphinx documentation.](http://www.sphinx-doc.org/en/master/usage/markdown.html)

## License
This project is available under the GPLv3 license.
