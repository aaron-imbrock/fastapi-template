# Package Setup

## SETUP

[Poetry DOCS](https://python-poetry.org/docs/repositories/)

Pypi tokens live in: `~/.pypirc`

In the format of:

```bash
[testpypi]
  username = __token__
  password = pypi-abcdefg
[pypi]
  username = __token__
  password = pypi-abcdefg
```

Add test pypi repo with token: `poetry config http-basic.test-pypi https://test.pypi.org/legacy/`

Add pypi repo with token: `poetry config http-basic.pypi`

## Building a package to release

```bash
poetry version minor
poetry lock
poetry check
# poetry build - creates a dist directory containing your package files: a .tar.gz source archive and a .whl wheel file.
# poetry publish - pushes package to designated repo
poetry publish --build -r test-pypi
```

### Install Dependencies

```shell
python3 -m pip install --upgrade pip
pip install --upgrade setuptools build twine
```

### Tag release

```shell
git tag v0.1
git push origin v0.1
```

### Build a distribution (for releases, do this on main with a fresh tag)

```shell
python3 -m build
```

### To first test release that package

```shell
twine upload --repository testpypi dist/*
```

### To formally release that package

```shell
twine upload dist/*
```

### To see what the current version will be

```shell
python -m setuptools_scm
```
