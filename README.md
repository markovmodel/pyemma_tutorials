# pyemma_tutorials

[![CircleCI](https://circleci.com/gh/markovmodel/pyemma_tutorials.svg?style=svg)](https://circleci.com/gh/markovmodel/pyemma_tutorials)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

[PyEMMA](http://pyemma.org) (EMMA = Emma's Markov Model Algorithms) is an open source Python/C package for analysis of extensive molecular dynamics (MD) simulations.

### Content

The first [notebook 📓](notebooks/00-pentapeptide-showcase.ipynb) in this tutorial guides through the basic analysis workflow using real MD data of a pentapeptide:

<img src="https://ftp.imp.fu-berlin.de/pub/cmb-data/pentapeptide-320.png" width="320" height="171" />

We keep the details minimal throughout the showcase but point to the more specialized notebooks which allow you to go in-depth on selected topics.

In detail, the remaining eight notebooks revisit all aspects shown in the showcase, provide additional details and variants, and contain exercises (and solutions) to self-check your learning progress:

1. Data-I/O and featurization [➜ 📓](notebooks/01-data-io-and-featurisation.ipynb)
2. Dimension reduction and discretization [➜ 📓](notebooks/02-dimension-reduction-and-discretisation.ipynb)
3. MSM estimation and validation [➜ 📓](notebooks/03-msm-estimation-and-validation.ipynb)
4. MSM analysis [➜ 📓](notebooks/04-msm-analysis.ipynb)
5. PCCA and TPT analysis [➜ 📓](notebooks/05-pcca-tpt.ipynb)
6. Hidden Markov state models (HMMs) [➜ 📓](notebooks/06-hidden-markov-state-models.ipynb)
7. Expectations and Observables [➜ 📓](notebooks/07-expectations-and-observables.ipynb)
8. Common problems & bad data situations [➜ 📓](notebooks/08-common-problems.ipynb)

**Please note that this is a work in progress and we value any kind of feedback that helps us improving this tutorial.**

### Installation
We recommended to install the PyEMMA tutorials with conda. The following command will create a new environment that comes with all the dependencies of the tutorial.

If you do not have conda, please follow the instructions here:

https://conda.io/miniconda.html

After installing miniconda, you can install the tutorial either via

``` bash
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
Now we have a fresh conda environment containing the notebooks and the software to run them. We can now just activate the environment and run the notebook server by invoking:

``` bash
conda activate pyemma_tutorials  # skip this, if you have installed in your root environment or used pip to install.
pyemma_tutorials
```

The last command will start the notebook server and your browser should pop up pointing to a list of notebooks. You can choose either to preview or to create your own copy of the notebook. The latter will create a copy of the chosen notebook in your home directory, so your changes will not be lost after shutting down the notebook server.

### Deinstallation

To uninstall you can remove the whole environment which will also uninstall the contained software again:
``` bash
conda env remove -n pyemma_tutorials
```

or if you have installed the package directly

``` bash
conda remove pyemma_tutorials
```

