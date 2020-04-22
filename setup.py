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
      version='0.0.3',
      description='French preprocessing project with tools for tokenisation, simplification, grammatical tagging (Part-of-Speech tagging) and lemmatization',
      author='Anaïs HOAREAU',
      packages=find_packages(),
      package_data={'french_preprocessing': ['data/lexique.txt',
                                             'stanford-postagger-full-2018-10-16/build.xml',
                                             'stanford-postagger-full-2018-10-16/LICENSE.txt',
                                             'stanford-postagger-full-2018-10-16/README.txt',
                                             'stanford-postagger-full-2018-10-16/sample-input.txt',
                                             'stanford-postagger-full-2018-10-16/sample-output.txt',
                                             'stanford-postagger-full-2018-10-16/stanford-postagger-3.9.2-javadoc.jar',
                                             'stanford-postagger-full-2018-10-16/stanford-postagger-3.9.2-sources.jar',
                                             'stanford-postagger-full-2018-10-16/stanford-postagger-3.9.2.jar',
                                             'stanford-postagger-full-2018-10-16/stanford-postagger-gui.bat',
                                             'stanford-postagger-full-2018-10-16/stanford-postagger-gui.sh',
                                             'stanford-postagger-full-2018-10-16/stanford-postagger.bat',
                                             'stanford-postagger-full-2018-10-16/stanford-postagger.jar',
                                             'stanford-postagger-full-2018-10-16/stanford-postagger.sh',
                                             'stanford-postagger-full-2018-10-16/TaggerDemo.java',
                                             'stanford-postagger-full-2018-10-16/TaggerDemo2.java'
                                             'stanford-postagger-full-2018-10-16/models/french-ud.tagger',
                                             'stanford-postagger-full-2018-10-16/models/french-ud.tagger.props',
                                             'stanford-postagger-full-2018-10-16/models/french.tagger',
                                             'stanford-postagger-full-2018-10-16/models/french.tagger.props',
                                             'stanford-postagger-full-2018-10-16/models/README-Models.txt',
                                             'stanford-postagger-full-2018-10-16/models/wsj-0-18-bidirectional-distsim.tagger',
                                             'stanford-postagger-full-2018-10-16/models/wsj-0-18-bidirectional-distsim.tagger.props',
                                             'stanford-postagger-full-2018-10-16/models/wsj-0-18-bidirectional-nodistsim.tagger',
                                             'stanford-postagger-full-2018-10-16/models/wsj-0-18-bidirectional-nodistsim.tagger.props',
                                             'stanford-postagger-full-2018-10-16/models/wsj-0-18-caseless-left3words-distsim.tagger',
                                             'stanford-postagger-full-2018-10-16/models/wsj-0-18-caseless-left3words-distsim.tagger.props',
                                             'stanford-postagger-full-2018-10-16/models/wsj-0-18-left3words-distsim.tagger',
                                             'stanford-postagger-full-2018-10-16/models/wsj-0-18-left3words-distsim.tagger.props',
                                             'stanford-postagger-full-2018-10-16/models/wsj-0-18-left3words-nodistsim.tagger',
                                             'stanford-postagger-full-2018-10-16/models/wsj-0-18-left3words-nodistsim.tagger.props',
                                             'stanford-postagger-full-2018-10-16/data/enclitic-inflections.data']},
      include_package_data=True,)
