# Presentation of the terminal multiplexer *tmux* (LL)

leo.ledru@univ-smb.fr

# Keywords

+ **geekeries**

+ **terminal**

# Objectif

Le terminal donne à première vue des nausées, des sueurs, voire des crises de violence éxacerbées. Cependant à force de m'entendre dire par des personnes de confiance que jouer au geek dans le terminal c'était aussi un gain de temps considérable je me suis penché sur la question.
Au début, on ouvre des terminaux un peu dans tous les sens et on comprend pas bien en quoi ça peut être efficace. En fait, c'est parce qu'une des premières choses à faire est de se faire la main avec un terminal multiplexer pour profiter au mieux du terminal.
Entendez par "terminal multiplexer" un programme qui permet de gérer vos différents terminaux, de jongler entre chacun d'eux facilement, d'ouvrir des terminaux dans des terminaux, en bref de mixer matrix et inception.
Il y a plusieurs programme de ce genre, par pur hasard je me suis retrouvé à utiliser tmux, alors j'ouvre ce dossier pour partager mon utilisation de cet outil bien pratique.

# tmux !

## Intro

Installer tmux : `sudo apt-get install tmux`  

Une commande simple :  
    `$ tmux`
et bim une session tmux s'ouvre  
En fait ça ressemble à un terminal tout ce qu'il y a de plus normal, ormis en bas où vous pouvez voir quelques nouvelles infos, notamment dans quelle fenêtre de la session tmux ouverte vous vous trouvez, on va y revenir.  

**Mais quel est l'intérêt ? Je n'ai toujours qu'un seul terminal ouvert...**  
Essayer de taper Ctrl+b " (càd la touche Ctrl et la touche b en même temps, puis ")
Alors ? Et oui il y a maintenant deux terminaux ouverts visibles simultannément, vous pouvez vous exciter sur le raccourci Ctrl+b " pour en ouvrir autant que vous voulez.
**Rq : toutes les raccourcis interagissant avec tmux débute par Ctrl+b**   

**Voici qqs raccourcis utiles :**  
Ctrl+b " : split le volet horizontalement  
Ctrl+b % : split le volet verticalement  
Ctrl+b arrow key : switch entre les différents volets   
Ctrl+b c : crée une nouvelle fenêtre  
Ctrl+b n : bouge vers la fenêtre suivante  
Ctrl=b p : '...' précédente  

**volets vs fenêtres ?**  
Les volets sont visibles simultannément au sein d'une fenêtre tmux, tandis que les différentes fenêtres sont indiquées en bas dans la fameuse barre qui est apparu à l'ouverture de tmux. Ainsi vous pouvez par exemple avoir 3 fenêtres avec dans chacune 4 volets ouverts.  
Chaque fenêtre peut-être nommée pour savoir ce qu'il y a dedans - Ctrl+b , - permet de renommer la fenêtre active
Ctrl+b <numéro de fenêtre> permet de switcher directement vers la fenêtre numéro <numéro de fenêtre>
  
**Session**  
A chaque ouverture de tmux, une session est créée, elle contient vos volets et vos fenêtres. Mais imaginons que vous voulez lancer des tâches en arrière plan par exemple, parce que celle-ci sont longues.  
Voici comment tmux peut servir à cela :  

+ Taper tmux pour ouvrir une session

+ Une fois que vous avez fait ce que vous voulez (e.g lancer un programme matlab, ou si vous êtes diaboliques un programme R), vous voulez maintenant que ces actions restent actives mais en arrière plan

+ Ctrl+b d : hop ! la session tmux est "détachée" et vous revenez sur le terminal initial ou vous aviez tapé tmux

+ tmux attach : hop vous êtes de nouveau dans la session

Commandes utiles :  
`tmux` : créer nouvelle session  
`tmux ls` : liste des session actives en arrière plan  
`tmux attach -t <numéro de la session>` : attache la session numéro <numéro de la session>  
`tmux new -s <nom>` : crée une session nommée <nom>, c'est bien plus pratique que des numéros pour savoir à quoi correspondent chacune de vos sessions  
`tmux rename-session -t <ancien nom/numéro><nouveau nom/numéro>` : renomme une session  

**Quitter tmux**  
Pour fermer seulement l'onglet actif Ctrl+b d  
Pour fermer de multiples volets et fenêtres ouvertes Ctrl+b puis taper :kill-session et presser entrée  

**Configurer tmux**  
Tout comme le shell ou bien vim, tmux est configurable et c'est là que se trouve sa véritable puissance, bien que simplement ce qui a été présenté jusqu'à présent soit suffisant pour être utile.  
Le fichier de configuration de tmux doit être créé dans le home et nommé .tmux.conf  
    `$ cd vim .tmux.conf` # crée le fichier .tmux.conf en l'ouvrant avec vim  
Une des premières choses que l'on peut mettre dans ce fichier :  
    ```
    bind -n M-Left select-pane -L  
    bind -n M-Right select-pane -R  
    bind -n M-Up select-pane -U  
    bind -n M-Down select-pane -D  
    ```
Cette liste de commande permet de switcher entre les onglets avec Alt + arrow key à la place de Ctrl+b arrow key, ça semble anodin mais c'est bien plus agréable  
Pour que les modifications du fichier .tmux.conf soient prises en compte relancer tmux ou taper la commande dans la session en cours :  
    `$ tmux source-file .tmux.conf`  
    
De très nombreuses autres commandes de configuation sont possibles, à vous de creuser, et n'hésiter pas à les partager  

Par exemple, si Ctrl+b ne vous convient pas :  
    ```
    unbind C-b # supprime le raccourci Ctrl+b  
    set -g prefix C-a # remplace par Ctrl+a  
    ```
    
Quand vous travaillez avec plusieurs fenêtres, pour savoir quand il se passe quelque chose dans une fenêtre :  
    ```
    setw -g monitor-activity on  
    set -g visual-activity on  
    ```
    
## Utilisation avancée de tmux  

**Script tmux**
Imaginez que lorsque vous travaillez sur certain projet vous avez toujours les mêmes besoins en terme de terminaux à ouvrir. A chaque début de journée vous relancer tout ça avant de vous mettre en route. Si tel est le cas, vous pouvez être intéressé par le fait d'automatiser cette mise en route ; c'est possible avec des scripts !  

Pour faire cela, il suffit de créer un petit fichier séparé du .tmux.conf dans lequel le script est écrit, ensuite écrire dans le .tmux.conf le raccourci clavier que l'on veut définir pour appeler ce script. Voyons cela avec un exemple !  

Dans un travail en cours j'ai toujours besoin de 4 volets ouverts : mon espace où sont mes codes, mon espace dans une machine de calcul distante, une console matlab, un espace vim pour éditer les codes. Il est possible d'ouvrir tout ça d'un seul coup avec un racourci clavier.  

Première étape, je crée un fichier .tmux.lama qui sera le script (lama c'est le nom que j'ai choisi pour ce script, donc en général on peut faire .tmux.nom_choisi) : `$ vim .tmux.lama`  
Voici son contenu :  
    `selectp -t 0 # sélectionner le premier volet`  
    `splitw -h -p 50 # split ce volet horizontalement en deux parties 50/50`  
    `selectp -t 0 # sélectionner le premier volet`  
    `splitw -v -p 50 'commande pour ce connecter à la machine de calcul' # séparer le premier volet verticalement 50/50 et se connecter dans le second volet à la machine de calcul`  
    `selectp -t 2 # sélectionner le second volet`  
    `splitw -v 50 'commande pour ouvrir matlab' # vous avez compris`  
    `selectp -t 0 # revenir au premier volet`    
Vous avez remarquez que entre des apostrophes ' ' on peut directement écrire une commande à effectuer dès l'ouverture.  
Ce script étant fait, il reste à pouvoir l'appeler avec un raccourci clavier.  
    
On ouvre le fichier de config (`$ vim .tmux.conf`), et on ajoute :  
`bind L source-file ~/.tmux.lama` ici je choisi comme raccourci L (la casse est respectée), cela signifie que après avoir ouvert tmux, en faisant Ctrl+b L mon script est appelé et mes 4 volets pré-préparés s'ouvrent.  





# Références
https://lukaszwrobel.pl/blog/tmux-tutorial-split-terminal-windows-easily/  
https://www.hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/  
https://www.bugsnag.com/blog/tmux-and-vim  
