# encoding: utf-8

import nbformat
import os
import re

def export(in_file, out_file):
    nb = nbformat.v4.new_notebook()
    with open(in_file, encoding='utf8') as fh:
        bibtex = fh.read()

    src = '<!--bibtex\n{bibtex}\n-->'.format(bibtex=bibtex)

    # remove bibdesk comments
    src = re.sub(pattern='@comment.*\{.*\}\}', repl='', string=src, flags=re.DOTALL)
    src = re.sub(pattern=r"\{\\'\{e\}\}", repl='é', string=src)
    src = re.sub(pattern=r"\{\\'\{a\}\}", repl='á', string=src)
    src = re.sub(pattern=r'\\"\{o\}', repl='ö', string=src)
    cell = nbformat.v4.new_markdown_cell(src)
    nb.cells.append(cell)

    with open(out_file, 'w', encoding='utf-8') as fh:
        nbformat.write(nb, fh)


if __name__ == '__main__':
    devtools_dir = os.path.abspath(os.path.dirname(__file__))
    in_file = os.path.join(devtools_dir, '../manuscript/literature.bib')
    out_file = os.path.join(devtools_dir, '../notebooks/Bibliography.ipynb')
    export(in_file, out_file)
