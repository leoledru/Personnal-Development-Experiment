# Faire le café avec VIM ? Pas loin... 

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

## Le café arrive: les plugins (pathogen) 

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


## Les colorthemes 

## Details des plugins 

### NERDTree

*a faire, notamment comment naviguer entre dossiers et fichier! je suis preneur*

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




## Reférences 

https://artisan.karma-lab.net/configurer-vim

https://vimawesome.com/

https://www.youtube.com/watch?v=wlR5gYd6um0 
*voir 30.45 cmii comment all an ident line* 



