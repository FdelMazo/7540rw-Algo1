def domino():
	"""Imprime todas las fichas de domino"""
	a = 0
	b = 0
	for k in range (0,7):
		a = k
		for i in range (a, 7):
			b = i
			print (a, b)
