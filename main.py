from maze_generator.recursive_generator import generer_labyrinthe_recursive
from maze_generator.kruskal_generator import generer_labyrinthe_kruskal

from maze_solver.recursive_solver import resoudre_labyrinthe_recursive
from maze_solver.A_star_solver import resoudre_labyrinthe_a_star
from ascii_to_jpg import convertir_ascii_vers_jpg

print("=== AMAZING MAZE ===")
print("1 - Générer un labyrinthe")
print("2 - Résoudre un labyrinthe")
print("3 - Convertir ASCII en JPG")

choix = input("Votre choix : ")

if choix == "1":
    print("1 - Recursive Backtracking")
    print("2 - Kruskal")

    methode = input("Choisissez la méthode de génération : ")
    n = int(input("Entrez la taille du labyrinthe : "))
    nom_fichier = input("Entrez le nom du fichier (.txt) : ")

    if methode == "1":
        generer_labyrinthe_recursive(n, nom_fichier)

    elif methode == "2":
        generer_labyrinthe_kruskal(n, nom_fichier)

    else: 
        print("Méthode invalide.")   


elif choix == "2":
    
    print("1 - Recursive Backtracking")
    print("2 - A*")

    methode = input("Choisissez la méthode de résolution : ")

    nom_fichier = input("Entrez le nom du fichier du labyrinthe (.txt): ")
    nom_fichier_solution = input("Entrez le nom du fichier avec la solution (.txt): ")

    if methode == "1":
        resoudre_labyrinthe_recursive(
            nom_fichier,
            nom_fichier_solution
        )

    elif methode == "2":
        resoudre_labyrinthe_a_star(
            nom_fichier,
            nom_fichier_solution
        )

    else:
        print("Méthode invalide.") 

elif choix == "3":
    nom_fichier_maze = input("Entrez le nom du fichier à convertir (.txt): ")
    nom_image = input("Entrez le nom de l'image (.jpg): ")

    convertir_ascii_vers_jpg(
        nom_fichier_maze,
        nom_image
    )  

else:
    print("Choix invalide.")                      