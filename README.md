# pyemma_tutorials

[![CircleCI branch](https://img.shields.io/circleci/project/github/markovmodel/pyemma_tutorials/master.svg)](https://github.com/markovmodel/pyemma_tutorials)


### Installation
We recommended to install the PyEMMA tutorials with conda. The following command will create a new environment that comes with all the dependencies of the tutorial.

`curl  https://raw.githubusercontent.com/markovmodel/PyEMMA_tutorials/master/environment.yml > environment.yml`
`conda env create -f environment.yml`

Clone this repository to a location destination:

`git clone https://github.com/markovmodel/pyemma_tutorials.git`

#### Offline execution
An internet connection will be needed during the execution of the tutorial notebooks, because we obtain simulation data to analyze. You can pre-fetch this data in case you want to run it offline like this:

`cd pyemma_tutorials`
`mkdir data; cd data`
`mdshare fetch *`
