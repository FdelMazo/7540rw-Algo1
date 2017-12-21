#Pide dos intervalos en horas minutos y segundos y devuelve su suma
import ej31
string = input("Ingrese 3 numeros separados por una coma")
tuplestring = tuple(string)
a = tuplestring[0]
b = tuplestring[3]
c = tuplestring[6]
a = int(a)
b = int(b)
c = int(c)
n1 = ej31.seg(a, b, c)

string2 = input("Ingrese otros 3 numeros")
tuplestring2 = tuple(string2)
d = tuplestring2[0]
e = tuplestring2[3]
f = tuplestring2[6]
d = int(d)
e = int(e)
f = int(f)
n2 = ej31.seg(d,e,f)

n = n1 + n2

h,m,s = e31.hora(n)
print ("{} horas, {} minutos, {} segundos".format(h,m,s))


