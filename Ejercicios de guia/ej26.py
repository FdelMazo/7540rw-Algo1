import ej26anexo
def main():
    """"Imprime el factorial de un numero hasta que el usuario no introduzca mas"""
	while True:
        n = input("Ingrese un N o *: ")
        if n == "*":
            break
        n = int(n)
        fact = ej26anexo.factorial(n)
        print (n, fact, sep=", ")
    


