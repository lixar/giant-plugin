#!/usr/bin/env python

from setuptools import setup
setup(
    name = "{{ cookiecutter.repo_name }}",
    version = "{{ cookiecutter.version }}",
    packages = ['{{ cookiecutter.repo_name }}'],
)