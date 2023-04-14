import random, numpy, time
from matplotlib import pyplot, animation

def miseAJour(grille):
	taille = len(grille)
	nouvelleGrille = numpy.zeros((taille, taille))
	for i in range(taille):
		for j in range(taille):
			nombreDeVoisinsVivants = int(
				grille[i - 1][j - 1] +
				grille[i - 1][j] +
				grille[i - 1][(j + 1) % taille] +
				grille[i][j - 1] +
				grille[i][(j + 1) % taille] +
				grille[(i + 1) % taille][j - 1] +
				grille[(i + 1) % taille][j] +
				grille[(i + 1) % taille][(j + 1) % taille]
			)
			if grille[i][j] == 1:
				if nombreDeVoisinsVivants < 2 or nombreDeVoisinsVivants > 3:
					nouvelleGrille[i][j] = 0
				else:
					nouvelleGrille[i][j] = 1
			else:
				if nombreDeVoisinsVivants == 3:
					nouvelleGrille[i][j] = 1
	return nouvelleGrille


def grilleVide(taille):
	return numpy.zeros((taille, taille))

def grillePleine(taille):
	return numpy.ones((taille, taille))

def grilleAleatoire(taille):
	grille = numpy.zeros((taille, taille))
	for i in range(taille):
		for j in range(taille):
			grille[i][j] = random.randint(0, 1)
	return grille


def ajouterLWSS(grille, x, y):

	#  #
	    #
	#   #
	 ####

	grille[y][x] = 1
	grille[y][x + 3] = 1

	grille[y + 1][x + 4] = 1

	grille[y + 2][x] = 1
	grille[y + 2][x + 4] = 1

	grille[y + 3][x + 1] = 1
	grille[y + 3][x + 2] = 1
	grille[y + 3][x + 3] = 1
	grille[y + 3][x + 4] = 1

def ajouterPlaneur(grille, x, y):

	  #
	# #
	 ##

	 grille[y][x + 2] = 1

	 grille[y + 1][x] = 1
	 grille[y + 1][x + 2] = 1

	 grille[y + 2][x + 1] = 1
	 grille[y + 2][x + 2] = 1

def ajouterCanonPlanneur(grille, x, y):

	                        #
	                      # #
	            ##      ##            ##
	           #   #    ##            ##
	##        #     #   ##
	##        #   # ##    # #
	          #     #       #
	           #   #
	            ##

	grille[y][x + 24] = 1

	grille[y + 1][x + 22] = 1
	grille[y + 1][x + 24] = 1

	grille[y + 2][x + 12] = 1
	grille[y + 2][x + 13] = 1
	grille[y + 2][x + 20] = 1
	grille[y + 2][x + 21] = 1
	grille[y + 2][x + 34] = 1
	grille[y + 2][x + 35] = 1

	grille[y + 3][x + 11] = 1
	grille[y + 3][x + 15] = 1
	grille[y + 3][x + 20] = 1
	grille[y + 3][x + 21] = 1
	grille[y + 3][x + 34] = 1
	grille[y + 3][x + 35] = 1

	grille[y + 4][x] = 1
	grille[y + 4][x + 1] = 1
	grille[y + 4][x + 10] = 1
	grille[y + 4][x + 16] = 1
	grille[y + 4][x + 20] = 1
	grille[y + 4][x + 21] = 1

	grille[y + 5][x] = 1
	grille[y + 5][x + 1] = 1
	grille[y + 5][x + 10] = 1
	grille[y + 5][x + 14] = 1
	grille[y + 5][x + 16] = 1
	grille[y + 5][x + 17] = 1
	grille[y + 5][x + 22] = 1
	grille[y + 5][x + 24] = 1

	grille[y + 6][x + 10] = 1
	grille[y + 6][x + 16] = 1
	grille[y + 6][x + 24] = 1

	grille[y + 7][x + 11] = 1
	grille[y + 7][x + 15] = 1

	grille[y + 8][x + 12] = 1
	grille[y + 8][x + 13] = 1

def ajouterPentominoR(grille, x, y):

	 ##
	##
	 #

	grille[y][x + 1] = 1
	grille[y][x + 2] = 1

	grille[y + 1][x] = 1
	grille[y + 1][x + 1] = 1

	grille[y + 2][x + 1] = 1


taille = 100
vitesse = 100
generationMaximum = 100

grille = grilleAleatoire(taille)

# grille = grilleVide(taille)
# ajouterLWSS(grille, 50, 50)
# ajouterCanonPlanneur(grille, 10, 10)
# ajouterPentominoR(grille, 50, 50)

pyplotFigure = pyplot.figure()
images = []

for i in range(generationMaximum):

	images.append((pyplot.imshow(grille, cmap = 'binary'),))
	grille = miseAJour(grille)

a = animation.ArtistAnimation(pyplotFigure, images, interval = 1000 / vitesse, repeat = False, blit = True)

# La fonction ArtistAnimation() est une fonction de la bibliothèque Matplotlib qui permet de créer une animation à partir d'une séquence d'images, voici les arguments que prend la fonction :
	# l'objet Figure sur lequel l'animation sera affichée
	# une séquence d'images qui seront affichées dans l'animation. Dans notre cas, chaque image correspond à une génération différente de la grille de jeu.
	# l'intervalle de temps en millisecondes entre chaque image de l'animation.
	# un booléen qui indique si l'animation doit être répétée ou non.
	# un booléen qui indique si la fonction doit réafficher uniquement les parties de la figure qui ont changé entre deux images consécutives. Cette option peut accélérer considérablement le temps de rendu de l'animation.

pyplot.show()
