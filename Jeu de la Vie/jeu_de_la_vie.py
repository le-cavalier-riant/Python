# =================================================================================================================== #
#                                                                                                                     #
#                                                    Jeu de la Vie                                                    #
#                                                                                                                     #
# =================================================================================================================== #

import numpy
import random
import time

from matplotlib import pyplot, animation


# =================================================================================================================== #
# fonctions
# =================================================================================================================== #

def mise_a_jour(grille):
    taille = len(grille)
    nouvelle_grille = numpy.zeros((taille, taille))
    for i in range(taille):
        for j in range(taille):
            nombre_de_voisins_vivants = int(
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
                if nombre_de_voisins_vivants < 2 or nombre_de_voisins_vivants > 3:
                    nouvelle_grille[i][j] = 0
                else:
                    nouvelle_grille[i][j] = 1
            else:
                if nombre_de_voisins_vivants == 3:
                    nouvelle_grille[i][j] = 1
    return nouvelle_grille


def animer_canvas(grille, generation_maximum, intervalle_temporelle):
    images = []
    for i in range(generation_maximum):
        pyplot.axis("off")
        images.append((pyplot.imshow(grille, cmap="binary"),))
        grille = mise_a_jour(grille)
    animation.ArtistAnimation(
        pyplot.figure(), images, interval=1000 * intervalle_temporelle, repeat=False, blit=True
    )
    pyplot.show()


def animer_console(grille, generation_maximum, intervalle_temporelle, cadrillage_affiche):
    # pas optimisée pour taille > 40
    for i in range(generation_maximum):
        print("\n	Génération", i + 1, ":")
        for j in range(len(grille)):
            print("")
            for k in range(len(grille)):
                if grille[j][k] == 0:
                    if cadrillage_affiche:
                        print("□ ", end="")
                    else:
                        print("  ", end="")
                else:
                    print("■ ", end="")
        print("\n")
        time.sleep(intervalle_temporelle)
        grille = mise_a_jour(grille)


# =================================================================================================================== #
# génération des grilles
# =================================================================================================================== #

def grille_vide(taille):
    return numpy.zeros((taille, taille))


def grille_pleine(taille):
    return numpy.ones((taille, taille))


def grille_aleatoire(taille):
    grille = numpy.zeros((taille, taille))
    for i in range(taille):
        for j in range(taille):
            grille[i][j] = random.randint(0, 1)
    return grille


# =================================================================================================================== #
# ajout d'ogranismes
# =================================================================================================================== #

def ajouter_lwss(grille, x, y):
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


def ajouter_planeur(grille, x, y):
    #
    # #
    ##

    grille[y][x + 2] = 1

    grille[y + 1][x] = 1
    grille[y + 1][x + 2] = 1

    grille[y + 2][x + 1] = 1
    grille[y + 2][x + 2] = 1


def ajouter_canon_a_planneur(grille, x, y):
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


def ajouter_pentomino_r(grille, x, y):
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
