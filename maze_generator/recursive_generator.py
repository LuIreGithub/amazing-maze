import random


n = int(input("Entrez la taille du labyrinthe : "))
nom_fichier = input ("Entrez le nom du fichier: ")

taille = 2*n+1

labyrinthe = [ ]

for i in  range (taille):
    ligne = []

    for j in range(taille):
        if i % 2 != 0 and j % 2 != 0:
            ligne.append(".")

        else:
            ligne.append("#")    
    labyrinthe.append(ligne)

visited = set() 

directions = [(-2,0), (2,0), (0,-2), (0,2)]

def generer_chemin(i,j):
    visited.add((i, j))
    
    directions_locales = directions.copy()
    random.shuffle(directions_locales)

    for (di, dj) in directions_locales:
        ni = i + di
        nj = j + dj

        if (1 <= ni <= 2*n - 1 and 1 <= nj <= 2*n - 1) and (ni, nj) not in visited:
            mur_i = (i + ni) // 2
            mur_j = (j + nj) // 2

            labyrinthe[mur_i][mur_j] = "."
            

            generer_chemin(ni, nj)

labyrinthe[0][1] = "."

generer_chemin(1, 1)

labyrinthe[2*n][2*n - 1] = "."

with open(nom_fichier, "w") as fichier:
    for ligne in labyrinthe:
        fichier.write("".join(ligne) + "\n")

