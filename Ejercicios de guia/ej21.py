def interes():
	"""Pide un capital C, una tasa de interes T y un cantidad de años Y y devuelve el monto final"""
	c = int(input("Especifique una cantidad de pesos "))
	t = int(input("A que tasa de interes? "))
	y = int(input("Cuantos años? "))
	n = (1+t/100)**y
	m = c * n
	return "El monto final es: " + m