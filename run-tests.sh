#!/usr/bin/env bash
#
# This file is part of Brazil Data Cube Configuration Library.
# Copyright (C) 2021 INPE.
#
# Brazil Data Cube Configuration Library is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle bdc_config examples tests setup.py && \
isort bdc_config examples tests setup.py --check-only --diff && \
black --check --diff -l 120 -t py37 bdc_config tests setup.py  && \
check-manifest --ignore ".drone.yml,.readthedocs.*,.editorconfig" && \
sphinx-build -qnW --color -b doctest docs/sphinx/ docs/sphinx/_build/doctest && \
pytest
