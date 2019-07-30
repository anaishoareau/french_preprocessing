# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 07/2019
GitHub : https://github.com/anaishoareau
Linkedin : https://www.linkedin.com/in/ana%C3%AFs-hoareau-a2a042183/
"""
# MANQUE FONCTION DE SUPRESSION 

# IMPORTS
from french_preprocessing.general_tools import remove_accents
import os

# DEFINITIONS DE LA CLASSE PERMETTANT DE MODIFIER LE LEXIQUE
class LexiqueTools(object):
    
    def __init__(self):
        # Chargement du chemin du dossier tools
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.lexiques_path = self.dir_path + '\\data\\'
        f = open(self.lexiques_path + 'lexique.txt','r')
        f_ss_accent = open(self.lexiques_path + 'lexique_ss_accent.txt','r')
        f_ac_accent = open(self.lexiques_path + 'lexique_ac_accent.txt','r')
        self.lexique = dict(eval(f.read()))
        self.lexique_ss_accent = dict(eval(f_ss_accent.read()))
        self.lexique_ac_accent = dict(eval(f_ac_accent.read()))
    
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
        with open(self.lexiques_path + 'lexique.txt','w') as f:
            f.write(str(self.lexique))
        with open(self.lexiques_path + 'lexique_ss_accent.txt','w') as f:
            f.write(str(self.lexique_ss_accent))
        with open(self.lexiques_path + 'lexique_ac_accent.txt','w') as f:
            f.write(str(self.lexique_ac_accent))
            
    # Méthode qui prend en argument une string, son lemme associé, son tag
    # qui ajoute ce nouvel élément au dictionnaire (ne fait rien s'il y est déjà)
    # ne renvoie rien
    def add_element(self,word, lemma, tag):
        tag_list = ['v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et']
        if tag not in tag_list:
            print("ERROR tag not in the list : 'v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et'")
            return
        else:
            
            # On s'occupe du mot sans transformation
            
            if word not in self.lexique.keys():
                self.lexique[word] = {tag:lemma}
            else:
                self.lexique[word][tag]=lemma
                    
            # On réalise la même opération pour le mot sans accents  
            
            word_ss_accent = remove_accents(word)
            
            if word != word_ss_accent:
                
                # INSERTION DANS LE LEXIQUE GENERAL
                
                # Si le mot a des accents, on regarde sa version sans accent
                if word_ss_accent not in self.lexique.keys():
                    # Si elle n'est pas déjà présente dans le dictionnaire, on l'ajoute avec les tags et lemmes de sa version
                    # avec accents
                    self.lexique[word_ss_accent] = {tag:lemma}
                else:
                    # Sinon on ajoute le tag ou on met à jour la valeur du lemme si le tag existe déjà
                    self.lexique[word_ss_accent][tag] = lemma
                
                # INSERTION DANS LE LEXIQUE DONT LES MOTS ONT DES ACCENTS
                
                # Le mot a des accents et on l'ajoute donc dans lexique_ac_accent si nécessaire    
                if word not in self.lexique_ac_accent.keys():
                    self.lexique[word] = {tag:lemma}
                else:
                    # Sinon on ajoute le tag ou on met à jour la valeur du lemme si le tag existe déjà
                    self.lexique_ac_accent[word][tag]=lemma
            
            else:
                
                # INSERTION DANS LE LEXIQUE DONT LES MOTS N'ONT PAS D'ACCENT
                
                # Le mot n'a pas d'accent et on l'ajoute donc dans lexique_ss_accent si nécessaire
                if word not in self.lexique_ss_accent.keys():
                    self.lexique[word] = {tag:lemma}
                else:
                    # Sinon on ajoute le tag ou on met à jour la valeur du lemme si le tag existe déjà
                    self.lexique_ss_accent[word][tag]=lemma
    
    # Méthode qui permet de supprimer un élement des lexiques
    # Prend en argument le mot à supprimer et son tag (si on ne veut supprimer qu'une version du mot)
    # Ne retourne rien
    def remove_element(self, word, tag):
        tag_list = ['v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et']
        if tag not in tag_list:
            print("ERROR tag not in the list : 'v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et'")
            return
        word_ss_accent = remove_accents(word)
        if word != word_ss_accent:
            # Le mot à donc des accents et il existe une version de lui sans accent
            # on supprime le mot dans ses deux versions dans le lexique
            del self.lexique[word][tag]
            del self.lexique[word_ss_accent][tag]
            # On supprime le mot dans sa version avec accents dans le lexique_ac_accent
            del self.lexique_ac_accent[word][tag]
            # On supprime le mot dans sa version sans accent dans le lexique_ss_accent
            del self.lexique_ss_accent[word_ss_accent][tag]
        else:
            # Le mot n'a pas d'accent
            # On le supprime dans le lexique
            del self.lexique[word][tag]
            # On le supprime dans le lexique_ss_accent
            del self.lexique_ss_accent[word][tag]
     
    # Méthode de mise à jour des lexiques (ajouts et réécriture) 
    # pour un dictionnaire correctement formé
    # Prend en argument le dictionnaire des mots à ajouter et ne renvoie rien
    def lexique_update(self,dictionary):
        
        for word in dictionary.keys():
            for tag in dictionary[word].keys():
                self.add_element(word, dictionary[word][tag],tag)
                
        self.lexique_rewrite()
                
                
        