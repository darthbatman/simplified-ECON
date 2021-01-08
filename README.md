# simplified-ECON

`simplified-ECON` is a simplified version of the ECON pipeline introduced in the following paper: [Concept Mining via Embedding](https://ysu1989.github.io/papers/icdm18_concept.pdf). This repository also includes a comparison between AutoPhrase and ECON results on the same input corpus (10000 arXiv computer science paper abstracts).

## Pipeline

1. Candidate Generation

2. Superspan Sequence Generation

3. Embedding Construction

4. Feature Generation

5. Classifier Training

6. Concept Recognition

## Usage

### Environment

Navigate to the `simplified-ECON` directory and setup a new `conda` environment using the following commands.

```
conda create -n se python=3.8.5 -y
conda activate se
conda install ipykernel -y
ipython kernel install --user --name=se
```

Clone the [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) repository. In the `candidate_generation.ipynb` and `feature_generation.ipynb` notebooks, set `AUTOPHRASE_PATH` to the path of the cloned AutoPhrase repository.

### Dependencies

Install the dependencies using the following command.

`pip install -r requirements.txt`

### Execution

To run the pipeline, run the cells of the Jupyter notebooks in the order of the pipeline steps listed above, using `jupyter lab`, ensuring the `se` kernel is selected.

To compare the results of the AutoPhrase and ECON pipelines, run the cells of the `autophrase_comparison.ipynb` notebook.

## Authors

* Rishi Masand

## Resources

Keqian Li, Hanwen Zha, Yu Su, and Xifeng Yan, ["Concept Mining via Embedding"](https://ysu1989.github.io/papers/icdm18_concept.pdf), 2018.

Jingbo Shang, Jialu Liu, Meng Jiang, Xiang Ren, Clare R Voss, and Jiawei Han, ["Automated Phrase Mining from Massive Text Corpora"](https://arxiv.org/abs/1702.04457), 2017.