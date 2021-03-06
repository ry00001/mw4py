# -*- coding: utf-8 -*-
import codecs
import os
import re
import setuptools


def local_file(file):
  return codecs.open(
    os.path.join(os.path.dirname(__file__), file), 'r', 'utf-8'
  )

install_reqs = [
  line.strip()
  for line in local_file('requirements.txt').readlines()
  if line.strip() != ''
]

version = re.search(
  "^__version__ = \((\d+), (\d+), (\d+)\)$",
  local_file('wikipydia/__init__.py').read(),
  re.MULTILINE
).groups()


setuptools.setup(
  name = "mw4py",
  version = '.'.join(version),
  author = "ry00001",
  author_email = "ry00001@protonmail.com",
  description = "Asynchronous (asyncio, aiohttp) Wikipedia API wrapper",
  license = "MIT",
  keywords = "python wikipedia API",
  url = "https://github.com/ry00001/mw4py",
  download_url = 'https://github.com/ry00001/mw4py/archive/v0.0.1-alpha.tar.gz',
  install_requires = install_reqs,
  packages = ['mw4py'],
  long_description = local_file('README.md').read(),
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3'
  ]
)