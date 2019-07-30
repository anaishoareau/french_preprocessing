# FRENCH PREPROCESSING

## ( README EN CONSTRUCTION )

French preprocessing tools for tokenisation, simplification, 
grammatical tagging (Part-of-Speech tagging) and lemmatization

## OBJECTIF DU PROJET

#### SOURCES : 

- PALLIER Christophe, NEW Boris, 2019 Openlexicon, GitHub repository, https://github.com/chrplr/openlexicon

- NEW Boris, PALLIER Christophe, BRYSBAERT Marc and FERRAND Ludovic. 2004. "Lexique 2: A New French Lexical Database." Behavior Research Methods, Instruments, & Computers 36 (3): 516–524. [pdf](New et al. - 2004 - Lexique 2 A new French lexical database.pdf)

- NEW Boris, PALLIER Christophe, FERRAND Ludovic and MATOS Rafael. 2001. "Une Base de Données Lexicales Du Français Contemporain Sur Internet: LEXIQUE" L’Année Psychologique 101 (3): 447–462. [pdf](New et al. - 2001 - Une base de données lexicales du français contempo.pdf)

- NEW Boris, BRYSBAERT Marc, VERONIS Jean, and PALLIER Christophe. 2007. "The Use of Film Subtitles to Estimate Word Frequencies." Applied Psycholinguistics 28 (4): 661–77. https://doi.org/10.1017/S014271640707035X. (pdf)

## Détail des méthodes et exemples d'utilisaiton 

fp = FrenchPreprocessing(object)

#### Méthodes :

- fp.tokenize_and_simplify(string)

- fp.tag(list_of_string)

- fp.lemmatize(list_word_tag)

- fp.preprocessing(string)


