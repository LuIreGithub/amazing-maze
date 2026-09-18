from pathlib import Path
import random
import time

dossier_outputs = Path(__file__).parent.parent / "outputs"

dossier_outputs.mkdir(exist_ok=True)

def generer_labyrinthe_kruskal(n, nom_fichier):
    debut = time.perf_counter()

    chemin_fichier = dossier_outputs / nom_fichier

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


    parents = list(range(n**2))
    tailles = [1] * (n**2)

    def find(x):
        while parents[x] != x:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x

    def union(a,b):
        racine_a = find(a)
        racine_b = find(b)

        if tailles[racine_a] < tailles[racine_b]:
            parents[racine_a] = racine_b
            tailles[racine_b] += tailles[racine_a]
        else:
            parents[racine_b] = racine_a
            tailles[racine_a] += tailles[racine_b]

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
        if find(cellule1) != find(cellule2):

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
        
            union(cellule1,cellule2)

        
            connexions_acceptes += 1

            if connexions_acceptes == n**2-1:
                break   

    labyrinthe[0][1] = "."
    labyrinthe[2*n][2*n-1] = "."   

    fin = time.perf_counter()  

    with open(chemin_fichier, "w") as fichier:
       for ligne in labyrinthe:
           fichier.write("".join(ligne) + "\n")


    temps = fin - debut
    print(f"Temps de génération : {temps:.4f} secondes")
            
