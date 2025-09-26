count = int(input().strip())

for i in range(count):
    arr = list(map(int, input().strip().split(" ")))
    contBand = [False, False]  # [Yin, Yang]
    for j in range(1, len(arr)):
        try:
            if arr[0] % arr[j] == 0:
                contBand[j-1] = True
        except ZeroDivisionError:
            if  (arr[j] == 0 and arr[0] == 0):
                contBand[j-1] = True
            else:
                contBand[j-1] = False

    if contBand[0] and contBand[1]:
        print("Yin Yang")
    elif contBand[0]:
        print("Yin")
    elif contBand[1]:
        print("Yang")
    else:
        print("Ni Yin Ni Yang")


