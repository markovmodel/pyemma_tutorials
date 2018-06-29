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
