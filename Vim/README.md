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

## Reférences 

https://artisan.karma-lab.net/configurer-vim

https://vimawesome.com/





