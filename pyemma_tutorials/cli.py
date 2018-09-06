
def _nglview_pip_installed_workaround():
    # This is a workaround for people having a pip installation of nglview. The XDG_DATA_DIR is being searched for the
    # javascript nbextensions. This would cause mixing up different versions of the widget.
    # Further info:
    # https://jupyter.readthedocs.io/en/latest/migrating.html?highlight=data-dir#finding-the-location-of-important-files
    # https://github.com/arose/nglview/issues/696#issuecomment-332850270
    # https://github.com/arose/nglview/issues/718#issuecomment-346041897
    import os
    os.environ['JUPYTER_DATA_DIR'] = 'non-sense'
    assert os.getenv('JUPYTER_DATA_DIR', False)


def main():
    from notebook.notebookapp import main as main_
    from .util import configs_location

    # main eats, argv list and kwargs
    notebook_cfg, notebook_cfg_json = configs_location()

    _nglview_pip_installed_workaround()

    # extend passed arguments with our config files
    import sys
    argv = sys.argv[1:] + ['--config=%s' % notebook_cfg, '--config=%s' % notebook_cfg_json]
    print('invoking notebook server with arguments:', argv)
    main_(argv=argv)


if __name__ == '__main__':
    main()
