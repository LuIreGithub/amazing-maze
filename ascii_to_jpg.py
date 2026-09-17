from PIL import Image, ImageDraw
from pathlib import Path

dossier_outputs = Path(__file__).parent / "outputs"
dossier_outputs.mkdir(exist_ok=True)

def convertir_ascii_vers_jpg(nom_fichier_maze, nom_image):

    chemin_fichier = dossier_outputs / nom_fichier_maze

    with open(chemin_fichier, "r") as fichier:
         lignes = fichier.readlines()

    labyrinthe = []

    for ligne in lignes:
        labyrinthe.append(list(ligne.strip()))


    taille = len(labyrinthe)
    taille_case = 20
    taille_image = taille * taille_case

    image = Image.new("RGB", (taille_image, taille_image), "white")

    dessin = ImageDraw.Draw(image)

    for i in range(taille):
      for j in range(taille):

          x = j * taille_case
          y = i * taille_case

          if labyrinthe[i][j] == "#":
              couleur = "black"

          elif labyrinthe[i][j] == ".":
              couleur = "green"

          elif labyrinthe[i][j] == "*":
              couleur = "blue"

          elif labyrinthe[i][j] == "o":
              couleur = "red"          

          dessin.rectangle(
            [x, y, x + taille_case, y + taille_case],
            fill=couleur
          )



    chemin_image = dossier_outputs / nom_image

    image.save(chemin_image)


