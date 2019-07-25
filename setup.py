# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 07/2019
GitHub : https://github.com/anaishoareau
Linkedin : https://www.linkedin.com/in/ana%C3%AFs-hoareau-a2a042183/
"""
from setuptools import setup, find_packages

setup(name='french_preprocessing',
      version='0',
      description='French preprocessing project with tools for tokenisation, simplification, grammatical tagging (Part-of-Speech tagging) and lemmatization',
      url='https://github.com/anaishoareau/preprocessing',
      author='Anaïs HOAREAU',
      package_data={'': ['*.txt']},
      include_package_data=True,
      packages=find_packages(),
      install_requires=['spacy','nltk'])