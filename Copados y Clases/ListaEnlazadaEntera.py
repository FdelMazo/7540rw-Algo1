class _Nodo:
	def __init__(self, dato=None, prox=None):
		self.dato = dato
		self.prox = prox
		
	def __str__(self):
		return str(self.dato)

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
	"""Modela una lista enlazada."""
	def __init__(self):
		"""Crea una lista enlazada vacía."""
		# referencia al primer nodo (None si la lista está vacía)
		self.prim = None
		# cantidad de elementos de la lista
		self.len = 0

	def __str__(self):
		cadena = ""
		n_act = self.prim
		while n_act:
			cadena += str(n_act.dato) + ","
			n_act = n_act.prox
		return "[{}]".format(cadena.rstrip(","))
		
	def __len__(self):
		return self.len
		
	def pop(self, i=None):
		"""Elimina el nodo de la posición i, y devuelve el dato contenido.
		Si i está fuera de rango, se levanta la excepción IndexError.
		Si no se recibe la posición, devuelve el último elemento."""
		if i is None:
			i = self.len - 1
		if i < 0 or i >= self.len:
			raise IndexError("Índice fuera de rango")
		if i == 0:
			# Caso particular: saltear la cabecera de la lista
			dato = self.prim.dato
			self.prim = self.prim.prox
		else:
			# Buscar los nodos en las posiciones (i-1) e (i)
			n_ant = self.prim
			n_act = n_ant.prox
			for pos in range(1, i):
				n_ant = n_act
				n_act = n_ant.prox
			# Guardar el dato y descartar el nodo
			dato = n_act.dato
			n_ant.prox = n_act.prox
		self.len -= 1
		return dato
			
	def downsample(self,k):
		if k<1:
			raise ValueError
		cont=1
		ant=self.prim
		act=ant.prox
		while act:
			if cont%k!=0:
				ant.prox=act.prox
			else:
				ant=act
			cont+=1
			act=act.prox	
		self.prim = self.prim.prox

	def remove(self, x):
		"""Borra la primera aparición del valor x en la lista.
		Si x no está en la lista, levanta ValueError"""
		if self.len == 0:
			raise ValueError("Lista vacía")
		if self.prim.dato == x:
			# Caso particular: saltear la cabecera de la lista
			self.prim = self.prim.prox
		else:
			# Buscar el nodo anterior al que contiene a x (n_ant)
			n_ant = self.prim
			n_act = n_ant.prox
			while n_act is not None and n_act.dato != x:
				n_ant = n_act
				n_act = n_ant.prox
			if n_act == None:
				raise ValueError("El valor no está en la lista.")
			# Descartar el nodo
			n_ant.prox = n_act.prox
		self.len -= 1
		
	def insert(self, i, x):
		"""Inserta el elemento x en la posición i.
		Si la posición es inválida, levanta IndexError"""
		if i < 0 or i > self.len:
			raise IndexError("Posición inválida")
		nuevo = _Nodo(x)
		if i == 0:
			# Caso particular: insertar al principio
			nuevo.prox = self.prim
			self.prim = nuevo
		else:
			# Buscar el nodo anterior a la posición deseada
			n_ant = self.prim
			for pos in range(1, i):
				n_ant = n_ant.prox
			# Intercalar el nuevo nodo
			nuevo.prox = n_ant.prox
			n_ant.prox = nuevo
		self.len += 1
	
	def append(self, x):
		self.insert(len(self),x)
	
	def index(self, x):
		for i, val in zip(range(len(self)),self):
			if val == x:
				return i
			else:
				raise ValueError("El valor no esta en la lista")
						

	def esta_vacia(self):
		return self.prim is None
	
	def extend(self, otro):
		if type(otro) is not ListaEnlazada:
			raise TypeError
		if otro.esta_vacia():
			return
		if not self.prim:
			self.prim = otro.prim
		elif not self.prim.prox:
			self.prim.prox = otro.prim
		else:
			n_ant = self.prim
			n_act = n_ant.prox
			for pos in range(1,len(self)-1):
				n_ant = n_act
				n_act = n_ant.prox
			n_act.prox = otro.prim
		self.len += otro.len
		
	def reverse(self):
		n_ant = None
		n_act = self.prim
		n_next = actual.prox
		while n_act:
			n_act.prox = n_ant
			n_ant = n_act
			n_act = n_next
			if n_next:
				n_next = n_next.prox
			self.prim = n_ant
	
	def __iter__(self):
		"""Devuelve un iterador de la lista."""
		return _IteradorListaEnlazada(self.prim)

	def __next__(self):
		return next(iter(self))
	