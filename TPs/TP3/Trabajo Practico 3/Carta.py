from copy import copy
from random import choice
COLORES = ['Rojo', 'Verde', 'Azul', 'Amarillo']

class Carta:
	"""Modelo de representación de una carta"""
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
		if self.num == 0 or self.num:
			return "Numerica"
		elif self.especial:
			if not self.color:
				if self.especial == "Guason" or self.especial == "Carta Blanca":
					return "Propia"
				return "Comodin"
			return "Especial"
	
	def encaja(self, otro):
		"""Método encajar, recibe las dos cartas
		Devuelve True si encajan. De lo contrario False"""
		if self.tipo == "Propia":
			return True
		elif self.tipo == "Comodin":
			if otro.tipo == "Comodin" and self.color != otro.color:
				return False
			return True
		elif self.tipo == "Numerica":
			if self.num == otro.num:
				return True
		elif self.tipo == "Especial":
			if otro.especial and 'Sumar' in self.especial and 'Sumar' in otro.especial:
				return True
			elif self.especial == otro.especial:
				return True
		if self.color == otro.color:
			return True	
		if otro.tipo == "Propia":
			return True
			


