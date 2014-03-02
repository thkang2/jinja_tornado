#!/usr/bin/env python

from setuptools import setup

setup(name='jinja_tornado',
      version='0.0.1',
      description='jinja2 template support for tornado web framework',
      author='thkang2',
      author_email='thkang91@gmail.com',
      url='https://github.com/thkang2/jinja_tornado',
      packages=['jinja_tornado'],
      install_requires=['tornado', 'Jinja2'],
      zip_safe = False
)
