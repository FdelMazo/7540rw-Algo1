def tuplas_diccionario(lista_tuplas):
	dict = {}
	for i,j in lista_tuplas:
		if i in dict:
			dict[i].append(j)
		else:
			dict[i] = j.split(",")
	return dict
	
def contar_palabras(cadena):
	lista_palabras = cadena.split()
	dict = {}
	for i in lista_palabras:
		if i in dict:
			dict[i] += 1
		else:
			dict[i] = 1
	return dict
	
def contar_letras(cadena):
	lista_letras = list(cadena)
	dict = {}
	for i in lista_letras:
		if i in dict:
			dict[i] += 1
		else:
			dict[i] = 1
	return dict

def usar_agenda(agenda):
	while True:
		nombre = input("El numero de quien desea ver/agendar: ")
		if nombre == "*":
			return
		if nombre in agenda:
			print(agenda[nombre])
		else:
			agenda[nombre] = input("Ingrese num")