import os
import versioneer

from setuptools import setup


def copy_notebooks():
    import shutil
    dest = os.path.join('pyemma_tutorials', 'notebooks')
    ignored_patterns = ('data', '*.xtc', '*.pyemma', '*.pdb', '*.dcd')
    import fnmatch
    def ignore(src, fn):
        return any(fnmatch.fnmatch(fn, p) for p in ignored_patterns)
    try:
        shutil.rmtree(dest, ignore_errors=True)
        shutil.copytree('notebooks', dest, ignore=ignore)
        print('moved notebooks into pkg')
    except OSError:
        pass


metadata=dict(
    name='pyemma_tutorials',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['pyemma_tutorials'],
    package_data={'pyemma_tutorials': ['notebooks/*',
                                       'jupyter_notebook_config.py',
                                       'jupyter_notebook_config.json',
                                       ]},
    include_package_data=True,
    entry_points={'console_scripts': ['pyemma_tutorials = pyemma_tutorials.cli:main'],},
    install_requires=['pyemma',
                      'mdshare',
                      'nbexamples',
                      'nglview',
                      'notebook',
                      'jupyter_contrib_nbextensions',
    ],
    zip_safe=False,
)

if __name__ == '__main__':
    copy_notebooks()
    setup(**metadata)
