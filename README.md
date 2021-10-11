# configleaf

![PyPI](https://img.shields.io/pypi/v/configleaf?style=flat-square)
[![Python application](https://github.com/a-poor/configleaf/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/a-poor/configleaf/actions/workflows/python-app.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/configleaf?style=flat-square)
[![CodeFactor](https://www.codefactor.io/repository/github/a-poor/configleaf/badge)](https://www.codefactor.io/repository/github/a-poor/configleaf)
![PyPI - License](https://img.shields.io/pypi/l/configleaf?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/a-poor/configleaf?style=flat-square)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


_created by Austin Poor_

An application configuration library, inspired by Go's [Viper](https://github.com/spf13/viper), written in Python.

## Installation

`configleaf` can be installed with pip:

```sh
$ pip install configleaf
```

## Quick Start

Here's a short example of `configleaf` in action:

```python
...
```

## About

...

## Dependencies

* `python-dotenv`: For reading from `.env` config files
* `pyyaml`: For reading from `YAML` config files
* `boto3`: For reading from AWS SecretsManager

## Contributing

Pull requests are super welcome! For major changes, please open an issue first to discuss what you would like to change. And please make sure to update tests as appropriate.

Or... feel free to just open an issue with some thoughts or suggestions or even just to say Hi and tell me if this library has been helpful!

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
  * AWS AppConfig
  * GCP alternative
  * Azure alternative
* Get secret values (separate interface from remote k/v store)
  * ex AWS SecretsManager
  * ie Load secret name from a config then get the value from a secrets manager
* Live reload configs
* Create a config-loading interface to allow for adding plugins

