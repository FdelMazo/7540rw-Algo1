class Caramelera:
	def __init__(self, max):
		self.max = max
		self.inn = 0
		
	def __str__(self):
		return "Caramelera con {}/{} caramelos".format(self.inn, self.max)
	def poner(self, n):
		if self.inn + n > self.max:
			raise ValueError("No entran")
		self.inn += n
		
	def caramelos(self):
		return self.inn
		
	def sacar(self,n):
		if self.inn - n < 0:
			raise ValueError("No hay tantos")
		self.inn -= n
		
a = Caramelera(20)
a.poner(4)
a.sacar(3)
a.caramelos()
print(a)
#a.poner(21)
#a.sacar(22)