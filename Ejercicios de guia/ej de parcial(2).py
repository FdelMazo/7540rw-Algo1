class _Persona:
	def __init__(self, nombre):
		self.nombre = nombre
		
class Colectivo:
	def __init__(self):
		self.diccionario_destino_persona = {}
	
	def __str__(self):
		cadena = str(self.diccionario_destino_persona)
		return cadena
	
	def subir(self, persona, destino):
		assert type(destino) is str
		assert type(persona) is _Persona
		if destino in self.diccionario_destino_persona:
			self.diccionario_destino_persona[destino].append(persona.nombre)
		else:
			self.diccionario_destino_persona[destino] = (persona.nombre).split()
		
	def bajar(self, destino):
		if destino in self.diccionario_destino_persona:
			a = self.diccionario_destino_persona[destino]
			del self.diccionario_destino_persona[destino]
			return(a)
		else:
			print("No hay personas para que se bajen")

		
a = _Persona("fede")
c = _Persona("Lucas")
b = Colectivo()
b.subir(a,"ramos")
b.subir(c,"ramos")
b.bajar("ramos")
b.subir(c,"haedo")
print(b)
