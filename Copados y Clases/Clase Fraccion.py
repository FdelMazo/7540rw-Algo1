def mcd(num1,num2):
	nums = num1,num2 
	listas = []
	if num1 == num2:
		return num1
	for n in nums:
		lista = []
		for i in range(2, n):
			while n%i == 0:
				n = n//i
				lista.append(i)
		listas.append(lista)
	cd = []
	for i in listas[0]:
		if i in listas[1]:
			cd.append(i)
	return max(cd)
	
class Fraccion:
	def __init__(self, numerador, divisor):
		self.num = numerador
		self.div = divisor
	
	def __str__(self):
		if self.div == 1:
			return "{}".format(self.num)
		else:
			return "{}/{}".format(self.num, self.div)
	
	def __add__(self,otro):
		if type(otro) is not Fraccion:
			raise TypeError
		num_nuevo = otro.div * self.num + self.div * otro.num
		div_nuevo = self.div * otro.div
		return Fraccion(num_nuevo, div_nuevo)
		
	def __mul__(self,otro):
		if type(otro) is not Fraccion:
			raise TypeError
		num_nuevo = self.num * otro.num
		div_nuevo = self.div * otro.div
		return Fraccion(num_nuevo,div_nuevo)
	
	def simplificar(self):
		try:
			mcd1 = mcd(self.num, self.div)
		except:
			return self
		if self.num%mcd1 == 0 and self.div%mcd1 ==0:
			num_nuevo = self.num // mcd1
			div_nuevo = self.div // mcd1		
		return Fraccion(num_nuevo,div_nuevo)

a = Fraccion(18,6)
b = Fraccion(2,3)
c = a + b
d = a*b
print(a.simplificar())