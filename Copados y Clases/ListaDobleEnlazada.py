class _Nodo:
	def __init__(self, dato=None, prox=None, ant=None):
		self.dato = dato
		self.prox = prox
		self.ant = ant
		
	def __str__(self):
		return str(self.dato)

class ListaDoblementeEnlazada:
	def __init__(self):
		self.prim = None
		self.len = 0
		
	def __str__(self):
		cadena = ""
		n_act = self.prim
		while n_act:
			cadena += str(n_act.dato) + ","
			n_act = n_act.prox
		return "[{}]".format(cadena.rstrip(","))

	def append(self,dato):
		if self.len == 0
			self.prim = _Nodo(dato)
		else:
			nodo = self.prim
			while nodo.prox != Nodo:
				nodo = nodo.prox
			n_ant = nodo
			nodo.prox = _Nodo(dato, None, n_ant)
		self.len += 1	
		
	def insert(self,dato,pos):
		if pos == self.len
			self.append(dato)
		else:
			nodo = nodo.prim
			for i in range(pos-1):
				nodo = nodo.prox
			n_ant = nodo
			n_prox = nodo.prox
			nuevo_nodo = _Nodo(dato, n_prox, n_ant)
			nodo.prox = nuevo_nodo
			n_prox.ant = nuevo_nodo
			self.len += 1
			
	def pop(self,pos):
		nodo = self.prim
		if pos == 0:
			dato = nodo.dato
			nodo_nuevo_1 = nodo.prox
			nodo_nuevo_1.ant = None
			self.prim = nodo_nuevo_1
		elif pos == self.len:
			while nodo.prox != None:
				nodo = nodo.prox
			dato = nodo.dato
			n_ant = nodo.ant
			n_ant.prox = None
		else:
			for i in range(pos-1):
				nodo = nodo.prox
			dato = nodo.prox.dato
			n_prox = nodo.prox.prox
			prox.ant = nodo
			nodo.prox = prox
		self.len -=1
		return dato
		
	def remove(self, dato_eliminar):
		nodo = self.prim
		if nodo.dato == dato_eliminar:
			n_seg = nodo.prox
			n_seg.ant = None
			self.prim = nodo_seg
		else:
			while nodo != None:
				if nodo.dato == dato_eliminar:
					n_ant = nodo.ant
					n_prox = nodo.prox
					n_prox.ant = n_ant
					n_ant.prox = n_prox
		self.len -=1
