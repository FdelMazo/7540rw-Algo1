from CartaEspecial import CartaEspecial

class JugadorHumano:
	"""Modelo de representación de un jugador."""
	def __init__(self, nombre):
		"""Crea un jugador; nombre tiene que ser un string"""
		nombre = input("Como te llamas? ")
		while not nombre.isalpha():
			nombre = input("Como te llamas? ")
		self.nombre = nombre
		self.mano = []
		self.der = None
		self.izq = None
		
	def __repr__(self):
		"""Representacion formal"""
		return self.nombre
	
	def ver_mano(self):
		"""Ve el nombre y la mano del jugador. Devuelve cadena"""
		return "{}: {}".format(self,self.mano)
		
	def gano(self):
		"""Verifica que el jugador haya ganado o no la partida"""
		return len(self.mano)==0

	def sacar_carta_del_mazo(self, mazo, pozo=None):
		"""Saca una carta del mazo y la agrega a la mano"""
		carta = mazo.sacar_carta(pozo)
		self.mano.append(carta)


	def jugar(self, mazo, pozo,iterador):
		"""Método jugar; Recibe el self, el mazo,
		el pozo y el iterador.
		Pide la carta al usuario, la juega y continua."""
		print(pozo, '\n')
		carta_jugar = self.pedir_accion(pozo)
		self.jugar_carta(mazo,carta_jugar, pozo,iterador)

	def jugar_carta(self, mazo, carta, pozo, iterador):
		"""Método jugar carta; Recibe self, el mazo, la carta a jugar,
		el pozo, el mazo y el iterador. Juega la carta por el usuario:
		si la carta es None, roba del mazo y pregunta al usuario si desea jugarla.
		De lo contrario, la apila en el pozo."""
		if carta == None:
			sacada = mazo.sacar_carta(pozo)
			self.mano.append(sacada)
			print(sacada)
			if sacada.encaja(pozo.tope()):
				tirar = input('Tirar? (Si/No) ')
				if tirar.capitalize() in 'Si' and tirar.capitalize() != "":
					self.jugar_carta(mazo,sacada,pozo,iterador)
			else:
				print('{} saco una carta del mazo y termino su turno.'.format(self))
		else:
			if carta.tipo == "Comodin":
				carta.pedir_color(True)
			pozo.apilar(carta)
			self.mano.remove(carta)
			print('{} tiro la carta {}'.format(self, carta))
			if isinstance(carta,CartaEspecial):
				carta.aplicar_especialidad(self,mazo,iterador,pozo)

	def pedir_accion(self, pozo):
		"""Método pedir acción; recibe el mazo y
		pide al usuario la carta que va a jugar o
		si va a sacar del mazo. Si roba del mazo devuelve
		None, de lo contrario devuelve la carta a jugar."""
		print("Tu turno \nCartas en mano")
		for i, carta in enumerate(self.mano, 1):
			print(i,'- ', carta)
		print()
		print("Para sacar del mazo: 'Sacar'")
		accion = input('Qué carta vas a jugar? ')
		while True:
			if accion.capitalize() in 'Sacar':
				return None
			if accion.isdigit() and 1 <= int(accion) <= len(self.mano):
				carta = self.mano[int(accion) - 1]
				if carta.encaja(pozo.tope()):
					return carta
			print('No podes usar esa carta, elegi de nuevo')
			accion = input('Qué carta vas a jugar? ')					
				
	def jugar_encadenacion(self):
		"""Funcion llamada cuando un jugador tira una carta de sumar
		Si el jugador es el usuario le muestra sus cartas y le permite encadenar
		Si el jugador es una maquina se recorren sus cartas y si se puede se tira la primera que se encuentra"""
		bool, carta = False, None
		lista_encadenar = []
		for i, posible_carta in enumerate(self.mano,1):
			if posible_carta.especial != None and 'Sumar' in posible_carta.especial:
				lista_encadenar.append(i)
				print(i, "- ", posible_carta)
		if lista_encadenar == []:
			return bool, carta
		print()
		print("Para no tirar nada y ser el encadenado: '0'")
		accion = input('Qué carta queres encadenar? ')
		while True:
			if accion == '0' or accion == "":
				break
			elif accion.isdigit() and int(accion) in lista_encadenar:
				carta = self.mano[int(accion) - 1]
				bool = True
				break
			print('No podes usar esa carta, elegi de nuevo')
			accion = input('Qué carta vas a jugar? ')								
		if carta and carta.tipo == "Comodin":
			carta.pedir_color(True)
		return bool, carta
	
