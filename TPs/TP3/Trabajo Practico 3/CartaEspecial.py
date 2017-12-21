from Carta import Carta
from copy import copy
from random import choice

COLORES = ['Rojo', 'Verde', 'Azul', 'Amarillo']
class CartaEspecial(Carta):
	def __init__(self, num, color, especial):
		"""Crea una carta; num tiene que ser un
		valor numérico y, junto color y especial strings."""
		self.num = num
		self.color = color
		self.especial = especial
		self.tipo = self.tipo()
		
	def __repr__(self):
		"""Representación formal de una cadena de texto."""
		if self.tipo == "Comodin" or self.tipo == "Propia":
			if self.color:
				return "'{}, {}'".format(self.especial, self.color)
			return "'{}'".format(self.especial)
		elif self.tipo == "Especial":
			return "'{}, {}'".format(self.especial, self.color)
		return "'{} {}'".format(self.num, self.color)
		
	def tipo(self):
		"""Determina el tipo de una Carta considerando sus atributos"""
		if self.especial:
			if not self.color:
				if self.especial == "Guason" or self.especial == "Carta Blanca":
					return "Propia"
				return "Comodin"
			return "Especial"
			
	def pedir_color(self, booleano):
		"""Pide el color del comodín al usuario."""
		if booleano:
			color = input("{}: ".format('/'.join(COLORES))).capitalize()
			while not color in COLORES:
				color = input("{}: ".format('/'.join(COLORES))).capitalize()
			self.color = color
		else:
			self.color = choice(COLORES)
			
	def aplicar_especialidad(self, jugador, mazo, iterador, pozo):
		"""Aplica la especialidad de la carta."""
		if self.tipo == "Propia":
			if self.especial == 'Carta Blanca':
				print("{} ha tirado la carta mas zonza y trivial de todo el juego, una simple carta blanca!".format(jugador))
			elif self.especial == 'Guason':
				for i in range(2):
					jugador.sacar_carta_del_mazo(mazo,pozo)
				print("Oh no! El diabolico Guason forza a {} a sacar dos cartas del mazo!".format(jugador))
		elif self.especial == 'Saltear':
			iterador = next(iterador)
			print('{} hizo que {} se saltee un turno!'.format(jugador,iterador))
		elif self.especial == 'Invertir Sentido':
			iterador.invertirsentido()
			print('{} ha invertido el sentido!'.format(jugador))
		elif 'Sumar' in self.especial:
			copia_iterador = copy(iterador)
			acum = 1
			num = int(self.especial.split()[-1])
			lista_nombres = []
			jug_sig = next(copia_iterador)
			bool, cartaencadenada = jug_sig.jugar_encadenacion()
			while bool:
				lista_nombres.append(str(jug_sig))
				acum +=1
				num += int(cartaencadenada.especial.split()[-1])
				print("{} encadeno su propia {}".format(jug_sig,cartaencadenada))
				jug_sig.mano.remove(cartaencadenada)
				jug_sig = next(copia_iterador)
				bool, cartaencadenada = jug_sig.jugar_encadenacion()
			for i in range(acum):
				jugadorencad = next(iterador)
			for i in range(num):
				jugadorencad.sacar_carta_del_mazo(mazo,pozo)			
			if lista_nombres == []:
				print("{} hizo que {} saque {} cartas y pierda su turno!".format(jugador,jugadorencad,num))
			else:
				print("Cuantas encadenaciones!! Finalmente, {} saco {} cartas y se quedo sin turno!!!".format(jugadorencad, num))
		