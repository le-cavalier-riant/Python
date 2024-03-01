# =================================================================================================================== #
#                                                                                                                     #
#                                                    Jeu de la Vie                                                    #
#                                                                                                                     #
# =================================================================================================================== #

import jeu_de_la_vie

taille = int(input("\n	Quelle taille de grille souhaitez-vous ?\n"))
generation_maximum = int(input("\n	Combien de générations souhaitez-vous ?\n"))
pause = int(input("\n	Quel temps de pause entre chaque générations souhaitez-vous ? (nombre entier)\n"))
afficher_cadrillage = input("\n	Souhaitez-vous afficher le cadrillage ?\n		[N] : Non | [O] : Oui\n")
if afficher_cadrillage == "O" or afficher_cadrillage == "o":
	afficher_cadrillage = True
else:
	afficher_cadrillage = False

grille1 = jeu_de_la_vie.grille_aleatoire(taille)
jeu_de_la_vie.animer_console(grille1, generation_maximum, pause, afficher_cadrillage)

# grille2 = jeu_de_la_vie.grille_vide(taille)
# jeu_de_la_vie.ajouter_lwss(grille2, 50, 50)
# jeu_de_la_vie.ajouter_canon_a_planneur(grille2, 10, 10)
# jeu_de_la_vie.ajouter_pentomino_r(grille2, 50, 50)
# jeu_de_la_vie.animer_canvas(grille2, generation_maximum, pause)

# =================================================================================================================== #
#                                                                                                                     #
#                                                    Jeu de la Vie                                                    #
#                                                                                                                     #
# =================================================================================================================== #
