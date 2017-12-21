def juego(n):
	"""Imprime todas las fichas que pueda tener un juego simil al domino pero en vez de 6, n"""
	for k in range(0,7):
		for i in range(k, 7):
			print (k,i)
