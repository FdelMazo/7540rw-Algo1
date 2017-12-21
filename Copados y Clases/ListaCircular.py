class _Nodo:
	def __init__(self, dato=None, prox=None):
		self.dato = dato
		self.prox = prox
		
	def __str__(self):
		return str(self.dato)

class ListaCircular:
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
	
	def append(self, dato):
		n_nuevo = _Nodo(dato)
		nodo = self.prim
		if nodo == None:
			self.prim = n_nuevo
		else:
			while nodo.prox != None:
				nodo = nodo.prox
			nodo.prox = n_nuevo
		n_nuevo.prox = self.prim
		self.len+=1
		
	def insert(self, dato, pos):
		if pos == self.len:
			self.append(dato)
		elif pos == 0:
			nodo = self.prim
			n_nuevo = _Nodo(dato, nodo)
			self.prim = n_nuevo
			self.len+=1	
		else:
			nodo = self.prim
			for i in range(pos-1):
				nodo = nodo.prox
			n_sig = nodo.prox
			nodo.prox = _Nodo(dato,n_sig)
			self.len+=1
		
	def pop(self,pos):
		nodo = self.prim
		for i in range(pos-1):
			nodo = nodo.prox
		dato = nodo.prox.dato
		if pos == self.len:
			nodo.prox = self.prim
		else:
			n_cont = nodo.prox.prox
			nodo.prox = n_cont
		self.len-=1
		return dato

	def remove(self,dato):
		nodo = self.prim
		if nodo.dato == dato:
			self.prim = nodo_prox
		else:
			contador = 0
			while nodo.prox.valor != dato and contador <= self.len:
				nodo = nodo.prox
				contador +=1
				if contador == self.len:
					raise ValueError
				n_cont = nodo.prox.prox
				nodo.prox = n_cont
		self.len-=1
