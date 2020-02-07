#!/usr/bin/env python
#
# Future-proof for Python 2.7 users.
from __future__ import absolute_import, division, print_function
#
# Standard imports.
#
from glob import glob
import os
import re
import sys
#
#from distutils.command.sdist import sdist as DistutilsSdist
from setuptools import setup, find_packages
from setuptools.extension import Extension
#
#from python.voidfinder._git import get_version, SetVersion

from Cython.Build import cythonize
import numpy
#
# Package setup.
#
setup_keywords = dict()
#
setup_keywords['name'] = 'voidfinder'
setup_keywords['description'] = 'VoidFinder package'
setup_keywords['author'] = 'Kelly Douglass, University of Rochester'
setup_keywords['author_email'] = 'kellyadouglass@rochester.edu'
setup_keywords['license'] = 'BSD'
setup_keywords['url'] = 'https://github.com/DESI-UR/Voids/VoidFinder'
setup_keywords['version'] = '0.1.1'
#
# Use README.md as a long_description.
#
setup_keywords['long_description'] = ''
if os.path.exists('README.md'):
    with open('README.md') as readme:
        setup_keywords['long_description'] = readme.read()
#
# Set other keywords for the setup function.
#
setup_keywords['provides'] = [setup_keywords['name']]
setup_keywords['requires'] = ['Python (>3.7.0)']
setup_keywords['zip_safe'] = False
setup_keywords['use_2to3'] = False
setup_keywords['packages'] = ['voidfinder', 
                              'voidfinder.viz']
#setup_keywords['package_dir'] = {'': 'python'}
#setup_keywords['cmdclass'] = {'version': SetVersion, 'sdist': DistutilsSdist}
#setup_keywords['test_suite'] = 'nose.collector'
#setup_keywords['tests_require'] = ['nose']

extensions = [
              Extension("voidfinder._voidfinder_cython_find_next", 
                        ["voidfinder/_voidfinder_cython_find_next.pyx"],
                        include_dirs=[".", numpy.get_include()],
                        library_dirs=["m"]),
                        
              Extension("voidfinder._voidfinder_cython", 
                        ["voidfinder/_voidfinder_cython.pyx"],
                        include_dirs=[".", numpy.get_include()],
                        library_dirs=["m"]),

              Extension("voidfinder.viz.unionize",
                        ["voidfinder/viz/unionize.pyx"],
                        include_dirs=[numpy.get_include()],
                        library_dirs=["m"]),
    
              Extension("voidfinder.viz.neighborize",
                        ["voidfinder/viz/neighborize.pyx"],
                        include_dirs=[numpy.get_include()],
                        library_dirs=["m"])





              ]

setup_keywords["ext_modules"] = cythonize(extensions)
#
# Internal data directories.
#
#setup_keywords['data_files'] = [('VoidFinder/data/config', glob('data/config/*')),
#                                ('VoidFinder/data/examples', glob('data/examples/*'))]
#
# Run setup command.
#
setup(**setup_keywords)