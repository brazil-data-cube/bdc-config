#
# This file is part of Brazil Data Cube Configuration Library.
# Copyright (C) 2021 INPE.
#
# Brazil Data Cube Configuration Library is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Example for Brazil Data Cube Configuration Library."""
import secrets

from bdc_config import BDCConfig

config = BDCConfig("myconfig.ini")

config.add("default", access_token=secrets.token_urlsafe())
config.save()

config2 = BDCConfig("myconfig.ini")

print(config2["default"]["access_token"])
