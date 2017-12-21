from Uno import Uno
MENU = ['1']#,2]

def main():
	seleccion = 'Seguir'
	while seleccion!= 'Salir':
		print("Que juego deseas jugar?")
		print("1 --> Uno")
		print("2 --> Chin Chon") #No Implementado
		accion = input("Ingrese un numero: ")
		while accion not in MENU:
			accion = input("Ingrese un numero: ")
		if accion == '1':
			JUEGO = Uno
		juego = JUEGO()
		juego.inicializar()
		print()
		juego.jugar()
		#juego.puntuar() #No Implementado
		print("Termino el juego!")
		seleccion = input('Seguir o salir? ')
		while not seleccion.capitalize() in ['Salir','Seguir']:
			seleccion = input("Escribir 'salir' o 'seguir': ")
	
main()