def seleccion(arr, n):

    printArr(arr, n+1)
    maj = majorIndexSearch(arr[:-n]) if len(arr) % 2 == 0 else majorIndexSearch(arr[:-n-1])
    current = arr[-1-n]
    arr[-1-n] = arr[maj]
    arr[maj] = current
    
    if n >= len(arr)-2 :
        n+=1
        printArr(arr, n+1)
        return arr
    else:
        return seleccion(arr, n+1)    

def majorIndexSearch(subArr: list):
    maj = 0    
    for i in range (len(subArr)):
        if subArr[maj] < subArr[i]:
            maj = i
    return maj
    
def printArr(arr, n):
    print(n, "->", end=" ")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

arr = list(map(int, input().strip().split(" "))) #arreglo

arr = seleccion(arr, 0)

for x in arr:
    print(x, end=" ")