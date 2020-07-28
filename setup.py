# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 07/2019
"""

"""
desinstallation du package 
	pip uninstall french-preprocessing
A partir du repertoire contenant le setup
	python setup.py install
verification de l'installation du package
	pip list
"""

from setuptools import setup, find_packages

setup(name='french_preprocessing',
      version='0.1.0',
      description='French preprocessing project with tools for tokenisation, simplification, grammatical tagging (Part-of-Speech tagging) and lemmatization',
      author='Anaïs HOAREAU',
      packages=find_packages(),
      package_data={'french_preprocessing': ['data/lexique.txt']},
      include_package_data=True,)
