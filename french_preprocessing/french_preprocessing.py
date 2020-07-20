# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 07/2020
"""
 
# IMPORTS
import os
import re
import torch
import numpy as np

from transformers import AutoTokenizer, AutoModelForTokenClassification

#from nltk.tag import StanfordPOSTagger
from nltk import RegexpTokenizer
#from general_tools import stanford_tag_reduction
from general_tools import camembert_tag_reduction


default_stopwords = ["y","y'","m", "l", "d", "t", "qu", "s","c","m'",'hein', 'celle-là', 'ceux-ci', 'dring', 'sa', 'ollé', 'en', 'a', "d'", 'plutôt', 'auxquels', 'celles-ci', 'dès', 'tel', 'lui-meme', 'quelle', 'les', 'dont', 'aie', 'quand', 'pour', 'où', 'lès', 'suivant', 'ho', 'memes', 'hem', 'surtout', 'mien', 'tellement', 'qui', 'le', 'quels', 'tant', 'une', 'tien', 'ohé', 'i', 'mêmes', 'ceux', "l'", 'quelque', 'si', 'unes', 'lequel', 'tous', 'chacune', 'son', 'que', 'quel', 'au', 'ai', 'celui-là', 'chaque', 'ouste', 'es', 'hep', 'elles-mêmes', 'lors', 'cette', 'cependant', 'toc', 'tsouin', 'chacun', 'seule', 'siennes', 'hum', 'la', 'certains', "t'", 'trop', 'dans', 'desquels', 'lui', 'hors', 'celles-là', 'lui-même', 'pouah', 'toi-même', 'boum', 'vive', 'rend', 'mes', 'vos', 'nous', "qu'", 'des', 'tiens', 'hé', 'lorsque', 'zut', 'vlan', 'mienne', 'na', 'ma', 'selon', "s'", 'vous-mêmes', 'eh', 'ah', 'ses', 'meme', 'lesquels', 'miens', 'vôtres', 'paf', 'pif', 'quant-à-soi', 'tes', "c'", 'sien', 'ça', 'lesquelles', 'tout', 'telles', 'même', 'ces', 'maint', 'notre', 'quanta', 'elle-même', 'aupres', 'bas', 'votre', 'plusieurs', 'moi', 'par', 'hurrah', 'bah', 'laquelle', 'auxquelles', 'vé', 'peux', 'pure', 'tiennes', "aujourd'hui", 'hormis', 'couic', 'vous', 'ore', 'envers', 'moindres', 'aucune', 'gens', 'ouias', 'cela', 'quelles', 'aux', 'pff', 'etc', 'toutefois', 'leurs', 'ton', 'clic', 'las', 'pfut', "t'", 'toutes', 'cet', 'ta', 'da', 'toute', 'aucun', 'o', 'sapristi', 'quoi', 'desquelles', 'té', 'vôtre', 'euh', 'pres', 'as', 'fi', 'ci', 'allo', 'oh', "s'", 'quiconque', 'floc', 'avec', 'se', 'bat', 'tic', 'jusqu', "qu'", 'unique', 'certes', 'celles', 'dire', 'tienne', 'ha', 'nôtre', 'jusque', 'tac', 'ceux-là', 'sienne', 'uns', 'ouf', 'moi-même', 'et', 'vers', 'miennes', 'autrefois', 'houp', 'été', 'à', "d'", 'nouveau', 'être', 'peu', 'dite', "s'", 'dit', 'tels', 'ou', 'toi', 'entre', 'avoir', 'hop', 'delà', 'nos', 'tres', 'telle', 'voilà', 'dessous', 'soit', 'autres', 'psitt', 'hélas', 'anterieur', 'hou', 'près', 'auquel', 'juste', 'chut', 'un', 'stop', 'eux', 'ès', 'vifs', 'ce', 'quoique', 'du', 'moi-meme', 'mon', 'brrr', 'sous', 'parmi', 'deja','déja','celle', 'siens', 'suffisant', 'â', "l'", 'apres', 'sans', 'soi-même', 'là', 'pur', 'via', 'differentes', 'specifique', 'holà', 'tsoin', 'pan', 'car', 'donc', 'dits', 'merci', 'particulièrement', 'nous-mêmes', 'personne', 'allô', 'soi', 'voici', 'sur', 'vif', 'celle-ci', 'malgré', 'puis', 'sauf', 'autre', 'hui', 'ceci', 'leur', 'celui-ci', 'necessairement', 'sacrebleu', 'hue', 'eux-mêmes', 'outre', 'alors', 'desormais', 'plouf', 'longtemps', 'malgre', 'après', 'de', 'oust', 'neanmoins', 'certain', 'crac', 'depuis', 'olé', 'hi', 'te', 'puisque', "m'", 'me', 'ô', 'celui', 'aussi', 'rares', 'chiche', 'rien', 'pfft', "c'", 'vu', 'clac', 'duquel', 'aavons', 'avez', 'ont', 'eu', 'avais', 'avait', 'avions', 'aviez', 'avaient', 'eus', 'eut', 'eûmes', 'eûtes', 'eurent', 'aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient', 'aies', 'ait', 'ayons', 'ayez', 'aient', 'eusse', 'eusses', 'eût', 'eussions', 'eussiez', 'eussent', 'ayant', 'suis', 'est', 'sommes', 'êtes', 'sont', 'étais', 'était', 'étions', 'étiez', 'étaient', 'fus', 'fut', 'fûmes', 'fûtes', 'furent', 'serai', 'seras', 'sera', 'serons', 'serez', 'seront', 'serais', 'serait', 'serions', 'seriez', 'seraient', 'sois', 'soyons', 'soyez', 'soient', 'fusse', 'fusses', 'fût', 'fussions', 'fussiez', 'fussent', 'étant']
#no_stop = ['mais','m’', 'flac', 'désormais', 'cinq', 'naturelles', 'differents', 'cent', 'nombreux', 'dernier', 'exterieur', 'peut', 'allaient', 'maximale', 'retour', 'relative', 'remarquable', 'cher', 'plus', 'tenir', 'chers', 'anterieure', 'afin', 'suivants', 'chez', 'comment', 'partant', 'autrement', 'abord', 'on', 'beau', 'd’', 'différentes', 'precisement', 'vives', 'possessif', 'vivat', 'pourrait', 'enfin', 'effet', 'treize', 'comparables', 'pire', 'parseme', 'compris', 'devers', 'peuvent', 'permet', 'possessifs', 'procedant', 'ainsi', 'bigre', 'avant', 'revoilà', 'naturelle', 'dessus', 'différente', 'quatre-vingt', 'ils', 'beaucoup', 'comparable', 'tu', 'dehors', 'tenant', 'trente', 'minimale', 'suit', 'troisièmement', 'néanmoins', 'ouverts', 'seulement', 'douzième', 'suffit', 'j’', 'toujours', 'quinze', 'ouverte', 'assez', 'anterieures', 'absolument', 'parlent', 'quelconque', 'notamment', 'combien', 't’', 'dix', 'directement', 'onze', 'sixième', 'cinquantaine', 'speculatif', 'dedans', 'différent', 'qu’', 'onzième', 'pu', 'subtiles', 'parler', 'suivre', 'avons', 'quant', 'parfois', 'environ', 'possible', 'non', 'probante', 'bravo', 's', 'moyennant', 'durant', 'restent', 'quelques', 'different', 'certaine', 'première', 'restant', 'devant', 'troisième', 'dix-sept', 'parle', 'premièrement', 'mince', 'revoici', 'c’', 'necessaire', 'uniformement', 'importe', 'ailleurs', 'neuvième', 'ouvert', 'faisaient', 'derrière', 'neuf', 'pas', 'aujourd', 'etais', 'pense', 'tente', 'seul', 'dix-neuf', 'sein', 'autrui', 'certaines', 'huitième', "j'", 'rarement', 'reste', 'vingt', 'encore', 'derriere', 'je', 'parce', 'naturel', 'egale', 'très', 'comme', 'rare', 'quatorze', 'directe', 'quatrième', 'etre', 'façon', 'chères', 'trois', 'nombreuses', 'souvent', 'vas', 'dixième', 'touchant', 'superpose', 'devra', 'strictement', 'plein', 'contre', 'etait', 'multiple', 'semblent', 'egales', "quelqu'un", 'exactement', 'deuxièmement', 'font', 's’', 'deux', 'cinquantième', 'premier', 'tardive', 'etaient', 'concernant', 'diverses', 'attendu', 'debout', 'passé', 'diverse', 'suivante', 'seize', 'proche', 'restrictif', 'allons', 'excepté', 'sept', 'etant', 'divers', 'feront', 'cinquante', 'faisant', 'particulière', 'laisser', 'multiples', 'nul', 'semble', 'pouvait', 'rendre', 'maintenant', 'sait', "n'", 'ni', 'ne', 'pourquoi', 'doit', 'relativement', 'extenso', 'egalement', 'douze', 'vais', 'dix-huit', 'bien', 'tend', 'uniques', 'prealable', 'basee', 'cinquième', 'chère', 'vont', 'derniere', 'deuxième', 'sent', 'n’', 'pourrais', 'va', 'specifiques', 'quatre', 'possibles', 'quarante', 'sinon', 'particulier', 'pendant', 'l’', 'mille', 'suffisante', 'moins', 'semblable', 'suivantes', 'il', 'ils', 'six', 'semblaient', 'différents', 'doivent', 'huit', 'elle', 'elles','septième', 'fais', 'quatrièmement', 'soixante', 'fait', 'probable']
 
class FrenchPreprocessing(object):  

    def __init__(self, stopwords = default_stopwords, symbols = """#§_-@+=*<>()[]{}/\\"'""", punct = """!;:,.?-..."""):

        # Chargement du path du dossier du ficher actuel
        dir_path = os.path.dirname(os.path.abspath(__file__))

        # Chargement du lexique
        f=open(dir_path + '/data/lexique.txt','r', encoding="utf8")
        self.lexique = dict(eval(f.read()))
        
        # Défnition des stopwords
        self.stopwords = stopwords
        self.symbols = symbols
        self.punct = punct
        
        ## INITIALISATION DU TAGGER
        
        # Initialisation des path pour le StanfordPOSTagger
        # jar = dir_path + '/stanford-postagger-full-2018-10-16/stanford-postagger-3.9.2.jar'
        # model = dir_path + '/stanford-postagger-full-2018-10-16/models/french.tagger'
        # self.java_path = java_path
        # os.environ['JAVAHOME'] = self.java_path
        
        # Initialisation du StanfordPOSTagger
        #self.pos_tagger = StanfordPOSTagger(model, jar, encoding = 'utf8')
        
        self.model = AutoModelForTokenClassification.from_pretrained("gilf/french-camembert-postag-model")
        self.tokenizer = AutoTokenizer.from_pretrained("gilf/french-camembert-postag-model")

        
    # La fonction tokenize :
    # - prend en argument une phrase à tokeniser (string)
    # - renvoie une liste contenant les mots de la phrase tokenisée
    def pretokenize(self, string):
        # Supression des espaces non nécessaires
        space = re.compile(r' +')
        string = re.sub(space, ' ', string)
        
        # Harmonisation des numéros de téléphone
        tel = re.compile(r'(?P<sep1>0[0-9])( |/+|\-|\\+)(?P<sep2>[0-9]{2})( |/+|\.|\-|\\+)(?P<sep3>[0-9]{2})( |/+|\.|\-|\\+)(?P<sep4>[0-9]{2})( |/+|\.|\-|\\+)(?P<sep5>[0-9]{2})')
        string = tel.sub(r'\g<sep1>.\g<sep2>.\g<sep3>.\g<sep4>.\g<sep5>',string)
        
        # Tokenisation 
        # Le tokenizer supprime automatiquement les caractères suivant isolés : `^ ° ¤ ¨
        # Reconnait comme token :
        # - Email
        # - Site web, nom de domaine, utilisateur etc
        # - Numéro de téléphone réduit
        # - Nom composé
        # - Mot courant
        # - Ponctuation
        tokenizer = RegexpTokenizer(r'''(\w{2,}'\w+|\w'|[a-zA-ZÀ-Ÿà-ÿ0-9_\.\-]+@[a-zA-ZÀ-Ÿà-ÿ0-9\-\.]+\.[a-zA-ZÀ-Ÿà-ÿ0-9]+|[a-zA-ZÀ-Ÿà-ÿ0-9:@%/;$~_?\+\-=\\\.&\|£€]+[a-zA-ZÀ-Ÿà-ÿ0-9#@%/$~_?\+\-=\\&\|£€]+|[\wÀ-Ÿà-ÿ]+[/\-][\wÀ-Ÿà-ÿ]+|[\wÀ-Ÿà-ÿ0-9]+|\.\.\.|[\(\)\[\]\{\}\"\'\.,;\:\?!\-\_\*\#\§=+<>/\\])''')
        pretokens = tokenizer.tokenize(string)
        return pretokens
    
    # camemBERT tokenisation

    # Tokenisation
    def tag(self, pretokens):
        
        # camemBERT tokenization
        tokens = self.tokenizer(pretokens, is_pretokenized = True, return_tensors="pt")["input_ids"]
        input_ids = self.tokenizer(pretokens, is_pretokenized = True, return_tensors="pt")["input_ids"][0]
        
        # Tagging
        with torch.no_grad():
            entities = self.model(tokens)[0][0].cpu().numpy()
            input_ids = tokens.cpu().numpy()[0]
        
        score = np.exp(entities) / np.exp(entities).sum(-1, keepdims=True)
        labels_idx = score.argmax(axis=-1)
        
        filtered_labels_idx = [(idx, label_idx) for idx, label_idx in enumerate(labels_idx)]
            
        entities = []
        for idx, label_idx in filtered_labels_idx:
            entity = {
                "word": self.tokenizer.convert_ids_to_tokens(int(input_ids[idx])),
                #"score": score[idx][label_idx].item(),
                "entity": self.model.config.id2label[label_idx],
                #"index": idx
            }
            entities += [entity]
    
        # Reshape camemBERT outputs
        entities_reshaped = []
        for e in entities:
            if e['word'] not in ['<s>', '</s>', '▁']:
                e['word'] = re.sub('▁', '', e['word'])
                entities_reshaped.append(e)
        
        entities_reshaped_2 = []
        i,j = 0,0
        while i < len(pretokens):
            if entities_reshaped[j]['word'] == pretokens[i]:
                entities_reshaped_2.append((entities_reshaped[j]['word'].lower(), camembert_tag_reduction(entities_reshaped[j]['entity'])))
                i+=1
                j+=1
            else:
                tag = entities_reshaped[j]['entity'] 
                word = entities_reshaped[j]['word']
                while word != pretokens[i]:
                    j+=1
                    word += entities_reshaped[j]['word']
                entities_reshaped_2.append((word.lower(),camembert_tag_reduction(tag)))
                i+=1
                j+=1
        return entities_reshaped_2


    # La fonction tag :
    # - prend une liste de strings formant une phrase (principe du StanfordPOSTagger)
    # - renvoie une liste de tuples du type : (mot de la liste, son tag)
    # def tag(self, list_of_string):
    #     temp = self.pos_tagger.tag(list_of_string)
    #     list_word_tag = []
    #     # Précédente version de la fonction tag :
    #     # for e in temp:
    #     #     list_word_tag.append((e[0].lower(),stanford_tag_reduction(e[1])))
    #     # Elle supprimait les "_" présents dans les mots. Exemple : user_name -> username.
    #     # La nouvelle version conserve les "_".
    #     for i in range(len(temp)):
    #         list_word_tag.append((list_of_string[i].lower(), stanford_tag_reduction(temp[i][1])))
    #     return list_word_tag
            
    # Suppression des stop_words
    def delete_stopwords(self, list_word_tag):
        reduced_list_word_tag = []
        for i in range(len(list_word_tag)):
            e = list_word_tag[i][0]
            if e.lower() not in self.stopwords:
                reduced_list_word_tag.append((e, list_word_tag[i][1]))
        return reduced_list_word_tag
    
    # Suppression des symboles 
    def delete_symbols(self, list_word_tag):
        reduced_list_word_tag = []
        for i in range(len(list_word_tag)):
            e = list_word_tag[i]
            if e[0] not in self.symbols :
                reduced_list_word_tag.append((e[0], e[1]))
        return reduced_list_word_tag
    
    # Suppression de la ponctuation
    def delete_punct(self, list_word_tag):
        reduced_list_word_tag = []
        for i in range(len(list_word_tag)):
            e = list_word_tag[i]
            if e[0] not in self.punct :
                reduced_list_word_tag.append((e[0], e[1]))
        return reduced_list_word_tag
    
    # La fonction lemmatise :
    # - prend en argument une liste de tuples du type (mot de la liste, son tag)
    # - renvoie une liste qui contient les mots de la phrase lemmatisés (strings)
    def lemmatize(self, reduced_list_word_tag):
        list_lemmatized = []
        
        for e in reduced_list_word_tag:
            word = e[0].lower()
            tag = e[1]
            lexique = self.lexique 
            # On lemmatise
            if word in lexique.keys():
                dict_lemma = lexique[word]
                if tag in dict_lemma.keys():
                    list_lemmatized.append(dict_lemma[tag])
                else:
                    list_lemmatized.append(word)
            else:
                list_lemmatized.append(word)
                
        return " ".join(list_lemmatized)
    
    # Méthode qui réalise le préprocessing d'un texte en français 
    # Prend une string et retourne une string qui a subit 
    #le pré-processing (tokenisation, tagging, simplification, lemmatisation)
    def preprocessing(self, string):
        pretokens = self.pretokenize(string)
        list_word_tag = self.tag(pretokens)
        reduced_list_word_tag = self.delete_stopwords(list_word_tag)
        reduced_list_word_tag = self.delete_symbols(reduced_list_word_tag)
        reduced_list_word_tag = self.delete_punct(reduced_list_word_tag)
        lematized_string = self.lemmatize(reduced_list_word_tag)
        return lematized_string
