import csv
def logear(archivodatos,archivolog):
	with open(archivodatos,'r') as archivo:
		dict = {}
		logear = []
		reader = csv.reader(archivo, delimiter=",")
		for linea in reader:
			try:
				vendedor = linea[2]
				monto = linea[4]
				monto = float(monto)
				if vendedor in dict:
					dict[vendedor] += monto
				else:
					dict[vendedor] = monto
			except ValueError:
				logear.append("La linea {} tiene un error".format(linea))
	with open(archivolog, 'w') as archivo2:
		archivo2.writelines(logear)
	return dict
		
print(logear("notas.csv","log.txt"))