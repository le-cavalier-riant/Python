import math

def pointFixe(fonction, valeurInitiale, erreurMinimale, iterationMaximale):

	n = 0
	valeur_n = valeurInitiale  # x à l'itération n
	valeur_nPlus1 = fonction(valeur_n)  # x à litération n + 1
	erreur_nplus1 = abs(valeur_nPlus1 - valeur_n)  # erreur a l'itération n + 1
	print("Iteration n°", n, ", x = ", valeur_nPlus1, ", erreur = ", erreur_nplus1, sep = "")
	valeur_n = valeur_nPlus1  # incrémentation

	while erreur_nplus1 >= erreurMinimale and n < iterationMaximale:

		n += 1
		valeur_nPlus1 = fonction(valeur_n)
		erreur_nplus1 = abs(valeur_nPlus1 - valeur_n)
		print("Iteration n°", n, ", x = ", valeur_nPlus1, ", erreur = ", erreur_nplus1, sep = "")
		valeur_n = valeur_nPlus1

# math.sin(x) - 2 * x + 1 = 0
	# x = (math.sin(x) + 1) / 2

# math.exp(x) - x = 10
	# x = math.exp(x) + 10
		# ne converge pas
	# x = math.log(x + 10)

# math.log(x**2 + 4) * math.exp(x) - 10 = 0
	# x = math.sqrt(math.exp(10 * math.exp(-x)) - 4)
		# ne converge pas
	# x = math.log(10) - math.log(math.log(x**2 + 4))

# x**4 + 3 * x = 9
	# x = 3 - (x**4) / 3
		# ne converge pas
	# x = math.pow(9 - 3 * x, 1/4)

def g(x):

	return math.pow(9 - 3 * x, 1/4) # x = 1.464917708946866, erreur = 2.9497071452055934e-11
	return math.log(10) - math.log(math.log(x**2 + 4))  # x = 1.656251724484239, erreur = 6.844658173577045e-11
	return math.log(x + 10)  # x = 2.5279632019813723, erreur = 9.247713705917704e-12
	return (math.sin(x) + 1) / 2  # x = 0.8878622115964132, erreur = 5.5417448407979464e-11

pointFixe(g, 0, 10**-10, 100)
