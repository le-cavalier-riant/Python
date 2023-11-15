from matplotlib import pyplot
import math

def euler(x_minimum, x_maximum, nombreIntervalles, y_minimum, fonction):

	y_sortie = []
	x_sortie = []
	pas = (x_maximum - x_minimum) / nombreIntervalles
	y_sortie.append(y_minimum)
	x_sortie.append(x_minimum)
	y_instantApres = y_minimum + pas * fonction(x_minimum, y_minimum)
	x_instantApres = x_minimum + pas
	for i in range(nombreIntervalles - 1):
		y_instantApres = y_minimum + pas * fonction(x_minimum, y_minimum)
		x_instantApres = x_minimum + pas
		y_sortie.append(y_instantApres)
		x_sortie.append(x_instantApres)
		y_minimum = y_instantApres
		x_minimum = x_instantApres
	return x_sortie, y_sortie

def fonctionExacte(t):

	return (3 / 5) * math.exp(5 * t) - 3 / 5

def deriveeAprochee(t, valeur):

	return 5 * valeur + 3

N = 100

temps, y_euler = euler(0, 1, N, 0, deriveeAprochee)
y_exact = []
for j in range(len(temps)):
	y_exact.append(fonctionExacte(temps[j]))
pyplot.figure()
pyplot.plot(temps, y_euler, label = "Valeur approchée")
pyplot.plot(temps, y_exact, label = "Valeur exacte")
pyplot.plot()
pyplot.xlabel("t [0, 1]")
pyplot.ylabel("y(t)")
pyplot.title("N = " + str(N))
erreurs = []
for k in range(len(temps)):
	erreurs.append(abs(y_euler[k] - y_exact[k]))
pyplot.figure()
pyplot.plot(temps, erreurs)
pyplot.xlabel("t [0, 1]")
pyplot.ylabel("Erreur")
pyplot.title("Erreur N = " + str(N))
pyplot.show()
