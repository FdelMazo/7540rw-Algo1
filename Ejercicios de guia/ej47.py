def validar(n):
	"""Chequea que el numero no sea mayor a 5000, no sea negativo y que sea un entero. Despues, le agrega digitos 0 hasta llegar a 4 digitos"""
	if int(n)<= 4999 and int(n)>=0:
		r = list(map(int, str(n)))
		while len(r) <4:
			r.insert(0,0)
		return r
	return false

def romanos(n):
	"""Pasa enteros a romanos"""
	r = validar(n)
	romano = [""]
	while r[-1]<=9:
		if r[-1] == 9:
			r[-1]==0
			romano.append("IX")
			break
		if r[-1] > 5:
			romano.append("I")
			r[-1]-=1
		elif r[-1] == 5:
			romano.insert(0,"V")
			r[-1]==0
			break
		elif r[-1]<=5:
			for x in range(r[-1]):
				romano.append("I")
			break
	romano.remove("")
	while r[-2]<=9:
		if r[-2] == 9:
			r[-2]==0
			romano.insert(0, "XC")
			break
		if r[-2] > 5:
			romano.insert(0, "X")
			r[-2]-=1
		elif r[-2] == 5:
			romano.insert(0,"L")
			r[-2]==0
			break
		elif r[-2]<=5:
			for x in range(r[-2]):
				romano.insert(0, "X")
			break
	while r[-3]<=9:
		if r[-3] == 9:
			r[-3]==0
			romano.insert(0, "CM")
			break
		if r[-3] > 5:
			romano.insert(0, "C")
			r[-3]-=1
		elif r[-3] == 5:
			romano.insert(0,"D")
			r[-3]==0
			break
		elif r[-3]<=5:
			for x in range(r[-3]):
				romano.insert(0, "C")
			break
	for y in range(r[-4]):
		romano.insert(0,"M")
	a = ""
	for x in romano:
		a += str(x) 
	return a