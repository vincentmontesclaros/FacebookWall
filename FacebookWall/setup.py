#!/usr/bin/env python

from setuptools import setup

VERSION = '0.0.1'

setup(
  name='FacebookWall',
  version=VERSION,
  description='Building a FacebookWall-like App',
  author='Vincent Montesclaros',
  author_email='montesclaros.vince@gmail.com',

  # I'm not sure what's ideal, but I think we'd like to move these apps down a directory
  # so instead of "src/FacebookWall/app," we'd have "src/app."
  # Anyway, for now the value in this is that you don't have to write "import FacebookWall.app,"
  # you can write "import app."
  packages=['',],
  package_dir={ '' : 'src/FacebookWall' },

  install_requires=[
    'django == 1.6.8',
  ]
)
