#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='aawtools',
      version='0.0.1',
      description='Package of tools for the Advanced Analytics Workspace (AAW)',
      author='Andrew Scribner',
      author_email='ca.scribner+1@gmail.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
#       license='LICENSE.txt',
    )
