#include<stdio.h>
#include<stdlib.h> 

int main(int argc, char const *argv[]){

	FILE *fichier=NULL; // on créer un pointeur de type file  
	fichier=fopen("README.md","w");
	if(fichier!=NULL)
	{
		fputs("# Notes\n \n## Idea and Protocol\n \n## Data used\n",fichier); // Ici ajouter la date du workday, passer en argument  
		fclose(fichier); 
	}
	else
	{
		printf("L'ouverture à échouée \n"); 
	}
	return 0; 
}
