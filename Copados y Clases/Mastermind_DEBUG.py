#Sacar las lineas con DEBUG para que el juego funcione

import random
DIGITOS = 4
def mastermind():
	"""Funcion principal del juego Mastermind"""
	print("Bienvenido al Mastermind!")
	print("Instrucciones: Tenes que adivinar un codigo de {} digitos distintos. Tu cantidad de aciertos son los numeros que estan correctamente posicionados, tu cantidad de coincidencias son los numeros bien elegidos pero mal posicionados. Suerte!".format(DIGITOS))
	
	codigo = elegir_codigo()
	intentos = 1
	propuesta = input("Que codigo propones? (o pone 'Me retiro') ")
	retirarse = "Me retiro"
	while propuesta != codigo and propuesta != retirarse:
		intentos+=1
		aciertos, coincidencias = analizar_propuesta(propuesta, codigo)
		print ("Tu propuesta ({}) tiene {} aciertos y {} coincidencias.".format(propuesta,aciertos,coincidencias))
		propuesta = input("Propone otro codigo: ")
	if propuesta == retirarse:
		print ("El codigo era: {}".format(codigo))
	else:
		print ("Ganaste! Ganaste en {} intentos".format(intentos))

def elegir_codigo():
	"""Elige un codigo de DIGITOS digitos al azar"""
	digitos= ("0","1","2","3","4","5","6","7","8","9")
	codigo = ""
	for i in range(DIGITOS):	
		candidato = random.choice(digitos)
		print("[DEBUG] candidato:", candidato)
		while candidato in codigo:
			candidato = random.choice(digitos)
		codigo = codigo + candidato
		print("[DEBUG] el codigo va siendo", codigo)
	return codigo

def analizar_propuesta(propuesta, codigo):
		"""Determina aciertos y coincidencias"""
		aciertos = 0
		coincidencias = 0
		for i in range(DIGITOS):
			if propuesta[i] == codigo[i]:
				aciertos += 1
			elif propuesta[i] in codigo:
				coincidencias += 1
		return aciertos,coincidencias
mastermind()