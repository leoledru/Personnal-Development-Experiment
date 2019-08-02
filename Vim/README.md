# La belle vi  

## Une première étape: le .vimrc et .vim/{} 

Le fichier ~/.vimrc permet de configurer vim.
Par exemple, pour mettre les numéros de ligne en marge, on va le créer (si pas déjà fait), et mettre dedans: 
	
	set number 

Pour la coloration synthaxique: 

	filetype plugin indent on 
	syntax on 

Le paramétrage de vim ne s'arrête pas au .vimrc (*aller plus loin détails*), aussi il est préférable de mettre un peu d'ordre: 

	cd 
	mkdir -p .vim/{autoload,colors,plugin,spell,config,bundle}
	mv .vimrc .vim/
	ln -s .vim/vimrc .vimrc

Par exemple, config peut servir à placer des bouts de vimrc, quand celui-ci devriendra assez grand, par thématiques par exemple (*à compléter*)
## Les colorthemes 

*a faire*
gruvbox theme utilisé 

## Comment manoeuvrer sa vi (mouvements/déplacements dans vim)

### Les basics 

### Plus complexes 



## Les plugins (pathogen) 

1. Installer le gestionnaire de plugins: ici pathogen 

	cd ~.vim
	git clone https://github.com/tpope/vim-pathogen.git
	cd autoload 
	ln -s ../pathogen/autoload/pathogen.vim . 

Pour les mises à jours des plugins que l'on aura installé: 

	cd ~/.vim/pathogen 
	git pull 

Enfin, pour que la magie opère, il faut rajouter les lignes suivantes dans le vimrc: 
	
	call pathogen#infect() 
	call pathogen#helptags() 

Et voilà terminares 

### Un premier indispensable: NERDTree 

Le git du projet: https://github.com/scrooloose/nerdtree

Tout simplement, la manip à faire:

	cd ~/.vim/bundle 
	git clone https://github.com/scrooloose/nerdtree

Voilà, maintenant on peut tapper :NERDTree dans vim et voir ce qu'il se passe héhé 


## Details des plugins 

### NERDTree

+ ctrl w + w pour swicher entre toggle nerdtree et files (comme pour les split) 

+ si on veut NERDTree à chaque fois au lancement de vim, ajouter dans le .vimrc

	" Activation de NERDTree au lancement de vim
	autocmd vimenter * NERDTree

### ultisnips & vim-snippets: Qu'a vim à envier aux IDE ? 

Indispensables tous les deux, ils permettent d'utiliser des snippets (bouts de codes pré-écris) de différents languages. 

Prenons deux exemples: 

1. En language C:

Si on tappe dans vim main et qu'on fait tab, on aura alors le fameux: 
	int main (int argc, char *argv[])
		{
			return 0;
		}

2. Pour un document latex: 

+ Un simple up (+tab) : 

	\usepackage[arg1]{arg2} (ctlr + j/k pour passer entre les arg)

+ begin (+tab): 

	\begin{arg}
	
	\end{arg}

#### Ajouts snippets 

markdown.snippets: 

+ Commentaires 
	snippet <!
	<!--${1:text}-->

matlab.snippets (à creer): *a faire*


### youCompleteMe (ycm) & supertab: Parés pour coder efficacement, plus d'excuses ! 

Ces deux là viennent parfaire les deux précédents. 

Il y a cependant deux petites difficultés à surmonter, pour ycm, qui d'une part, est chiant à installer (fonctionnelement je veux dire), et d'autre part entraîne des conflits avec ultisnips. 

#### Installation fonctionnelle de ycm 

	cd ~/.vim/bundle/youCompleteMe 
	sudo apt-get install (arch: pacman -S) python-pip 
	git submodule update --init --recursive 
	./install.py --clang-completer (peut nécessiter sudo apt-get install build-essential python-dev cmake) 
	sudo bash ./install.sh


#### Conflits ycm-ultisnips

Ajouter dans le vimrc: 

	" YouCompleteMe and UltiSnips compatibility, with the helper of supertab
	" (via http://stackoverflow.com/a/22253548/1626737)
	let g:SuperTabDefaultCompletionType    = '<C-n>'
	let g:SuperTabCrMapping                = 0
	let g:UltiSnipsExpandTrigger           = '<tab>'
	let g:UltiSnipsJumpForwardTrigger      = '<tab>'
	let g:UltiSnipsJumpBackwardTrigger     = '<s-tab>'
	let g:ycm_key_list_select_completion   = ['<C-j>', '<C-n>', '<Down>']
	let g:ycm_key_list_previous_completion = ['<C-k>', '<C-p>', '<Up>']

### vim-surround     

+ Ajouter des surrounds: ysiw" (ou bien ', (, <emph>, etc.)

+ Modifier des surrounds: cs"' 

+ supprimer: ds" 

### vim-bookmarks 

Permet de gérer efficacement les marque-pages, outil très puissant de vim aussi. 

Comment ça marche les marque-pages déjà ? 

**Sans vim-bookmarks**
On met une marque en tappant m + a-z ([A-Z] pour les globaux). 
	ma 

Pour s'y rendre, on fait `a    (` (ou apostrophe marche aussi)  

**Avec vim-bookmarks** 

La vi devient belle avec vim-bookmarks ! 

Voici ce qu'il "faut" rajouter dans le .vimrc, avec les détails sur ce que ça fait: 

	" vim-bookmarks 
	" Hihglighting / number of ctermbg is from gruvbox / see git repo for image 
	" 167 un rouge sympa / 239 un noir plus clair 
	highlight BookmarkSign ctermbg=NONE ctermfg=132
	highlight BookmarkLine ctermbg=237 ctermfg=NONE

	" Enables highligh of the marked lines  
	let g:bookmark_highlight_lines = 1

	" Sign of bookmarks in the left column  
	let g:bookmark_sign = '♥'
	"let g:bookmark_sign = '>>'	

	" automatically close bookmarks split when jumping to a bookmark 
	let g:bookmark_auto_close = 1

	" Next line allows grouping of bookmarks per root directory. This way bookmarks from other projets are not interfering. This is done by saving a file called .vim-bookmartks into the current working directory. CARE, you should add the filemame .vim-bookmarks to your (global) .gitignore file so it doesn't get checked into verson control.
	let g:bookmark_save_per_working_dir = 1
	let g:bookmark_auto_save = 1 

	" Uncomment the following line to disable all default key bindings and thus classic m[a-z] work again  
	" let g:bookmark_no_default_key_mappings = 1

Comment l'utiliser: 

+ mm: créé une marque au niveau du curseur (marque sur la ligne) 
+ mn: se déplace à la prochaine marque 
+ mp: se déplace à la précédente 
+ ma: ouvre le toggle pour voir tous les bookmarks / entr pour s'y déplacer (ça ferme le toggle si on a mit l'option dans le .vimrc 
+ mc: clear bookmarks uniquement dans le buffer actuel 
+ mx: clear bookmarks dans tous les buffers 
+ mkk/mjj: fait descendre/monter d'une ligne le bookmark 
+ mgN: le bouge à la ligne N 

Ces trois derniers c'est un peu le "point négatif" je trouve, dans le sens où si on modifie du texte en amont, la marque se déplace aussi. 









## Reférences 

https://artisan.karma-lab.net/configurer-vim

https://vimawesome.com/

https://www.youtube.com/watch?v=wlR5gYd6um0 
*voir 30.45 cmii comment all an ident line* 



