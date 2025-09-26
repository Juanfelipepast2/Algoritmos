# En la primera línea un número entero positivo T, y a continuación T líneas en las que en cada línea hay una lista 
# que representa un arreglo no vacío A donde las componentes se encuentran separadas por un espacio en blanco y 
# contiene los coeficientes del polinomio P(x)
# escritos en el orden del coeficiente independiente al coeficiente principal. 





def divSintetica(arr, c):
    arr2 = arr.copy()
    resultado = arr2.pop(0)
    resultado = arr2[0] * resultado 
    for i in range(0, len(arr2)):
        resultado = arr2[i] + (resultado * c)
    return resultado



t = int(input().strip()) 
for _ in range(t):
    arr = list(map(int, input().strip().split(" ")))
    arr = arr[::-1]
    band = True
    c = 1
    while band:
        if divSintetica(arr, c) == 0:
            print(".......",c)
            band = False
        
        
        c += 1  