def losange(tailleSouhaitee):

	tailleDouble = tailleSouhaitee * 2 + 1
	for i in range(1, tailleDouble, 2):
		print(" " * int((tailleDouble - i) / 2), "*" * i, " " * (tailleDouble - i))
	for i in range(tailleDouble, 0, -2):
		print(" " * int((tailleDouble - i) / 2), "*" * i, " " * (tailleDouble - i))
