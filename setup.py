from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='misl',
      version=version,
      description="make itunes suck less",
      long_description="""make itunes suck less""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='misl mp3 tags',
      author='bjh',
      author_email='bjh@nowhere.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
