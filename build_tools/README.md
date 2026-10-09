# Conda environment

uv is the recommended way to work on this project (see the root `README.md`).
If you prefer Conda, create and activate the optional environment from the
repository root, then install the package and its development tools with pip:

```bash
conda env create -f build_tools/environment.yml
conda activate template-python
python -m pip install --group dev -e .
```

This path resolves the latest versions allowed by `pyproject.toml` rather than
the exact versions pinned in `uv.lock`.
