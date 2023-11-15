# =================================================================================================================== #
#                                                                                                                     #
#                                                 Graphique Fibonacci                                                 #
#                                                                                                                     #
# =================================================================================================================== #

import Fibonacci

tailleSouhaitee = 20

demiTaille = int(tailleSouhaitee / 2 + 1)
FibonacciComplet = Fibonacci.suite(demiTaille, False) + Fibonacci.suite(demiTaille, True)
del FibonacciComplet[demiTaille] # on doit supprimer un "0" de trop

Fibonacci.graphique(FibonacciComplet)

# =================================================================================================================== #
#                                                                                                                     #
#                                                 Graphique Fibonacci                                                 #
#                                                                                                                     #
# =================================================================================================================== #