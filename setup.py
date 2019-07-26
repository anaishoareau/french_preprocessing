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
      packages=find_packages(),
      package_data={'french_preprocessing': ['data/lexique.txt', 'data/lexique_ss_accent.txt',
                                             'data/lexique_ac_accent.txt',
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
      include_package_data=True,
      install_requires=['spacy','nltk'])