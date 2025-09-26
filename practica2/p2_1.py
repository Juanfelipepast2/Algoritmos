
# Descripción del problema
# Dado un conjunto de arreglos de enteros positivos, deseamos calcular la suma de los valores enteros que se 
# encuentran en el intervalo conformado por el valor el valor mínimo y el valor máximo de cada arreglo. 
# Adicionalmente deseamos calcular la suma de los cuadrados y la de los cubos de los valores que se encuentran en dicho intervalo, para cada arreglo.

# Entrada
# En la primera línea un número entero N
# , y a continuación N líneas en la que en cada línea hay una cadena que representa un arreglo no vacío T
# de enteros que se encuentran separados por un espacio.

# Salida
# N
# líneas, en las cuales cada una contiene la suma de los valores, la suma de los cuadrados y la suma de los cubos, de los enteros que pertenecen al intervalo comprendido entre el valor mínimo (inclusive) y máximo (inclusive) de cada uno de los arreglos T
# . Los valores impresos en cada línea deben estar separados por un espacio.

# Ejemplos de entrada y salida
n = int(input())
sum = sqr = cube = 0
for i in range(n):
     aa = list(map(int, input().strip().split(" "))) 
     aa.sort()    
     for j in range (aa[0], aa[-1]+1):
          sum += j
          sqr += j**2
          cube += j**3
     
     print(sum, sqr, cube)   
     sum = sqr = cube = 0
# 2
# 6 9 12 3
# 0 1 2 3