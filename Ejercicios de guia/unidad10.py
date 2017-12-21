def imprimir_n_lineas(archivo, n):
	with open(archivo, 'r') as file:
		for i,linea in enumerate(file):
			print(i,linea)
			if i == n-1:
				break		

def copyfile(archivo):
	with open(archivo,'r') as file:
		lineas_a_escribir = file.readlines()
	archivo_nuevo = "copia_" + archivo
	with open(archivo_nuevo, 'w') as file2:
		file2.writelines(lineas_a_escribir)