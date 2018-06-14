"""

"""
import os
import sys

def notebook_location():
    import pkg_resources
    d = pkg_resources.resource_dir('pyemma_tutorials', 'notebooks')
    assert os.path.isdir(d)
    return d


def main():
    from notebook.notebookapp import main as main_
    # main eats, argv list and kwargs
    argv = sys.argv + [os.getenv('PREFIX')]
    kw = dict()
    main_(argv=argv, **kw)
