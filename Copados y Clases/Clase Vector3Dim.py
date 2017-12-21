class Vector3dim:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __str__(self):
		return "[{},{},{}]".format(self.x,self.y,self.z)
	def __mul__(self, k):
		return Vector3dim(k*self.x,k*self.y,k*self.z)
	def __add__(self,otro):
		if type(otro) is not Vector3dim:
			raise TypeError
		return Vector3dim(self.x+otro.x,self.y+otro.y,self.z+otro.z)
		
a = Vector3dim(1,2,3)
b = Vector3dim(4,5,6)
print(a+b)
print(a*3)