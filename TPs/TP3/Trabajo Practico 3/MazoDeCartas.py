from random import randrange

class MazoDeCartas:
	"""Representación de un mazo de cartas, basado en una lista enlazada."""
	def __init__(self):
		self.cartas = []
	
	def agregar_carta(self,carta):
		"""Agrega Cartas al mazo."""
		self.cartas.append(carta)

	def sacar_carta(self, pozo=None):
		"""Recibe el pozo y saca una o más cartas
		 que se añaden a la mano del jugador"""
		if len(self.cartas) == 0:
			self.remezclar(pozo)
			return self.sacar_carta()
		i = randrange(len(self.cartas))
		return self.cartas.pop(i)
		
	def remezclar(self, pozo):
		"""Recibe el pozo y lo remezcla para
		convertirlo en el nuevo mazo."""
		carta = pozo.desapilar()
		while not pozo.esta_vacio():
			self.agregar_carta(pozo.desapilar())
		pozo.apilar(carta)
		print('El mazo fue mezclado. La primer carta sigue siendo {}'.format(carta))

