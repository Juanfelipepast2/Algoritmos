def insertionSort(arr):
    n = t = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            n += 1
            t += 1
            arr[j + 1] = arr[j]
            j -= 1
        
        n += 1 
        
        arr[j + 1] = key
    return n, t


t = int(input().strip())

for i in range (t):
    arr = list(map(int, input().strip().split(" "))) #arreglo
    n, t = insertionSort(arr)    
    if n == len(arr)-1:
        print(n, "Best")
    elif t == len(arr)*(len(arr)-1)/2:
        print(n, "Worst")
    else:
        print(n, "Average")
