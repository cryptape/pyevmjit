#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='pyevmjit',
    version='0.1',
    packages=find_packages("."),
    include_package_data=True,
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
)
