import os
import pkg_resources


def notebook_location():
    d = pkg_resources.resource_filename('pyemma_tutorials', 'notebooks')
    assert os.path.isdir(d)
    return d


def main():
    from notebook.notebookapp import main as main_
    # main eats, argv list and kwargs
    notebook_cfg = pkg_resources.resource_filename('pyemma_tutorials', 'jupyter_notebook_config.py')
    assert os.path.exists(notebook_cfg)
    argv = ['--config=%s' % notebook_cfg, ]
    main_(argv=argv)


if __name__ == '__main__':
    main()
