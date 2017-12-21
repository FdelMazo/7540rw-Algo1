import time
def contrasena():
	"""El usuario tiene que poner la contraseña correcta para seguir"""
	contrasena ="Password"
	c1= input("Introduzca su contraseña: ")
	intentos= 0
	s = 0
	while c1 != contrasena and intentos<3:
		intentos += 1 
		s = s +1
		if c1 == contrasena:
			return True
		time.sleep(s)
		c1=input("Contraseña incorrecta, introduzca nueva: ")