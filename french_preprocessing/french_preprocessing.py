# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 07/2019
GitHub : https://github.com/anaishoareau
Linkedin : https://www.linkedin.com/in/ana%C3%AFs-hoareau-a2a042183/
"""

# IMPORTS
import os
from nltk.tag import StanfordPOSTagger

from french_preprocessing.general_tools import remove_accents
from french_preprocessing.general_tools import stanford_tag_reduction
from french_preprocessing.spacy_fr import SpacyFr

class FrenchPreprocessing(object):  

    def __init__(self, java_path = "C:/Program Files/Java/jre1.8.0_211/bin/java.exe"):
        
        # Chargement du path du dossier du ficher actuel
        dir_path = os.path.dirname(os.path.abspath(__file__))
        
        # CHARGEMENT DES LEXIQUES
        f_ss_accent=open(dir_path + '\\data\\lexique_ss_accent.txt','r')
        f_ac_accent=open(dir_path + '\\data\\lexique_ac_accent.txt','r')
        
        self.lexique_ss_accent = dict(eval(f_ss_accent.read()))
        self.lexique_ac_accent = dict(eval(f_ac_accent.read()))

        ## INITIALISATION DU TAGGER
        
        # Initialisation des path pour le StanfordPOSTagger
        jar = dir_path + '\\stanford-postagger-full-2018-10-16\\stanford-postagger-3.9.2.jar'
        model = dir_path + '\\stanford-postagger-full-2018-10-16\\models\\french.tagger'
        self.java_path = java_path
        os.environ['JAVAHOME'] = self.java_path
        
        # Initialisation du StanfordPOSTagger
        self.pos_tagger = StanfordPOSTagger(model, jar, encoding = 'utf8')
        
        # CHARGEMENT DU MODULE SPACY POUR LE FRANCAIS
        sf = SpacyFr()
        sf.init_stop_words()
        self.nlp = sf.nlp

    # La fonction tokenize :
    # - prend en argument une phrase à tokeniser (string)
    # - renvoie une liste contenant les mots de la phrase tokenisée
    def tokenize_and_simplify(self, string):
        doc = self.nlp(string)
        tokenized_list_of_string = []
        for token in doc:
            if (token.is_stop == False and token.is_punct == False and token.text != ' ' and token.text != '  '
                and token.text != '   ' and token.text != '    '):
                tokenized_list_of_string.append(token.text)
        return(tokenized_list_of_string) 
    
    # La fonction tag :
    # - prend une liste de strings formant une phrase (principe du StanfordPOSTagger)
    # - renvoie une liste de tuples du type : (mot de la liste, son tag)
    def tag(self, list_of_string):
        temp = self.pos_tagger.tag(list_of_string)
        list_word_tag = []
        for e in temp:
            list_word_tag.append((e[0],stanford_tag_reduction(e[1])))
        return(list_word_tag)
    
    # La fonction lemmatise :
    # - prend en argument une liste de tuples du type (mot de la liste, son tag)
    # - renvoie une liste qui contient les mots de la phrase lemmatisés (strings)
    def lemmatize(self, list_word_tag):
        # On regarde si le mot est avec ou sans accent 
        #pour choisir le bon lexique de comparaison
        list_lemmatized = []
        
        for e in list_word_tag:
            word = e[0]
            tag = e[1]
            
            if word == remove_accents(word):
                lexique = self.lexique_ss_accent
            else:
                lexique = self.lexique_ac_accent
                
            # On lemmatise
            if word in lexique.keys():
                dict_lemma = lexique[word]
                if tag in dict_lemma.keys():
                    list_lemmatized.append(dict_lemma[tag])
                else :
                    
                    nb_pos = 0
                    list_tag = []
                    for tag_lemma in dict_lemma.keys():
                        nb_pos += 1
                        list_tag.append(tag_lemma)
                    if nb_pos>1:
                        if 'nc' in list_tag:
                            list_lemmatized.append(dict_lemma['nc'])
                        elif 'adj' in list_tag: 
                            list_lemmatized.append(dict_lemma['adj'])
                        elif 'v' in list_tag:
                            list_lemmatized.append(dict_lemma['v'])
                        elif 'adv'in list_tag:
                            list_lemmatized.append(dict_lemma['adv'])
                        elif 'pro' in list_tag:
                            list_lemmatized.append(dict_lemma['pro'])
                        elif 'c' in list_tag:
                            list_lemmatized.append(dict_lemma['c'])
                        elif 'prep' in list_tag:
                            list_lemmatized.append(dict_lemma['prep'])
                        elif 'det' in list_tag:
                            list_lemmatized.append(dict_lemma['det'])
                        elif 'npp' in list_tag:
                            list_lemmatized.append(dict_lemma['npp'])
                        elif 'et' in list_tag:
                            list_lemmatized.append(dict_lemma['et'])
                        elif 'cl' in list_tag:
                            list_lemmatized.append(dict_lemma['cl'])
                        elif 'i' in list_tag:
                            list_lemmatized.append(dict_lemma['i'])
                        else :
                            list_lemmatized.append(dict_lemma['ponct'])
                    elif nb_pos == 1:
                        list_lemmatized.append(dict_lemma[list_tag[0]])
                    else:
                        list_lemmatized.append(word)
                            
            else:
                list_lemmatized.append(word)
                
        return(" ".join(list_lemmatized))
    
    # Méthode qui réalise le préprocessing d'un texte en français 
    # Prend une string et retourne une string qui a subit 
    #le pré-processing (tokenisation, simplification, tagging, lemmatisation)
    def preprocessing(self, string):
        tokenized_list_of_string = self.tokenize_and_simplify(string)
        list_word_tag = self.tag(tokenized_list_of_string)
        lematized_string = self.lemmatize(list_word_tag)
        return lematized_string