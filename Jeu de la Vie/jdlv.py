# =================================================================================================================== #
#                                                                                                                     #
#                                                    Jeu de la Vie                                                    #
#                                                                                                                     #
# =================================================================================================================== #

import jeuDeLaVie

taille = int(input("\n	Quelle taille de grille souhaitez-vous ?\n"))
generationMaximum = int(input("\n	Combien de générations souhaitez-vous ?\n"))
pause = int(input("\n	Quel temps de pause entre chaque générations souhaitez-vous ?\n"))
afficherCadrillage = input("\n	Souhaitez-vous afficher le cadrillage ?\n		[N] : Non | [O] : Oui\n")
if afficherCadrillage == "O" or afficherCadrillage == "o":
	afficherCadrillage = True
else:
	afficherCadrillage = False 

grille1 = jeuDeLaVie.grilleAleatoire(taille)
jeuDeLaVie.animerConsole(grille1, generationMaximum, pause, afficherCadrillage)

# grille2 = jeuDeLaVie.grilleVide(taille)
# jeuDeLaVie.ajouterLWSS(grille2, 50, 50)
# jeuDeLaVie.ajouterCanonPlanneur(grille2, 10, 10)
# jeuDeLaVie.ajouterPentominoR(grille2, 50, 50)
# jeuDeLaVie.animerCanvas(grille2, generationMaximum, pause)

# =================================================================================================================== #
#                                                                                                                     #
#                                                    Jeu de la Vie                                                    #
#                                                                                                                     #
# =================================================================================================================== #