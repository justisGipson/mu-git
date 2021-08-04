#!/usr/bin/env python3

from setuptools import setup

setup (name = 'mu_git',
       version = '1.0',
       packages = ['mu_git'],
       entry_points = {
         'console_scripts': [
           'mu_git = mu_git.cli:main'
         ]
      })
