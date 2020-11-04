import re

import pycmarkgfm

__version__ = '0.1.0'


def setup(app):
    app.connect('source-read', process_checkbox)
    return {'version': __version__,
            'parallel_read_safe': True}


def process_checkbox(app, docname, source):
    """
    Convert markdown checkboxes to html, since recommonmark can't. This requires 3 steps:
        Snip out checkboxes sections from the markdown
        Convert them to html
        Replace the old markdown checkboxes with an html

    This function is called by sphinx for each document. `source` is a 1-item list. To update the document, replace
    element 0 in `source`.
    """
    pat = re.compile(r'((?:{0}.+?\n)+)'.format(r'\s*[-*]\s\[[\sxX]\]\s'))
    blocks = pat.split(source[0])

    for i, block in enumerate(blocks):
        if pat.search(block):
            html_str = pycmarkgfm.gfm_to_html(block).replace(
                # Removing circles before checkboxes
                '<li', '<li style="list-style-type:none"'
            ).replace('<p>', '').replace('</p>', '')
            blocks[i] = '\n' + html_str + '\n'

    # re-assemble into markdown-with-tables-replaced
    # must replace element 0 for changes to persist
    source[0] = ''.join(blocks)
