# crabpy_pyramid

Bindings for the crabpy library and the pyramid framework

[![pypi](https://badge.fury.io/py/crabpy_pyramid.png)](http://badge.fury.io/py/crabpy_pyramid)
[![docs](https://readthedocs.org/projects/crabpy-pyramid/badge/?version=latest)](https://readthedocs.org/projects/crabpy-pyramid/?badge=latest)
[![CI](https://github.com/OnroerendErfgoed/crabpy_pyramid/actions/workflows/backend.yaml/badge.svg)](https://github.com/OnroerendErfgoed/crabpy_pyramid/actions/workflows/backend.yaml)
[![coverage](https://coveralls.io/repos/OnroerendErfgoed/crabpy_pyramid/badge.png?branch=master)](https://coveralls.io/r/OnroerendErfgoed/crabpy_pyramid?branch=master)
[![pypi](https://badge.fury.io/py/crabpy_pyramid.png)](http://badge.fury.io/py/crabpy_pyramid)


# Development

Dependencies are managed with [uv](https://docs.astral.sh/uv/) and declared in
`pyproject.toml`; `uv.lock` holds the full pinned resolution and is committed.

Install the library together with the dev dependencies in `.venv`:

```sh
uv sync
```

After changing dependencies in `pyproject.toml`, recompute the lock with
`uv lock` (add `--upgrade` to update everything to the latest allowed versions).

Run the tests and linting:

```sh
uv run pytest tests
uv run flake8
```

## Building the docs

More information about this library can be found in `docs`. The docs can be
built using [Sphinx](http://sphinx-doc.org).

```sh
uv run --with sphinx --with sphinxcontrib-httpdomain make -C docs html
```

## Build wheel or sdist

```sh
uv build
uv build --wheel
uv build --sdist
```
