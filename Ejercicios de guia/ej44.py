import math
def max_min(a,b,c):
	"""Devuelve el maximo o minimo de un polinomio de 2do grado"""
	if a>0:
		m = "Maximo"
	elif a<0:
		m = "Minimo"
	vx = -b / 2 * a
	vy = a *(vx **2) + b*vx + c
	print ("Su {} es:".format(m), vx, vy)

def raices(a,b,c):
	"""Devuelve las raices de un polinomio de segundo grado"""
	raiz = b**2 - 4 * a * c
	raiz2 = math.sqrt(raiz)
	r1 = (- b + raiz2) / 2 * a
	r2 = (- b - raiz2) / 2 * a
	return r1, r2
def interseccion(m1,b1,m2,b2):
	"""Da la interseccion entre dos rectas"""
	if m1 != m2:
		return False
	x = (b2-b1) / (m1 - m2)
	y = m1* x + b1
	return (x,y)
