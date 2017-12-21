#Polinomio([1,0,0,2,3]) --> 1x^4+2x+3

class Polinomio:
	def __init__(self,lista_mayoramenor):
		self.listadecoeficientes = lista_mayoramenor
		self.grado = len(lista_mayoramenor) - 1

	def __str__(self):
		cadena = ""
		for i, coef in zip(range(len(self.listadecoeficientes) -1,-1,-1), self.listadecoeficientes):
			if coef == 0:
				continue
			if coef == 1:
				coef = ""
			if "-" in str(coef):
				pass
			elif "-" not in str(coef) and not i == len(self.listadecoeficientes) - 1: 
				cadena += "+"
			cadena += "{}".format(coef)
			if i != 0:
				cadena += "x"
			if i == 1:
				continue
			if i != 0:
				cadena += "^{}".format(i)
			else:
				continue
		return cadena
	
	def __eq__(self,otro):
		return self.listadecoeficientes == otro.listadecoeficientes
			
	def derivar(self):
		lista_derivada = []
		nuevo = self.listadecoeficientes
		for i, coef in zip(reversed(range(len(nuevo))), self.listadecoeficientes):
			lista_derivada.append(i*coef)
		del lista_derivada[len(lista_derivada)-1]
		return Polinomio(lista_derivada)

a = Polinomio([-1,0,4,5])
b = Polinomio([1,0,1,2,3,5])

print(str(a))
print(a == b)
print(a.derivar())

	
	
	
	