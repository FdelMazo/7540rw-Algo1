def suma_matrices(lista1, lista2):
	"""Recibe dos matrices en formas de lista de listas y suma lugar a lugar"""
	if len(lista1) != len(lista2):
		return False
	suma = []
	for f in range(len(lista1)):
		if len(lista1[f]) != len(lista2[f]):
			return False
		fila = []
		for c in range(len(lista1)):
			fila.append(lista1[f][c]+lista2[f][c])
		suma.append(fila)
	return suma
