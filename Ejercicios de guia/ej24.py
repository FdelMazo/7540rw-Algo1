def pares():
        """te dice los pares entre dos numeros"""
        n1 = int(input("Ingrese un numero: "))
        n2 = int(input("Ingrese otro: "))
        if n1 < n2:
                if n1 % 2 != 0:
                        n1 = n1 + 1
                elif n1 % 2 == 0:
                        n1 = n1 + 2
                if n2 % 2 != 0:
                        n2 = n2 + 1
                elif n2 % 2 == 0:
                        n2 = n2 - 1
                for i in range (n1, n2, 2):
                        print (i)
        elif n2 < n1: 
                if n1 % 2 != 0:
                        n1 = n1 - 1
                elif n1 % 2 == 0:
                        n1 = n1 - 2
                if n2 % 2 != 0:
                        n2 = n2 - 1
                elif n2 % 2 == 0:
                        n2 = n2 + 1
                for i in range (n1, n2, -2):
                        print (i)
        else:
                print ("no hay pares")

if __name__ == "__main__":
        print (pares())
