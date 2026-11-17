# DonorDrivePython
A Python reference implementation of the [Donor Drive API](https://github.com/DonorDrive/PublicAPI)

This project provides a Python package a developer could import to create a project to access the Donor Drive API.

For an example of what you can build to provide extra functionality around the Donor Drive API, see my project, [ElDonationTracker](http://djotaku.github.io/ELDonationTracker/) for the Extra Life charity event. It takes the Donor Drive API information and converts it to text files and HTML files that the gamers can use for live streaming during the annual Extra Life Event.

## Development

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and use Python 3.10 or later (below Python 4). From the repository root:

```sh
uv sync --locked --python 3.11
uv run --locked pytest
uv build
```

`uv sync` creates `.venv` and installs the package and development dependencies.
Commit `uv.lock` to keep environments reproducible. Use `uv add <package>` for
runtime dependencies and `uv add --dev <package>` for development dependencies.
After manually editing dependencies in `pyproject.toml`, run `uv lock` and
`uv sync --locked`.

Publishing a GitHub release builds and uploads the package to PyPI using uv
and the repository's `PYPI_TOKEN` secret.
