import os

from setuptools import setup

if not os.getenv('CONDA_BUILD', False):
    raise NotImplementedError('this setup script is only ment to be used within conda-build')
else:
    import shutil
    try:
        shutil.copytree('notebooks', os.path.join('pyemma_tutorials', 'notebooks'))
        print('moved notebooks into pkg')
    except OSError:
        pass

metadata=dict(
    name='pyemma_tutorials',
    version=0,
    data_files=[('etc/jupyter/nbconfig/notebook.d/', ['pyemma_tutorial_notebook_cfg.json'])],
    packages=['pyemma_tutorials'],
    package_data={'pyemma_tutorials': ['notebooks/*',
                                       'jupyter_notebook_config.py',
                                       ]},
    include_package_data=True,
    zip_safe=False,
)

if __name__ == '__main__':
    setup(**metadata)
