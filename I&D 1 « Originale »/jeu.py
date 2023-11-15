# Jeu programmé par le groupe :
# - Artus de Chavagnac
# - Jean Manoury
# - Valentin Delangle
# - Nicolas Lesage
# - Théo Gaillard
# dans le cadre du projet informatique.

# ISEP 2022 - I1


from sys import exit  # quitter le code
from time import sleep  # attendre un temps donné
from numpy import random, floor  # générer un nombre aléatoire, arrondir un nombre
from typing import Any  # détailler les variables


class style:  # détermine le style d'affichage du texte dans la console
    succes: str = "\033[92m"
    attention: str = "\033[93m"
    echec: str = "\033[91m"
    gras: str = "\033[1m"
    aucun: str = "\033[0m"


# ==== VARIABLES GLOBALES ====

# === variables de valeurs ===

# - données de jeu -
abscisse: int
ordonnee: int
tour: int
vie: int
vieAvant: int
taillePetite: int
tailleMatrice: int
inventaire: list[int]
matrice = random.randint(0, 7, (5, 5))
difficulte: int
caracteristiqueAvant: int = 0

# - autres -
attente: int = 5  # secondes
decalage: str = 20 * " "
decalage2: str = 10 * " "

# - chargement depuis un fichier > charger() -
listeSauvegarde: list[Any]
listeMatrice: list[Any]
listeInventaire: list[Any]

# - affichage de la salle > salleCarte(x, y) -
murHaut: str
porteHaut: str
interieurHaut: str
porteGauche: str
porteDroite: str
porteDroiteGauche: str
interieurBas: str
porteBas: str
murBas: str
ligne: list[str]

# - dessins > messages -
bouclier: str = "|'-._/\\_.-'|\n" \
                "|    ||    |\n" \
                "|___o()o___|\n" \
                "|__((<>))__|\n" \
                "\\   o\\/o   /\n" \
                " \\   ||   /\n" \
                "  \\  ||  /\n" \
                "   '.||.'\n" \
                "     ‾‾"
epee: str = "      /|͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟\n" \
            "O|===|*|⟩---------------------⟩\n" \
            "      \\|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"

# ==== messages ====

# - erreurs -
touches: str = style.attention + "\n[Z] : haut         |  [A] : accepter\n" \
                                   "[S] : bas          |  [R] : refuser\n" \
                                   "[Q] : gauche       |  [+] : enregistrer\n" \
                                   "[D] : droite       |  [-] : quitter\n" + style.aucun
erreur: str = style.echec + "\nVeuillez repondre " + style.gras + "CORRECTEMENT ! ❌\n" + style.aucun + touches
erreurSeule: str = style.echec + "\nVeuillez repondre " + style.gras + "CORRECTEMENT ! ❌\n" + style.aucun
erreurMur: str = style.echec + "\nDésolé vous ne pouvez pas , il y a " + style.gras + "UN MUR ! ❌\n" + \
                  style.aucun

# - salles -
salleVide: str = style.aucun + "\n        Cette salle est " + style.gras + "VIDE\n" + style.aucun
salleDragon: str = style.attention + "\n       La salle est gardée par " + style.gras + "UN DRAGON !\n" + \
                    style.aucun
salleNourriture: str = style.succes + "\n      Cette salle contient un coffre avec de la " + style.gras + \
                        "NOURRITURE !\n" + style.aucun
salleEpee: str = style.succes + "\n        Cette salle contient un coffre avec " + style.gras + "UNE ÉPÉE !\n" + \
                  style.aucun + style.succes + epee + style.aucun
salleBouclier: str = style.succes + "\n        Cette salle contient un coffre avec " + style.gras + \
                      "UN BOUCLIER !\n" + style.aucun + style.succes + bouclier + style.aucun
salleRoidesdragons: str = style.attention + "\n        Cette salle est gardée par " + style.gras + \
                           "LE ROI DES DRAGONS !\n" + style.aucun
auRevoir: str = "\nTrès bien, j'éspère que vous avez aprécié votre partie, a bientôt !\n"
nouvellePartieMessage: str = "Voulez-vous " + style.gras + "RECOMMENCER" + style.aucun + " une partie ?\n"


# ==== fonctions ====

def annuler(cause: str):  # annule l'action qui s'est produite
    if cause == "mur":
        print(erreurMur)
    elif cause == "erreur":
        print(erreur)
    global vie, vieAvant
    vie = vieAvant
    effetsSansEffets(abscisse, ordonnee)
    salleCarte(abscisse, ordonnee)
    jeu(abscisse, ordonnee, tour)


def dessins(x: int, y: int):  # assemble la salle et la carte
    global ligne, murHaut, porteHaut, interieurHaut, porteGauche, porteDroite, porteDroiteGauche, interieurBas, \
        porteBas, murBas, matrice, caracteristiqueAvant
    ligne = ["   " + "͟͟͟" * tailleMatrice + "͟\n", "  /" + "   " * tailleMatrice + "/\\\n", " |" + "   " *
             int(((tailleMatrice - 3) / 2)) + "~ Carte ~" + "   " * int(((tailleMatrice - 3) / 2)) + "|‾‾\n"]
    for i in range(taillePetite - y):
        ligne.append(" |" + " □ " * (2 * taillePetite + 1) + "|\n")
    ligne.append(" |" + " □ " * (x + taillePetite) + " ■ " + " □ " * (taillePetite - x) + "|\n")
    for i in range(taillePetite + y):
        ligne.append(" |" + " □ " * (2 * taillePetite + 1) + "|\n")
    ligne.append(" |" + "   " * int(((tailleMatrice - 3) / 2)) + "tour n°" + style.gras + str(tour) + style.aucun
                 + " " * int(1 - floor(tour / 10)) + "   " * int(((tailleMatrice - 3) / 2)) + "|\n")
    ligne.append("͟|" + "͟͟͟" * (tailleMatrice - 1) + "͟  |\n")
    ligne.append("\\" + "   " * (tailleMatrice - 1) + "  \\/\n")
    ligne.append(" " + "‾‾‾" * tailleMatrice + "\n")
    for i in range(10 - tailleMatrice):
        ligne.append("\n")
    contenu = []
    if caracteristiqueAvant == 0:  # vide
        contenu = ["                             ",
                   "                             ",
                   "                             ",
                   "                             ",
                   "                             "]
    elif 0 < caracteristiqueAvant < 5 or caracteristiqueAvant == 9:  # dragon et RDD
        contenu = ["             .               ",
                   "        .>   )\\;`a__         ",
                   "       (  _ _)/ /-.' ~~      ",
                   "        `( )_ )/             ",
                   "         <_  <_              "]
    elif 4 < caracteristiqueAvant < 9:  # nourriture, épée et bouclier
        contenu = ["        ___________          ",
                   "       |\\__________|\\        ",
                   "       ||          ||        ",
                   "        \\‾‾‾‾‾‾‾‾‾‾‾\\|       ",
                   "        ‾‾‾‾‾‾‾‾‾‾‾‾         "]
    murHaut = decalage2 + "                                       " + decalage + ligne[0] + \
               decalage2 + " |\\‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾|\\   " + decalage + ligne[1] + \
               decalage2 + " | \\ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _| \\  " + decalage + ligne[2]

    porteHaut = decalage2 + "                |\\ |\\                  " + decalage + ligne[0] + \
                 decalage2 + " |\\‾ ‾ ‾ ‾ ‾ ‾ ‾\\ \\ \\‾ ‾ ‾ ‾ ‾ ‾ ‾|\\   " + decalage + ligne[1] + \
                 decalage2 + " | \\ _ _ _ _ _ _ \\|  \\_ _ _ _ _ _ | \\  " + decalage + ligne[2]

    interieurHaut = decalage2 + " |  |                             |  | " + decalage + ligne[3] + \
                     decalage2 + " |  |                             |  | " + decalage + ligne[4]

    porteGauche = decalage2 + "_|  |" + contenu[0] + "|  | " + decalage + ligne[5] + \
                   decalage2 + "\\ \\ |" + contenu[1] + "|  | " + decalage + ligne[6] + \
                   decalage2 + " \\_\\|" + contenu[2] + "|  | " + decalage + ligne[7] + \
                   decalage2 + "_    " + contenu[3] + "|  | " + decalage + ligne[8] + \
                   decalage2 + "\\|\\  " + contenu[4] + "|  | " + decalage + ligne[9] + \
                   decalage2 + " | \\                              |  | " + decalage + ligne[10]

    porteDroite = decalage2 + " |  |" + contenu[0] + "| _| " + decalage + ligne[5] + \
                   decalage2 + " |  |" + contenu[1] + " \\ \\ " + decalage + ligne[6] + \
                   decalage2 + " |  |" + contenu[2] + "  \\_\\" + decalage + ligne[7] + \
                   decalage2 + " |  |" + contenu[3] + "   _  " + decalage + ligne[8] + \
                   decalage2 + " |  |" + contenu[4] + "|\\ \\ " + decalage + ligne[9] + \
                   decalage2 + " |  |                             | \\_\\" + decalage + ligne[10]

    porteDroiteGauche = decalage2 + "_|  |" + contenu[0] + "| _| " + decalage + ligne[5] + \
                          decalage2 + "\\ \\ |" + contenu[1] + " \\ \\ " + decalage + ligne[6] + \
                          decalage2 + " \\_\\|" + contenu[2] + "  \\_\\" + decalage + ligne[7] + \
                          decalage2 + "_   " + contenu[3] + "   _  " + decalage + ligne[8] + \
                          decalage2 + "\\|\\  " + contenu[4] + "|\\ \\ " + decalage + ligne[9] + \
                          decalage2 + " | \\                              | \\_\\" + decalage + ligne[10]

    interieurBas = decalage2 + " |  |                             |  | " + decalage + ligne[11] + \
                    decalage2 + " |  |                             |  | " + decalage + ligne[12] + \
                    decalage2 + " |  |                             |  | " + decalage + ligne[13]

    porteBas = decalage2 + " \\ ‾ ‾ ‾ ‾ ‾ ‾ ‾|\\ |\\‾ ‾ ‾ ‾ ‾ ‾ ‾ \\ | " + decalage + ligne[14] + \
                decalage2 + "  \\ _ _ _ _ _ _ \\ \\\\ \\ _ _ _ _ _ _ _\\| " + decalage + ligne[15] + \
                decalage2 + "                 \\| \\|                 " + decalage + ligne[16]

    murBas = decalage2 + " \\ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾ \\ | " + decalage + ligne[14] + \
              decalage2 + "  \\_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\\| " + decalage + ligne[15] + \
              decalage2 + "                                       " + decalage + ligne[16]


def salleCarte(x: int, y: int):  # affiche la salle, la carte et positionne le joueur
    dessins(abscisse, ordonnee)
    if x == taillePetite:
        if y == taillePetite:
            print(murHaut, interieurHaut, porteGauche, interieurBas, porteBas, sep="")
        elif y == -taillePetite:
            print(porteHaut, interieurHaut, porteGauche, interieurBas, murBas, sep="")
        else:
            print(porteHaut, interieurHaut, porteGauche, interieurBas, porteBas, sep="")
    elif x == -taillePetite:
        if y == taillePetite:
            print(murHaut, interieurHaut, porteDroite, interieurBas, porteBas, sep="")
        elif y == -taillePetite:
            print(porteHaut, interieurHaut, porteDroite, interieurBas, murBas, sep="")
        else:
            print(porteHaut, interieurHaut, porteDroite, interieurBas, porteBas, sep="")
    elif y == taillePetite:
        print(murHaut, interieurHaut, porteDroiteGauche, interieurBas, porteBas, sep="")
    elif y == -taillePetite:
        print(porteHaut, interieurHaut, porteDroiteGauche, interieurBas, murBas, sep="")
    else:
        print(porteHaut, interieurHaut, porteDroiteGauche, interieurBas, porteBas, sep="")
    for i in range(17, tailleMatrice + 7):
        print("                                       " + decalage + ligne[i], sep=""),


def charger():  # recuperer la progression depuis un fichier de sauvegarde
    global listeSauvegarde, abscisse, ordonnee, tour, taillePetite, tailleMatrice, matrice, listeMatrice, vie, \
        difficulte
    fichierLecture = input("\nQuel est le nom du " + style.gras + "FICHIER" + style.aucun + " de sauvegarde ?\n")
    if fichierLecture == "":
        fichierLecture = "sauvegarde.txt"
    try:
        open(fichierLecture, "r")
        sauvegardeLecture = open(fichierLecture, "r")
        listeSauvegarde = sauvegardeLecture.readline().split(",")
        abscisse = int(listeSauvegarde[0])
        ordonnee = int(listeSauvegarde[1])
        tour = int(listeSauvegarde[2])
        taillePetite = int(listeSauvegarde[3])
        tailleMatrice = 2 * taillePetite + 1
        difficulte = int(15 * int(listeSauvegarde[4]) + 1)
        matrice = random.randint(0, 7, (tailleMatrice, tailleMatrice))
        listeMatrice = []
        for i in range(tailleMatrice):
            listeMatrice = listeSauvegarde[i + 5].split(" ")
            listeMatrice1 = listeMatrice[0].split("[")
            listeMatrice[0] = listeMatrice1[1]
            listeMatrice0 = listeMatrice[tailleMatrice - 1].split("]")
            listeMatrice[tailleMatrice - 1] = listeMatrice0[0]
            for j in range(tailleMatrice):
                matrice[i][j] = listeMatrice[j]
        vie = int(listeSauvegarde[tailleMatrice + 5])
        listeInventaire0 = listeSauvegarde[tailleMatrice + 6].split("[")
        inventaire[0] = int(listeInventaire0[1])
        listeInventaire1 = listeSauvegarde[tailleMatrice + 7].split("]")
        listeInventaire2 = listeInventaire1[0].split(" ")
        inventaire[1] = int(listeInventaire2[1])
        print(style.succes + "\nLa progression a bien été chargée depuis le fichier : '", fichierLecture,
              "'" + style.aucun, sep="")
    except FileNotFoundError:
        print(style.echec + "\nLe fichier ", fichierLecture, " n'existe pas !\n" + style.aucun, sep='"')
        chargerDemande = input("Voulez-vous charger une partie ?\n")
        if chargerDemande == "a" or chargerDemande == "A" or chargerDemande == "":
            charger()
        if chargerDemande == "r" or chargerDemande == "R":
            initialisation()
            print(style.succes + "\nTrès bien, la partie va commencer !\nBonne chance !\n"
                                   "    Voilà les touches pour jouer :" + style.aucun, touches)
            sleep(attente)
            print("\n" * 20)
            return
        else:
            print(erreur)
            charger()
    return


def effets(x: int, y: int):  # effets de la salle sur le joueur
    global tailleMatrice, vie, vieAvant, difficulte, caracteristiqueAvant
    vieAvant = vie
    caracteristique: int = matrice[taillePetite - y][taillePetite + x]
    caracteristiqueAvant = caracteristique
    if caracteristique == 0:  # vide
        print(salleVide)
    elif 0 < caracteristique < 5:  # dragon
        print(salleDragon)
        if inventaire[1] == 1:
            vie -= random.randint(0, (difficulte - 10))
            print("Grâce au bouclier, vous avez perdu moins de points de vie.\n")
        else:
            vie -= random.randint(10, difficulte)
        print(style.echec + "Vous avez " + style.gras + "PERDU" + style.aucun + style.echec
              + " des points de vie !\n" + style.aucun)
        if vie < 1:
            mort()
        if inventaire[0] == 1:
            print(style.succes + "Vous avez " + style.gras + "VAINCU" + style.aucun + style.succes
                  + " le dragon \n" + style.aucun)
            matrice[taillePetite - y][taillePetite + x] = 0
    elif 4 < caracteristique < 7:  # nourriture
        print(salleNourriture)
        if vie > 79:
            print(style.attention + "Vous avez assez de points de vie, vous ne prenez " + style.gras + "PAS" +
                  style.aucun + style.attention + " la nourriture.\n" + style.aucun)
            etat()
            return
        vie += random.randint(10, 31)
        if vie > 100:
            vie = 100
        print(style.succes + "Vous avez " + style.gras + "GAGNE" + style.aucun + style.succes +
              " des points de vie !\n" + style.aucun)
        matrice[taillePetite - y][taillePetite + x] = 0
    elif caracteristique == 7:  # épée
        inventaire[0] = 1
        print(salleEpee)
        matrice[taillePetite - y][taillePetite + x] = 0
    elif caracteristique == 8:  # bouclier
        inventaire[1] = 1
        print(salleBouclier)
        matrice[taillePetite - y][taillePetite + x] = 0
    elif caracteristique == 9:  # roi des dragons
        print(salleRoidesdragons)
        if inventaire[1] == 1:
            vie -= random.randint(difficulte - 20, difficulte)
        else:
            vie -= random.randint(difficulte - 10, difficulte + 10)
        if vie < 1:
            mort()
        else:
            if inventaire[0] == 1:
                if inventaire[1] == 1:
                    partieGagnee()
                else:
                    print(style.echec + "Vous devez avoir un " + style.gras + "BOUCLIER" + style.echec
                          + " pour combattre le Roi des Dragons !\n" + style.aucun)
            elif inventaire[1] == 0:
                print(style.echec + "Vous devez avoir une " + style.gras + "EPEE" + style.echec + " et un " +
                      style.gras + "BOUCLIER" + style.echec + " pour combattre le Roi des Dragons !\n" +
                      style.aucun)
            else:
                print(style.echec + "Vous devez avoir une " + style.gras + "EPEE" + style.echec +
                      " pour combattre le Roi des Dragons !\n" + style.aucun)
    etat()


def effetsSansEffets(x: int, y: int):  # effets de la salle sur le joueur, mais sans affectation
    global tailleMatrice, vie, vieAvant
    caracteristique = matrice[taillePetite - y][taillePetite + x]
    if caracteristique == 0:  # vide
        print(salleVide)
    elif 0 < caracteristique < 5:  # dragon
        print(salleDragon)
        if inventaire[0] == 1:
            print(style.succes + "Vous avez " + style.gras + "VAINCU" + style.aucun + style.succes +
                  " le dragon \n" + style.aucun)
    elif 4 < caracteristique < 7:  # nourriture
        print(salleNourriture)
    elif caracteristique == 7:  # épée
        print(salleEpee)
    elif caracteristique == 8:  # bouclier
        print(salleBouclier)
    elif caracteristique == 9:  # roi des dragons
        print(salleRoidesdragons)
        if inventaire[0] == 1:
            if inventaire[1] == 1:
                partieGagnee()
            else:
                print(style.echec + "Vous devez avoir un " + style.gras + "BOUCLIER" + style.echec +
                      " pour combattre le Roi des Dragons !\n" + style.aucun)
        elif inventaire[1] == 0:
            print(style.echec + "Vous devez avoir une " + style.gras + "EPEE" + style.echec + " et un " +
                  style.gras + "BOUCLIER" + style.echec + " pour combattre le Roi des Dragons !\n" + style.aucun)
        else:
            print(style.echec + "Vous devez avoir une " + style.gras + "EPEE" + style.echec +
                  " pour combattre le Roi des Dragons !\n" + style.aucun)
    etat()


def enregistrer():  # sauvegarder la progression dans un fichier de sauvegarde
    global abscisse, ordonnee, tour, taillePetite, matrice, vie, inventaire, listeMatrice
    fichierEcriture = input("Comment voulez vous appeler votre fichier de sauvegarde ? (Précisez l'extension)\n")
    if fichierEcriture == "":
        fichierEcriture = "sauvegarde.txt"
    try:
        open(fichierEcriture, "r")
        print(style.echec + "\nUn fichier existe déja sous ce nom !" + style.aucun)
        enregistrerDemande = input("Voulez-vous enregistrer votre progression ?\n")
        if enregistrerDemande == "a" or enregistrerDemande == "A" or enregistrerDemande == "":
            enregistrer()
        elif enregistrerDemande == "r" or enregistrerDemande == "R":
            return
        else:
            print(erreur)
            enregistrer()
    except FileNotFoundError:
        sauvegardeEcriture = open(fichierEcriture, "a")
        sauvegardeEcriture.write(
            str(abscisse) + "," + str(ordonnee) + "," + str(tour) + "," + str(taillePetite) + "," + str(difficulte) +
            ",")
        listeMatrice = []
        for i in range(tailleMatrice):
            listeMatrice.append(matrice[i])
            sauvegardeEcriture.write(str(listeMatrice[i]) + ",")
        sauvegardeEcriture.write(str(vie) + "," + str(inventaire))
        sauvegardeEcriture.close()
        print(style.succes + "\nLa progression a bien été enregistrée dans le fichier : \n'" + style.gras +
              fichierEcriture + style.aucun + style.succes + "'" + style.aucun, sep="")


def etat():
    global vie
    vieDixieme = int(vie / 10)
    if 50 < vie < 101:
        print(style.succes + "▰" * vieDixieme, "▱" * (10 - vieDixieme), " ", vie, " points de vie." +
              style.aucun, sep="")
    elif 25 < vie < 51:
        print(style.attention + "▰" * vieDixieme, "▱" * (10 - vieDixieme), " ", vie, " points de vie." +
              style.aucun, sep="")
    elif -1 < vie < 26:
        print(style.echec + "▰" * vieDixieme, "▱" * (10 - vieDixieme), " ", vie, " points de vie." +
              style.aucun, sep="")
    if inventaire[0] == 1:
        print(style.succes + "Vous avez une épée ! 🗡️" + style.aucun)
    else:
        print("Vous n'avez pas d'épée.")
    if inventaire[1] == 1:
        print(style.succes + "Vous avez un bouclier ! 🛡️\n" + style.aucun)
    else:
        print("Vous n'avez pas de bouclier.\n")


def initialisation():
    global tailleMatrice, taillePetite, abscisse, ordonnee, tour, matrice, vie, inventaire, vieAvant, difficulte
    difficulte = input("\nQuelle " + style.gras + "DIFFICULTE" + style.aucun + " de jeu voulez-vous ?\n" +
                       style.attention + "Facile : 1\nNormale : 2\nDifficile : 3\n" + style.aucun)
    if difficulte == "":
        difficulte = int(2)
    try:
        difficulte = int(difficulte)
        if difficulte < 1:
            print(style.echec + "\nVeuillez repondre " + style.gras + "CORRECTEMENT ! ❌\n" + style.aucun
                  + style.echec + "Veuillez saisir un " + style.gras + "ENTIER" + style.aucun + style.echec +
                  " supérieur à 1." + style.aucun)
            initialisation()
            return
        difficulte = int(15 * difficulte + 1)
    except ValueError:
        print(style.echec + "\nVeuillez repondre " + style.gras + "CORRECTEMENT ! ❌\n" + style.aucun
              + style.echec + "Veuillez saisir un " + style.gras + "ENTIER" + style.aucun + style.echec +
              " supérieur à 1." + style.aucun)
        initialisation()
    tailleMatrice = input("\nQuelle " + style.gras + "TAILLE" + style.aucun + " de carte voulez-vous ?\n" +
                           style.attention + "Petite : 5\nNormale : 7\nGrande : 9\n" + style.aucun)
    if tailleMatrice == "":
        tailleMatrice = int(5)
    try:
        tailleMatrice = int(tailleMatrice)
        taillePetite = int(floor((tailleMatrice - 1) / 2))
        tailleMatrice = int(2 * taillePetite + 1)
    except ValueError:
        print(style.echec + "\nVeuillez repondre " + style.gras + "CORRECTEMENT ! ❌\n" + style.aucun
              + style.echec + "Veuillez saisir un " + style.gras + "ENTIER IMPAIR" + style.aucun)
        initialisation()
        return
    abscisse = 0
    ordonnee = 0
    tour = 0
    matrice = random.randint(0, 7, (tailleMatrice, tailleMatrice))
    matrice[taillePetite][taillePetite] = 0  # la salle du milieu est vide
    affectationX0 = 0
    affectationY0 = 0
    affectation0 = [affectationX0, affectationY0]
    while affectation0 == [0, 0]:
        affectationX0 = random.randint(0, tailleMatrice)
        affectationY0 = random.randint(0, tailleMatrice)
        affectation0 = [affectationX0, affectationY0]
    matrice[affectationX0][affectationY0] = 7  # une seule salle avec une épéé
    affectationX1 = 0
    affectationY1 = 0
    affectation1 = [affectationX1, affectationY1]
    while affectation1 == [0, 0] or affectation1 == affectation0:
        affectationX1 = random.randint(0, tailleMatrice)
        affectationY1 = random.randint(0, tailleMatrice)
        affectation1 = [affectationX1, affectationY1]
    matrice[affectationX1][affectationY1] = 8  # une seule salle avec un bouclier
    affectationX2 = 0
    affectationY2 = 0
    affectation2 = [affectationX2, affectationY2]
    while affectation2 == [0, 0] or affectation2 == affectation0 or affectation2 == affectation1:
        affectationX2 = random.randint(0, tailleMatrice)
        affectationY2 = random.randint(0, tailleMatrice)
        affectation2 = [affectationX2, affectationY2]
    matrice[affectationX2][affectationY2] = 9  # une seule salle avec le RDD
    vie = 100
    vieAvant = vie
    inventaire = [0, 0]
    dessins(abscisse, ordonnee)


def jeu(x: int, y: int, t: int):  # effectue l'action demandée par le joueur
    global abscisse, ordonnee, tour, vie, vieAvant
    touche = input(style.attention + "\nDans quelle " + style.gras + "DIRECTION" + style.attention
                   + " voulez-vous aller ?\n" + style.aucun)
    print("=" * 100, "\n" * 20, "=" * 100, sep="")
    if touche == "z" or touche == "Z":
        if taillePetite > y:
            y += 1
            t += 1
        else:
            annuler("mur")
            return
    elif touche == "s" or touche == "S":
        if -taillePetite < y:
            y -= 1
            t += 1
        else:
            annuler("mur")
            return
    elif touche == "q" or touche == "Q":
        if -taillePetite < x:
            x -= 1
            t += 1
        else:
            annuler("mur")
            return
    elif touche == "d" or touche == "D":
        if taillePetite > x:
            x += 1
            t += 1
        else:
            annuler("mur")
            return
    elif touche == "+":
        enregistrer()
        annuler("")
        return
    elif touche == "-":
        quitter()
        return
    else:
        annuler("erreur")
        return
    abscisse = x
    ordonnee = y
    tour = t
    vieAvant = vie


def mort():  # mort du joueur, fin de partie
    print(style.echec + style.gras + "Vous êtes mort !\n" + style.aucun)
    etat()
    salleCarte(abscisse, ordonnee)
    nouvellePartieDemande = input(nouvellePartieMessage)
    if nouvellePartieDemande == "a" or nouvellePartieDemande == "A" or nouvellePartieDemande == "":
        deroulement()
    elif nouvellePartieDemande == "r" or nouvellePartieDemande == "R":
        print(style.succes + auRevoir + style.aucun)
        exit()
    else:
        print(erreur)
        mort()


def partieGagnee():  # succès du joueur : le RDD est mort, fin de partie
    print(style.succes + "\n    Bravo vous avez vaincu le Roi des Dragons et récupéré le " + style.gras + "trésor !"
          + style.aucun + style.succes + "\nVous êtes le meilleur !\n" + style.aucun)
    nouvellePartieDemande = input(nouvellePartieMessage)
    if nouvellePartieDemande == "a" or nouvellePartieDemande == "A" or nouvellePartieDemande == "":
        deroulement()
    elif nouvellePartieDemande == "r" or nouvellePartieDemande == "R":
        quitter()
        return
    else:
        print(erreur)
        partieGagnee()


def quitter():  # quitter la partie
    quitterDemande = input("\nVoulez-vous vraiment " + style.gras + "QUITER" + style.aucun + " la partie ?\n")
    if quitterDemande == "a" or quitterDemande == "A" or quitterDemande == "":
        nouvellePartieDemande = input("Voulez-vous recommencer une partie ?\n")
        if nouvellePartieDemande == "a" or nouvellePartieDemande == "A" or nouvellePartieDemande == "":
            print("Très bien !")
            deroulement()
        elif nouvellePartieDemande == "r" or nouvellePartieDemande == "R":
            print(style.succes + auRevoir + style.aucun)
            exit()
        else:
            print(erreur)
            quitter()
    elif quitterDemande == "r" or quitterDemande == "R":
        annuler("")
    else:
        print(erreur)
        quitter()
        return


def menu():  # accueil et début de la partie
    print(style.succes + "\nBienvenue dans " + style.gras + "'Info & Dragons' !\n" + style.aucun, sep="")
    print(style.echec + "          /           /\n"
                          "         /' .,,,,  ./\n"
                          "        /';'     ,/\n"
                          "       / /   ,,//,'''\n"
                          "      ( ,, '_,  ,,,' '\n"
                          "      |    /@  ,,, ;' '\n"
                          "     /    .   ,''/' ','\n"
                          "    /   .     ./, ',, ' ;\n"
                          " ,./  .   ,-,',' ,,/''\\,'\n"
                          "|   /; ./,,'',,'' |   |\n"
                          "|     /   ','    /    |\n"
                          " \\___/'   '     |     |\n"
                          "   ',,'  |      /     '\\\n"
                          "        /      |        ~\\\n"
                          "       '       (\n" + style.aucun, sep="")
    print(style.succes + "    ~ MENU ~\n\n" + style.aucun +
          style.attention + "[A] : Nouvelle partie\n"
                              "[R] : Quitter\n"
                              "[E] : Charger partie\n"
                              "[C] : Crédits\n" + style.aucun, sep="")
    entree = input("Que voulez-vous faire ?\n")
    if entree == "a" or entree == "A" or entree == "":
        initialisation()
        print(style.succes + "\nTrès bien, la partie va " + style.gras + "COMMENCER" + style.aucun
              + style.attention + " !\nBonne chance !\n    Voilà les touches pour jouer :" + style.aucun, touches)
        sleep(attente)
        print("\n" * 20)
        return
    if entree == "e" or entree == "E":
        charger()
        return
    if entree == "c" or entree == "C":
        print("\n"
              "Jeu programmé par le groupe :\n"
              " - Artus de Chavagnac\n"
              " - Jean Manoury\n"
              " - Valentin Delangle\n"
              " - Nicolas Lesage\n"
              " - Théo Gaillard\n"
              "dans le cadre du projet informatique.\n\n"
              "ISEP 2022 - I1\n\n"
              "Vous êtes actuellement sur la version n°", style.gras + "12" + style.aucun, "\n\n",
              style.attention + "Pour revenir au menu, entrez une touche." + style.aucun, sep="")
        m = input("")
        if m == "":
            menu()
        else:
            menu()
    if entree == "r" or entree == "R":
        print(style.succes + auRevoir + style.aucun)
        exit()
    else:
        print(erreurSeule)
        menu()


def deroulement():  # succession des différentes fonctions
    global vie, vieAvant
    menu()
    while True:
        vieAvant = vie
        effets(abscisse, ordonnee)
        vieAvant = vie
        salleCarte(abscisse, ordonnee)
        jeu(abscisse, ordonnee, tour)


# ==== jeu ====

deroulement()
