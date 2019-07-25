# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 07/2019
GitHub : https://github.com/anaishoareau
Linkedin : https://www.linkedin.com/in/ana%C3%AFs-hoareau-a2a042183/
"""

# Fonction qui permet de supprimer les accents d'une string
# Prend une string et renvoie la string équivalente sans accents
def remove_accents(string):
    import unicodedata
    try:
        string = unicode(string, 'utf-8')
    except (TypeError, NameError):
        pass
    string = unicodedata.normalize('NFD', string)
    string = string.encode('ascii', 'ignore')
    string = string.decode("utf-8")
    return str(string)

#Les fonctions suivantes permettent d'uniformiser les tags utilisés 
#par les autres outils.
#
#Les tags qu'on conserve sont : 'v', 'nc', 'adj', 'c', 'npp', 'adv', 
#'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et'.

# Fonction de réduction des tags du StanfordPOSTagger
#Tags d'origine du StanfordPOSTagger : 'A','ADJ', 'ADJWH','ADV','ADVWH','C','CC',
#'CL','CLO','CLR','CLS','CS','DET','DETWH','ET','I','N','NC','NPP','P','PREF',
#'PRO','PROREL','PROWH','PUNC','V','VIMP','VINF','VPP','VPR','VS'
def stanford_tag_reduction(tag):
    tag_reduc = ''
    if tag in ['VS', 'VINF', 'VPP', 'VPR', 'VIMP']:
        tag_reduc = 'V'
    elif tag in ['N','PREF']:
        tag_reduc = 'NC'
    elif tag in ['CS', 'CC']:
        tag_reduc = 'C'
    elif tag in ['CLS', 'CLO', 'CLR']:
        tag_reduc = 'CL'
    elif tag in ['ADJWH', 'A']:
        tag_reduc = 'ADJ'
    elif tag == 'ADVWH':
        tag_reduc = 'ADV'
    elif tag in ['PROREL', 'PROWH']:
        tag_reduc = 'PRO'
    elif tag in ['DETWH']:
        tag_reduc = 'DET'
    elif tag == 'PUNC':
        tag_reduc = 'PONCT'
    elif tag == 'P':
        tag_reduc = 'PREP'
    else:
        tag_reduc = tag
        
    return(tag_reduc.lower())
    
# Fonction de réduction des tags présents à l'origine dans le Lexique382
#Tags d'origine du Lexique382 : 'ADV', 'ADJ','PRO', 'PRE', 'NOM', 'VER', 'ONO', 
#'CON', 'AUX', 'ART', 'EXP'
def lexique383_tag_reduction(tag):
    nouveau_tag = ''
    if tag == 'NOM':
        nouveau_tag = 'nc'
    elif tag == 'VER' or tag == 'AUX':
        nouveau_tag = 'v'
    elif tag == 'CON':
        nouveau_tag = 'c'
    elif tag == 'ONO':
        nouveau_tag = 'i'
    elif tag == 'ART':
        nouveau_tag = 'det'
    elif tag == 'PRE':
        nouveau_tag = 'prep'
    elif tag == 'EXP':
        nouveau_tag = 'cl'
    else:
        nouveau_tag = tag.lower()
    
    return nouveau_tag

# Fonction qui permet de générer les formes conjuguées des verbes du 1er groupe  
def conjug_1(first_group_verb, category):  
    ending = ['er', 'e', 'es', 'ons', 'ez', 'ent', 'é', 'ais', 'ait', 'ions', 'iez', 'aient', 'ai', 'as', 'a', 'âmes',
                   'âtes', 'èrent', 'erai', 'eras', 'era', 'erons', 'erez', 'eront', 'erais', 'erait', 'erions', 'eriez',
                   'eraient', 'asse', 'asses', 'ât', 'assions', 'assiez', 'assent', 'ant']
    conjug = []
    for en in ending:
        conjug.append([first_group_verb[:-2]+en, first_group_verb, 'v', category])
    return conjug

# Fonction qui permet de générer les formes conjuguées des verbes du 2eme groupe 
def conjug_2(second_group_verb, category):
    ending = ['ir', 'is', 'it', 'issons', 'issez', 'issent', 'issais', 'issait', 'issions', 
                     'issiez', 'issaient', 'îmes', 'îtes', 'irent', 'irai', 'iras', 'ira', 'irons', 
                     'irez', 'iront', 'irais', 'irait', 'irions', 'iriez', 'iraient', 'isse', 'isses', 
                     'issions', 'issiez', 'issent', 'i', 'issant']
    conjug = []
    for en in ending:
        conjug.append([second_group_verb[:-2]+en, second_group_verb, 'v', category])
    return conjug
                