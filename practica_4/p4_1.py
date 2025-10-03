t = int(input().strip())

for i in range(t):
    arr = list(map(int, input().strip().split(" "))) #arreglo
    objective = int(input().strip()) #numero objetivo

    primero = False
    initIndex = lastIndex = -1
    for i in range(len(arr)):
        if arr[i] == objective:
            if not primero:
                primero = True
                initIndex = i
            
            lastIndex = i


    
    print(initIndex, lastIndex)


#ESTO PUEDE SER MÁS EFICIENTE

#TODO PARA OTRO LABORATORIO