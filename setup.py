from setuptools import setup

setup (name = 'mu-git',
      version = '1.0',
      packages = ['mu-git'],
      entry_points = {
        'console-scripts': [
          'mu-git = mu-git.cli:main'
        ]
      })
