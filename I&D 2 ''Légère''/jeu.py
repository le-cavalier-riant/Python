# =================================================================================================================== #
#                                                                                                                     #
#                                         Jeu programmé par Artus de Chavagnac                                        #
#                                                                                                                     #
#                                                    Info & Dragons                                                   #
#                                                                                                                     #
#                                                 Version n°2 "Légère"                                                #
#                                                                                                                     #
# =================================================================================================================== #

import typing, numpy, time

# =================================================================================================================== #
	# Déclaration des variables globales
# =================================================================================================================== #

attente = 4  # secondes
bouclier = "|'-._/\\_.-'|\n|    ||    |\n|___o()o___|\n|__((<>))__|\n\\   o\\/o   /\n \\   ||   /\n  \\  ||  /\n   '.||.'\n     ‾‾"
decalageDroit = 20 * " "
decalageGauche = 10 * " "
epee = "      /|͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟͟\nO|===|*|>--------------------->\n      \\|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"
erreur = "\nVeuillez repondre CORRECTEMENT !\n"
erreurDeSaisieInitialisation = "\nVeuillez repondre CORRECTEMENT !\nVeuillez saisir un ENTIER supérieur à 1."
erreurMur = "\nDésolé vous ne pouvez pas , il y a UN MUR !\n"
credits = "\n ====================================================================================================================\n\n                                         Jeu programmé par Artus de Chavagnac\n\n                                                    Info & Dragons\n\n                                                 Version n°2 \"Légère\"\n\n ====================================================================================================================\n\n"
presentationDifficulte = "\n    Facile : 1\n    Normale : 2\n    Difficile : 3\n\n"
presentationTaille = "\n    Petite : 5\n    Normale : 7\n    Grande : 9\n\n"
salleBouclier = "\n        Cette salle contient un coffre avec UN BOUCLIER !\n" + bouclier
salleDragon = "\n       La salle est gardée par UN DRAGON !\n"
salleEpee = "\n        Cette salle contient un coffre avec UNE ÉPÉE !\n" + epee
salleNourriture = "\n      Cette salle contient un coffre avec de la NOURRITURE !\n"
salleRoidesdragons = "\n        Cette salle est gardée par LE ROI DES DRAGONS !\n"
salleVide = "\n        Cette salle est VIDE\n"
touches = "\n    [Z] : haut       |  [A] : accepter\n    [S] : bas        |  [R] : refuser\n    [Q] : gauche     |  [+] : enregistrer\n    [D] : droite     |  [-] : quitter\n\n"
nouvellePartieMessage = "Voulez-vous RECOMMENCER une partie ?\n"
auRevoir = "\nTrès bien, j'éspère que vous avez aprécié votre partie, a bientôt !\n"
erreur = "\nVeuillez repondre CORRECTEMENT !\n"
logoMenu = "\n                                            /           /\n                                           /' .,,,,  ./\n                                          /';'     ,/\n                                         / /   ,,//,'''\n                                        ( ,, '_,  ,,,' '\n                                        |@   /@  ,,, ;' '\n                                       /    .   ,''/' ','\n                                      /   .     ./, ',, ' ;\n                                   ,./  .   ,-,',' ,,/''\\,'\n                                  |   /; ./,,'',,'' |   |\n                                  |     /   ','    /    |\n                                   \\___/' / '     |     |\n                                    ',,'  |      /     '\\\n            _____________________________/      |       ~\\_____________________________\n            |                            '       (                                    |\n            |                                                                         |\n            |      _____            ____            ________                          |\n            |       | |            / __ \\            | |    ‾\\                        |\n            |       | |           / /  \\ |           | |      |\\             __       |\n            |       | |          |  \\  / /           | |      | |         /‾__ ‾\\     |\n            |       | |           \\  --_/____        | |      | |        //‾  \\  |    |\n            |       | |           _> <-  \\  /        | |      | |             / /     |\n            |       | |         /‾/\\  \\  | /         | |      | |            / /      |\n            |       | |       / /   \\  \\ //          | |      | |           / /       |\n            |       | |      |  |    \\   /           | |      | |         / /___/|    |\n            |       | |      |   \\___/ _  \\__/|      | |      |/        /________/    |\n            |       | |       \\_     _/ \\____/       | |    _/         L É G È R E    |\n            |      ‾‾‾‾‾        ‾‾‾‾‾               ‾‾‾‾‾‾‾‾                          |\n            |                                                                         |\n            |                                                                         |\n            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\n"
touchesMenu = "\n    [A] : Nouvelle partie\n    [R] : Quitter\n    [E] : Charger partie\n    [C] : Crédits\n\n"

# =================================================================================================================== #
	# Déclaration des fonctions
# =================================================================================================================== #

def quitter():  # quitter la partie

	quitterDemande = input("\nVoulez-vous vraiment QUITER la partie ?\n")
	if quitterDemande == "a" or quitterDemande == "A" or quitterDemande == "":
		nouvellePartieDemande = input(nouvellePartieMessage)
		if nouvellePartieDemande == "a" or nouvellePartieDemande == "A" or nouvellePartieDemande == "":
			print("Très bien !")
			deroulement()
			return
		elif nouvellePartieDemande == "r" or nouvellePartieDemande == "R":
			print(auRevoir)
			exit()
		else:
			print(erreur)
			quitter()
			return
	elif quitterDemande == "r" or quitterDemande == "R":
		annuler("")
		return
	else:
		print(erreur)
		quitter()
		return

def partieGagnee():  # succès du joueur : le roi dragon est mort, fin de partie

	print("\n    Bravo vous avez vaincu le Roi des Dragons et récupéré le trésor !\nVous êtes le meilleur !\n")
	nouvellePartieDemande = input(nouvellePartieMessage)
	if nouvellePartieDemande == "a" or nouvellePartieDemande == "A" or nouvellePartieDemande == "":
		deroulement()
	elif nouvellePartieDemande == "r" or nouvellePartieDemande == "R":
		quitter()
		return
	else:
		print(erreur)
		partieGagnee()

def espace(tour):  # rajoute un espace sur la carte pour les nombres inférieurs à 10

	if tour > 9:
		return 0
	else:
		return 1

def menu():  # accueil et début de la partie

	print(logoMenu)
	print("        ~ MENU ~\n" + touchesMenu, sep="")
	entreeMenu = input("Que voulez-vous faire ?\n")
	if entreeMenu == "a" or entreeMenu == "A" or entreeMenu == "":
		initialisation()
		print("\nTrès bien, la partie va COMMENCER !\n\nBonne chance !\n\n    Voilà les touches pour jouer :\n", touches)
		time.sleep(attente)
		print("\n" * 20)
		return
	elif entreeMenu == "e" or entreeMenu == "E":
		charger()
		return
	elif entreeMenu == "c" or entreeMenu == "C":
		print(credits + "    Pour revenir au menu, appuyez sur [Entrée].", sep="")
		input("")
		menu()
		return
	elif entreeMenu == "r" or entreeMenu == "R":
		print(auRevoir)
		exit()
	else:
		print(erreur)
		menu()

def charger():  # recuperer la progression depuis un fichier de sauvegarde

	global abscisse, ordonnee, tour, taillePetite, tailleMatrice, matrice, vie, difficulte
	fichierLecture = input("\nQuel est le nom de votre SAUVEGARDE ?\n")
	if fichierLecture == "":
		fichierLecture = "sauvegarde"
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
		matrice = numpy.random.randint(0, 7, (tailleMatrice, tailleMatrice))
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
		print("\nLa progression a bien été chargée depuis le fichier : '", fichierLecture, "'", sep="")
	except FileNotFoundError:
		print("\nLe fichier ", fichierLecture, " n'existe pas !\n", sep='"')
		chargerDemande = input("Voulez-vous charger une partie ?\n")
		if chargerDemande == "a" or chargerDemande == "A" or chargerDemande == "":
			charger()
		if chargerDemande == "r" or chargerDemande == "R":
			initialisation()
			print("\nTrès bien, la partie va commencer !\nBonne chance !\n    Voilà les touches pour jouer :", touches)
			time.sleep(attente)
			print("\n" * 20)
			return
		else:
			print(erreur)
			charger()
	return

def enregistrer():  # sauvegarder la progression dans un fichier de sauvegarde

	global abscisse, ordonnee, tour, taillePetite, matrice, vie, inventaire
	fichierEcriture = input("Comment voulez vous appeler votre SAUVEGARDE ?\n")
	if fichierEcriture == "":
		fichierEcriture = "sauvegarde"
	try:
		open(fichierEcriture, "r")
		print("\nUne sauvegarde existe déja sous ce nom !")
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
		sauvegardeEcriture.write(str(abscisse) + "," + str(ordonnee) + "," + str(tour) + "," + str(taillePetite) + "," + str(difficulte) + ",")
		listeMatrice = []
		for i in range(tailleMatrice):
			listeMatrice.append(matrice[i])
			sauvegardeEcriture.write(str(listeMatrice[i]) + ",")
		sauvegardeEcriture.write(str(vie) + "," + str(inventaire))
		sauvegardeEcriture.close()
		print("\nLa progression a bien été enregistrée dans la sauvegarde : \n'" + fichierEcriture + "'", sep="")

def annuler(cause):  # annule l'action qui s'est produite

	global vie, vieAvantEffets
	vie = vieAvantEffets
	if cause == "mur":
		print(erreurMur)
	elif cause == "erreur":
		print(erreur + touches)
	effets(abscisse, ordonnee, False)
	salleCarte(abscisse, ordonnee)
	jeu(abscisse, ordonnee, tour)
	return

def jeu(x, y, t):  # effectue l'action demandée par le joueur

	global abscisse, ordonnee, tour, vie, vieAvantEffets
	touche = input("\nDans quelle DIRECTION voulez-vous aller ?\n")
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
	elif touche == "t" or touche == "T":
		print(touche)
	else:
		annuler("erreur")
		return
	abscisse = x
	ordonnee = y
	tour = t
	vieAvantEffets = vie

def etat():

	global vie
	dixiemeDeVie = int(vie / 10)
	if 50 < vie:  # vert, bonne santé
		print("■" * dixiemeDeVie, "□" * (10 - dixiemeDeVie), " ", vie, " points de vie.", sep="")
	elif 25 < vie < 51:  # jaune santé moyenne
		print("■" * dixiemeDeVie, "□" * (10 - dixiemeDeVie), " ", vie, " points de vie.", sep="")
	elif vie < 26:  # rouge, santé critique
		print("■" * dixiemeDeVie, "□" * (10 - dixiemeDeVie), " ", vie, " points de vie.", sep="")
	if inventaire[0] == 1:
		print("Vous avez une épée !")
	else:
		print("Vous n'avez pas d'épée.")
	if inventaire[1] == 1:
		print("Vous avez un bouclier !\n")
	else:
		print("Vous n'avez pas de bouclier.\n")

def effets(x, y, impact: bool):  # effets de la salle sur le joueur

	global tailleMatrice, vie, vieAvantEffets, difficulte, caracteristiqueAvantEffets
	if impact:
		vieAvantEffets = vie
	caracteristique = matrice[taillePetite - y][taillePetite + x]
	if impact:
		caracteristiqueAvantEffets = caracteristique
	if caracteristique == 0:  # vide
		print(salleVide)
	elif 0 < caracteristique < 5:  # dragon
		print(salleDragon)
		if inventaire[1] == 1:
			if impact:
				vie -= numpy.random.randint(0, (difficulte - 10))
			print("Grâce au bouclier, vous avez perdu moins de points de vie.\n")
		else:
			if impact:
				vie -= numpy.random.randint(10, difficulte)
		print("Vous avez PERDU des points de vie !\n")
		if vie < 1:
			mort()
		if inventaire[0] == 1:
			print("Vous avez VAINCU le dragon \n")
			if impact:
				matrice[taillePetite - y][taillePetite + x] = 0
	elif 4 < caracteristique < 7:  # nourriture
		print(salleNourriture)
		if vie > 79:
			print("Vous avez assez de points de vie, vous ne prenez PAS la nourriture.\n")
			etat()
			return
		if impact:
			vie += numpy.random.randint(10, 31)
		if vie > 100:
			vie = 100
		print("Vous avez GAGNE des points de vie !\n")
		matrice[taillePetite - y][taillePetite + x] = 0
	elif caracteristique == 7:  # épée
		inventaire[0] = 1
		print(salleEpee)
		if impact:
			matrice[taillePetite - y][taillePetite + x] = 0
	elif caracteristique == 8:  # bouclier
		inventaire[1] = 1
		print(salleBouclier)
		if impact:
			matrice[taillePetite - y][taillePetite + x] = 0
	elif caracteristique == 9:  # roi des dragons
		print(salleRoidesdragons)
		if inventaire[1] == 1:
			if impact:
				vie -= numpy.random.randint(difficulte - 20, difficulte)
		else:
			if impact:
				vie -= numpy.random.randint(difficulte - 10, difficulte + 10)
		if vie < 1:
			mort()
		else:
			if inventaire[0] == 1:
				if inventaire[1] == 1:
					partieGagnee()
				else:
					print("Vous devez avoir un BOUCLIER pour combattre le Roi des Dragons !\n")
			elif inventaire[1] == 0:
				print("Vous devez avoir une EPEE et un BOUCLIER pour combattre le Roi des Dragons !\n")
			else:
				print("Vous devez avoir une EPEE pour combattre le Roi des Dragons !\n")
	etat()

def dessins(x, y):  # assemble la salle et la carte

	global carteLigne, murHaut, porteHaut, interieurHaut, porteGauche, porteDroite, porteDroiteGauche, interieurBas, porteBas, murBas, matrice, caracteristiqueAvantEffets
	carteLigne = ["   " + "͟͟͟" * tailleMatrice + "͟\n", "  /" + "   " * tailleMatrice + "/\\\n", " |" + "   " * int(((tailleMatrice - 3) / 2)) + "~ Carte ~" + "   " * int(((tailleMatrice - 3) / 2)) + "|‾‾\n"]
	for i in range(taillePetite - y):
		carteLigne.append(" |" + " □ " * (2 * taillePetite + 1) + "|\n")
	carteLigne.append(" |" + " □ " * (x + taillePetite) + " ■ " + " □ " * (taillePetite - x) + "|\n")
	for i in range(taillePetite + y):
		carteLigne.append(" |" + " □ " * (2 * taillePetite + 1) + "|\n")
	carteLigne.append(" |" + "   " * int(((tailleMatrice - 3) / 2)) + "tour n°" + str(tour) + " " * int(espace(tour)) + "   " * int(((tailleMatrice - 3) / 2)) + "|\n")
	carteLigne.append("͟|" + "͟͟͟" * (tailleMatrice - 1) + "͟  |\n")
	carteLigne.append("\\" + "   " * (tailleMatrice - 1) + "  \\/\n")
	carteLigne.append(" " + "‾‾‾" * tailleMatrice + "\n")
	for i in range(10 - tailleMatrice):
		carteLigne.append("\n")
	contenu = []
	if caracteristiqueAvantEffets == 0:  # vide
		contenu = ["                             ", "                             ", "                             ", "                             ", "                             "]
	elif 0 < caracteristiqueAvantEffets < 5 or caracteristiqueAvantEffets == 9:  # dragon et roi dragon
		contenu = ["             .               ", "        .>   )\\;`a__         ", "       (  ___)/ /-.' ~~      ", "        `( )_ )/             ", "         <_  <_              "]
	elif 4 < caracteristiqueAvantEffets < 9:  # nourriture, épée et bouclier
		contenu = ["        ___________          ", "       |\\__________|\\        ", "       ||          ||        ", "       \\‾‾‾‾‾‾‾‾‾‾‾\\|        ", "        ‾‾‾‾‾‾‾‾‾‾‾‾         "]
	murHaut = decalageGauche + "                                       " + decalageDroit + carteLigne[0] + decalageGauche + " |\\‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\\   " + decalageDroit + carteLigne[1] + decalageGauche + " | \\______________________________| \\  " + decalageDroit + carteLigne[2]
	porteHaut = decalageGauche + "                |\\ |\\                  " + decalageDroit + carteLigne[0] + decalageGauche + " |\\‾‾‾‾‾‾‾‾‾‾‾‾‾\\ \\ \\‾‾‾‾‾‾‾‾‾‾‾‾‾|\\   " + decalageDroit + carteLigne[1] + decalageGauche + " | \\____________ \\|  \\____________| \\  " + decalageDroit + carteLigne[2]
	interieurHaut = decalageGauche + " |  |                             |  | " + decalageDroit + carteLigne[3] + decalageGauche + " |  |                             |  | " + decalageDroit + carteLigne[4]
	porteGauche = decalageGauche + "_|  |" + contenu[0] + "|  | " + decalageDroit + carteLigne[5] + decalageGauche + "\\ \\ |" + contenu[1] + "|  | " + decalageDroit + carteLigne[6] + decalageGauche + " \\_\\|" + contenu[2] + "|  | " + decalageDroit + carteLigne[7] + decalageGauche + "__   " + contenu[3] + "|  | " + decalageDroit + carteLigne[8] + decalageGauche + "\\|\\  " + contenu[4] + "|  | " + decalageDroit + carteLigne[9] + decalageGauche + " | \\                              |  | " + decalageDroit + carteLigne[10]
	porteDroite = decalageGauche + " |  |" + contenu[0] + "| _| " + decalageDroit + carteLigne[5] + decalageGauche + " |  |" + contenu[1] + " \\ \\ " + decalageDroit + carteLigne[6] + decalageGauche + " |  |" + contenu[2] + "  \\_\\" + decalageDroit + carteLigne[7] + decalageGauche + " |  |" + contenu[3] + "  _  " + decalageDroit + carteLigne[8] + decalageGauche + " |  |" + contenu[4] + "|\\ \\ " + decalageDroit + carteLigne[9] + decalageGauche + " |  |                             | \\_\\" + decalageDroit + carteLigne[10]
	porteDroiteGauche = decalageGauche + "_|  |" + contenu[0] + "|__| " + decalageDroit + carteLigne[5] + decalageGauche + "\\ \\ |" + contenu[1] + " \\ \\ " + decalageDroit + carteLigne[6] + decalageGauche + " \\_\\|" + contenu[2] + "  \\_\\" + decalageDroit + carteLigne[7] + decalageGauche + "__   " + contenu[3] + " __  " + decalageDroit + carteLigne[8] + decalageGauche + "\\|\\  " + contenu[4] + "|\\ \\ " + decalageDroit + carteLigne[9] + decalageGauche + " | \\                              | \\_\\" + decalageDroit + carteLigne[10]
	interieurBas = decalageGauche + " |  |                             |  | " + decalageDroit + carteLigne[11] + decalageGauche + " |  |                             |  | " + decalageDroit + carteLigne[12] + decalageGauche + " |  |                             |  | " + decalageDroit + carteLigne[13]
	porteBas = decalageGauche + " \\‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\\ |\\‾‾‾‾‾‾‾‾‾‾‾‾‾‾\\ | " + decalageDroit + carteLigne[14] + decalageGauche + "  \\_____________\\ \\\\ \\______________\\| " + decalageDroit + carteLigne[15] + decalageGauche + "                 \\| \\|                 " + decalageDroit + carteLigne[16]
	murBas = decalageGauche + " \\‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\\ | " + decalageDroit + carteLigne[14] + decalageGauche + "  \\_________________________________\\| " + decalageDroit + carteLigne[15] + decalageGauche + "                                       " + decalageDroit + carteLigne[16]

def initialisation():

	global tailleMatrice, taillePetite, abscisse, ordonnee, tour, matrice, vie, inventaire, vieAvantEffets, difficulte, caracteristiqueAvantEffets
	difficulteSouhaitee = input("\nQuelle DIFFICULTE de jeu voulez-vous ?\n" + presentationDifficulte)
	if difficulteSouhaitee == "":
		difficulteSouhaitee = int(2)
	try:
		difficulteSouhaitee = int(difficulteSouhaitee)
		if difficulteSouhaitee < 1:
			print(erreurDeSaisieInitialisation)
			initialisation()
			return
		difficulte = int(15 * difficulteSouhaitee + 1)
	except ValueError:
		print(erreurDeSaisieInitialisation)
		initialisation()
		return
	tailleMatrice = input("\nQuelle TAILLE de carte voulez-vous ?\n" + presentationTaille)
	if tailleMatrice == "":
		tailleMatrice = int(5)
	try:
		tailleMatrice = int(tailleMatrice)
		taillePetite = int(round((tailleMatrice - 1) / 2))
		tailleMatrice = int(2 * taillePetite + 1)
	except ValueError:
		print(erreurDeSaisieInitialisation)
		initialisation()
		return
	abscisse = 0
	ordonnee = 0
	tour = 0
	matrice = numpy.random.randint(0, 7, (tailleMatrice, tailleMatrice))
	matrice[taillePetite][taillePetite] = 0  # la salle du milieu est vide
	affectationXEpee = taillePetite
	affectationYEpee = taillePetite
	affectationEpee = [affectationXEpee, affectationYEpee]
	while affectationEpee == [taillePetite, taillePetite]:
		affectationXEpee = numpy.random.randint(0, tailleMatrice)
		affectationYEpee = numpy.random.randint(0, tailleMatrice)
		affectationEpee = [affectationXEpee, affectationYEpee]
	matrice[affectationXEpee][affectationYEpee] = 7  # une seule salle avec une épéé
	affectationXBouclier = taillePetite
	affectationYBouclier = taillePetite
	affectationBouclier = [affectationXBouclier, affectationYBouclier]
	while affectationBouclier == [taillePetite, taillePetite] or affectationBouclier == affectationEpee:
		affectationXBouclier = numpy.random.randint(0, tailleMatrice)
		affectationYBouclier = numpy.random.randint(0, tailleMatrice)
		affectationBouclier = [affectationXBouclier, affectationYBouclier]
	matrice[affectationXBouclier][affectationYBouclier] = 8  # une seule salle avec un bouclier
	affectationXRoiDragon = taillePetite
	affectationYRoiDragon = taillePetite
	affectationRoiDragon = [affectationXRoiDragon, affectationYRoiDragon]
	while affectationRoiDragon == [taillePetite, taillePetite] or affectationRoiDragon == affectationEpee or affectationRoiDragon == affectationBouclier:
		affectationXRoiDragon = numpy.random.randint(0, tailleMatrice)
		affectationYRoiDragon = numpy.random.randint(0, tailleMatrice)
		affectationRoiDragon = [affectationXRoiDragon, affectationYRoiDragon]
	matrice[affectationXRoiDragon][affectationYRoiDragon] = 9  # une seule salle avec le roi dragon
	vie = 100
	vieAvantEffets = vie
	inventaire = [0, 0]
	caracteristiqueAvantEffets = 0
	dessins(abscisse, ordonnee)

def mort():  # mort du joueur, fin de partie

	print("† Vous êtes mort †\n")
	etat()
	salleCarte(abscisse, ordonnee)
	nouvellePartieDemande = input(nouvellePartieMessage)
	if nouvellePartieDemande == "a" or nouvellePartieDemande == "A" or nouvellePartieDemande == "":
		deroulement()
	elif nouvellePartieDemande == "r" or nouvellePartieDemande == "R":
		print(auRevoir)
		exit()
	else:
		print(erreur + touches)
		mort()

def salleCarte(x, y):  # affiche la salle, la carte et positionne le joueur

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
		print(" " * 49 + decalageDroit + carteLigne[i], end="")

# =================================================================================================================== #
# 	Déroulement du jeu
# =================================================================================================================== #

def deroulement():

	global vie, vieAvantEffets
	menu()
	while True:
		vieAvantEffets = vie
		effets(abscisse, ordonnee, True)
		vieAvantEffets = vie
		salleCarte(abscisse, ordonnee)
		jeu(abscisse, ordonnee, tour)

deroulement()

# =================================================================================================================== #
#                                                                                                                     #
#                                         Jeu programmé par Artus de Chavagnac                                        #
#                                                                                                                     #
#                                                    Info & Dragons                                                   #
#                                                                                                                     #
#                                                 Version n°2 "Légère"                                                #
#                                                                                                                     #
# =================================================================================================================== #