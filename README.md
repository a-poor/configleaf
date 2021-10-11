# configleaf

[![Python application](https://github.com/a-poor/configleaf/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/a-poor/configleaf/actions/workflows/python-app.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CodeFactor](https://www.codefactor.io/repository/github/a-poor/configleaf/badge)](https://www.codefactor.io/repository/github/a-poor/configleaf)
![PyPI - License](https://img.shields.io/pypi/l/configleaf?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/a-poor/configleaf?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/configleaf?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/configleaf?style=flat-square)

_created by Austin Poor_

An application configuration library, inspired by Go's Viper, written in Python.

## Installation

`configleaf` can be installed with pip:

```sh
$ pip install configleaf
```

## Quick Start

Here's a short example of `configleaf` in action:

```python
```

## About


## Dependencies

* `python-dotenv`: For reading from `.env` config files
* `pyyaml`: For reading from `YAML` config files
* `boto3`: For reading from AWS SecretsManager

## Contributing


## License

[MIT](./LICENSE.txt)

## To-Do

* Load environment variables
* Read config files
  * JSON
  * YAML
  * TOML
  * .env
  * .ini
* Read command line arguments
* Remote key/value config stores
  * redis
  * etcd
  * AWS SecretsManager
  * AWS AppConfig
* Live reload configs

