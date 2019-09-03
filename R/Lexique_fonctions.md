# Rentrer des données

* read.table(obj, dec=’’,’’) : lire un tableur . Argument dec: préciser si la décimale du dataframe est un . ou ,
* data.frame(nom premiere colonne=c(valeurs), nom deuxieme=c(valeurs) : créer dataframe en 1 étape
*  data.frame(x,y,z): combiner plusieurs data frame
* seq(from=1, to=10,by=3 ou length.out=3) : créer une séquence de 1 à 10 avec un pas de 3 ou seq de longueure totale 3 (3 valeurs)

# Visualiser les données
* print() : afficher un objet
* ls() : obtenir la liste des objets en mémoire
* mode() : donne la nature de l’objet (num, char, complex, logical)
* class() : donne la nature de l’obj 
* attributes (matrice1) : permet de connaître les dim d'une matrice

## Dataframe
* Str() : structure des données
* Summary : résumer stat descriptives 
* data() : jeux de données déjà présents dans R
* tail(x) : afficher les 6 dernières lignes. Equivalent à x[(nrow(x)-5):nrow(x), ]

# Modifier un jeu de données
* rm() : éliminer un objet ex rm(list=c(‘‘v1’’,’’v2’’)
* vec[1:3] ou vec[c(1,2,3]): selectionne les 3 premières valeurs de vec
* obj[-1] : exclure la valeur 1
* rep(x=5,times=20) : pour répéter 20 fois la valeur 5 (sortie=vecteur).
* obj.caracteres ← rep(x=c(‘‘nom’’, ‘‘nom’’), times= 20 : pour des caractères 

# Machinerie R
* save.image : générer un fichier de workspace
* load() : recharger un workspace
* setwd(‘‘/) : spécifier le working directory
* install.packages()

# Opérateurs mathématiques
* Ajout de vecteurs : de même taille → les vecteurs sont ajoutés éléments par éléments
* vec -24 : soustrait 24 à tt les valeurs du vecteur
* range(x) : étendue des éléments de x
* rank(x) : rang
* round(x,digits=1) : arrondir à 1 décimale
* cumsum(x) : somme cumulée
* prod(x) / cumprod(x) : produit / produit cumulé
* abs(x) : valeur absolue
* sqrt(x) : racine carrée
* log2(x) / log10(x) /log(x, base) /log(x)
* x^(y) : puissance

## Logique
* == : teste si deux éléments sont exactement égaux
* all() et any() : déterminer si tt ou au moins une des valeurs répondent au test
* all.equal() et identical() : mm chose pour des vecteurs
* which : détermine quelle valeur répond à une certaine condition. Donne les indices correspondants.
