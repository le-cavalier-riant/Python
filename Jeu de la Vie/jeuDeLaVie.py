# =================================================================================================================== #
#                                                                                                                     #
#                                                    Jeu de la Vie                                                    #
#                                                                                                                     #
# =================================================================================================================== #

import random, numpy, time
from matplotlib import pyplot, animation

# =================================================================================================================== #
	# fonctions
# =================================================================================================================== #

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

def animerCanvas(grille, generationMaximum, intervalleTemporelle):
	images = []
	for i in range(generationMaximum):
		pyplot.axis("off")
		images.append((pyplot.imshow(grille, cmap = "binary"),))
		grille = miseAJour(grille)
	anim = animation.ArtistAnimation(pyplot.figure(), images, interval = 1000 * intervalleTemporelle, repeat = False, blit = True)
	pyplot.show()

def animerConsole(grille, generationMaximum, intervalleTemporelle, cadrillageAffiche):  # pas optimisée pour taille > 40
	grilles = []
	for i in range(generationMaximum):
		print("\n	Génération", i + 1, ":")
		for j in range(len(grille)):
			print("")
			for k in range(len(grille)):
				if grille[j][k] == 0:
					if cadrillageAffiche:
						print("□ ", end = "")
					else:
						print("  ", end = "")
				else:
					print("■ ", end = "")
		print("\n")
		time.sleep(intervalleTemporelle)
		grille = miseAJour(grille)

# =================================================================================================================== #
	# génération des grilles
# =================================================================================================================== #

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

# =================================================================================================================== #
	# ajout d'ogranismes
# =================================================================================================================== #

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

# =================================================================================================================== #
#                                                                                                                     #
#                                                    Jeu de la Vie                                                    #
#                                                                                                                     #
# =================================================================================================================== #