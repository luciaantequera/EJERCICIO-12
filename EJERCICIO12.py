def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Listas de prueba
listas_de_prueba = [
    [6, 2, 8, 1, 4],   # Aleatoria
    [1, 2, 3, 4, 5],   # Ordenada
    [9, 7, 5, 3, 1]    # Invertida
]

# Pruebas de Bubble Sort
for lista in listas_de_prueba:
    print(f"Original: {lista} -> Ordenada: {bubble_sort(lista)}")

import time
import random

# Medición empírica del tiempo
for lista in listas_de_prueba:
    inicio = time.time()
    bubble_sort(lista)
    fin = time.time()
    print(f"Lista: {lista} -> Tiempo: {fin - inicio:.8f} segundos")
