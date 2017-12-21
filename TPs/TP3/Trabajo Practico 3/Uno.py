from random import choice
from Carta import Carta
from MazoDeCartas import MazoDeCartas
from JugadorHumano import JugadorHumano
from Pozo import Pozo
from Ciclo import Ciclo
from Maquina import Maquina
from CartaEspecial import CartaEspecial

NOMBRES = ['Ava','Alpha 5','Data','T-800','Wall-E','Hardcore Henry','Dolores','R2D2','Cyborg','Robocop','Deckard','Optimus Prime','TARS','HAL 9000','Samantha','Cyrax','Dalek','Gear Head']
COLORES = ['Rojo', 'Verde', 'Azul', 'Amarillo']
CARTAS_NUMERICAS = [1,2,3,4,5,6,7,8,9] 
CANT_CARTAS_ESPECIALES = 2
CANT_COMODINES = 4
CANT_CARTAS_PROPIAS = 2
CANT_REPARTIR = 7
CANT_MAQUINAS = 1,2,3

class Uno:
############### METODOS PRINCIPALES DEL JUEGO
	def __init__(self):
		self.mazo = self.crear_mazo()
		self.pozo = Pozo()
		self.ciclo = self.crear_ciclo()
		
	def inicializar(self):
		self.pozo.carta_inicial(self.mazo)
		self.repartir()
		
	def repartir(self):
		"""Recibe el mazo y el ciclo de juego.
		Agrega 7 cartas a cada jugador"""
		for num,jug in enumerate(self.ciclo):
			if num == len(self.ciclo):
				break
			for i in range(CANT_REPARTIR):
				jug.sacar_carta_del_mazo(self.mazo)

	def jugar(self):
		"""Dinámica del juego. Recorre el ciclo hasta que algun jugador gane"""
		iterador = iter(self.ciclo)
		while True:
			jugador = next(iterador)
			jugador.jugar(self.mazo,self.pozo,iterador)
			if jugador.gano():
				print("{} gano!".format(jugador), '\n')
				print('Perdedores;')
				perdedor = next(iterador)
				while perdedor != jugador:
					print(perdedor.ver_mano())
					perdedor = next(iterador)
				print()
				return
				
############## CREACIONES Y VARIOS		
	def crear_mazo(self):
		"""Crea el mazo de cartas, llama a la funcion que le agrega las cartas especiales y lo devuelve."""
		mazo = MazoDeCartas()
		for color in COLORES:
			mazo.agregar_carta(Carta(0,color,None))
			for i in range(2):
				for num in CARTAS_NUMERICAS:
					mazo.agregar_carta(Carta(num,color, None))
		self.crear_especiales(mazo)
		return mazo
		
	def crear_especiales(self, mazo):
		"""Recibe por parámetro el mazo y le
		añade las cartas especiales."""
		for color in COLORES:
			for i in range(CANT_CARTAS_ESPECIALES):
				mazo.agregar_carta(CartaEspecial(None, color, 'Saltear'))
				mazo.agregar_carta(CartaEspecial(None, color, 'Invertir Sentido'))
				mazo.agregar_carta(CartaEspecial(None, color, 'Sumar 2'))
		for i in range(CANT_COMODINES):
			mazo.agregar_carta(CartaEspecial(None, None, 'Comodin'))
			mazo.agregar_carta(CartaEspecial(None, None, 'Sumar 4'))
		for i in range(CANT_CARTAS_PROPIAS):
			mazo.agregar_carta(CartaEspecial(None,None,'Carta Blanca'))
			mazo.agregar_carta(CartaEspecial(None,None,'Guason'))

	def crear_ciclo(self):
		jugadorhumano = JugadorHumano(None)
		cant_jug = self.validar_cantidad_jugadores()
		inteligencia_artificial = self.crear_jugadores(cant_jug)
		ciclo = Ciclo(jugadorhumano)
		for maquina in inteligencia_artificial:
			ciclo.agregar_jugador(maquina)
		print("Jugadores en la mesa: {}".format(ciclo))
		return ciclo
		
	def crear_jugadores(self,num):
		"""Recibe el número de jugadores que eligió
		el usuario. Crea una lista con los nombres de
		estos jugadores y los devuelve."""
		AI = []
		usados = []
		for i in range(num):
			nombre = choice(NOMBRES)
			while nombre in usados:
				nombre = choice(NOMBRES)
			usados.append(nombre)
			AI.append(Maquina(nombre))
		return AI

	def validar_cantidad_jugadores(self):
		"""Pide la cantidad de jugadores, 
		valida que sea correcta 
		devuelve el número como entero."""
		numero = input('Contra cuantos? ')
		while not numero.isdigit() or int(numero) not in CANT_MAQUINAS:
				numero = input('Numero del 1 al 3: ')
		return int(numero)
				
