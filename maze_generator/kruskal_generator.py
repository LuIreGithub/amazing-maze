
import random
n = int(input("Ecrivez la taille du labyrinthe: "))
nom_fichier = input ("Entrez le nom du fichier: ")


taille = 2*n + 1

labyrinthe = []
for i in  range (taille):
    ligne = []

    for j in range(taille):
        if i % 2 != 0 and j % 2 != 0:
            ligne.append(".")

        else:
            ligne.append("#")    
    labyrinthe.append(ligne)


groupes = list ((range(n**2)))

connexions = []
for i in range(n):
    for j in range(n):
        cellule = i * n + j

        if j+1<n:
            droite = i * n + j + 1
            connexions.append((cellule, droite))

        if i+1<n:
            bas = (i+1)* n + j
            connexions.append((cellule, bas)) 

random.shuffle(connexions) 

connexions_acceptes = 0

for (cellule1, cellule2) in connexions:
    if groupes[cellule1] != groupes[cellule2]:

        i1 = cellule1 // n
        j1 = cellule1 % n

        i2 = cellule2 // n
        j2 = cellule2 % n

        ligne1 = 2*i1+1
        colonne1 = 2*j1+1

        ligne2 = 2*i2+1
        colonne2 = 2*j2+1

        mur_i = (ligne1 + ligne2) // 2
        mur_j = (colonne1 + colonne2) // 2

        labyrinthe[mur_i][mur_j] = "."
        
        groupe1 = groupes[cellule1]
        groupe2 = groupes[cellule2]

        for k in range(n**2):
            if groupes[k] == groupe2:
                groupes[k] = groupe1

        connexions_acceptes += 1

        if connexions_acceptes == n**2-1:
            break   

labyrinthe[0][1] = "."
labyrinthe[2*n][2*n-1] = "."     

with open(nom_fichier, "w") as fichier:
    for ligne in labyrinthe:
        fichier.write("".join(ligne) + "\n")



            
