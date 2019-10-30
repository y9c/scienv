#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from codecs import open

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, "README.md"), encoding="utf-8") as readme_file:
    long_description = readme_file.read()


# The sci packages
requirements = [
    "Click>=7.0",
    "numba >= 0.45.0",
    "Cython >= 0.28.0",
    "numpy >= 1.15.0",
    "scipy >= 1.0.0",
    "scikit-learn >= 0.20.0",
    "networkx >= 2.0",
    "matplotlib >= 3.0.0",
    "bokeh >= 1.0.0",
    "seaborn >= 0.8.0",
    "notebook >= 6.0.0",
    "jupyter >= 1.0.0",
    "jupyterlab >= 1.0.0",
]

setup_requirements = []

test_requirements = []

setup(
    author="Ye Chang",
    author_email="yech1990@gmail.com",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="One package for all scientific packages",
    entry_points={"console_scripts": ["scienv=scienv.cli:main"]},
    install_requires=requirements,
    license="MIT license",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="scienv",
    name="scienv",
    packages=find_packages(include=["scienv", "scienv.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/yech1990/scienv",
    version="0.0.0.dev0",
    zip_safe=False,
)
