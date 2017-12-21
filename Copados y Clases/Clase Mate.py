class Mate:
	def __init__(self, numero):
		self.cebadas = numero
		self.lleno_vacio = False
	
	def __str__(self):
		if self.lleno_vacio == True:
			cadena_lleno_vacio = "Lleno"
		elif self.lleno_vacio == False:
			cadena_lleno_vacio = "Vacio"
		return "Mate con {} cebadas restantes y actualmente {}".format(self.cebadas, cadena_lleno_vacio)
	def cebar(self):
		if self.lleno_vacio == False:
			self.lleno_vacio = True
		else:
			raise Exception("Cuidado! Ya esta lleno!")
			
	def beber(self):
		if self.lleno_vacio == False:
			raise Exception("El mate esta vacio")
		else:
			self.lleno_vacio = False
		self.cebadas -=1
		if self.cebadas < 0:
			print("Esta lavado")
			
mate = Mate(3)
mate.cebar()
mate.beber()
mate.cebar()
mate.beber()
print(mate)

		
	