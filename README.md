# Cutlass

![tests](https://github.com/antoniouaa/cutlass/actions/workflows/test.yml/badge.svg)
![black](https://github.com/antoniouaa/cutlass/actions/workflows/black.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Coverage Status](https://coveralls.io/repos/github/antoniouaa/cutlass/badge.svg?branch=master&service=github)](https://coveralls.io/github/antoniouaa/cutlass?branch=master)

Parse international phone numbers the right way.

## Args

### `in_file`

**Required** An excel file to read numbers from. The operations happen in-place by default.

### `[-o out_file]`

**Optional** An output file to dump the results into. If does not exist, create it. Otherwise, update it.

## Sample Usage

No build and install:

```console
python -m cutlass sample_excel_file.xls [-o output_excel_file.xls]
```

With build and install:

```console
cutlass sample_excel_file.xls [-o output_excel_file.xls]
```

## Build and Install

First you need [poetry](https://python-poetry.org/).
