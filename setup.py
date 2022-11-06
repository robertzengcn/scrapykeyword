#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from setuptools import setup
from setuptools import find_packages

version = re.search(
    "^__version__\s*=\s*'(.*)'",
    open('scrapysexkeyword/version.py').read(),
    re.M).group(1)

requirements = [r for r in open('requirements.txt', 'r').read().split('\n') if r]

# https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi

setup(name='scrapysexkeyword',
      version=version,
      description='A module to scrape keyword from adult site',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      include_package_data=True,
      author='Robert Zeng',
      author_email='zengjianze@gmail.com',
      packages=find_packages(),
      entry_points={'console_scripts': ['scrapykeyword = scrapysexkeyword.core:main']},
      install_requires=requirements,
      python_requires='>=3.9',
)
