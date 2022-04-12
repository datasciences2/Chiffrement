# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:19:35 2020

@author: NEM'S
"""

# encoding: utf-8 

# La fonction PGCD avec ses 2 arguments a et b
def pgcd(a,b):
    # L'algo PGCD
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a;

# L'utilisateur entre p
p = input('Entrez un grand nombre premier p : ')

# L'utilisateur entre q
q = input('Entrez un grand nombre premier q : ')

# On calcul n
n = p*q

print ("\nn = ",n,)

# On calcul phi(n)
phiden = (p-1)*(q-1)

print( "\nphi de n = ",phiden)

# Variable de la boucle
compteur = 0
PGCD1 = 0

# Notre e qui s'incrÃ©mentera
e = 0

# Tant que PGCD de e et phi(n) diffÃ©rent de 1
while PGCD1 != 1 :
    # Tant que compteur=0
    while compteur == 0 :   
        # Si p infÃ©rieur Ã  e et si q infÃ©rieur Ã  e et si e infÃ©rieur Ã  n
        if((p < e)and(q < e)and(e < phiden)) :
            # La boucle se coupe (on peut aussi mettre le mot-clÃ© : break
            compteur = 1     
        # Tant que rien n'est trouvÃ©, e s'incrÃ©mente
        e = e + 1
    # On rÃ©cupÃ¨re le rÃ©sultat du pgcd   
    PGCD1 = pgcd(e,phiden)

# On affiche notre clÃ© publique
print ("\nCle publique (",e,",n=",n,")")

# On demande d'entrer le texte Ã  crypter
mot = raw_input('\nEntrez le mot ou la phrase a crypte : ')	

# On rÃ©cupÃ¨re le nombre de caractÃ¨re du texte
taille_du_mot = len(mot)

i = 0

# Tant que i infÃ©rieur aux nombres de caractÃ¨res
while i < taille_du_mot :

    # Comme i s'incrÃ©mente jusqu'Ã  egalitÃ© avec la taille du mot, Ã  chaque passage dans la fonction chaque lettre sera converti.
    ascii = ord(mot[i])
	
    # On crypte la lettre ou plutot son code ASCII
    lettre_crypt = pow(ascii,e)%n
	
	# Si le code ASCII est supÃ©rieur Ã  n
    if ascii > n :
        print( "Les nombres p et q sont trop petits veulliez recommencer")
		
    # Si le bloc cryptÃ© est supÃ©rieur Ã  phi(n)
    if lettre_crypt > phiden :
        print ("Erreur de calcul")
 
    # On affiche chaque blocs cryptÃ©s
    print ("\n Block : ",lettre_crypt,)
   
    # On incrÃ©mente i
    i = i + 1

# On bloque le programme avant la fermeture
raw_input('\n\nFin\n\n')