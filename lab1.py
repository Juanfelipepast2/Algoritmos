str1 = "The avenger"
print(str1.count("e"))
print(str1.count("e",0,3))


cadena = "abcabcabcabc"
print(cadena.count("abc"))

print("------------------------")


#####upper, lower, capitalize, title, swapcase



##strip, ltrip, rstrip, por defecto son espacios en blanco, pero se puede poner cualquier caracter o cadena


#split, divide cadenas por parametros en una lista


#just justifica cadenas, ljust, rjust, center, rellena con espacios o con el caracter que se le pase


#zfill, rellena con ceros a la izquierda hasta completar el tamaño que se le pase


#REPLAce, reemplaza una subcadena por otra, se le puede pasar un tercer parametro que es el numero de veces que se quiere reemplazar

#listas


#la operacion lista * 3 está basada en la lista de klein

#las listas pueden tener listas dentro

#hay comparaciones entre listas que se hacen elemento a elemento
#las listas son mutables, se pueden cambiar los elementos
#las listas pueden tener elementos de diferentes tipos


#las cadenas pueden ser mayores a otras cadenas, se comparan elemento a elemento, #si una cadena es prefijo de otra, la mayor es la mas larga
#las listas se comparan igual que las cadenas, pueden varias segun su codigo ascii



print("------------------------")

print(["Rojas", 123] < ["Rosas", 123])
print(["Rosas", 123] < ["rosas", 123])
print(["Rosas", 123] < ["Rosas", 23])
print(["Rojas", 123] < ["Rosas", 123])



print("------------------------")
#subindices y slicing en listas
jugadores = ["Messi", "Ronaldo", "Neymar", "Mbappe"]


print(jugadores[0])
print(jugadores[3])
print(jugadores[-1])
print(jugadores[-2])



print("------------------------")


#iterar listas con for each
for jugador in jugadores:
    print(jugador, end=",")


#listas con ciclos o condicionales dentro o listas por comprension
d = 10
desplaza = [d + x for x in range(5)]
print("\n", desplaza)

potencia = [3** x for x in range(5)]
print("\n", potencia)



#"obtener varias variables con listas por comprension"
var1, var2, var3 = [x**2 for x in range(3)]
print(var1, var2, var3)


#de las funciones sse pueden obtener tuplas, que son inmutables, no se puede usar subindices para cambiar valores
print("----------------------")
t = (x**2 for x in range(3))
print(t)
print(next(t))
print(next(t))
print(next(t))          


#los valores de la lista se pueden cambiar con el subindice


#metodos de lista, insert, append, extend, remove, pop, clear, index, count, sort, reverse, copy
#copy hace una copia superficial, es decir, si la lista tiene listas dentro, no las copia, solo copia la referencia a la lista original

#INdex devuelve el indice del primer elemento que coincide con el valor buscado, si no lo encuentra da error
#Count cuenta el numero de veces que aparece un elemento en la lista


#se pueden convertir colecciones o tuplas en listas con list()
#se pueden convertir listas en tuplas con tuple()
#se pueden convertir listas en conjuntos con set(), los conjuntos no tienen orden ni elementos repetidos
#se pueden convertir conjuntos en listas con list()
#se pueden convertir cadenas en listas con list(), cada caracter es un elemento de la lista
#se pueden convertir listas en cadenas con join(), se le pasa la cadena que se quiere usar como separador
#se pueden convertir listas en cadenas con str(), pero no se puede elegir el separador, se usa la representacion de la lista

#pop elimina un valor pero lo retorna

#map sirve para aplicar una funcion a cada elemento de una lista o conjunto, devuelve un iterador, puede configurarse para solo ciertos elementos
#filter sirve para filtrar una lista o conjunto segun una condicion, devuelve un iterador