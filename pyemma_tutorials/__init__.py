"""
Jupyter notebook launcher for PyEMMA's tutorials series.
"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .util import notebook_location, configs_location, run_dir
