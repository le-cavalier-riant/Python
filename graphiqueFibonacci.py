from matplotlib import pyplot
from Fibonacci import Fibonacci

tailleSouhaitee = 10
FibonacciComplet = Fibonacci(tailleSouhaitee, False) + Fibonacci(tailleSouhaitee, True)
del FibonacciComplet[tailleSouhaitee] # on doit supprimer un "0" de trop

pyplot.plot(FibonacciComplet)

pyplot.show()
