import math

def pointFixe(fonction, x_initial, erreurMinimale, iterationMaximale):

	iterationActuelle = 0
	x_instantApres = fonction(x_initial)
	erreurInstantApres = abs(x_instantApres - x_initial)
	print("Iteration n°", iterationActuelle, ", x = ", x_instantApres, ", erreur = ", erreurInstantApres, sep = "")
	x_initial = x_instantApres
	while erreurInstantApres >= erreurMinimale and iterationActuelle < iterationMaximale:
		iterationActuelle += 1
		x_instantApres = fonction(x_initial)
		erreurInstantApres = abs(x_instantApres - x_initial)
		print("Iteration n°", iterationActuelle, ", x = ", x_instantApres, ", erreur = ", erreurInstantApres, sep = "")
		x_initial = x_instantApres

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
