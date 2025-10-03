alfabeto = list( input().strip().split("<")) #arreglo
alfabetoRedux = list(input().strip().split(" ")) #arreglo
insert = input().strip()

trad = list(range(0,len(alfabeto)))
gallery = dict(zip(alfabeto, trad))

printed = False


for i in range(len(alfabetoRedux)):
    if gallery[insert] < gallery[alfabetoRedux[i]] and not printed:
        print(insert, end = " ")
        printed = True

    
    print(alfabetoRedux[i], end= " ")
    