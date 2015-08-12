#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='nodocstrings',
      version='1.0',
      packages=find_packages(),
      entry_points={
          'nose.plugins': [
              'NoDocStrings = nodocstrings:NoDocStrings'
          ]
      },
      description="This is just a tiny nose plugin for those who don't like to see docstrings instead of function names",
      use_2to3 = True
)
