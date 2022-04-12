#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#define BUFSIZ 8192
int main( int argc, char ** argv ) //code ngbalenzela nehemie 
{
char buffer[BUFSIZ];
/*creation fonctions*/
void crypter(char*textClair,char *dataCrypt)
{
  char T[]      = "abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 \"²&é'\n\t(-è_çà)=~#{[@|`]^}°+$*ùµ£§%!:/;.,?âêûîôäëüïö<>\\";
    int  taille_T = strlen(T);
    int  taille_T_Clair = strlen(textClair);
 int nbr=taille_T%2;
int i,j;
  for(i=0;i<= taille_T_Clair; i++)
{for(j=0; j<=taille_T; j++)
  {
    if(textClair[i]==T[j] && j<=nbr){
     dataCrypt[i]=T[j+nbr];
    }
   if(textClair[i]==T[j] && j>nbr){
     dataCrypt[i]=T[j-nbr];
    }
    else{/*pour le traitement des autres langues*/
     break;
    }
}

}    

}
int fd;
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
char buffer[BUFSIZ];char cypher[BUFSIZ];
close(pfd[1]);
/* close write side
/* read some data and print the result on screen 
while (read(pfd[0], buffer, BUFSIZ) != 0)
printf
("child reads %s",
close(pfd[0]); *//* close the pipe */
/*creation file*/

fd=open("text_cripter.txt",O_WRONLY|O_CREAT|S_IRWXU);

if(fd==-1){
perror("error open()");
}
crypter(buffer,cypher);
write(df,cypher,sizeof(char));
  close(pfd[0]);
}
else
{
char c;
/* parent */
;
close(pfd[0]); /* close read side */
/* send some data into the pipe */
printf("Saisir les donnees a crypte");
 scanf("%s",c);
strcpy(buffer, &c);
write(pfd[1], buffer, strlen(buffer)+1);
close(pfd[1]); /* close the pipe */
}
return 0;
}