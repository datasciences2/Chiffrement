#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#define BUFSIZ 8192
int main( int argc, char ** argv )
{char clair[BUFSIZ];
char memory[BUFSIZ];
int fd;
/*creation fonctions*/
void decrypter(char *dataCrypt,char*textClair)//ngbalenzela code_decryptage
{
  char T[]      = "abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 \"²&é'\n\t(-è_çà)=~#{[@|`]^}°+$*ùµ£§%!:/;.,?âêûîôäëüïö<>\\";
    int  taille_T = strlen(T);
    int  taille_T_cyph = strlen(dataCrypt);
 int nbr=taille_T%2;
int i,j;
int nb_lus,nb_ecrits;
  for(i=0;i<= taille_T_cyph; i++)
{for(j=0; j<=taille_T; j++)
  {
    if((dataCrypt[i]==T[j]) && (j<=nbr)){
     textClair[i]=T[j+nbr];
    }
   if((dataCrypt[i]==T[j]) && (j>nbr)){
     textClair[i]=T[j-nbr];
    }
    else{/*pour le traitement des autres langues*/
     /*textClair[i]=" "*/break;
    }
}

}    

}

/* create the pipe */
int pfd[2];
if (pipe(pfd) ==1)
{
printf
("pipe failed n");
return 1;
}
/* create the child */
int pid;
if ((pid = fork()) < 0)
{
printf
("fork failed n");
return 2;
}
if (pid == 0)
{ /* child */
char buffer[BUFSIZ];
close(pfd[1]);
/* close write side
/* decrypter et imprimer le resultat*/
 decrypter(buffer,clair);
while (clair!= NULL)
printf("Text en claire du fichier est:\n\t %s",close(pfd[0])); /* close the pipe */

}
else
{
char c;
/* parent */
char buffer[BUFSIZ];
close(pfd[0]); /* close read side */
/* send some data into the pipe */
/*ouverture file*/


if(fd=open("text_cripter.txt",O_RDONLY)==-1){
perror("error open()");
}
int k=0;

 do
{
nb_lus=read(df,(char *)buffer, BUFSIZ);
if (nb_lus>0) nb_ecrits= write(1,(char*)buffer, sizeof(char));
 strcpy(memory,buffer);//copie du sauvegarde du text pour la rendre claire dans le fils 
}
while ((nb_lus==BUFSIZ)&&(nb_ecrits>0));
//close(df);
close(pfd[1]);

write(pfd[1], buffer, strlen(buffer)+1);
close(pfd[1]); /* close the pipe */
}
return 0;

}