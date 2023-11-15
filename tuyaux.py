import random

lignes = [["━", "┏", "┗", "┣", "┳", "┻", "╋"],  # droite
		  ["━", "┓", "┛", "┫", "┳", "┻", "╋"],  # gauche
		  ["┃", "┗", "┛", "┣", "┫", "┻", "╋"],  # haut
		  ["┃", "┏", "┓", "┣", "┫", "┳", "╋"]]  # bas
liste = []
for i in range(10):
	liste.append(lignes[random.randint(0, 3)][random.randint(0, 6)])
print(liste)
