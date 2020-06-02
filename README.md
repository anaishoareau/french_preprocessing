# FRENCH PREPROCESSING

Package regroupant des outils de pré-traitement pour les textes en langue française : 
tokenisation, simplification, tagging (Part-of-Speech tagging) et lemmatisation.

## Installation

Vérifier que la commande pip est installée, ainsi que git : https://packaging.python.org/tutorials/installing-packages/

#### Pour installer le package french_preprocessing, executer la commande :

```bash 
pip install git+https://github.com/anaishoareau/french_preprocessing.git
```

#### ATTENTION : Cette commande installe aussi les dépendances (le package python nltk). Si vous rencontrez des problèmes, il faut l'installer à part.

Version utilisée : nltk - 3.4


#### ATTENTON : Pour que le french_preprocessing fonctionne, il faut avoir installé java (JRE) : https://www.java.com/fr/download/ et donner le path du fichier java.exe à l'initialisation du FrenchPreprocessing, un exemple est proposé après.

## Objectifs et réalisations du projet

### Création d'un outil complet de préprocessing pour le français : 

- Tokenisation : Transformation de texte en tokens (unités lexicales)

- Grammatical tagging : Etiquetage grammatical (Part-of-speech tagging), autrement dit, l'association 
de tags grammaticaux (ex: 'nc' pour nom commun, 'v' pour verbe...) aux tokens d'un texte

- Simplification : Suppression des stopwords (mots à faible valeur lexicale comme 'le', 
"t'", 'dring'...), retrait de la ponctuation

- Lemmatisation : Remplacement des tokens d'un texte par leur lemme ("forme canonique" 
du mot, utilisée dans les dictionnaires)

### Précisions sur le travail effectué

- Tokenisation réalisée par le RegexpTokenizer de NLTK avec une expression régulière créée spécifiquement pour le français et qui permet de reconnaître, en plus des unités lexicales courantes, beaucoup d'adresses emails, de numéros de téléphone, de noms de domaines, etc. 

- Synthétisation de trois lexiques en un seul (lexique.txt): Lexique des formes fléchies du français (LEFFF), 
le Lexique 3.83, et le lexique utilisé par la librairie python spaCy pour 
créer une base de données développée pour l'outil de lemmatisation.

- Uniformisation des tags utilisés dans les deux lexiques (LEFFF et Lexique 3.83) et tagging
des données du lexique de spaCy à l'aide du StandfordPOSTagger pour intégrer le 'tag' 
en paramètre de l'outil de lemmatisation. Les tags du StanfordPOSTagger sont aussi uniformisés.
Les tags après uniformisation sont réduits à : 'v', 'nc', 'adj', 'c', 'npp', 'adv', 'det', 'pro', 
'prep', 'i', 'ponct', 'cl', 'et'

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

#### StanfordPOSTagger :

- The Stanford Natural Language Processing Group. "Stanford Log-linear Part-Of-Speech Tagger". 
https://nlp.stanford.edu/software/tagger.shtml

- TOUTANOVA Kristina and MANNING Christopher. 2000. "Enriching the Knowledge Sources Used 
in a Maximum Entropy Part-of-Speech Tagger". In Proceedings of the Joint SIGDAT Conference 
on Empirical Methods in Natural Language Processing and Very Large Corpora (EMNLP/VLC-2000), pp. 63-70.

- TOUTANOVA Kristina, KLEIN Dan, MANNING Christopher and SINGER Yoram. 2003. 
"Feature-Rich Part-of-Speech Tagging with a Cyclic Dependency Network". In Proceedings 
of HLT-NAACL 2003, pp. 252-259.


### Licences and Copyrights : 

- License Lexique 3.83 : Attribution-ShareAlike 4.0 International, https://github.com/chrplr/openlexicon/blob/master/LICENSE.txt
- License spaCy : The MIT License (MIT), https://github.com/explosion/spaCy/blob/master/LICENSE
- Copyright spaCy : Copyright (C) 2016-2019 ExplosionAI GmbH, 2016 spaCy GmbH, 2015 Matthew Honnibal
- License StanfordPOSTagger :  GNU General Public License, https://github.com/stanfordnlp/CoreNLP/blob/master/licenses/gpl-2.0/LICENSE.txt
- FrenchLefffLemmatizer : Lesser General Public License For Linguistic Resources, https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer/blob/master/LICENSE


## french_preprocessing.py : Détail des méthodes et exemples d'utilisation

#### Initialisation de la classe FrenchPreprocessing :

```python
from french_preprocessing.french_preprocessing import FrenchPreprocessing

fp = FrenchPreprocessing(java_path = 'C:/Program Files/Java/jre1.8.0_211/bin/java.exe', stop_words = personalized_list)
```
#### Méthodes de la classe FrenchPreprocessing :

##### - fp.tokenize(string)

Prend une string en entrée et retourne une liste de string formée des tokens 
de la string d'entrée en enlevant les symboles inutiles : [token1, token2].

Exemples :

```python 
# Définitions des chaines de caractères

string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! Un jour, j'en suis certaine, ils contrôleront le monde..."

complex_string = """Aujourd'hui j'ai plein d'adresses à tester comme http://test.com/eelg/.
En voici quelques unes : https://www.example.com/, www.example.com/etcetc, example.com/etcetc, mais j'ai aussi des adresses emails : zeofjreoigjerigjer@gmail.com et krjr@offo.edu.au.
Voici d'autres tests ; user:pass@example.com/etcetc (www.exemple.com) et example.com/etcetc?query=aasd.
Mon numéro de téléphone est le 06 02 02 02 02 mais on peut aussi me joindre au 07/02/02/02/02 !"""

# Applications de la méthode tokenize

fp.tokenize(string)

>>> ["J'", 'aime', 'les', 'chats', '.', 'Ce', 'sont', 'vraiment', 'des', 'êtres', 'supérieurs', '!', 'Un', 'jour', ',', "j'", 'en', 'suis', 'certaine', ',', 'ils', 'contrôleront', 'le', 'monde', '...']

fp.tokenize(complex_string)

>>> ["Aujourd'hui", "j'", 'ai', 'plein', "d'", 'adresses', 'à', 'tester', 'comme', 'http://test.com/eelg/', '.', 'En', 'voici', 'quelques', 'unes', ':', 'https://www.example.com/', ',', 'www.example.com/etcetc', ',', 'example.com/etcetc', ',', 'mais', "j'", 'ai', 'aussi', 'des', 'adresses', 'emails', ':', 'zeofjreoigjerigjer@gmail.com', 'et', 'krjr@offo.edu.au', '.', 'Voici', "d'", 'autres', 'tests', ';', 'user:pass@example.com/etcetc', 'www.exemple.com', 'et', 'example.com/etcetc?query=aasd', '.', 'Mon', 'numéro', 'de', 'téléphone', 'est', 'le', '06.02.02.02.02', 'mais', 'on', 'peut', 'aussi', 'me', 'joindre', 'au', '07.02.02.02.02', '!']
```

##### - fp.tag(list_of_string)

Prend une liste de string en entrée et retourne une liste de tuples de string 
du type : [(token1, tag1), (token2, tag2)].

Exemple :

```python
string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! Un jour, j'en suis certaine, ils contrôleront le monde..."

fp.tag(fp.tokenize(string))

>>> [("j'", 'cl'), ('aime', 'v'), ('les', 'det'), ('chats', 'nc'), ('.', 'ponct'), ('ce', 'cl'), ('sont', 'v'), ('vraiment', 'adv'), ('des', 'det'), ('êtres', 'nc'), ('supérieurs', 'adj'), ('!', 'ponct'), ('un', 'det'), ('jour', 'nc'), (',', 'ponct'), ("j'", 'cl'), ('en', 'cl'), ('suis', 'v'), ('certaine', 'adj'), (',', 'ponct'), ('ils', 'cl'), ('contrôleront', 'v'), ('le', 'det'), ('monde', 'nc'), ('...', 'ponct')]
```

##### - fp.delete_stop_words(list_word_tag)

Prend une liste de tuples de string en entrée du type : [(token1, tag1), (token2, tag2)], supprime les stopwords proposés par défaut ou bien supprime ceux proposés à la défintion de FrenchPreprocessing, et retourne un objet du même type. 

Exemple :

```python
# Dans cette exemple, les stopwords supprimés sont ceux qui font partie de la liste par défaut.

string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! Un jour, j'en suis certaine, ils contrôleront le monde..."

fp.delete_stop_words(fp.tag(fp.tokenize(string)))

>>> [("j'", 'cl'), ('aime', 'v'), ('chats', 'nc'), ('.', 'ponct'), ('vraiment', 'adv'), ('êtres', 'nc'), ('supérieurs', 'adj'), ('!', 'ponct'), ('jour', 'nc'), (',', 'ponct'), ("j'", 'cl'), ('certaine', 'adj'), (',', 'ponct'), ('ils', 'cl'), ('contrôleront', 'v'), ('monde', 'nc'), ('...', 'ponct')]
```

##### - fp.delete_punct(list_word_tag)

Prend une liste de tuples de string en entrée du type : [(token1, tag1), (token2, tag2)], supprime la ponctuation, et retourne un objet du même type. 

Exemple :

```python
string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! Un jour, j'en suis certaine, ils contrôleront le monde..."

fp.delete_punct(fp.delete_stop_words(fp.tag(fp.tokenize(string))))

>>> [("j'", 'cl'), ('aime', 'v'), ('chats', 'nc'), ('vraiment', 'adv'), ('êtres', 'nc'), ('supérieurs', 'adj'), ('jour', 'nc'), ("j'", 'cl'), ('certaine', 'adj'), ('ils', 'cl'), ('contrôleront', 'v'), ('monde', 'nc')]
```

##### - fp.lemmatize(list_word_tag)

Prend une liste de tuples de string en entrée du type : [(token1, tag1), (token2, tag2)], 
et retourne une string des lemmes des tokens de la liste : "lemma_token_1 lemma_token_2".

Exemple :

```python
string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! Un jour, j'en suis certaine, ils contrôleront le monde..."

fp.lemmatize(fp.delete_punct(fp.delete_stop_words(fp.tag(fp.tokenize(string)))))

>>> je aimer chat vraiment être supérieur jour je certain il contrôler monde
```

##### - fp.preprocessing(string)

Prend une string en entrée et lui applique tous les traitements précédents. 
Cette méthode retourne donc la string ayant subi un pré-processing complet. 

Exemple :

```python
string = "J'aime les chats. Ce sont vraiment des êtres supérieurs ! Un jour, j'en suis certaine, ils contrôleront le monde..."

fp.preprocessing(string)

>>> je aimer chat vraiment être supérieur jour je certain il contrôler monde
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
