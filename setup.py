#
# This file is part of Brazil Data Cube Configuration Library.
# Copyright (C) 2021 INPE.
#
# Brazil Data Cube Configuration Library is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Brazil Data Cube Configuration Library."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()

history = open("CHANGES.rst").read()

docs_require = [
    "Sphinx>=2.2",
    "sphinx_rtd_theme",
    "sphinx-copybutton",
]

tests_require = [
    "coverage>=4.5",
    "pytest>=5.2",
    "pytest-cov>=2.8",
    "pytest-pep8>=1.0",
    "pydocstyle>=4.0",
    "isort>4.3",
    "check-manifest>=0.40",
    "black>=19.10a",
]

examples_require = []

extras_require = {
    "docs": docs_require,
    "examples": examples_require,
    "tests": tests_require,
}

extras_require["all"] = [req for _, reqs in extras_require.items() for req in reqs]

setup_requires = [
    "pytest-runner>=5.2",
]

install_requires = []

packages = find_packages()

g = {}
with open(os.path.join("bdc_config", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="bdc_config",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    keywords=["Time series", "Earth Observations"],
    license="MIT",
    author="Brazil Data Cube Team",
    author_email="brazildatacube@inpe.br",
    url="https://github.com/brazil-data-cube/bdc-config",
    project_urls={
        "Repository": "https://github.com/brazil-data-cube/bdc-config",
        "Issues": "https://github.com/brazil-data-cube/bdc-config/issues",
        "Documentation": "https://bdc_config.readthedocs.io/en/latest/",
    },
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={},
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)
