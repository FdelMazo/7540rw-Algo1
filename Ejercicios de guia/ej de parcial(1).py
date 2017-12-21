import csv

def cambiar_campos(archivo, numero1, numero2):
	numero1 -=1
	numero2 -=1
	nuevas_lineas=[]
	with open(archivo) as file:
		reader = csv.reader(file, delimiter=",")
		for linea in reader:
			linea[numero1], linea[numero2] = linea[numero2], linea[numero1]
			nuevas_lineas.append(linea)
	with open("copia_"+archivo, 'w') as file2:
		writer = csv.writer(file2)
		writer.writerows(nuevas_lineas)

cambiar_campos("notas.csv",1,2)