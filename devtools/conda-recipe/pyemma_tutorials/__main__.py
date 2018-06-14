import os
import sys

def notebook_location():
    import pkg_resources
    d = pkg_resources.resource_filename('pyemma_tutorials', 'notebooks')
    print(d)
    assert os.path.isdir(d)
    return d


def main():
    from notebook.notebookapp import main as main_
    # main eats, argv list and kwargs
    notebook_cfg = ''
    argv = ['--config=%s' % notebook_cfg, notebook_location()]
    kw = dict()
    print('argv:', argv, '\tkw:', kw)
    main_(argv=argv, **kw)


if __name__ == '__main__':
    main()
