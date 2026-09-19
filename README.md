# ADS Project – Experiment 7

## CI/CD Pipeline with Open Source Tools

This repository uses GitHub Actions for continuous integration and DVC for dataset version metadata.

### Pipeline

1. Test DVC metadata using PyTest.
2. Run Flake8 linting.
3. Validate DVC installation and repository status.
4. Compile Python test files.
5. Pass the deployment gate after all checks succeed.

### DVC dataset

The dataset is represented by `products.csv.dvc`. The DVC metadata records the MD5 checksum and size of the tracked `products.csv` file.

A DVC remote is not currently configured in this repository, so the CI workflow intentionally performs `dvc status` rather than `dvc pull`.
