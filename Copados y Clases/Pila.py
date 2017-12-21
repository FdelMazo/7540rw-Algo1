class Pila:
	"""Representa una pila con operaciones de apilar, desapilar y
	verificar si está vacía."""
	def __init__(self):
		"""Crea una pila vacía."""
		self.items = []

	def __str__(self):
		"""Va de abajo hasta el tope"""
		return str(self.items)

	def apilar(self, x):
		"""Apila el elemento x."""
		self.items.append(x)
		
	def desapilar(self):
		"""Devuelve el elemento tope y lo elimina de la pila.
		Si la pila está vacía levanta una excepción."""
		if self.esta_vacia():
			raise IndexError("La pila está vacía")
		return self.items.pop()
		
	def esta_vacia(self):
		"""Devuelve True si la lista está vacía, False si no."""
		return len(self.items) == 0

	def ver_primero(self):
		return self.items[-1]
