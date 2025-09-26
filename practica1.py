# Practica 1 - Ejercicio 1
# cantProblemas = int(input())
# for i in range(cantProblemas):
#     a, b = list(map(int, input().strip().split(" ")))
#     print(a + b, end=" ")
#     print(a * b, end=" ")
#     print(a ** b)
# Practica 1 - Ejercicio 2
a, b, c, d, e, f = list(map(int, input().strip().split(" ")))
delt = b**2 - (4*a*c)
if delt > 0:
    print("hiperbola")
elif delt == 0:
    print("parabola")
else:
    if a == c:
        print("circunferencia")
    else:
        print("elipse")

    