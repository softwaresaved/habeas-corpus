# Don’t mention it: challenges to using software mentions to investigate citation and discoverability - Data and Notebooks

This deposit contains the data and Jupyter notebooks used for sampling and annotation analysis of
our submission to the PeerJ Computer Science special issue [*Software Citation, Indexing, and Discoverability*](https://peerj.com/collections/84-software):

`Stephan Druskat, Neil P. Chue Hong, Sammie Buzzard, Olexandr Konovalov, and Patrick Kornek. Don’t mention it: challenges to using software mentions to investigate citation and discoverability.`

> **Note**
>
> If you just want to have a look at the contents of the replication package, you can view them in a GitHub repository at https://github.com/softwaresaved/habeas-corpus/tree/main/replication-package (includes notebook outputs).


Datasets that were used:

- Wade, Alex D., & Williams, Ivana. (2021). CORD-19 Software Mentions [Data set]. https://doi.org/10.5061/dryad.vmcvdncs0 (*CSM*)
- Istrate, Ana-Maria et al. (2022), CZ Software Mentions: A large dataset of software mentions in the biomedical literature, Dryad, Dataset, https://doi.org/10.5061/dryad.6wwpzgn2c (*CZI*)

The notebooks contain code for:

- Sampling CSM ([`CSM_sampling.ipynb`](./notebooks/CSM_sampling.ipynb))
- Sampling CZI ([`CZI_sampling.ipynb`](./notebooks/CZI_sampling.ipynb))
- Linking CZI, i.e., adding repository links to the sample ([`CZI_linking.ipynb`](./notebooks/CZI_linking.ipynb))
- Analyzing mention type annotations combined over both samples ([`combined-mention-types-study.ipynb`](./notebooks/combined-mention-types-study.ipynb))
- Analyzing licenses combined over both samples ([`combined-license-study.ipynb`](./notebooks/combined-license-study.ipynb))
- Calculating inter-annotator agreement (Krippendorff's alpha) for the CSM sample ([`inter-annotator-agreement.ipynb`](./notebooks/inter-annotator-agreement.ipynb))

The data directory contains:

- The original annotated CSM sample from SSI CW21 (`CSM_CW_sample.csv`)
- The new annotated CSM sample (`CSM_sample.csv`)
- The annotated CSM samples used for calculating Krippendorff's alpha (`IAA_*.csv`)
- The annotated CZI sample (`ICZI_sample.csv`)

The root directory also contains 

- a copy of this README, 
- `requirements.txt` that contains the frozen dependencies that are necessary to run the notebooks,
- a PDF with the annotation guidelines,
- a Shell script that can be used to retrieve the CSM dataset.

## Dataset retrieval

The original CSM dataset can be retrieved by running the `get_csm.sh` Shell script:

```shell
. ./get_csm.sh
```

CZI is downloaded from the sampling notebook, see above.

## Running the notebooks

To run the notebooks, you need Python 3 >= 3.11 and the respective version of `python3-venv`.

ON a Linux system, install the dependencies:

```shell
python3.11 -m venv .venv  # Creates a Python virtual environment to isolate the runtime environment
. .venv/bin/activate  # Activates the virtual environment
pip install --upgrade pip  # Updates the package manager pip
pip install -r requirements.txt  # Installs the required Python packages
```

You can then run `jupyter notebook` to start the graphical user interface to work with the notebooks.

> **Note**
>
> 1. The CZI sampling notebook requires resources that your local computer may not have (due to file size and memory requirements). Run on an HPC resource using [`nbconvert`](https://nbconvert.readthedocs.io/en/latest/) if necessary.
> 2. You may have to adapt file paths for input and output files.

## License information

Copyright (c) 2023 The authors

These resources are shared under [CC BY-4.0 Intl.](https://spdx.org/licenses/CC-BY-4.0.html) (data) and the [MIT license](https://spdx.org/licenses/MIT.html) (code).

## :warning: Security note

If you find any security issue with the contents of this deposit, please write an email with details to [stephan.druskat@dlr.de](mailto:stephan.druskat@dlr.de).
