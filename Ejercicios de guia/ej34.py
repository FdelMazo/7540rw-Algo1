import math
def calcular_norma(x,y):
	"""Calcula la norma de un punto"""
	return math.sqrt(x**2+y**2)

def restar_puntos(punto1,punto2):
	"""Resta dos puntos"""
	x1 = punto1[0]
	y1 = punto1[1]
	x2 = punto2[0]
	y2 = punto2[1]
	return x2-x1, y2-y1

def distancia(punto1, punto2):
        """Calcula la distancia entre dos puntos"""
		x,y = restar_puntos(punto1,punto2)
        return calcular_norma(x,y)

def pedir_punto():
        """Pide un punto en el plano xy a un usuario"""
		punto = input("Dar un punto en el plano xy separados por una coma: ")
        punto = punto.split(", ")
        x = int(punto[0])
        y = int(punto[1])
        return x, y

def semiperimetro(a,b,c):
        """Calcula el semiperimetro de un triangulo de 3 lados"""
		p = a + b + c
        return p/2

def area(a,b,c,p):
        """Calcula el area de un triangulo"""
		raiz = p*(p-a)*(p-b)*(p-c)
        return math.sqrt(raiz)

def main():
        """Funcion principal para calcular el area de un triangulo"""
		punto1 = pedir_punto()
        punto2 = pedir_punto()
        punto3 = pedir_punto()
        lado1 = distancia(punto1, punto2)
        lado2 = distancia(punto2, punto3)
        lado3 = distancia(punto1, punto3)      
        semiperimetro1 = semiperimetro(lado1,lado2,lado3)
        area1 = area(lado1,lado2,lado3,semiperimetro1)
        print ("El area es {} ".format(area1))
main()
        
