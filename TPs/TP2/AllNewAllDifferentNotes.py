import csv

OPCIONES = '12345678'

############MAIN, MENU PRINCIPAL Y FUNCIONES AUXILIARES##########

def main():
	"""Funcion principal del programa"""
	saludo()
	menu()
	
def saludo():
	"""Saluda al usuario imprimiendo una cadena"""
	print ("Hola! Bienvenido al Uncanny Notes")
	
def elegir_archivo():
	"""Pide al usuario el nombre del archivo
	Devuelve el nombre del archivo csv"""
	archivo = input("Qué archivo de notas quiere manejar? ").lower()
	while not archivo.isalpha():
		archivo = input("El archivo debe tener carácter alfabético: ").lower()
	archivo = "{}.csv".format(archivo)
	return archivo

def diccionario(archivo):
	"""Arma un diccionario del archivo
	Recibe el archivo CSV
	Devuelve diccionario de etiquetas: notas"""
	diccionario = {}
	try:
		with open(archivo, 'r') as file:
			lineas = file.readlines()
			for linea in lineas:
				etiqueta = linea.split("|")[0]
				palabras = linea.split("|")[1].rstrip("\n")
				if etiqueta == "":
						etiqueta = "Sin Etiqueta"
				if etiqueta in diccionario:
					diccionario[etiqueta].append(palabras)
				else:
					diccionario[etiqueta] = palabras.split()
	except:
		return diccionario	
	return diccionario
	
def menu():
	"""Menú principal del programa"""
	archivo = elegir_archivo()
	while True:
		archivo_dict = diccionario(archivo)
		print ("1 --> Agregar Notas\n2 --> Ver Notas\n3 --> Buscar en Notas\n"
		"4 --> Eliminar Notas\n5 --> Generar archivo HTML\n6 --> Cambiar de archivo\n7 --> Salir") #8 --> Debug
		seleccion = input("Ingrese su opcion: ")
		while not seleccion in OPCIONES:
			seleccion = input("Ingrese de nuevo (numero entre 1 y 7): ")
		print()
		if seleccion == "1":
			seguir = "SI"
			while seguir == "SI":
				nota_agregar = elegir_que_agregar()
				agregar_notas(nota_agregar, archivo)
				seguir = input("Seguir agregando? ").upper()
		elif seleccion == "2":
			imprimir_notas(archivo, archivo_dict)
		elif seleccion == "3":
			buscar_notas(archivo, archivo_dict)
		elif seleccion == "4":
			nota_eliminar, etiqueta = elegir_que_eliminar(archivo, archivo_dict)
			eliminar_notas(nota_eliminar, etiqueta, archivo)
		elif seleccion == "5":
			HTML = generar_html(archivo, archivo_dict)
			crear_archivo_html(HTML, archivo)
		elif seleccion == "6":
			archivo = elegir_archivo()
		elif seleccion == "7":
			break
		elif seleccion == "8":
			print(diccionario(archivo))
			imprimir_DEBUG(archivo)

def archivo_valido(archivo, archivo_dict):
	"""Confirma que el archivo exista y tenga notas escritas
	Recibe el archivo CSV
	Devuelve booleano"""
	if archivo_dict != {}:
		return True
	print("El archivo no existe o está vacío")
	return False

def imprimir_DEBUG(archivo):
	"""FUNCION PARA EL PROGRAMADOR"""
	if not archivo_valido(archivo):
		return	
	with open(archivo, 'r') as file:
		for linea in file:
			linea = linea.rstrip("\n")
			print (linea)
	
############FUNCIONES DEL PROGRAMA############

def elegir_que_agregar():
	"""Le pregunta al usuario que notas quiere agregar
	Recibe el archivo
	Devuelve la linea a agregar por la funcion agregar_notas"""
	palabras = input("Ingrese la nota: ")
	while palabras == "" or "|" in palabras:
		print("La nota no puede ni contener el caracter '|' ni estar vacia")
		palabras = input ("Ingrese la nota: ")
	etiqueta = input("Ingrese una etiqueta para las notas: ")
	while len(etiqueta.split()) > 1:
		print("La etiqueta debe ser de una sola palabra")
		etiqueta = input("Ingrese la etiqueta: ") 
	etiqueta = etiqueta.strip().capitalize()
	nota_agregar = [etiqueta, palabras.rstrip("\n")]
	return nota_agregar

def agregar_notas(nota, archivo):
	"""Agrega notas al archivo
	Recibe el archivo CSV y la nota a agregar de la funcion elegir_agregar
	Modifica el archivo CSV agregando la linea de etiqueta, nota"""
	with open(archivo,'a',newline='') as file:
		file_csv = csv.writer(file, delimiter="|")
		file_csv.writerow(nota)
	print("Listo!")
	
def imprimir_notas(archivo, archivo_dict):
	"""Imprime las notas de manera amigable para el usuario
	Recibe el archivo CSV
	Imprime cadenas"""
	if not archivo_valido(archivo, archivo_dict):
		return	
	for etiqueta, lista_de_palabras in archivo_dict.items():
		print("[{}]".format(etiqueta))
		for palabras in lista_de_palabras:
			print("- {}".format(palabras))
		print()
		
def buscar_notas(archivo, archivo_dict):
	"""Busca un texto que da el usuario en el archivo
	Recibe el archivo CSV y pide una cadena de texto
	Imprime las notas que contengan el texto"""
	if not archivo_valido(archivo, archivo_dict):
		return
	texto = input("Que desea buscar? ")
	for etiqueta, lista_de_palabras in archivo_dict.items():
		if texto.upper() in "".join(lista_de_palabras).upper():
			print("[{}]".format(etiqueta))
		else:
			print("No hay notas con ese término")
		for palabras in lista_de_palabras:
			if texto.upper() in palabras.upper():
				print("- {}".format(palabras))

def elegir_que_eliminar(archivo, archivo_dict):
	"""Le pregunta al usuario que nota desea eliminar
	Recibe el archivo CSV y confirma con el usuario que nota eliminar
	Devuelve una tupla de la seleccion del usuario (nota, etiqueta)"""
	if not archivo_valido(archivo, archivo_dict):
		return
	for etiquetadict in archivo_dict.keys():
		print("[{}]".format(etiquetadict))
	etiqueta = input("Ingrese la etiqueta que desea ver: ").capitalize()
	if etiqueta == "" or etiqueta == "Sin etiqueta":
		etiqueta = "Sin Etiqueta"
	while etiqueta not in archivo_dict:
		print("Esa etiqueta no se encuentra en el archivo")
		etiqueta = input("Intente de nuevo: ").capitalize()
	lista_de_palabras = archivo_dict[etiqueta]
	print("[{}]".format(etiqueta))
	for palabra,i in zip(lista_de_palabras, range(1, len(lista_de_palabras)+1)):
			print("{}.".format(i), format(palabra))
	seleccion = input("Que nota desea eliminar? ")
	while not seleccion.isdigit() or int(seleccion) not in range(1, len(lista_de_palabras)+1):
		seleccion = input("Ingrese una nota valida: ")
	if etiqueta == "Sin Etiqueta":
		etiqueta = ""
	nota_eliminar = lista_de_palabras[int(seleccion)-1]
	return nota_eliminar, etiqueta
	
def eliminar_notas(nota, etiqueta, archivo):	
	"""Elimina la nota del archivo
	Recibe la nota, la etiqueta y el archivo CSV
	Modifica el archivo CSV eliminando la linea deseada"""
	seguir = input("Esta por eliminar '{}' de '{}', seguir? (Si/No): ".format(nota, etiqueta)).upper()
	if not seguir == "SI":
		return
	linea_eliminar = "{}|{}\n".format(etiqueta,nota)
	with open(archivo,'r') as file:
		lineas = file.readlines()
		for linea,i in zip(lineas, range(len(lineas))):
			if linea == linea_eliminar:
				lineas.pop(i)
				lineas_nuevas = lineas
	with open(archivo, 'w') as file:
		file.writelines(lineas_nuevas)
			
def generar_html(archivo, archivo_dict):
	"""Genera un archivo HTML basandose en el CSV
	Recibe el archivo CSV
	Crea (no devuelve) el archivo HTML correspondiente"""
	if not archivo_valido(archivo, archivo_dict):
		return
	HTML = ['<!DOCTYPE html>','<html><head>','</head><body>','</body></html>']
	titulo = archivo.replace('.csv','').capitalize()
	HTML.insert(3, '<title>Listado</title><h1>{}</h1>'.format(titulo))
	for etiqueta in archivo_dict.keys():
		HTML.insert(4, "<h3>{}</h3>".format(str(etiqueta.capitalize())))
		for lista_de_palabras in archivo_dict.values():
			for palabras in lista_de_palabras:
				if palabras in archivo_dict[etiqueta]:
					HTML.insert(5,"<li>{}</li>".format(str(palabras).capitalize()))
	return HTML
	
def crear_archivo_html(HTML, archivo):	
	archivo_html = archivo.replace(".csv",".html")
	with open(archivo_html, 'w') as nota:
		nota.writelines(HTML)
	print("Listo!")	

main()
