# Cimpress API Wrapper

[![image]]

[![image][1]]

[![Documentation Status]]

[![Updates]]

# Notes
This is very much a WIP. PRs welcome.

#Features
-   TODO

#Credits

This package was created with [Cookiecutter] and the [audreyr/cookiecutter-pypackage] project template.



  [image]: https://img.shields.io/pypi/v/python_cimpress.svg
  [![image]]: https://pypi.python.org/pypi/python-cimpress
  [1]: https://img.shields.io/travis/mwisner/python_cimpress.svg
  [![image][1]]: https://travis-ci.org/mwisner/python-cimpress
  [Documentation Status]: https://readthedocs.org/projects/python-cimpress/badge/?version=latest
  [![Documentation Status]]: https://python-cimpress.readthedocs.io/en/latest/?badge=latest
  [Updates]: https://pyup.io/repos/github/mwisner/python-cimpress/shield.svg
  [![Updates]]: https://pyup.io/repos/github/mwisner/python-cimpress/
  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [audreyr/cookiecutter-pypackage]: https://github.com/audreyr/cookiecutter-pypackage

# Testing
1) Setup Env vars:
```bash
cp .env.example .env
```
Then add the correct creds

2) Create venv
https://docs.python.org/3/library/venv.html#creating-virtual-environments

4) Activate venv

5) Set Env Vars
```bash
eval $(cat .env | sed ‘s/^/export /’)
```
