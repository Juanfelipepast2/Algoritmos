import math

def sumaDiv(a: int):
    sum = 1 
    sq = math.ceil(math.sqrt(a))
    if a == 1:
        return -1
    for i in range (2, sq):
        if a % i == 0:
            sum += i
            sum += int(a/i)
    if sum == a:
        return 0
    elif sum > a:
        return 1
    else: 
        return -1
cadena  = list(map(int, input().strip().split(" "))) 
for x in cadena:
    print(sumaDiv(x), end=" ")