# Create Automaticaly repo's each "day of work" (BG) 

benjamin.girardot@mio.osupytheas.fr

## Keywords 

+ organisation 

+ geekeries

## Objectives

L'idée est de créer en une commande un **repertoire de travail fonctionnel**, cad un repertoire qui contient un résumé
des pistes explorées la journée. 
Alors bien entendu c'est destiné aux journées où on produit des choses. 

L'intérêt est de garder une trace des pistes qu'on a exploré, même si ça conduit pas à grand chose. Par exemple, des remarques
sur les programmes développés, ce qu'ils produisent et pourquoi, les discussions qui accompagnent les résultats, etc. 

Donc pour ça, le programme va créer un repertoire workDayJJMMYY/, qui contient: 
 + README.md : fichier en question, qui a la structure suivante (mais modifiable selon les préférence)
  1. Ideas and objectives 
  2. Data used 
  3. Programs involved 
  4. Results & Discussion 
  5. References 
 Au final ça prend pas beaucoup de temps à remplir un fichier comme ça, et ça en fait gagner beaucoup quand on se replonge dedans !
 
 + Figures/ : un repertoire où sera stocké les figures qui seront appellées dans README.md 
 
 + *à ajouter*
 
 ## How to procede 
 
 1. Créer, si pas déjà fait, repertoire /home/username/bin (répertoire qui contient des scripts bash qu'on veut pouvoir appeler de n'importe où)
 
 2. Déplacer son script d'intérêt dans ce repertoire: 
   mv workDay /home/username/bin 
 
 3. Le rendre executable hein (chmod +x workDay)
 
 4. Rajouter à la variable d'environnement $PATH ce repertoire créer: 
  export PATH=$PATH:$HOME/bin
 
 
 
 
