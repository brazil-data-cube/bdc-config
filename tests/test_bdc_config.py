#
# This file is part of Brazil Data Cube Configuration Library.
# Copyright (C) 2021 INPE.
#
# Brazil Data Cube Configuration Library is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for Brazil Data Cube Configuration Library."""
import os
from configparser import ConfigParser

from bdc_config import BDCConfig, _user_data_dir


class TestBDCConfig:
    """Tests for bdc_config."""

    def test_read(self):
        """Test read_config function."""
        # this will create an empty config file if doens't exists
        BDCConfig()

        assert os.path.exists(os.path.join(_user_data_dir(), "config.ini"))

    def test_add(self):
        """Test write_config function."""
        config = BDCConfig()
        config.add("default", test="123")
        config.save()

        assert "default" in config
        assert "test" in config["default"]
        assert config["default"]["test"] == "123"

    def test_read_save(self):
        """Test previous saved config."""
        config = BDCConfig()

        assert "default" in config
        assert "test" in config["default"]
        assert config["default"]["test"] == "123"
