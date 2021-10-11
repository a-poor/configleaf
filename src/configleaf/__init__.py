import os
import sys
import json
import configparser
from pathlib import Path
from __future__ import annotations
from typing import Optional, List, Any, Union

import toml
import yaml
import redis
import dotenv


__version__ = "0.0.1"


class ConfigManager:
    valid_types = ["ini", "toml", "yaml", "json", "env"]

    def __init__(
        self,
        config_file: Optional[str] = None,
        config_file_type: Optional[str] = None,
        config_paths: List[str] = ["."],
    ):
        """
        :param config_file: The config file name to parse, without the extension.
        :param config_file_type: The type of config file to parse. 
            If not specified, will try to guess. Must be one of the following
            types: `ini`, `toml`, `yaml`, `json`, `env`.
        :param config_paths: A list of paths to search for the config file.
        """
        # Check the params
        cft = None if config_file_type is None else config_file_type.lower()
        if cft is not None and cft not in self.valid_types:
            raise ValueError(f"`config_file_type` must be one of the following: {self.valid_types}")

        # Store the params
        self.config_file = config_file
        self.config_file_type = cft
        self.config_paths = config_paths

        # Stores the data
        self.set_values = {}
        self.flag_values = {}
        self.env_values = {}
        self.config_values = {}
        self.kvs_values = {}
        self.default_values = {}

    def _parse_env(self):
        pass

    def _parse_flags(self):
        pass

    def _parse_config_json(self):
        pass

    def _parse_config_yaml(self):
        pass

    def _parse_config_toml(self):
        pass

    def _parse_config_ini(self):
        pass

    def _parse_config_env(self):
        pass

    def _parse_config(self):
        file_extensions = []
        for d in self.config_paths:
            p = Path(d) / self.config_file

    def _parse_kvs(self):
        pass

    def parse(self):
        pass

    def set(self, key: str, value: Any) -> ConfigManager:
        """Manually set a value for a key.

        :param key: The key to set the value for
        :param value: The value to set
        :returns: The ConfigManager instance
        """
        self.defaults[key] = value
        return self

    def _get_env(self, key: str, to_upper: bool = True) -> Optional[str]:
        """
        :param key: The key to get the value for
        :param to_upper: Whether or not to convert the value to uppercase
        :returns: The value associated with the key set as an environment
            variable, or `None` if it doesn't exist.
        """
        k = key.upper() if to_upper else key
        return os.environ.get(k)

    def _get_flag(self, key: str) -> Optional[str]:
        pass

    def _get_config(self):
        pass

    def _get_kvs(self):
        pass

    def _get_default(self, key: str) -> Optional[Any]:
        """
        :param key: Key to get the default value for
        :returns: The default value for the key, or `None` if it doesn't exist
        """
        return self.default_values.get(key)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        # Check if the value was set manually
        if key in self.set_values:
            return self.set_values[key]

        # Check if the value was set by a flag
        if key in self.flag_values:
            return self.flag_values[key]

        # Check if the value is set as an environment variable
        if key in self.env_values:
            return self.env_values[key]

        # Check if the value is set in the config file
        if key in self.config_values:
            return self.config_values[key]

        # Check if the value is set in a key/value store
        if key in self.kvs_values:
            return self.kvs_values[key]

        # Check if a default value was set
        if key in self.default_values:
            return self.default_values[key]

        # Return the default value
        return default
