print("Listas con Python")
# Lista de enteros
listaNumeros = [2, 12, 5, 45, 21, 78, 99, 1]
# Las listas comienzan en cero y finalizan en (len - 1)
print("Numero 0: ", listaNumeros[0])
print("Numero 1: ", listaNumeros[1])
print("Último número: ", listaNumeros[len(listaNumeros) - 1])
print("Otro último: ", listaNumeros[-1])
# Lista de strings
listaNombres = ['Carlos', 'Ana', 'Marta', 'Antonio',
                'Fernando', 'Sandra', 'Luis']
print("Nombre 2: ", listaNombres[1])
print("Nombre 4: ", listaNombres[3])
print("Prueba: ", listaNombres[::-1])
# append() crea un nuevo elemento en la lista al final
listaNombres.append("Lucia")
print("Nombre 8: ", listaNombres[7])
# insert() crea un elemento nuevo en una posición indicada.
# Desplaza los elementos existentes desde la posición indicada
#  hacia la derecha.
listaNombres.insert(4, "Infiltrado")
# Vamos a recorrer todos los elmentos de la lista y mostrar
# su posición.
for i in range(len(listaNombres)):
    print(str(i) + "=" + listaNombres[i])
# remove() elimina un objeto dentro de la lista y mueve
# los elementos a la derecha del borrado hacia la izquierda
listaNombres.append("Ana")
# Si hay más de uno igual, elimina sólo el primero
listaNombres.remove("Ana")
# Si se intenta eliminar un elemento que no existe peta
# listaNombres.remove("Aitana")
print(listaNombres)
# pop() elimina un elemento por su posición
# (y guarda lo borrado en una variable, si se quiere, no es obligatorio)
listaNombres.pop(1)
print(listaNombres)
# del permite utilizar los índices para eliminar. Permite slicing
# i.e., del lista[3] borra la posición 3
# i.e., del lista[0:4] borra la sublista de las posiciones de 0 a 4
del listaNombres[2]
print(listaNombres)
del listaNombres[1:3]
print(listaNombres)
# clear() borra todo el contenido de una lista
listaNombres.clear()
print(listaNombres)
listaNombres = ['Carlos', 'Ana', 'Marta', 'Antonio',
                'Fernando', 'Sandra', 'Luis']
# in es operador relacional para condiciones
print("Está Fernando? ", "Fernando" in listaNombres)
print("Está Silvia? ", "Silvia" in listaNombres)
# Mostramos los números con un bucle
for i in listaNumeros:
    print(i)
# sort() permite ordenar la lista de forma ascendente
listaNumeros.sort()
for i in listaNumeros:
    print(i)
# sort(reverse = True) permite ordenar la lista de forma ascendente
listaNumeros.sort(reverse=True)
for i in listaNumeros:
    print(i)
listaNombres.sort()
for j in listaNombres:
    print(i)
listaNombres.sort(reverse=True)
for k in listaNombres:
    print(i)
