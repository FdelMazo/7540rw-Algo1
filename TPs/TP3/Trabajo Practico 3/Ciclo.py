class _IteradorCiclo:
	"""Modelo de un iterador de una ronda de jugadores. Pensado como objeto privado del objeto Ciclo"""
	def __init__(self, prim, length):
		"""Constructor"""
		self.actual = prim
		self.sentidoderecha = True

	def __next__(self):
		"""Llama al siguiente iterable, dependiendo del sentido de la ronda"""
		jugador = self.actual
		if self.sentidoderecha == True:
			self.actual = self.actual.der
		else:
			self.actual = self.actual.izq
		return jugador		

	def invertirsentido(self):
		"""Cambia el sentido del iterador, y por ende, de la ronda"""
		if not self.sentidoderecha:
			self.sentidoderecha = True
		else:
			self.sentidoderecha = False
		next(self)
		next(self)
		
class Ciclo:
	"""Modelo de una ronda de jugadores"""
	def __init__(self,jugador1):
		"""Crea una ronda con el jugador que recibe como parametro como el primero y la ronda gira para la derecha"""
		self.prim = jugador1
		self.ult = jugador1
		self.invariacion()
		self.len = 1
		
	def __str__(self):
		"""Representacion 'informal'. Devuelve los nombres de los jugadores"""
		cadena = ''
		for num, jugador in enumerate(self):
			if num == len(self):
				break
			cadena += str(jugador) + ", "
		return "[{}]".format(cadena.rstrip(", "))
		
	def __len__(self):
		"""Devuelve el largo de la lista"""
		return self.len

	def __iter__(self):
		"""Devuelve un iterador de la lista."""
		return _IteradorCiclo(self.prim, len(self))		

	def invariacion(self):
		"""Invariacion del objeto circular. Modifica para que en todo momento el ultimo jugador tenga al primero a su derecha y el primero al ultimo a su izquierda"""
		self.prim.izq = self.ult
		self.ult.der = self.prim
							
	def agregar_jugador(self, jugador):
		"""Agrega un jugador a la derecha del ultimo"""
		jugador.izq = self.ult
		self.ult.der = jugador
		self.ult = jugador
		self.invariacion()
		self.len+=1