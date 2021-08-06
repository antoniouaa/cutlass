# Cutlass

![tests](https://github.com/antoniouaa/cutlass/actions/workflows/test.yml/badge.svg)
![black](https://github.com/antoniouaa/cutlass/actions/workflows/black.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Coverage Status](https://coveralls.io/repos/github/antoniouaa/cutlass/badge.svg?branch=master)](https://coveralls.io/github/antoniouaa/cutlass?branch=master)

Parse international phone numbers the right way.

## Args

### `in_file`

**Required** An excel file to read numbers from.

### `[-o out_file]`

**Optional** An output file to dump the results into. If does not exist, create it. Otherwise, update it. If an output file is not provided the script will just dump the results to stdout and not change any Excel file.

## Sample Usage

Run with poetry

```sh
python -m cutlass in_file.xls [-o out_file.xls]
```

## Build and Install

First you need [poetry](https://python-poetry.org/).

Clone the repository and build it with poetry.

```sh
git clone https://github.com/antoniouaa/cutlass.git
cd cutlass

poetry build
pip install .
cutlass in_file.xls [-o out_file.xls]
```
