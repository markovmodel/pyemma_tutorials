# pyemma_tutorials

[![CircleCI](https://circleci.com/gh/markovmodel/pyemma_tutorials.svg?style=svg)](https://circleci.com/gh/markovmodel/pyemma_tutorials)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

[PyEMMA](http://pyemma.org) (EMMA = Emma's Markov Model Algorithms) is an open source Python/C package for analysis of extensive molecular dynamics (MD) simulations.

The notebooks in this tutorial guide through the necessary steps to analyze simulation data and provide exercises (and solutions). In detail the first four notebooks introduce to most common steps of a PyEMMA analysis pipeline:

<img src="https://ftp.imp.fu-berlin.de/pub/cmb-data/pentapeptide-320.png" width="973" height="521" />

1. extracting features and loading data
2. dimension reduction and discretization
3. Markov state model (MSM) estimation and validation
4. MSM coarse graining and analysis

The notebooks after that provide a more in-depth introduciton to special features of MSMs/PyEMMA:

5. hidden Markov state models (HMMs)
6. computing observables
7. VAMP-based feature selection
8. common pitfalls with bad data

Please note that this is a work in progress and we value any kind of feedback that helps us improving this tutorial.

### Installation
We recommended to install the PyEMMA tutorials with conda. The following command will create a new environment that comes with all the dependencies of the tutorial.

If you do not have conda, please follow the instructions here:

https://conda.io/miniconda.html

After installing miniconda, you can install the tutorial either via

```bash
conda create -n pyemma_tutorials -c conda-forge pyemma_tutorials
```

... or you can also install the tutorial in an existing environment by

``` bash
conda install -c conda-forge pyemma_tutorials
```

If you intend to install with pip, for which can not give any support, you feel free to run:

``` bash
pip install git+https://github.com/markovmodel/pyemma_tutorials
```

### Usage
Now we have a fresh conda environment containing the notebooks and the software to run them. We can now just activate the environment
and run the notebook server by invoking:

```bash
conda activate pyemma_tutorials  # skip this, if you have installed in your root environment or used pip to install.
pyemma_tutorials
```

The last command will start the notebook server and your browser should pop up pointing to a list of notebooks. You can choose either to preview or to create your
own copy of the notebook. The latter will create a copy of the chosen notebook in your home directory, so your changes will not be lost after shutting down the notebook server.

### Deinstallation

To uninstall you can remove the whole environment which will also uninstall the contained software again:
``` bash
conda env remove -n pyemma_tutorials
```

or if you have installed the package directly

``` bash
conda remove pyemma_tutorials
```

