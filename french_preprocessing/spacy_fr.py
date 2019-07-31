# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 07/2019
GitHub : https://github.com/anaishoareau
Linkedin : https://www.linkedin.com/in/ana%C3%AFs-hoareau-a2a042183/
"""


import spacy
import os

class SpacyFr(object):
    
    def __init__(self):
        try:
            self.nlp = spacy.load('fr_core_news_sm')
        except:
            # Si il y a besoin de préciser le proxy, il faut rajouter les lignes suivantes :
            #proxy='nom de votre proxy'
            #os.environ['http_proxy'] = proxy
            #os.environ['HTTP_PROXY'] = proxy
            #os.environ['https_proxy'] = proxy
            #os.environ['HTTPS_PROXY'] = proxy
            
            os.system('python -m spacy download fr_core_news_sm')
            self.nlp = spacy.load('fr_core_news_sm')
        
        
    def init_stop_words(self):
        stop = ["m", "l", "d", "t", "qu", "s","c","m'", 'hein', 'celle-là', 'ceux-ci', 'dring', 'sa', 'ollé', 'en', 'a', "d'", 'plutôt', 'auxquels', 'celles-ci', 'dès', 'tel', 'lui-meme', 'quelle', 'les', 'dont', 'aie', 'quand', 'pour', 'où', 'lès', 'suivant', 'ho', 'memes', 'hem', 'surtout', 'mien', 'tellement', 'qui', 'le', 'quels', 'tant', 'une', 'tien', 'ohé', 'i', 'mêmes', 'ceux', "l'", 'quelque', 'si', 'unes', 'lequel', 'tous', 'chacune', 'son', 'que', 'quel', 'au', 'ai', 'celui-là', 'chaque', 'ouste', 'es', 'hep', 'elles-mêmes', 'lors', 'cette', 'cependant', 'toc', 'tsouin', 'chacun', 'seule', 'siennes', 'hum', 'la', 'certains', "t'", 'trop', 'dans', 'desquels', 'lui', 'hors', 'celles-là', 'lui-même', 'pouah', 'toi-même', 'boum', 'vive', 'rend', 'mes', 'vos', 'nous', "qu'", 'des', 'tiens', 'hé', 'lorsque', 'zut', 'vlan', 'mienne', 'na', 'ma', 'selon', "s'", 'vous-mêmes', 'eh', 'ah', 'ses', 'meme', 'lesquels', 'miens', 'vôtres', 'paf', 'pif', 'quant-à-soi', 'tes', "c'", 'sien', 'ça', 'lesquelles', 'tout', 'telles', 'même', 'ces', 'maint', 'notre', 'quanta', 'elle-même', 'aupres', 'bas', 'votre', 'plusieurs', 'moi', 'par', 'hurrah', 'bah', 'laquelle', 'auxquelles', 'vé', 'peux', 'pure', 'tiennes', "aujourd'hui", 'hormis', 'couic', 'vous', 'ore', 'envers', 'moindres', 'aucune', 'gens', 'ouias', 'cela', 'quelles', 'aux', 'pff', 'etc', 'toutefois', 'leurs', 'ton', 'clic', 'las', 'pfut', "t'", 'toutes', 'cet', 'ta', 'da', 'toute', 'aucun', 'o', 'sapristi', 'quoi', 'desquelles', 'té', 'vôtre', 'euh', 'pres', 'as', 'fi', 'ci', 'allo', 'oh', "s'", 'quiconque', 'floc', 'avec', 'se', 'bat', 'tic', 'jusqu', "qu'", 'unique', 'certes', 'celles', 'dire', 'tienne', 'ha', 'nôtre', 'jusque', 'tac', 'ceux-là', 'sienne', 'uns', 'ouf', 'moi-même', 'et', 'vers', 'miennes', 'autrefois', 'houp', 'été', 'à', "d'", 'nouveau', 'être', 'peu', 'dite', "s'", 'dit', 'elles', 'tels', 'ou', 'toi', 'entre', 'avoir', 'hop', 'delà', 'nos', 'tres', 'telle', 'voilà', 'dessous', 'soit', 'autres', 'psitt', 'hélas', 'anterieur', 'hou', 'près', 'auquel', 'juste', 'chut', 'un', 'stop', 'eux', 'ès', 'vifs', 'ce', 'quoique', 'du', 'moi-meme', 'mon', 'brrr', 'sous', 'parmi', 'deja', 'celle', 'siens', 'suffisant', 'â', "l'", 'apres', 'sans', 'soi-même', 'là', 'pur', 'via', 'differentes', 'specifique', 'holà', 'tsoin', 'pan', 'car', 'donc', 'dits', 'merci', 'particulièrement', 'nous-mêmes', 'personne', 'allô', 'soi', 'voici', 'sur', 'vif', 'celle-ci', 'malgré', 'puis', 'sauf', 'autre', 'hui', 'ceci', 'leur', 'celui-ci', 'necessairement', 'sacrebleu', 'hue', 'eux-mêmes', 'outre', 'alors', 'desormais', 'plouf', 'longtemps', 'malgre', 'après', 'de', 'oust', 'neanmoins', 'certain', 'crac', 'depuis', 'olé', 'hi', 'te', 'puisque', "m'", 'me', 'ô', 'celui', 'aussi', 'rares', 'chiche', 'rien', 'pfft', "c'", 'vu', 'clac', 'duquel', 'aavons', 'avez', 'ont', 'eu', 'avais', 'avait', 'avions', 'aviez', 'avaient', 'eus', 'eut', 'eûmes', 'eûtes', 'eurent', 'aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient', 'aies', 'ait', 'ayons', 'ayez', 'aient', 'eusse', 'eusses', 'eût', 'eussions', 'eussiez', 'eussent', 'ayant', 'suis', 'est', 'sommes', 'êtes', 'sont', 'étais', 'était', 'étions', 'étiez', 'étaient', 'fus', 'fut', 'fûmes', 'fûtes', 'furent', 'serai', 'seras', 'sera', 'serons', 'serez', 'seront', 'serais', 'serait', 'serions', 'seriez', 'seraient', 'sois', 'soyons', 'soyez', 'soient', 'fusse', 'fusses', 'fût', 'fussions', 'fussiez', 'fussent', 'étant']
        no_stop = ['m’', 'flac', 'désormais', 'cinq', 'naturelles', 'differents', 'cent', 'nombreux', 'dernier', 'exterieur', 'peut', 'allaient', 'maximale', 'retour', 'relative', 'remarquable', 'cher', 'plus', 'tenir', 'chers', 'anterieure', 'afin', 'suivants', 'chez', 'comment', 'partant', 'autrement', 'abord', 'on', 'beau', 'd’', 'différentes', 'precisement', 'vives', 'possessif', 'vivat', 'pourrait', 'enfin', 'effet', 'treize', 'comparables', 'pire', 'parseme', 'compris', 'devers', 'peuvent', 'permet', 'possessifs', 'procedant', 'ainsi', 'bigre', 'avant', 'revoilà', 'naturelle', 'dessus', 'différente', 'quatre-vingt', 'ils', 'beaucoup', 'comparable', 'tu', 'dehors', 'tenant', 'trente', 'minimale', 'suit', 'troisièmement', 'néanmoins', 'ouverts', 'seulement', 'douzième', 'suffit', 'j’', 'toujours', 'quinze', 'ouverte', 'assez', 'anterieures', 'absolument', 'parlent', 'quelconque', 'notamment', 'combien', 't’', 'dix', 'directement', 'onze', 'sixième', 'cinquantaine', 'speculatif', 'dedans', 'différent', 'qu’', 'onzième', 'pu', 'subtiles', 'parler', 'suivre', 'avons', 'quant', 'parfois', 'environ', 'possible', 'non', 'probante', 'mais', 'bravo', 's', 'moyennant', 'durant', 'restent', 'quelques', 'different', 'certaine', 'première', 'restant', 'devant', 'troisième', 'dix-sept', 'parle', 'premièrement', 'mince', 'revoici', 'c’', 'necessaire', 'uniformement', 'importe', 'ailleurs', 'neuvième', 'ouvert', 'faisaient', 'derrière', 'neuf', 'pas', 'aujourd', 'etais', 'pense', 'tente', 'seul', 'dix-neuf', 'sein', 'autrui', 'certaines', 'huitième', "j'", 'rarement', 'reste', 'vingt', 'encore', 'derriere', 'je', 'parce', 'naturel', 'egale', 'très', 'comme', 'rare', 'quatorze', 'directe', 'quatrième', 'etre', 'façon', 'chères', 'trois', 'nombreuses', 'souvent', 'vas', 'dixième', 'touchant', 'superpose', 'devra', 'strictement', 'plein', 'contre', 'etait', 'multiple', 'semblent', 'egales', "quelqu'un", 'exactement', 'deuxièmement', 'font', 's’', 'deux', 'cinquantième', 'premier', 'tardive', 'etaient', 'concernant', 'diverses', 'attendu', 'debout', 'passé', 'diverse', 'suivante', 'seize', 'proche', 'restrictif', 'allons', 'excepté', 'sept', 'etant', 'divers', 'feront', 'cinquante', 'faisant', 'particulière', 'laisser', 'multiples', 'nul', 'semble', 'pouvait', 'rendre', 'maintenant', 'sait', "n'", 'ni', 'ne', 'pourquoi', 'doit', 'relativement', 'extenso', 'egalement', 'douze', 'vais', 'dix-huit', 'bien', 'tend', 'uniques', 'prealable', 'basee', 'cinquième', 'chère', 'vont', 'derniere', 'deuxième', 'sent', 'n’', 'pourrais', 'va', 'specifiques', 'quatre', 'possibles', 'quarante', 'sinon', 'particulier', 'pendant', 'l’', 'mille', 'suffisante', 'moins', 'semblable', 'suivantes', 'il', 'six', 'semblaient', 'différents', 'doivent', 'huit', 'elle', 'septième', 'fais', 'quatrièmement', 'soixante', 'fait', 'probable']
        for e in no_stop:
            self.nlp.vocab[e].is_stop = False

        for e in stop:
            self.nlp.vocab[e].is_stop = True


