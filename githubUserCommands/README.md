# GitHub (BG) 

## Commandes utiles

+ git statuts

+ git pull 

+ git commit 

## Clone SSH vs HTTPS

Cloner un repository depuis le dépôt distant vers le dépôt local (son pc) permet de travailler localement sur celui-ci avant de pusher son travail vers le dépôt distant. Lors du clonage le repository distant est copié localement à l'emplacement où l'utilisateur se trouve. Le repository local créé est directement lié au repository distant, pas besoin d'ajouter un remote pour pusher. 
Il existe deux manières de cloner un repository : 

+ Cloner en ssh permet de ne pas avoir à s'authentifier (login et mdp) à chaque intéraction avec git, cependant cela demande quelques manipulations. Voir : https://help.github.com/en/articles/connecting-to-github-with-ssh

+ Cloner en HTTPS est très facile, mais git demande l'authentification à chaque action. Une solution permet de faire retenir l'authentification à git pendant un certain laps de temps :

	$ git config --global credential.helper cache

Set git to use the credential memory cache
	
	$ git config --global credential.helper 'cache --timeout=3600'

Set the cache to timeout after 1 hour (setting is in seconds)

## Demarche PDE 

### Gérant du rep 

Celui qui gère le master (qui mergera les branches parallèles)

### Collaborateurs du rep 

Petis commits/modifications: directement edit sur gitHub *et pull request* 

Grosses modifications: travailler localement: 

Si on veut faire des grosses modifications hors de la branche master, la procédure prévue est donc: 

1. git checkout -b titreDeLaBrancheSecondaire (créer la branche secondaire)   

	Faire ses modifications ... 

2. git add . (tous les fichiers) / nom_des_fichiers_à_transmettre (seulement certains). *Definir quand l'utiliser exactement*

3. git commit -am "message decrivant changements réalisés" 

4. git push origin (vérifier git remote) titreDeLaBrancheSecondaire
