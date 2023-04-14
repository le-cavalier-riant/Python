def losange(tailleSouhaitee):

	n = tailleSouhaitee * 2 + 1
	for i in range(1, n, 2):
		print(" " * int((n - i) / 2), "*" * i, " " * (n - i))
	for i in range(n, 0, -2):
		print(" " * int((n - i) / 2), "*" * i, " " * (n - i))
