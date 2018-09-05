import pkg_resources
import os


def notebook_location():
    d = pkg_resources.resource_filename('pyemma_tutorials', 'notebooks')
    assert os.path.isdir(d)
    return d


def configs_location():
    notebook_cfg = pkg_resources.resource_filename('pyemma_tutorials', 'jupyter_notebook_config.py')
    notebook_cfg_json = pkg_resources.resource_filename('pyemma_tutorials', 'jupyter_notebook_config.json')

    assert os.path.exists(notebook_cfg)
    assert os.path.exists(notebook_cfg_json)

    return notebook_cfg, notebook_cfg_json


def run_dir():
    """ directory in which the user copies of the notebooks will reside. """
    import os
    target = os.path.expanduser('~/pyemma_tutorials')
    os.makedirs(target, exist_ok=True)

    # copy static data into run dir
    src = os.path.join(notebook_location(), 'static')

    def copytree(src, dst, symlinks=False, ignore=None):
        # shutil.copytree fails for existing target dirs...
        import shutil
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

    copytree(src, os.path.join(target, 'static'))

    return target
