"""
Jupyter notebook launcher for PyEMMA's tutorials series.
"""

from .__main__ import notebook_location, main

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
