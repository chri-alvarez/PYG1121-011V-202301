import numpy as np
import random


lista = []

for i in range(10):
    lista.append(random.randint(0, 100))

print(lista)

arreglo = np.array(lista)
print(arreglo)


arreglo2 = np.ones(10)
for i in range(len(arreglo2)):
    arreglo2[i]=random.randint(0, 100)

print(arreglo2)

print("El número mayor del arreglo 1 es ",arreglo.max())
print("El número mayor del arreglo 2 es ",arreglo2.max())
print("El número menor del arreglo 1 es ",arreglo.min())
print("El número menor del arreglo 2 es ",arreglo2.min())
print("El promedio del arreglo 1 es ",arreglo.mean())
print("El promedio del arreglo 2 es ",arreglo2.mean())
print("La suma del arreglo 1 es ",arreglo.sum())
print("La suma del arreglo 2 es ",arreglo2.sum())