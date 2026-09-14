from pathlib import Path

dossier_outputs = Path(__file__).parent.parent / "outputs"


import heapq

nom_fichier = input("Entrez le nom du fichier du labyrinthe : ")

chemin_fichier = dossier_outputs / nom_fichier

with open(chemin_fichier, "r") as fichier:
    lignes = fichier.readlines()

labyrinthe = []

for ligne in lignes:
    labyrinthe.append(list(ligne.strip()))

taille = len(labyrinthe)
n = (taille-1)//2

depart = (0, 1)
sortie = (2*n, 2*n-1)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
explorees = set()

def heuristique(i, j):
    return abs(i - sortie[0]) + abs(j - sortie[1])

cases_a_explorer = []
f_depart = heuristique(0,1)
heapq.heappush(cases_a_explorer, (f_depart,depart))

precedent = {}

couts_g = {depart: 0}

while cases_a_explorer:
    f, position = heapq.heappop(cases_a_explorer)
    i, j = position

    if position in explorees:
        continue
    explorees.add(position)
    labyrinthe[i][j]= "*"

    if (i, j) == sortie:
        break


    for di, dj in directions:
        ni = i + di
        nj = j + dj
        voisin = (ni, nj)

        if 0 <= ni < taille and 0 <= nj < taille:
            if labyrinthe[ni][nj] != "#":

                g_actuel = couts_g[(i,j)]
                nouveau_g = g_actuel + 1

                if voisin not in couts_g or nouveau_g < couts_g[voisin]:
                    couts_g[voisin] = nouveau_g
                    f_voisin = nouveau_g + heuristique(ni,nj)
                    heapq.heappush(cases_a_explorer,(f_voisin, voisin))
                    precedent[voisin] = (i,j)

position = sortie

while position != depart:
    i,j = position
    labyrinthe[i][j] = "o"
    position = precedent[position]

labyrinthe[depart[0]][depart[1]] = "o"

nom_fichier_solution = input("Entrez le nom du fichier avec la solution : ")

chemin_solution = dossier_outputs / nom_fichier_solution
with open(chemin_solution, "w") as fichier:
    for ligne in labyrinthe:
        fichier.write("".join(ligne) + "\n")



