# FRENCH PREPROCESSING

Package regroupant des outils de pré-traitement pour les textes en langue française : 
tokenisation, simplification, tagging (Part-of-Speech tagging) et lemmatisation.

## OBJECTIF ET REALISATIONS DU PROJET

### Création d'un outil complet de préprocessing pour le français : 

- Tokenisation : Transformation de texte en tokens (unités lexicales)
- Simplification : Supression des stopwords (mots à faible valeur lexicale comme 'le', 
"t'", 'dring'...), retrait de la ponctuation.
- Tagging : Etiquetage grammatical (Part-of-speech tagging),autrement dit, l'association 
de tags grammaticaux (ex: 'nc' pour nom commun, 'v' pour verbe...) aux tokens d'un texte.
- Lemmatisation : Remplacement des tokens d'un texte par leur lemme ("forme canonique" 
du mot, utilisée dans les dictionnaires).

### Précisions sur le travail effectué

- Utilisation de spaCy pour la Tokenisation, redéfinition des stopwords pour la simplification.

- Synthétisation de trois lexiques : Lexique des formes fléchies du français (LEFFF), 
le Lexique 3.83, et le lexique utilisé par la librarie python spaCy pour 
créer une base de données développée pour l'outil de lemmatisation.

- Synthétisation des tags utilisé dans les deux lexiques (LEFFF et Lexique 3.83) et tagging
des données du lexique de spaCy à l'aide du StandfordPOSTagger pour intégrer le 'tag' 
en paramètre de l'outil de lemmatisation.

- Création de deux lexiques à partir du lexique.txt (complet) : lexique_ac_accent.txt 
(contenant les mots avec accents) et lexique_ss_accent.txt (contenant les mots sans accents et
les versions sans accent des mots présentant des accents ). Ce choix est adapté à 
l'utilisation du lemmatiseur pour l'étude de textes extraits des réseaux sociaux 
(où l'accentuation est parfois omise).

- Développement d'outils dans lexique_tools.py pour la modification du lexique afin de l'augmenter facilement, 
sans compromettre le fichier texte.

- Création d'outils généraux dans general_tools.py pour appliquer la réduction de tag (réduction adaptée 
aux tags du StanfordPOSTagger, et aux tags du Lexique 3.83), supprimer les accents d'un mot, obtenir 
toutes les formes conjuguées des verbes réguliers du français (1er et 2ème groupe).

### Sources et crédits : 

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

#### spaCy

- spaCy, GitHub repository, https://github.com/explosion/spaCy

#### StanfordPOSTagger

- The Stanford Natural Language Processing Group. "Stanford Log-linear Part-Of-Speech Tagger". 
https://nlp.stanford.edu/software/tagger.shtml

- TOUTANOVA Kristina and MANNING Christopher. 2000. "Enriching the Knowledge Sources Used 
in a Maximum Entropy Part-of-Speech Tagger". In Proceedings of the Joint SIGDAT Conference 
on Empirical Methods in Natural Language Processing and Very Large Corpora (EMNLP/VLC-2000), pp. 63-70.

- TOUTANOVA Kristina, KLEIN Dan, MANNING Christopher and SINGER Yoram. 2003. 
"Feature-Rich Part-of-Speech Tagging with a Cyclic Dependency Network". In Proceedings 
of HLT-NAACL 2003, pp. 252-259.


### Licenses and Copyrights : 

- License Lexique 3.83 : Attribution-ShareAlike 4.0 International, https://github.com/chrplr/openlexicon/blob/master/LICENSE.txt
- License spaCy : The MIT License (MIT), https://github.com/explosion/spaCy/blob/master/LICENSE
- Copyright spaCy : Copyright (C) 2016-2019 ExplosionAI GmbH, 2016 spaCy GmbH, 2015 Matthew Honnibal
- License StanfordPOSTagger :  GNU General Public License, https://github.com/stanfordnlp/CoreNLP/blob/master/licenses/gpl-2.0/LICENSE.txt
- FrenchLefffLemmatizer : Lesser General Public License For Linguistic Resources, https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer/blob/master/LICENSE


## french_preprocessing.py : Détail des méthodes et exemples d'utilisaiton

#### Intialisation de la classe FrenchPreprocessing :

java_path = 'C:\\Program Files\\Java\\jre1.8.0_211\\bin\\java.exe'
fp = FrenchPreprocessing(java_path)

#### Méthodes de la classe FrenchPreprocessing :

- fp.tokenize_and_simplify(string)
Prend une string en entrée et retourne une liste de string formée des tokens 
de la string d'entrée, après l'application des simplifications : [token1, token2]

- fp.tag(list_of_string)
(Cette méthode s'applique sur une string ayant subit le prétraitement 
précédent fp.tokenize_and_simplify(string))
Prend une liste de string en entrée et retourne une liste de
liste de deux strings du type : [[token1,tag], [token2,tag2]]

- fp.lemmatize(list_word_tag)
(Cette méthode s'applique sur une string ayant subit les prétraitements précédents
fp.tag(fp.tokenize_and_simplify(string)))
Prend une liste de liste de deux strings en entrée du type : [[token1,tag], [token2,tag2]], 
et retourne une string des lemmes des tokens de la liste : "lemma_token_1 lemma_token_2".

- fp.preprocessing(string)
Prend une string en entrée et lui applique tous les traitements précédents. 
Cette méthode retourne donc la string ayant subit un pré-processing complet. 

Exemple : 
string_entree = "La vie est si belle aujourd'hui ! Je pense que tu devrais 
aller observer les loutres dans leurs habitats naturels..."
string_sortie = "vie beau je penser tu devoir aller observer loutre habitat naturel"

#### Exemple de code d'execution :

from french_preprocessing.french_preprocessing import FrenchPreprocessing

fp = FrenchPreprocessing('C:\\Program Files\\Java\\jre1.8.0_211\\bin\\java.exe')

string_entree = "La vie est si belle aujourd'hui ! Je pense que tu devrais aller observer les loutres dans leurs habitats naturels..."

string_sortie = fp.preprocessing(string_entree)

print(string_sortie)

> vie beau je penser tu devoir aller observer loutre habitat naturel

## lexique_tools.py : Détail des méthodes et exemples d'utilisation

#### Intialisation de la classe LexiqueTools :

lt = LexiqueTools()

#### Méthodes de la classe FrenchPreprocessing :

- lt.in_lexique(word)
Prend une string en entrée, renvoie False si le mot n'est pas dans le dictionnaire, sinon
renvoie la valeur associée à la string dans le dictionnaire.

Exemple :

lt.in_lexique('mangé') -> {'v': 'manger', 'adj': 'mangé'}

lt.in_lexique('cemotnexistepas') -> False

- lt.lexique_rewrite()
Ne prend rien en argument et ne renvoie rien, sert à réécrire les lexiques dans 
les différents fichiers textes lorsque des modifications ont eu lieu.

Doit être utilisée après les ajouts ou les suppressions de mots, 
sinon les changements ne sont pas pris en compte.

- lt.add_element(word, lemma, tag)
Prend en argument une string, son lemme associé, son tag et ne renvoie rien. 
Cette méthode ajoute le nouvel élément (word, lemma, tag) au dictionnaire, ou 
ne fait rien s'il y est déjà.

- lt.remove_element(word, tag)
Prend en argument le mot à supprimer et son tag, ne revoie rien.
Supprime tag associé au mot désiré ou ne fais rien si le tag n'existe 
pas dans le dictionnaire associé au mot.

Exemple : 

lt.in_lexique('mangé')
> {'v': 'manger', 'adj': 'mangé'}

lt.remove_element('mangé', 'v')

lt.in_lexique('mangé')
> {'adj': 'mangé'}

- lt.lexique_update(dictionary)
Prend en argument le dictionnaire des mots à ajouter au lexique, ne renvoie rien.
Réalise une sucession d'ajouts des mots de "dictionnary" dans le lexique.

Exemple :

lt.in_lexique('mangé')
> {'adj': 'mangé'}

dictionnary = {'mangé':{'v':'manger'}, 'nouveaumot':{'nc':'nouveaulemme', 'v':'nouveaulemme2'}}

lt.lexique_update(dictionary)

lt.in_lexique('mangé')
> {'v':'manger','adj': 'mangé'}

lt.in_lexique('nouveaumot')
> {'nc':'nouveaulemme', 'v':'nouveaulemme2'}

##### ATTENTION : Après chaque série de manipulations, il est nécessaire de réécrire les lexiques à l'aide de la méthode : lexique_rewrite().

## general_tools.py : Détail des méthodes et exemples d'utilisation

#### Fonctions de general_tools.py :

- conjug_1(first_group_verb)
Prend en argument un verbe du 1er groupe dans sa forme canonique, 
renvoie la liste des formes conjuguées de ce verbe.

Exemple :
conjug_1('manger')
> ['manger', 'mange', 'manges', 'mangons', 'mangez', 'mangent', 'mangé', 'mangais', 'mangait', 'mangions', 'mangiez', 'mangaient', 'mangai', 'mangas', 'manga', 'mangâmes', 'mangâtes', 'mangèrent', 'mangerai', 'mangeras', 'mangera', 'mangerons', 'mangerez', 'mangeront', 'mangerais', 'mangerait', 'mangerions', 'mangeriez', 'mangeraient', 'mangasse', 'mangasses', 'mangât', 'mangassions', 'mangassiez', 'mangassent', 'mangant']

- conjug_2(second_group_verb)
Prend en argument un verbe du 2eme groupe dans sa forme canonique, 
renvoie la liste des formes conjuguées de ce verbe.

Exemple :
conjug_1('réussir')
> ['réussir', 'réussis', 'réussit', 'réussissons', 'réussissez', 'réussissent', 'réussissais', 'réussissait', 'réussissions', 'réussissiez', 'réussissaient', 'réussîmes', 'réussîtes', 'réussirent', 'réussirai', 'réussiras', 'réussira', 'réussirons', 'réussirez', 'réussiront', 'réussirais', 'réussirait', 'réussirions', 'réussiriez', 'réussiraient', 'réussisse', 'réussisses', 'réussissions', 'réussissiez', 'réussissent', 'réussi', 'réussissant']