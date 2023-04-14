def Fibonacci(tailleSouhaitee, valeursPositives):

	if valeursPositives:
		FibonacciPositif = [0, 1]
		for i in range(2, tailleSouhaitee):
			FibonacciPositif.append(FibonacciPositif[i - 1] + FibonacciPositif[i - 2])
		return FibonacciPositif
	else:
		FibonacciNegatif = [1, 0]
		for i in range(2, tailleSouhaitee):
			FibonacciNegatif.insert(0, (FibonacciNegatif[1] - FibonacciNegatif[0]))
		return FibonacciNegatif
