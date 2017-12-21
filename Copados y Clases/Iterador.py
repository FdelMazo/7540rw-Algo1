class _IteradorListaEnlazada:
	def __init__(self, prim):
		self.actual = prim
		
	def __next__(self):
		if self.actual is None:
			raise StopIteration()
		dato = self.actual.dato
		self.actual = self.actual.prox
		return dato

class ListaEnlazada:
	#Continuacion
	def __iter__(self):
		"""Devuelve un iterador de la lista."""
		return _IteradorListaEnlazada(self.prim)

	def __next__(self):
		return next(iter(self))
	
