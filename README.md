# FrenchPreprocessing

#### Utilisation du modèle CamemBERT pour le tagging.

Package regroupant des outils de pré-traitement pour les textes en langue française : 
tokenisation, simplification, tagging (Part-of-Speech tagging) et lemmatisation.

## Installation

Vérifier que la commande pip est installée, ainsi que git : https://packaging.python.org/tutorials/installing-packages/

#### Pour installer le package french_preprocessing, executer la commande :

```bash 
pip install git+https://github.com/anaishoareau/french_preprocessing.git
```

#### ATTENTION : Cette commande installe aussi les dépendances. Si vous rencontrez des problèmes, il faut les installer à part.

Versions utilisées :  

nltk - 3.4  
numpy - 1.18.1  
torch - 1.5.1 (Informations d'installation : https://pytorch.org/)   
transformers - 3.0.2  

#### ATTENTON : Pour que le french_preprocessing fonctionne, il faut avoir installé java (JRE) : https://www.java.com/fr/download/ et donner le path du fichier java.exe à l'initialisation du FrenchPreprocessing, un exemple est proposé après.

## Objectifs et réalisations du projet

### Création d'un outil complet de préprocessing pour le français : 

- Tokenisation : Transformation de texte en tokens (unités lexicales)

- Grammatical tagging : Etiquetage grammatical (Part-of-speech tagging), autrement dit, l'association 
de tags grammaticaux (ex: 'nc' pour nom commun, 'v' pour verbe...) aux tokens d'un texte

- Simplification : Suppression des stopwords (mots à faible valeur lexicale comme 'le', 
"t'", 'dring'...), suppression de la ponctuation

- Lemmatisation : Remplacement des tokens d'un texte par leur lemme ("forme canonique" 
du mot, utilisée dans les dictionnaires)

### Précisions sur le travail effectué

- Tokenisation réalisée par le RegexpTokenizer de NLTK avec une expression régulière créée pour le projet et qui permet de reconnaître, en plus des unités lexicales courantes du français, les adresses emails, numéros de téléphone, noms de domaines, etc. 

- Synthétisation de trois lexiques en un seul (lexique.txt): Lexique des formes fléchies du français (LEFFF), le Lexique 3.83, et le lexique utilisé par la librairie python spaCy pour créer une base de données développée pour l'outil de lemmatisation.

- Uniformisation des tags utilisés dans les deux lexiques (LEFFF et Lexique 3.83) et tagging des données du lexique de spaCy 
à l'aide du StandfordPOSTagger pour intégrer le 'tag' en paramètre de l'outil de lemmatisation. Les tags du modèle CamemBERT sont aussi uniformisés.
Les tags après uniformisation sont réduits à : 'v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 
'prep', 'i', 'ponct', 'cl', 'et'

- Récupération du tagging effectué par CamemBERT avec gestion des séquences de plus de 512 tokens (tokens de la forme utilisée par le tokenizer RoBERTa).

- Développement d'outils dans lexique_tools.py pour la modification du lexique afin de l'augmenter facilement, 
sans compromettre les fichiers texte.

- Création d'outils généraux dans general_tools.py pour appliquer la réduction de tag (réduction adaptée 
aux tags du StanfordPOSTagger, et aux tags du Lexique 3.83), obtenir toutes les formes conjuguées des verbes réguliers du français (1er et 2ème groupe).

## Sources et crédits 

#### LEXIQUE 3.83 : 

- PALLIER Christophe, NEW Boris, 2019 Openlexicon, GitHub repository, 
https://github.com/chrplr/openlexicon

- NEW Boris, PALLIER Christophe, BRYSBAERT Marc and FERRAND Ludovic. 2004. 
"Lexique 2: A New French Lexical Database." Behavior Research Methods, 
Instruments, & Computers 36 (3): 516–524. https://link.springer.com/article/10.3758/BF03195598

- NEW Boris, PALLIER Christophe, FERRAND Ludovic and MATOS Rafael. 2001. 
"Une Base de Données Lexicales Du Français Contemporain Sur Internet: LEXIQUE" 
L’Année Psychologique 101 (3): 447–462. 
https://www.persee.fr/doc/psy_0003-5033_2001_num_101_3_1341

- NEW Boris, BRYSBAERT Marc, VERONIS Jean, and PALLIER Christophe. 2007. 
"The Use of Film Subtitles to Estimate Word Frequencies." 
Applied Psycholinguistics 28 (4): 661–77. https://doi.org/10.1017/S014271640707035X

#### LEFFF (Morphological and syntactic lexicon for French) :

- SAGOT Benoît. 2010. "The Lefff, a freely available and large-coverage morphological 
and syntactic lexicon for French." In Proceedings of the 7th international conference 
on Language Resources and Evaluation (LREC 2010), Istanbul, Turkey. https://hal.inria.fr/inria-00521242/

- COULOMBE Claude, FrenchLefffLemmatizer, GitHub repository, 
https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer

#### spaCy :

- spaCy, GitHub repository, https://github.com/explosion/spaCy

#### CamemBERT :

- MARTIN Louis, MULLER Benjamin, SUÁREZ Pedro Javier Ortiz, et al. 2019. "Camembert: a tasty french language model." arXiv preprint arXiv:1911.03894. https://arxiv.org/abs/1911.03894

- MARTIN Louis, MULLER Benjamin, SUÁREZ Pedro Javier Ortiz, et al. "Les modèles de langue contextuels Camembert pour le français: impact de la taille et de l'hétérogénéité des données d'entrainement." In : Actes de la 6e conférence conjointe Journées d'Études sur la Parole (JEP, 31e édition), Traitement Automatique des Langues Naturelles (TALN, 27e édition), Rencontre des Étudiants Chercheurs en Informatique pour le Traitement Automatique des Langues (RÉCITAL, 22e édition). Volume 2: Traitement Automatique des Langues Naturelles. ATALA, 2020. p. 54-65. https://hal.archives-ouvertes.fr/hal-02784755/

### Licences and Copyrights : 

- License Lexique 3.83 : Attribution-ShareAlike 4.0 International, https://github.com/chrplr/openlexicon/blob/master/LICENSE.txt
- License spaCy : The MIT License (MIT), https://github.com/explosion/spaCy/blob/master/LICENSE
- Copyright spaCy : Copyright (C) 2016-2019 ExplosionAI GmbH, 2016 spaCy GmbH, 2015 Matthew Honnibal
- Transformers : Apache License, https://github.com/huggingface/transformers/blob/master/LICENSE
- License CamemBERT :  MIT License, https://camembert-model.fr/
- FrenchLefffLemmatizer : Lesser General Public License For Linguistic Resources, https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer/blob/master/LICENSE


## french_preprocessing.py : Détail des méthodes et exemples d'utilisation

#### Initialisation de la classe FrenchPreprocessing :

Les éléments par défaut sont : 
```python
default_stopwords = ["y","y'","m", "l", "d", "t", "qu", "s","c","m'",'hein', 'celle-là', 'ceux-ci', 'dring', 'sa', 'ollé', 'en', 'a', "d'", 'plutôt', 'auxquels', 'celles-ci', 'dès', 'tel', 'lui-meme', 'quelle', 'les', 'dont', 'aie', 'quand', 'pour', 'où', 'lès', 'suivant', 'ho', 'memes', 'hem', 'surtout', 'mien', 'tellement', 'qui', 'le', 'quels', 'tant', 'une', 'tien', 'ohé', 'i', 'mêmes', 'ceux', "l'", 'quelque', 'si', 'unes', 'lequel', 'tous', 'chacune', 'son', 'que', 'quel', 'au', 'ai', 'celui-là', 'chaque', 'ouste', 'es', 'hep', 'elles-mêmes', 'lors', 'cette', 'cependant', 'toc', 'tsouin', 'chacun', 'seule', 'siennes', 'hum', 'la', 'certains', "t'", 'trop', 'dans', 'desquels', 'lui', 'hors', 'celles-là', 'lui-même', 'pouah', 'toi-même', 'boum', 'vive', 'rend', 'mes', 'vos', 'nous', "qu'", 'des', 'tiens', 'hé', 'lorsque', 'zut', 'vlan', 'mienne', 'na', 'ma', 'selon', "s'", 'vous-mêmes', 'eh', 'ah', 'ses', 'meme', 'lesquels', 'miens', 'vôtres', 'paf', 'pif', 'quant-à-soi', 'tes', "c'", 'sien', 'ça', 'lesquelles', 'tout', 'telles', 'même', 'ces', 'maint', 'notre', 'quanta', 'elle-même', 'aupres', 'bas', 'votre', 'plusieurs', 'moi', 'par', 'hurrah', 'bah', 'laquelle', 'auxquelles', 'vé', 'peux', 'pure', 'tiennes', "aujourd'hui", 'hormis', 'couic', 'vous', 'ore', 'envers', 'moindres', 'aucune', 'gens', 'ouias', 'cela', 'quelles', 'aux', 'pff', 'etc', 'toutefois', 'leurs', 'ton', 'clic', 'las', 'pfut', "t'", 'toutes', 'cet', 'ta', 'da', 'toute', 'aucun', 'o', 'sapristi', 'quoi', 'desquelles', 'té', 'vôtre', 'euh', 'pres', 'as', 'fi', 'ci', 'allo', 'oh', "s'", 'quiconque', 'floc', 'avec', 'se', 'bat', 'tic', 'jusqu', "qu'", 'unique', 'certes', 'celles', 'dire', 'tienne', 'ha', 'nôtre', 'jusque', 'tac', 'ceux-là', 'sienne', 'uns', 'ouf', 'moi-même', 'et', 'vers', 'miennes', 'autrefois', 'houp', 'été', 'à', "d'", 'nouveau', 'être', 'peu', 'dite', "s'", 'dit', 'tels', 'ou', 'toi', 'entre', 'avoir', 'hop', 'delà', 'nos', 'tres', 'telle', 'voilà', 'dessous', 'soit', 'autres', 'psitt', 'hélas', 'anterieur', 'hou', 'près', 'auquel', 'juste', 'chut', 'un', 'stop', 'eux', 'ès', 'vifs', 'ce', 'quoique', 'du', 'moi-meme', 'mon', 'brrr', 'sous', 'parmi', 'deja','déja','celle', 'siens', 'suffisant', 'â', "l'", 'apres', 'sans', 'soi-même', 'là', 'pur', 'via', 'differentes', 'specifique', 'holà', 'tsoin', 'pan', 'car', 'donc', 'dits', 'merci', 'particulièrement', 'nous-mêmes', 'personne', 'allô', 'soi', 'voici', 'sur', 'vif', 'celle-ci', 'malgré', 'puis', 'sauf', 'autre', 'hui', 'ceci', 'leur', 'celui-ci', 'necessairement', 'sacrebleu', 'hue', 'eux-mêmes', 'outre', 'alors', 'desormais', 'plouf', 'longtemps', 'malgre', 'après', 'de', 'oust', 'neanmoins', 'certain', 'crac', 'depuis', 'olé', 'hi', 'te', 'puisque', "m'", 'me', 'ô', 'celui', 'aussi', 'rares', 'chiche', 'rien', 'pfft', "c'", 'vu', 'clac', 'duquel', 'aavons', 'avez', 'ont', 'eu', 'avais', 'avait', 'avions', 'aviez', 'avaient', 'eus', 'eut', 'eûmes', 'eûtes', 'eurent', 'aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient', 'aies', 'ait', 'ayons', 'ayez', 'aient', 'eusse', 'eusses', 'eût', 'eussions', 'eussiez', 'eussent', 'ayant', 'suis', 'est', 'sommes', 'êtes', 'sont', 'étais', 'était', 'étions', 'étiez', 'étaient', 'fus', 'fut', 'fûmes', 'fûtes', 'furent', 'serai', 'seras', 'sera', 'serons', 'serez', 'seront', 'serais', 'serait', 'serions', 'seriez', 'seraient', 'sois', 'soyons', 'soyez', 'soient', 'fusse', 'fusses', 'fût', 'fussions', 'fussiez', 'fussent', 'étant']
default_symbols = """#§_-@+=*<>()[]{}/\\"'"""
default_punct = """!;:,.?-..."""
```

On peut imaginer compléter la liste default_stopwords par de nouveaux stopwords comme : 
```python
other_stopwords = ['mais','m’', 'flac', 'désormais', 'cinq', 'naturelles', 'differents', 'cent', 'nombreux', 'dernier', 'exterieur', 'peut', 'allaient', 'maximale', 'retour', 'relative', 'remarquable', 'cher', 'plus', 'tenir', 'chers', 'anterieure', 'afin', 'suivants', 'chez', 'comment', 'partant', 'autrement', 'abord', 'on', 'beau', 'd’', 'différentes', 'precisement', 'vives', 'possessif', 'vivat', 'pourrait', 'enfin', 'effet', 'treize', 'comparables', 'pire', 'parseme', 'compris', 'devers', 'peuvent', 'permet', 'possessifs', 'procedant', 'ainsi', 'bigre', 'avant', 'revoilà', 'naturelle', 'dessus', 'différente', 'quatre-vingt', 'ils', 'beaucoup', 'comparable', 'tu', 'dehors', 'tenant', 'trente', 'minimale', 'suit', 'troisièmement', 'néanmoins', 'ouverts', 'seulement', 'douzième', 'suffit', 'j’', 'toujours', 'quinze', 'ouverte', 'assez', 'anterieures', 'absolument', 'parlent', 'quelconque', 'notamment', 'combien', 't’', 'dix', 'directement', 'onze', 'sixième', 'cinquantaine', 'speculatif', 'dedans', 'différent', 'qu’', 'onzième', 'pu', 'subtiles', 'parler', 'suivre', 'avons', 'quant', 'parfois', 'environ', 'possible', 'non', 'probante', 'bravo', 's', 'moyennant', 'durant', 'restent', 'quelques', 'different', 'certaine', 'première', 'restant', 'devant', 'troisième', 'dix-sept', 'parle', 'premièrement', 'mince', 'revoici', 'c’', 'necessaire', 'uniformement', 'importe', 'ailleurs', 'neuvième', 'ouvert', 'faisaient', 'derrière', 'neuf', 'pas', 'aujourd', 'etais', 'pense', 'tente', 'seul', 'dix-neuf', 'sein', 'autrui', 'certaines', 'huitième', "j'", 'rarement', 'reste', 'vingt', 'encore', 'derriere', 'je', 'parce', 'naturel', 'egale', 'très', 'comme', 'rare', 'quatorze', 'directe', 'quatrième', 'etre', 'façon', 'chères', 'trois', 'nombreuses', 'souvent', 'vas', 'dixième', 'touchant', 'superpose', 'devra', 'strictement', 'plein', 'contre', 'etait', 'multiple', 'semblent', 'egales', "quelqu'un", 'exactement', 'deuxièmement', 'font', 's’', 'deux', 'cinquantième', 'premier', 'tardive', 'etaient', 'concernant', 'diverses', 'attendu', 'debout', 'passé', 'diverse', 'suivante', 'seize', 'proche', 'restrictif', 'allons', 'excepté', 'sept', 'etant', 'divers', 'feront', 'cinquante', 'faisant', 'particulière', 'laisser', 'multiples', 'nul', 'semble', 'pouvait', 'rendre', 'maintenant', 'sait', "n'", 'ni', 'ne', 'pourquoi', 'doit', 'relativement', 'extenso', 'egalement', 'douze', 'vais', 'dix-huit', 'bien', 'tend', 'uniques', 'prealable', 'basee', 'cinquième', 'chère', 'vont', 'derniere', 'deuxième', 'sent', 'n’', 'pourrais', 'va', 'specifiques', 'quatre', 'possibles', 'quarante', 'sinon', 'particulier', 'pendant', 'l’', 'mille', 'suffisante', 'moins', 'semblable', 'suivantes', 'il', 'ils', 'six', 'semblaient', 'différents', 'doivent', 'huit', 'elle', 'elles','septième', 'fais', 'quatrièmement', 'soixante', 'fait', 'probable']
```

Initialisation de l'outil :
```python
from french_preprocessing.french_preprocessing import FrenchPreprocessing

fp = FrenchPreprocessing(java_path = "C:/Program Files (x86)/Java/jre1.8.0_251/bin/java.exe", stopwords = default_stopwords, symbols = default_symbols, punct = default_punct)
```
#### Méthodes de la classe FrenchPreprocessing :

##### - fp.pretokenize(string)

Prend une string en entrée et retourne une liste de string formée des prétokens 
de la string d'entrée en enlevant les symboles inutiles : [token1, token2].

Exemples :

```python 
# Définitions des chaines de caractères

string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! (Un jour, j'en suis certaine, ils contrôleront le monde...) #chats #révolution"

complex_string = """Aujourd'hui j'ai plein d'adresses à tester comme http://test.com/eelg/.
En voici quelques unes : https://www.example.com/, www.example.com/etcetc, example.com/etcetc, mais j'ai aussi des adresses emails : zeofjreoigjerigjer@gmail.com et krjr@offo.edu.au.
Voici d'autres tests ; user:pass@example.com/etcetc (www.exemple.com) et example.com/etcetc?query=aasd.
Mon numéro de téléphone est le 06 02 02 02 02 mais on peut aussi me joindre au 07/02/02/02/02 !"""

# Applications de la méthode tokenize

fp.tokenize(string)

>>> ["J'", 'aime', 'les', 'chats', '.', 'Ce', 'sont', 'vraiment', 'des', 'êtres', 'supérieurs', '!', '(', 'Un', 'jour', ',', "j'", 'en', 'suis', 'certaine', ',', 'ils', 'contrôleront', 'le', 'monde', '...', ')', '#', 'chats', '#', 'révolution']

fp.tokenize(complex_string)

>>> ["Aujourd'hui", "j'", 'ai', 'plein', "d'", 'adresses', 'à', 'tester', 'comme', 'http://test.com/eelg/', '.', 'En', 'voici', 'quelques', 'unes', ':', 'https://www.example.com/', ',', 'www.example.com/etcetc', ',', 'example.com/etcetc', ',', 'mais', "j'", 'ai', 'aussi', 'des', 'adresses', 'emails', ':', 'zeofjreoigjerigjer@gmail.com', 'et', 'krjr@offo.edu.au', '.', 'Voici', "d'", 'autres', 'tests', ';', 'user:pass@example.com/etcetc', 'www.exemple.com', 'et', 'example.com/etcetc?query=aasd', '.', 'Mon', 'numéro', 'de', 'téléphone', 'est', 'le', '06.02.02.02.02', 'mais', 'on', 'peut', 'aussi', 'me', 'joindre', 'au', '07.02.02.02.02', '!']
```

##### - fp.tag(list_of_string)

Prend une liste de string en entrée et retourne une liste de tuples de string 
du type : [(token1, tag1), (token2, tag2)].

Exemple :

```python
string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! (Un jour, j'en suis certaine, ils contrôleront le monde...) #chats #révolution"

fp.tag(fp.tokenize(string))

>>> [("j'", 'cl'), ('aime', 'v'), ('les', 'det'), ('chats', 'nc'), ('.', 'ponct'), ('ce', 'cl'), ('sont', 'v'), ('vraiment', 'adv'), ('des', 'det'), ('êtres', 'nc'), ('supérieurs', 'adj'), ('!', 'ponct'), ('(', 'det'), ('un', 'det'), ('jour', 'det'), (',', 'ponct'), ("j'", 'cl'), ('en', 'cl'), ('suis', 'v'), ('certaine', 'adj'), (',', 'ponct'), ('ils', 'cl'), ('contrôleront', 'v'), ('le', 'det'), ('monde', 'nc'), ('...', 'ponct'), (')', 'det'), ('#', 'det'), ('chats', 'nc'), ('#', 'det'), ('révolution', 'nc')]
```

##### - fp.delete_stopwords(list_word_tag)

Prend une liste de tuples de string en entrée du type : [(token1, tag1), (token2, tag2)], supprime les stopwords proposés par défaut ou bien supprime ceux proposés à la défintion de FrenchPreprocessing, et retourne un objet du même type. 

Exemple :

```python
# Dans cette exemple, les stopwords supprimés sont ceux qui font partie de la liste par défaut.

string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! (Un jour, j'en suis certaine, ils contrôleront le monde...) #chats #révolution"

fp.delete_stopwords(fp.tag(fp.tokenize(string)))

>>> [("j'", 'cl'), ('aime', 'v'), ('chats', 'nc'), ('.', 'ponct'), ('vraiment', 'adv'), ('êtres', 'nc'), ('supérieurs', 'adj'), ('!', 'ponct'), ('(', 'det'), ('jour', 'det'), (',', 'ponct'), ("j'", 'cl'), ('certaine', 'adj'), (',', 'ponct'), ('ils', 'cl'), ('contrôleront', 'v'), ('monde', 'nc'), ('...', 'ponct'), (')', 'det'), ('#', 'det'), ('chats', 'nc'), ('#', 'det'), ('révolution', 'nc')]
```

##### - fp.delete_symbols(list_word_tag)

Prend une liste de tuples de string en entrée du type : [(token1, tag1), (token2, tag2)], supprime les symboles proposés en entrée ou ceux par défaut : #§_-@+=*<>()[]{}/\\"', et retourne un objet du même type. 

Exemple :

```python
string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! (Un jour, j'en suis certaine, ils contrôleront le monde...) #chats #révolution"

fp.delete_punct(fp.delete_stop_words(fp.tag(fp.tokenize(string))))

>>> [("j'", 'cl'), ('aime', 'v'), ('les', 'det'), ('chats', 'nc'), ('.', 'ponct'), ('ce', 'cl'), ('sont', 'v'), ('vraiment', 'adv'), ('des', 'det'), ('êtres', 'nc'), ('supérieurs', 'adj'), ('!', 'ponct'), ('un', 'det'), ('jour', 'det'), (',', 'ponct'), ("j'", 'cl'), ('en', 'cl'), ('suis', 'v'), ('certaine', 'adj'), (',', 'ponct'), ('ils', 'cl'), ('contrôleront', 'v'), ('le', 'det'), ('monde', 'nc'), ('...', 'ponct'), ('chats', 'nc'), ('révolution', 'nc')]
```

##### - fp.delete_punct(list_word_tag)

Prend une liste de tuples de string en entrée du type : [(token1, tag1), (token2, tag2)], supprime les symboles de ponctuation proposés en entrée ou ceux par défaut : !;:,.?-..., et retourne un objet du même type. 

Exemple :

```python
string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! (Un jour, j'en suis certaine, ils contrôleront le monde...) #chats #révolution"

fp.delete_punct(fp.delete_stop_words(fp.tag(fp.tokenize(string))))

>>> [("j'", 'cl'), ('aime', 'v'), ('les', 'det'), ('chats', 'nc'), ('ce', 'cl'), ('sont', 'v'), ('vraiment', 'adv'), ('des', 'det'), ('êtres', 'nc'), ('supérieurs', 'adj'), ('(', 'det'), ('un', 'det'), ('jour', 'det'), ("j'", 'cl'), ('en', 'cl'), ('suis', 'v'), ('certaine', 'adj'), ('ils', 'cl'), ('contrôleront', 'v'), ('le', 'det'), ('monde', 'nc'), (')', 'det'), ('#', 'det'), ('chats', 'nc'), ('#', 'det'), ('révolution', 'nc')]
```

##### - fp.lemmatize(list_word_tag)

Prend une liste de tuples de string en entrée du type : [(token1, tag1), (token2, tag2)], 
et retourne une string des lemmes des tokens de la liste : "lemma_token_1 lemma_token_2".

Exemple :

```python
string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! (Un jour, j'en suis certaine, ils contrôleront le monde...) #chats #révolution"

fp.lemmatize(fp.delete_punct(fp.delete_symbols(fp.delete_stopwords(fp.tag(fp.tokenize(string))))))

>>> je aimer chat vraiment être supérieur jour je certain il contrôler monde chat révolution
```

##### - fp.preprocessing(string)

Prend une string en entrée et lui applique tous les traitements précédents. 
Cette méthode retourne donc la string ayant subi un pré-processing complet. 

Exemple :

```python
string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! (Un jour, j'en suis certaine, ils contrôleront le monde...) #chats #révolution"

fp.preprocessing(string)

>>> je aimer chat vraiment être supérieur jour je certain il contrôler monde chat révolution
```

## lexique_tools.py : Détail des méthodes et exemples d'utilisation

#### Initialisation de la classe LexiqueTools :

```python 
from french_preprocessing.lexique_tools import LexiqueTools

lt = LexiqueTools()
```

#### Méthodes de la classe LexiqueTools :

##### - lt.in_lexique(word)

Prend une string en entrée, renvoie False si le mot n'est pas dans le dictionnaire, sinon
renvoie la valeur associée à la string dans le dictionnaire.

Exemple :

```python 
lt.in_lexique('mangé')
>>> {'v': 'manger', 'adj': 'mangé'}

lt.in_lexique('cemotnexistepas')
>>> False
```

##### - lt.lexique_rewrite()

Ne prend rien en argument et ne renvoie rien, sert à réécrire le lexique 
lorsque des modifications ont eu lieu.

Doit être utilisée après les ajouts ou les suppressions de mots, 
sinon les changements ne sont pas pris en compte.

##### - lt.add_element(word, lemma, tag)

Prend en argument une string, son lemme associé, son tag et ne renvoie rien. 
Cette méthode ajoute le nouvel élément (word, lemma, tag) au dictionnaire, ou 
ne fait rien s'il y est déjà.

##### - lt.remove_element(word, tag)

Prend en argument le mot à supprimer et son tag, ne revoie rien.
Supprime tag associé au mot désiré ou ne fais rien si le tag n'existe 
pas dans le dictionnaire associé au mot.

Exemple : 

```python 
lt.in_lexique('mangé')
>>> {'v': 'manger', 'adj': 'mangé'}

lt.remove_element('mangé', 'v')

lt.in_lexique('mangé')
>>> {'adj': 'mangé'}
```

##### - lt.lexique_update(dictionary)

Prend en argument le dictionnaire des mots à ajouter au lexique, ne renvoie rien.
Réalise une succession d'ajouts des mots de "dictionnary" dans le lexique.

Exemple :

```python 
lt.in_lexique('mangé')
>>> {'adj': 'mangé'}

dictionnary = {'mangé':{'v':'manger'}, 'nouveaumot':{'nc':'nouveaulemme', 'v':'nouveaulemme2'}}

lt.lexique_update(dictionary)

lt.in_lexique('mangé')
>>> {'v':'manger','adj': 'mangé'}

lt.in_lexique('nouveaumot')
>>> {'nc':'nouveaulemme', 'v':'nouveaulemme2'}
```

##### ATTENTION : Après chaque série de manipulations, il est nécessaire de réécrire le lexique à l'aide de la méthode : lexique_rewrite().

## general_tools.py : Détail de deux fonctions utiles et exemples d'utilisation

```python 
from french_preprocessing.general_tools import conjug_1, conjug_2
```

#### Fonctions de general_tools.py :

##### - conjug_1(first_group_verb)

Prend en argument un verbe du 1er groupe dans sa forme canonique, 
renvoie la liste des formes conjuguées de ce verbe.

Exemple :

```python 
conjug_1('manger')
>>> ['manger', 'mange', 'manges', 'mangons', 'mangez', 'mangent', 'mangé', 'mangais', 'mangait', 'mangions', 'mangiez', 'mangaient', 'mangai', 'mangas', 'manga', 'mangâmes', 'mangâtes', 'mangèrent', 'mangerai', 'mangeras', 'mangera', 'mangerons', 'mangerez', 'mangeront', 'mangerais', 'mangerait', 'mangerions', 'mangeriez', 'mangeraient', 'mangasse', 'mangasses', 'mangât', 'mangassions', 'mangassiez', 'mangassent', 'mangant']
```
##### - conjug_2(second_group_verb)

Prend en argument un verbe du 2eme groupe dans sa forme canonique, 
renvoie la liste des formes conjuguées de ce verbe.

Exemple :

```python 
conjug_1('réussir')
>>> ['réussir', 'réussis', 'réussit', 'réussissons', 'réussissez', 'réussissent', 'réussissais', 'réussissait', 'réussissions', 'réussissiez', 'réussissaient', 'réussîmes', 'réussîtes', 'réussirent', 'réussirai', 'réussiras', 'réussira', 'réussirons', 'réussirez', 'réussiront', 'réussirais', 'réussirait', 'réussirions', 'réussiriez', 'réussiraient', 'réussisse', 'réussisses', 'réussissions', 'réussissiez', 'réussissent', 'réussi', 'réussissant']
```

##### - stanford_tag_reduction(tag)

Prend en argument un tag et renvoie son tag réduit. 

Tag d'entrée : 'A', 'ADJ', 'ADJWH', 'ADV', 'ADVWH', 'C', 'CC', 'CL', 'CLO', 'CLR', 'CLS', 'CS', 
'DET', 'DETWH', 'ET', 'I', 'N', 'NC', 'NPP', 'P', 'PREF', 'PRO', 'PROREL', 'PROWH', 'PUNC', 'V', 
'VIMP', 'VINF', 'VPP', 'VPR', 'VS'

Tag de sortie : 'v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et'

##### - lexique383_tag_reduction(tag)

Prend en argument un tag et renvoie son tag réduit. 

Tag d'entrée : 'ADV', 'ADJ','PRO', 'PRE', 'NOM', 'VER', 'ONO', 'CON', 'AUX', 'ART', 'EXP'

Tag de sortie : 'v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 'prep', 'i', 'ponct', 'cl', 'et'
