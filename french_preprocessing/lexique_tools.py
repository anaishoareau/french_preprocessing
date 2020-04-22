# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 04/2020
"""

# IMPORTS 

import os

# DEFINITIONS DE LA CLASSE PERMETTANT DE MODIFIER LE LEXIQUE
class LexiqueTools(object):
    
    def __init__(self):

        # Chargement du path du dossier du ficher actuel
        dir_path = os.path.dirname(os.path.abspath(__file__))
        
        # Chargement du lexique
        f=open(dir_path + '/data/lexique.txt','r')

        self.lexique = dict(eval(f.read()))

    # Méthode qui prend en argument une string 
    # qui renvoie False si le mot n'est pas dans le dictionnaire 
    # qui renvoie la valeur associée à la clé correspondante à la string sinon
    def in_lexique(self, word):
         if word in self.lexique.keys():
             return self.lexique[word]
         else:
             return False
    
    # Methode de réécriture des lexiques
    # Ne prend rien en argument et ne renvoie rien
    # Doit être utilisée après les ajouts ou les suppressions
    def lexique_rewrite(self):
        self.f.write(str(self.lexique))

    # Méthode qui prend en argument une string, son lemme associé, son tag
    # qui ajoute ce nouvel élément au dictionnaire (ne fait rien s'il y est déjà)
    # ne renvoie rien
    def add_element(self,word, lemma, tag):
        tag_list = ['v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et']
        if tag not in tag_list:
            print("ERROR tag not in the list : 'v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et'")
            return
        else:
            if word not in self.lexique.keys():
                self.lexique[word] = {tag:lemma}
            else:
                self.lexique[word][tag]=lemma
                    
    # Méthode qui permet de supprimer un élement des lexiques
    # Prend en argument le mot à supprimer et son tag (si on ne veut supprimer qu'une version du mot)
    # Ne retourne rien
    def remove_element(self, word, tag):
        tag_list = ['v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et']
        if tag not in tag_list:
            print("ERROR tag not in the list : 'v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et'")
            return
        else:
            del self.lexique[word][tag]

    # Méthode de mise à jour des lexiques (ajouts et réécriture) 
    # pour un dictionnaire correctement formé
    # Prend en argument le dictionnaire des mots à ajouter et ne renvoie rien
    def lexique_update(self,dictionary):
        
        for word in dictionary.keys():
            for tag in dictionary[word].keys():
                self.add_element(word, dictionary[word][tag],tag)
                
        self.lexique_rewrite()