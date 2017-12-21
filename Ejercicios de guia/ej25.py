def triang(n):
        """Imprime los numeros triangulares hasta un numero n"""
		j = 0
        for i in range(1, n+1):
                j = j + i
                print(i, j, sep=" ")
	
