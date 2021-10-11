import os
import json
import configparser
from pathlib import Path

from typing import Optional, List, Any
from __future__ import annotations

import yaml
import dotenv


__version__ = "0.0.1"


class ConfigManager:
    def __init__(
        self, 
        config_file: Optional[str] = None, 
        config_file_type: Optional[str] = None, 
        config_paths: List[str] = [],
    ):
        """
        :param config_file: The config file to parse, without the extension
        :param config_file_type: The type of config file to parse. If not specified, will try to guess.
        :param config_paths: A list of paths to search for the config file.
        """
        self.config_file = config_file
        self.config_file_type = config_file_type
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

    def _parse_config(self):
        pass

    def _parse_kvs(self):
        pass

    def parse(self):
        pass

    def set(self, key: str, value: Any) -> ConfigManager:
        self.defaults[key] = value
        return self

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



