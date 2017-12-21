class Pozo:
	"""Modelo de representación de un pozo de cartas, basado en una pila"""
	def __init__(self):
		"""Constructor"""
		self.items = []
		
	def __str__(self):
		"""Representación de una cadena de texto."""
		return	'Pozo: ' + str(self.tope())
	
	def carta_inicial(self, mazo):
		"""Recibe el mazo, y de manera random,
		elige una carta, que mientras no sea especial,
		la apila"""
		carta = mazo.sacar_carta()
		while carta.especial:
			mazo.agregar_carta(carta)
			carta = mazo.sacar_carta()
		self.apilar(carta)
		
	def apilar(self, x):
		"""Apila el elemento x."""
		self.items.append(x)
		
	def desapilar(self):
		"""Devuelve el elemento tope y lo elimina de la pila.
		Si la pila está vacía levanta una excepción."""
		if self.esta_vacio():
			raise IndexError("La pila está vacía")
		return self.items.pop()
		
	def tope(self):
		"""Devuelve el elemento en el tope de la pila"""
		return self.items[-1]
		
	def esta_vacio(self):
		"""Devuelve True si la lista está vacía, False si no."""
		return len(self.items) == 0
	
	