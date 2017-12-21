def identidad(n):
	"""Devuelve la matriz de identidad"""
	for i in range (n):
		for j in range(n):
			if i==j:
				print(1, end=" ")
			else:
				print(0, end=" ")
		print()
				
def identidad2(n):
	"""Otra manera"""
	for i in range(n,0,-1):
		print(" 0"*(n-i),1,"0 "*(i-1))

print(identidad(3))

print("-------")

print(identidad2(3))
