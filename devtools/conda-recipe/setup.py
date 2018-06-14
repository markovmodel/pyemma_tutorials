from setuptools import setup
from glob import glob

metadata=dict(
    name='pyemma_tutorials',
    version=0,
    # this works if invoked directly
    data_files=[('pyemma_tutorial_notebooks', glob('notebooks/*.ipynb'))],
    packages=['pyemma_tutorials'],
    include_package_data=True,
    zip_safe=False,
)

if __name__ == '__main__':
    setup(**metadata)
