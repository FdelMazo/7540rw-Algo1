import sys
import random
import time


def quicksort(lista):
    if len(lista) < 2:
        return lista
    pivote = lista[0]
    menores = []
    mayores = []
    for i in range(1, len(lista)):
        elemento = lista[i]
        if elemento <= pivote:
            menores.append(elemento)
        else:
            mayores.append(elemento)

    return quicksort(menores) + [pivote] + quicksort(mayores)


def mergesort(lista):
    if len(lista) < 2:
        return lista
    izq = lista[:len(lista)//2]
    der = lista[len(lista)//2:]
    ordenado_izq = mergesort(izq)
    ordenado_der = mergesort(der)
    return merge(ordenado_izq, ordenado_der)


def merge(a, b):
    resul = []
    cant1 = 0
    cant2 = 0
    while cant1 < len(a) and cant2 < len(b):
        if a[cant1] < b[cant2]:
            resul.append(a[cant1])
            cant1 += 1
        else:
            resul.append(b[cant2])
            cant2 += 1
    resul += a[cant1:]
    resul += b[cant2:]
    return resul


def swap(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]


def posicion_maximo(lista, largo):
    max_pos = 0
    for i in range(largo):
        if lista[i] > lista[max_pos]:
            max_pos = i
    return max_pos


def seleccion(lista):
    for i in range(len(lista)):
        pos_max = posicion_maximo(lista, len(lista) - i)
        swap(lista, pos_max, len(lista) - i - 1)


def burbujeo(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                swap(lista, j, j + 1)


def insercion(lista):
    for i in range(1, len(lista)):
        x = lista[i]
        j = i
        while j > 0 and lista[j-1] > x:
            lista[j] = lista[j-1]
            j = j - 1
        lista[j] = x

def bench(lista_desordenada, f, nombre):
    print("{: <10s}".format(nombre), end="")
    sys.stdout.flush()
    start = time.time()
    f(lista_desordenada[:])
    end = time.time()
    print("{:8.4f} segundos".format(end - start))

def main(cantidad):
    lista_ordenada = list(range(cantidad))
    lista_desordenada = lista_ordenada[:]
    random.shuffle(lista_desordenada)

    bench(lista_desordenada, quicksort, "Quicksort")
    bench(lista_desordenada, mergesort, "Mergesort")
    bench(lista_desordenada, seleccion, "Seleccion")
    bench(lista_desordenada, insercion, "Insercion")
    bench(lista_desordenada, burbujeo, "Burbujeo")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Uso: python ordenamientos.py [cantidad de elementos a ordenar]")
    else:
        main(int(sys.argv[1]))