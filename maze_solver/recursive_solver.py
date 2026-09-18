from pathlib import Path
import time

dossier_outputs = Path(__file__).parent.parent / "outputs"

dossier_outputs.mkdir(exist_ok=True)

def resoudre_labyrinthe_recursive(nom_fichier, nom_fichier_solution):
    debut = time.perf_counter()
    chemin_fichier = dossier_outputs / nom_fichier

    with open(chemin_fichier, "r") as fichier:
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
    fin = time.perf_counter()

    chemin_solution = dossier_outputs / nom_fichier_solution
    with open(chemin_solution, "w") as fichier:
      for ligne in labyrinthe:
          fichier.write("".join(ligne) + "\n")

    temps = fin - debut
    print(f"Temps de résolution : {temps:.4f} secondes")      

           


    