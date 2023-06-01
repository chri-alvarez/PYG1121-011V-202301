import numpy as np
import random

arreglo = np.zeros((3,3))
print(arreglo)

filas, columnas = arreglo.shape

for i in range(filas):
    for j in range(columnas):
        arreglo[i,j]= random.randint(0,100)

print(arreglo)
print("Promedio es",arreglo.mean())
print("Máximo es", arreglo.max())
print("Mínimo es",arreglo.min())
print("Diagonal es",arreglo.diagonal())


diagonal = np.diag([1,2,3])
print("Diagonal",diagonal)