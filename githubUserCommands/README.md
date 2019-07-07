# GitHub 

## Commandes utiles 

+ git statuts

+ git pull 

+ git commit 

## Demarche PDE 

### Gérant du rep 

Celui qui gère le master (qui mergera les branches parallèles)

### Collaborateurs du rep 

Petis commits/modifications: directement edit sur gitHub *et pull request* 

Grosses modifications: travailler localement: 

Si on veut faire des grosses modifications hors de la branche master, la procédure prévue est donc: 

1. git checkout -b titreDeLaBrancheSecondaire (créer la branche secondaire)   

	Faire ses modifications ... 

2. git add . (tous les fichiers) / nom_des_fichiers_à_transmettre (seulement certains). *Definir quand l'utiliser exactement*

3. git commit -am "message decrivant changements réalisés" 

4. git push origin (vérifier git remote) titreDeLaBrancheSecondaire


