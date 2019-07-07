# PANDOC 

## Video Luke smith Notes 

### Exemple simple 

Eire son .md de notes 

Pour convertir en présentation : 
	$ pandoc file.md -t beamer -o file.pdf 
-o : output 

On peut aussi transmettre des "metadonnées", comme le titre, thème etc. 

### Listes : 

Attention mettre espaces entre les lignes : 

+ List item 1  

+ List item 2 

+ List item 3 

### Metadonnées

Se met entre --- : 
--- 
title:
- Benjamin's talk 
author: 
- Benjamin Girardot
theme: 
- Copenhagen
colortheme: 
- albatros,etc
--- 

### Styles d'écrite : 

<!--
**bold text** 
*emphatic text* 
-->


### Images : 

 
	![nom de l'image](chemin/de/l'image.png)
	


## Citations 

Need vim-pandoc and vim-pandoc-syntax 
Which by the way modify the .md syntax. I don't know how to deal with that. 

### How does it work ? 

Add the option --bibliography file.bib when compile 


## Md to beamer 

Previous description : pandoc file.md (--bibliography bib.bib) -t beamer -o file.pdf 

## Md to latex classic file 

pandoc file.md (--bibliography bib.bib) -s -o file.pdf 

# Exemple review 

---
title:
- (REVIEW) Natural selection contributes to food web stability
documentclass:
- report
geometry:
- margin=1in
linestretch:
- 1.25
bibliography:
- biblio.bib
---


# Automatic created files 

*a faire*
