from luces_afuera_niveles import niveles
from time import sleep
from string import ascii_uppercase
from random import randrange
from sys import exit
from copy import deepcopy

########FUNCIONES META########

def saludo():
	"""Saluda al usuario y le da instrucciones cortas. Esta pensada para ser solo ejecutada una vez, al principio del programa
	Imprime cadenas de texto."""
	print ("Hola! Bienvenido al juego Luces Afuera.")
	print ("El objetivo es muy simple, apagar todas las luces.") 
	print ("Las luces prendidas son los puntos o y las apagadas los puntos ·")
	print ("Cuando presionás una luz, escribiendo su posicion, como por ejemplo D4 o A3, ésta se prende o apaga dependiendo de su estado inicial.")
	print ("Pero OJO! Cada vez que presionás una luz, sus vecinas tambien se presionarán.")
	print ("En todo momento podes escribir RESET y volver al tablero original, pero esto te hace perder puntos.")
	print ()

def menu():
	"""Menú principal del juego
	Le pide al usuario una cadena de texto
	Ejecuta la función correspondiente"""
	print ("1 --> Jugar: Modo Normal")
	print ("2 --> Jugar: Modo Random (Mas difícil)")
	print ("3 --> Instrucciones Enteras")
	print ("4 --> Salir")
	print ()
	seleccion = input("Ingrese su opción: ")
	while not seleccion.isdigit() or int(seleccion) not in [1,2,3,4]:
		seleccion = input("Ingrese de nuevo: ")
	if seleccion == "1":
		modonormal()
	elif seleccion == "2":
		modorandom()
	elif seleccion == "3":
		instrucciones()
	elif seleccion == "4":
		exit()
		
def modonormal():
	"""Juega los 5 niveles predeterminados, o hasta que pierda el usuario
	Imprime el puntaje y cuando termina de ejecutarse vuelve al menu"""
	copia_niveles = deepcopy(niveles)
	puntos_totales = 0
	for nivel in copia_niveles:
		ganar, puntos_del_nivel = juego(nivel)
		puntos_totales += puntos_del_nivel
		if not ganar:
			break
		if puntos_totales < 0:
			puntos_totales = 0
		print ("Tenes {} puntos".format(puntos_totales))
		print ("Siguiente nivel")
		sleep(1)
	print ("Termino el juego! Terminaste con {} puntos".format(puntos_totales))
			
def modorandom():
	"""Juega en una dimension elegida por el usuario 5 veces y despues juega hasta que el usuario no quiera mas
	Pide una dimensión para crear y randomizar el tablero y juega. Luego le pregunta al usuario si quiere seguir
	Imprime el puntaje y cuando termina de ejecutarse vuelve al menu"""
	dim = input("Elija la dimension del tablero (entre 5 y 10): ")
	puntos_totales = 0
	while not dim.isdigit() or int(dim) > 10 or int(dim) < 5 :
			dim = input("Ingrese de nuevo: ")
	dim = int(dim)
	for x in range(5):
		nivel = randomizar(crear_nivel_vacio(dim))
		ganar, puntos_del_nivel = juego(nivel)
		puntos_totales += puntos_del_nivel
		if not ganar:
			break
		if puntos_totales < 0:
			puntos_totales = 0
		print("Tenes {} puntos".format(puntos_totales))
		print ("Siguiente nivel")
		sleep(1)
	print ("Termino el juego! Terminaste con {} puntos".format(puntos_totales))
	
def instrucciones():
	"""Instrucciones enteras del juego
	Imprime cadenas de texto"""
	print ("Tenes dos modos de juegos, el normal y el random.")
	print ("En el modo normal vas a jugar en niveles ya preseleccionados.")
	print ("En el random vas a jugar niveles creados al azar por la computadora, te pueden tocar niveles muy faciles como niveles muy dificiles.")
	print ("En el modo normal vas a jugar en un tablero de 5x5, mientras que en el random vos elegís la dimensión del tablero.")
	print ()
	print ("El objetivo es apagar todas las luces antes de quedarte sin turnos.")
	print ("Las luces apagadas son los puntos · y las luces prendidas son los puntos o.")
	print ("En cada turno podes elegir la luz que queres presionar, por ejemplo, la D4.")
	print ("Cada vez que elijas la posicion de la luz que quieras prender o apagar")
	print ("la luz que tenga arriba, la que tenga abajo, la que tenga a la izquierda, y la que tenga a la derecha también van a prenderse o apagarse")
	print ("Siempre podes volver a las INSTRUCCIONES, simplemente escribiendolo. Tambien podes ver tu estado actual con TABLERO")
	print ("Escribiendo RESETEAR, podes, a cambio de muchos puntos resetear el nivel a su estado inicial")
	print ()	
	
def crear_nivel_vacio(dimension):
	"""Crea un nivel de todas luces apagadas
	Recibe una dimension entre 5 y 10
	Devuelve un nivel"""
	nivel_vacio = []
	for f in range(dimension):
		fila = []
		for c in range(dimension):
			fila.append(0)
		nivel_vacio.append(fila)
	return nivel_vacio
	 
def randomizar(nivel_vacio):
	"""Cambia luces al azar de un nivel vacio 
	Recibe un nivel de todas lucas apagadas de n*n entre 5 y 10
	Devuelve el mismo nivel, modificado"""
	n = len(nivel_vacio)
	luces_a_cambiar = randrange(2*n, (n*n)-n)
	for x in range(luces_a_cambiar):
			fila = randrange(len(nivel_vacio))
			columna = randrange(len(nivel_vacio))
			nivel_vacio[fila][columna] = 1
	return nivel_vacio
	
def juego_debug(nivel):
	"""Funcion DEBUG. No aplicada en ningun momento"""
	turno = 0
	imprimir_tablero_debug(nivel)
	while turno <15:
		pos = validar_input(input("Ingrese: "))
		for luz in luces_contiguas(pos):
			presionar(luz, nivel)
		turno +=1
		imprimir_tablero_debug(nivel)
		
def imprimir_tablero_debug(nivel):
	"""Funcion DEBUG. No aplicada en ningun momento"""
	print("   ", end=" ")
	for letra in range(len(nivel)):
		print (ascii_uppercase[letra], end=" ")
	print()
	print("   ", end=" ")
	for letra in range(len(nivel)):
		print (letra, end=" ")
	print()
	for fila, x in zip(nivel, range(0,10)): 
		print ("{:<2}|".format(x), end=" ")
		for numero in fila:
			if numero == 0:
				print ("·",end=" ")
			elif numero == 1:
				print ("o",end=" ")
		print ()

########FUNCIONES DEL JUEGO########

def imprimir_tablero(nivel):
	"""Imprime el nivel de manera mas amigable para el usuario
	Recibe un nivel (lista de listas)
	Imprime el tablero"""
	print("   ", end=" ")
	for letra in range(len(nivel)):
		print (ascii_uppercase[letra], end=" ")
	print ()
	for fila, x in zip(nivel, range(1,11)): 
		print ("{:<2}|".format(x), end=" ")
		for numero in fila:
			if numero == 0:
				print ("·",end=" ")
			elif numero == 1:
				print ("o",end=" ")
		print ()	
	print()

def lucesprendidas(nivel):
	"""Chequea las luces prendidas en un nivel. Para saber si gano o para saber cuantos puntos perdio cuando resetea el nivel
	Recibe un nivel (lista de listas)
	Devuelve la cantidad de luces prendidas en este"""
	prendidas = 0
	for fila in nivel:
		for numero in fila:
			if numero==1:
				prendidas += 1
	return prendidas

def validar_input(accion,nivel):
	"""Evalua que ingreso el usuario en la funcion del juego
	Recibe la cadena de texto que halla ingresado y el nivel en el que esta jugando
	Devuelve a la funcion juego un parametro o aplica la funcion correspondiente"""
	accion = accion.upper()
	if accion == "INST" or accion == "INSTRUCCIONES":
		instrucciones()
	elif accion == "MAPA" or accion == "TABLERO":
		imprimir_tablero(nivel)
	elif accion == "RESET" or accion == "RESETEAR":
		return "RESET"
	if not posicion_valida(accion, nivel):
		return validar_input(input("Ingrese de nuevo: "), nivel)
	else:
		return posicion_valida(accion, nivel)
			
def posicion_valida(accion,nivel):
	"""Modifica la posicion del usuario para que sea acorde al resto del programa
	Recibe la posicion ingresada por el usuario y el nivel que esta jugando
	Devuelve una lista"""
	accion = list(accion)
	if len(accion) == 3 and accion[1].isdigit() and accion[2].isdigit():
		numero = accion.pop(1) + accion.pop(1)
		accion = [accion[0], numero]
	elif len(accion) != 2 or not accion[1].isdigit():
		return False
	letra = ord(accion[0].upper()) - ord("@")
	num = int(accion[1])
	if letra in range(1, len(nivel)+1) and num in range(1,len(nivel)+1):
		return [letra-1, num-1]
		
def luces_contiguas(luz):
	"""Arma la lista de luces que forma la cruz de luces vecinas
	Recibe la luz que el usuario quiere prender/apagar
	Devuelve la lista de luces"""
	return [luz, [luz[0], luz[1]-1], [luz[0], luz[1]+1], [luz[0]-1, luz[1]], [luz[0]+1, luz[1]]] 
	
def presionar(luz, nivel):
	"""Prende o apaga una luz, dependiendo de su estado original
	Recibe la luz a tocar y el nivel en el que se esta jugando
	Modifica el nivel cambiando los estados de las luces"""
	c = luz[0]
	f = luz[1]
	if c > len(nivel)-1 or c < 0 or f > len(nivel)-1 or f < 0:
		return
	elif nivel[f][c] == 0:
		nivel[f][c] = 1
	elif nivel[f][c] == 1:
		nivel[f][c] = 0

########FUNCIONES PRINCIPALES: JUEGO Y MAIN########
		
def juego(nivel):
	"""Juega un nivel
	Recibe una lista de listas
	Devuelve un valor booleano indicando si gano o perdio, y un valor entero que es la cantidad de puntos obtenidos en el nivel
	Efectos secundarios, cambia el nivel constantemente"""
	nivel_original = deepcopy(nivel)
	turnos = 3 * len(nivel)
	puntos = 0
	while turnos > 0:
		print ()
		imprimir_tablero(nivel)
		print ("Te quedan {} turnos".format(turnos))
		print ()
		posicion = validar_input(input("Ingrese: "), nivel)	
		if posicion == "RESET":
			puntos = 50 * lucesprendidas(nivel)
			print ("Perdiste {} puntos.".format(puntos))
			turnos -= 1
			nivel = nivel_original
			continue
		for luz in luces_contiguas(posicion):
			presionar(luz, nivel)
		turnos -= 1
		if lucesprendidas(nivel) == 0:
			imprimir_tablero(nivel)
			print ("Ganaste! Ganaste 500 puntos.")
			return True, puntos + 500
	if turnos == 0:
		print ("Perdiste. Perdiste 300 puntos.")
		return False, puntos - 300

def main():
	"""Funcion principal del programa
	Ejecuta el saludo y luego el menu"""
	saludo()
	while True:
		menu()
		print()
		sleep(1)
	
main()
