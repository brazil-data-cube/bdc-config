#
# This file is part of Brazil Data Cube Configuration Library.
# Copyright (C) 2021 INPE.
#
# Brazil Data Cube Configuration Library is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Brazil Data Cube Configuration Library."""

import os
import sys
from configparser import ConfigParser

from .version import __version__

__all__ = ("__version__",)

# modified from https://github.com/ActiveState/appdirs/blob/master/appdirs.py#L44
def _user_data_dir(appname="BrazilDataCube"):
    """Return full path to the user-specific data dir for this application."""
    if sys.platform == "win32":
        const = "CSIDL_LOCAL_APPDATA"
        path = os.path.normpath(_get_win_folder(const))
        path = os.path.join(path, appname)
    elif sys.platform == "darwin":
        path = os.path.expanduser("~/Library/Application Support/")
        path = os.path.join(path, appname)
    else:
        path = os.getenv("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
        path = os.path.join(path, appname)

    return path


class BDCConfig(ConfigParser):
    def __init__(self, path=None):
        """Initialize Config.

        Args:
            path (str): custom path for config file
        """
        super().__init__()

        self.base_dir = _user_data_dir()
        self.path = path if path else os.path.join(self.base_dir, "config.ini")

        if not os.path.exists(self.path):
            if not os.path.exists(self.base_dir):
                os.makedirs(self.base_dir)

            with open(self.path, "a"):
                os.utime(self.path, None)

        self.read(self.path)

    def add(self, section, **kwargs):
        """Write into a section of BrazilDataCube config.ini."""
        if section in self:
            self[section].update(kwargs)
        else:
            self[section] = kwargs

    def save(self, path=None):
        """Save config into disk."""
        with open(path if path else self.path, "w") as configfile:
            self.write(configfile)
