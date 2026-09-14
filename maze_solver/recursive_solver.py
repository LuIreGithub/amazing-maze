nom_fichier = input("Entrez le nom du fichier du labyrinthe : ")

with open(nom_fichier, "r") as fichier:
    lignes = fichier.readlines()

labyrinthe = []

for ligne in lignes:
    labyrinthe.append(list(ligne.strip()))

taille = len(labyrinthe)
n = (taille-1)//2

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def resoudre(i, j):
    if (i, j) == (2*n, 2*n - 1):
        labyrinthe[i][j] = "o"
        return True

    labyrinthe[i][j] = "*"

    for (di, dj) in directions:

        ni = i+di
        nj = j+dj 

        if 0 <= ni < taille and 0<= nj < taille:

            if labyrinthe[ni][nj] == ".":

                if resoudre(ni, nj):
                    labyrinthe[i][j] = "o"
                    return True
    return False   

resoudre(0,1)

nom_fichier_solution = input("Entres le nom du fichier avec la solution : ")

with open(nom_fichier_solution, "w") as fichier:
    for ligne in labyrinthe:
        fichier.write("".join(ligne) + "\n")

                


    