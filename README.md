# Amazing Maze

## 1. Contexte du projet

Amazing Maze est un projet d'algorithmique dont l'objectif est de générer, résoudre et visualiser des labyrinthes parfaits.

Un labyrinthe parfait est un labyrinthe dans lequel il existe un chemin unique entre deux cellules accessibles.

Le projet permet d'étudier et de comparer plusieurs approches algorithmiques :
- Recursive Backtracking et Kruskal pour la génération des labyrinthes ;
- Recursive Backtracking et A* pour leur résolution.

Les labyrinthes sont d'abord représentés sous forme ASCII dans des fichiers texte, puis peuvent être convertis en images JPG afin de visualiser le labyrinthe, le parcours d'exploration et le chemin final.

## 2. Données et représentation des labyrinthes

Le programme prend en entrée un entier naturel `n`, qui représente le nombre de cellules du labyrinthe sur chaque côté. Le labyrinthe logique contient donc `n²` cellules.

Pour représenter à la fois les cellules et les murs dans un fichier ASCII, une matrice de taille `(2n + 1) × (2n + 1)` est utilisée. Les cellules du labyrinthe se trouvent aux indices impairs et les positions intermédiaires représentent les murs qui peuvent être ouverts lors de la génération.

Les différents caractères utilisés sont :

- `#` représente un mur.
- `.` représente une cellule accessible ou un chemin libre.
- `*` représente une cellule explorée par le solveur mais qui ne fait pas partie du chemin final.
- `o` représente une cellule appartenant au chemin final entre l'entrée et la sortie.

L'entrée du labyrinthe est toujours située en haut à gauche, à la position `(0, 1)`, et la sortie en bas à droite, à la position `(2n, 2n-1)`.

Ces deux positions sont ouvertes après la génération du labyrinthe afin de permettre l'entrée et la sortie.

## 3. Structure et utilisation du projet

Le projet est organisé en plusieurs modules afin de séparer la génération, la résolution et la visualisation des labyrinthes.

```text
amazing_maze/
│
├── main.py
├── ascii_to_jpg.py
│
├── maze_generator/
│   ├── recursive_generator.py
│   └── kruskal_generator.py
│
├── maze_solver/
│   ├── recursive_solver.py
│   └── A_star_solver.py
│
├── outputs/
│
└── README.md
```

Le fichier main.py constitue le point d'entrée du programme. Il permet de choisir entre les différentes fonctionnalités:

- générer un labyrinthe avec Recursive Backtracking ou Kruskal;
- résoudre un labyrinthe avec Recursive Backtracking ou A* ;
- convertir un fichier ASCII en image JPG.

Pour lancer le programme:

```bash
python main.py
```
Les fichiers générés par le programme sont enregistrés dans le dossier outputs/.

## 4. Algorithmes utilisés

### 4.1 Génération - Recursive Backtracking

La première méthode de génération utilise l'algorithme Recursive Backtracking. La génération commence à la cellule `(1, 1)` et les quatre directions possibles sont mélangées aléatoirement afin de produire des labyrinthes différents à chaque exécution.

L'algorithme choisit une cellule voisine qui n'a pas encore été visitée, supprime le mur entre les deux cellules, puis continue récursivement depuis cette nouvelle cellule. Lorsqu'une cellule n'a plus de voisin disponible, l'algorithme revient à la cellule précédente et essaie une autre direction : c'est le principe du backtracking.

Les cellules déjà visitées sont enregistrées dans l'ensemble `visited`. Une cellule déjà visitée ne peut pas être reconnectée, ce qui empêche la création de cycles. Toutes les cellules sont finalement connectées et il existe un chemin unique entre deux cellules accessibles : le labyrinthe généré est donc parfait.

La complexité temporelle est `O(n²)`, car les `n²` cellules sont visitées une seule fois et seulement quatre directions sont testées pour chaque cellule. La complexité spatiale est également `O(n²)` dans le pire cas, notamment à cause de l'ensemble `visited` et de la pile d'appels récursifs.

### 4.2 Génération - Kruskal

La deuxième méthode de génération utilise l'algorithme de Kruskal. Au début, chaque cellule du labyrinthe appartient à un groupe différent. Toutes les connexions possibles entre cellules voisines sont ensuite créées et mélangées aléatoirement.

Pour chaque connexion, l'algorithme vérifie si les deux cellules appartiennent à des groupes différents. Si c'est le cas, le mur qui les sépare est supprimé et les deux groupes sont fusionnés. Si les cellules appartiennent déjà au même groupe, le mur est conservé afin d'éviter la création d'un cycle.

Le processus continue jusqu'à obtenir `n² - 1` connexions acceptées. Toutes les cellules sont alors connectées sans cycle, ce qui garantit la génération d'un labyrinthe parfait.

Dans notre implémentation, la fusion de deux groupes est optimisée avec une structure Union-Find. La fonction `find()` permet de retrouver la racine du groupe auquel appartient une cellule, tandis que la fonction `union()` permet de fusionner deux groupes.

La structure Union-Find utilise également la compression de chemin et l'union par taille afin de rendre les recherches et les fusions plus efficaces.

Le labyrinthe contient `n²` cellules et un nombre de connexions possibles proportionnel á `n²`. Grâce à Union-Find, les opérations de recherche et de fusion ont coût amorti presque constante. La complexité temporelle de cette implémentation est donc proche de `O(n²)` et la complexité spatiale est `O(n²)`.

### 4.3 Résolution - Recursive Backtracking

La première méthode de résolution utilise également le Recursive Backtracking. L'exploration commence à l'entrée du labyrinthe et avance récursivement dans les cellules accessibles.

Chaque cellule explorée est marquée par `*`. Lorsqu'une impasse est rencontrée, la fonction retourne `False` et revient à la cellule précédente afin d'essayer une autre direction.

Lorsque la sortie est atteinte, la fonction retourne `True`. Cette valeur se propage alors à travers les appels récursifs précédents et les cellules appartenant au chemin correct sont marquées par `o`. Les cellules marquées par `*` à la fin correspondent donc aux zones explorées qui ne font pas partie du chemin final.

Dans le pire cas, le solveur peut explorer un nombre de cellules proportionnel à `n²`. Sa complexité temporelle est donc `O(n²)`. La profondeur de la récursion peut également atteindre `O(n²)`, ce qui peut provoquer une erreur de limite de récursion pour de grands labyrinthes.

### 4.4 Résolution - A*

La deuxième méthode de résolution utilise l'algorithme A*. Contrairement au Recursive Backtracking, A* choisit les cellules à explorer en fonction d'une estimation du meilleur chemin vers la sortie.

Pour chaque cellule, l'algorithme calcule :

`f = g + h`

où `g` représente le coût du chemin parcouru depuis l'entrée et `h` représente une estimation de la distance restante jusqu'à la sortie.

Dans notre implémentation, `h` correspond à la distance de Manhattan, car les déplacements sont possibles uniquement dans quatre directions : haut, bas, gauche et droite.

Une file de priorité basée sur `heapq` permet de sélectionner efficacement la cellule ayant la plus petite valeur de `f`. Les cellules explorées sont marquées par `*`. Le dictionnaire `precedent` conserve la cellule précédente de chaque position afin de reconstruire le chemin final lorsque la sortie est atteinte. Ce chemin est ensuite marqué par `o`.

Dans le pire cas, A* peut explorer un nombre de cellules proportionnel à `n²`. Les opérations d'insertion et d'extraction dans le heap ont une complexité logarithmique. La complexité temporelle peut donc être estimée à `O(n² log n)`, tandis que la complexité spatiale est `O(n²)`.

## 5. Visualisation ASCII vers JPG

Afin de faciliter la visualisation des labyrinthes, un script permet de convertir les fichiers ASCII en images JPG à l'aide de la bibliothèque Pillow.

Chaque caractère du fichier est représenté par une couleur différente :

- `#` : noir pour les murs ;
- `.` : vert pour les cellules accessibles ;
- `*` : bleu pour les cellules explorées par le solveur ;
- `o` : rouge pour le chemin final.

Le même script peut être utilisé pour visualiser aussi bien un labyrinthe généré qu'un labyrinthe résolu. La représentation graphique permet ainsi de distinguer facilement les murs, les zones explorées et le chemin trouvé entre l'entrée et la sortie.

## 6. Tests de performance et analyse 

Les performances des différents algorithmes peuvent être comparées à partir de leur complexité temporelle et spatiale.

Le Recursive Backtracking utilisé pour la génération et la résolution possède une complexité temporelle de `O(n²)`, car le labyrinthe contient `n²` cellules logiques et chaque cellule est visitée au plus une fois. Sa complexité spatiale est également `O(n²)`. Cependant, l'utilisation de la récursion peut atteindre la limite de récursion de Python pour de grands labyrinthes.

Notre implémentation de Kruskal possède une complexité temporelle pouvant atteindre `O(n⁴)`. En effet, lors de la fusion de deux groupes, la liste des `n²` cellules est parcourue. Cette opération est répétée de nombreuses fois pendant la génération. Cette implémentation devient donc beaucoup moins adaptée lorsque `n` augmente. Une structure Union-Find permettrait d'améliorer cette partie.

Pour A*, la complexité temporelle peut être estimée à `O(n² log n)`. Le facteur logarithmique provient notamment de l'utilisation du heap comme file de priorité. Même si sa complexité théorique est supérieure à celle du Recursive Backtracking, son heuristique peut lui permettre d'explorer moins de cellules en pratique.

Lorsque `n` est multiplié par 10, un algorithme en `O(n²)` voit son coût théorique multiplié approximativement par 100, tandis qu'un algorithme en `O(n⁴)` peut voir son coût multiplié par environ 10 000.

Les tailles proposées de 1 000, 10 000 et 100 000 montrent également les limites de la représentation utilisée. Pour `n = 1 000`, le labyrinthe contient déjà 1 000 000 de cellules logiques et la matrice ASCII contient environ 4 millions de positions. Pour `n = 100 000`, cette matrice contiendrait environ 40 milliards de positions. La mémoire disponible devient donc également une limitation importante pour les très grandes tailles.

## 7. Conclusion

Ce projet nous a permis de comprendre que plusieurs algorithmes peuvent avoir le même objectif, mais que leur efficacité peut être très différente selon la manière de stocker les informations et la façon d'aborder le problème.

Par exemple, la récursion se distingue par sa simplicité, mais elle peut rapidement atteindre la limite de récursion de Python lorsque la taille du labyrinthe augmente. Avec l'algorithme de Kruskal, nous avons appris que la manière de gérer les groupes de cellules a une grande influence sur les performances. L'utilisation de Union-Find pour identifier et fusionner les groupes nous a permis de rendre notre implémentation beaucoup plus efficace.

Enfin, nous avons constaté que tout matériel possède des limites en termes de temps de calcul et de mémoire. Ces contraintes doivent être prises en compte lors de la conception d'un algorithme, car la quantité de ressources utilisées a également un impact sur le coût de calcul, de stockage et, plus généralement, sur la consommation énergétique.