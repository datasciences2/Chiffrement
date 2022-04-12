# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:02:59 2020

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
	
# La fonction factoriser avec en argument n
def factoriser(n):
    b=2
    while b:
        while n%b!=0 :
            b=b+1
        if n/b==1 :
            print ("p = ", b)
            # On crÃ©e une variable global p pour la rÃ©utiliser hors de la fonction et p=b
            global p
            p = b
            break
        print( "\nq = ", b)
        # On crÃ©e une variable global q pour la rÃ©utiliser hors de la fonction et q=b
        global q
        q=b
        n=n/b;
		
pqconnu = 0
pqconnu = input("Si vous etes en possession de p et q, entrez 1 sinon 0 : ")

if pqconnu == 0 :	
	
	# On rÃ©cupÃ¨re n
	n = input("Entrez le nombre n : ")

	# On appelle la fonction pour le factoriser
	factoriser(n)

	# On calcul phi(n)
	phiden = (p-1)*(q-1)

	# Variable pour notre boucle while
	compteur = 0
	PGCD1 = 0

	# Notre e qui s'incrÃ©mentera
	e = 0

	# Tant que PGCD de e et phi(n) diffÃ©rent de 1
	while PGCD1 != 1 :
	    # Tant que compteur=0
	    while compteur == 0 :   
	        # 
	        if((p < e)and(q < e)and(e < phiden)) :
	            # La boucle se coupe (on peut aussi mettre le mot-clef : break
	            compteur = 1     
	        # Tant que rien n'est trouvÃ©, e s'incrÃ©mente
	        e = e + 1
	    # On rÃ©cupÃ¨re le rÃ©sultat du pgcd   
	    PGCD1 = pgcd(e,phiden)

	# On calcul d
	d = 0
	compteur = 0
	
	while compteur == 0:
		# Les conditions vu ci-dessus :
		 if((e * d % phiden == 1)and(p < d)and(q < d)and(d < phiden)):
		    compteur = 1
		d = d + 1
        d = d - 1

	# On affiche la clÃ© privÃ©
	print ("\nCle privee (d=",d,",n=",n,")")
	
if pqconnu == 1 :
    p = input("Entrez le nombre p : ")
    q = input("Entrez le nombre q : ")

    # On calcul n
    n = p*q

    # On calcul phiden
    phiden = (p-1)*(q-1)

    #On demande d
    d = input("Entrez le nombre d : ")
	
# On rÃ©cupÃ¨re le nombre de lettre cryptÃ© (soit des bloc de un caractÃ¨re)
i = input("Combien il y a de bloc :")

compteur = 0

# Tant que r infÃ©rieur au nombre de lettre
while compteur < i :
    # L'utilisateur entre le premier bloc a dÃ©cryptÃ©
    lettre_crypt = input("\nEntree le bloc a decrypte :")
    # On trouve le ASCII de chaque lettre par le calcul de dÃ©codage
    ascii = (pow(lettre_crypt,d)%n)
    # Avec la fonction chr(ASCII), on trouve le caractÃ¨re correspondant
    print ("lettre :",chr(ascii))
    compteur = compteur + 1	
	
# On bloque le programme avant la fermeture
raw_input('\n\nFin\n\n')