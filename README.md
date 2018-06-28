# pyemma_tutorials

[![CircleCI](https://circleci.com/gh/markovmodel/pyemma_tutorials.svg?style=svg)](https://circleci.com/gh/markovmodel/pyemma_tutorials)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

[PyEMMA](http://pyemma.org) (EMMA = Emma's Markov Model Algorithms) is an open source Python/C package for analysis of extensive molecular dynamics (MD) simulations.

The notebooks in this tutorial guide through the necessary steps to analyze simulation data and provide exercises (and solutions). In detail the first four notebooks introduce to most common steps of a PyEMMA analysis pipeline:

1. extracting features and loading data
2. dimension reduction and discretization
3. Markov state model (MSM) estimation and validation
4. MSM coarse graining and analysis

The notebokks after that provide a more in-depth introduciton to special features of MSMs/PyEMMA:

5. hidden Markov state models (HMMs)
6. computing observables
7. VAMP-based feature selection
8. common pitfalls with bad data

Please note that this is a work in progress and we value any kind of feedback that helps us improving this tutorial.

### Installation
We recommended to install the PyEMMA tutorials with conda. The following command will create a new environment that comes with all the dependencies of the tutorial.

```bash
curl  https://raw.githubusercontent.com/markovmodel/PyEMMA_tutorials/master/environment.yml > environment.yml
conda env create -f environment.yml
```

Clone this repository to a location destination:

```bash
git clone https://github.com/markovmodel/pyemma_tutorials.git
```
