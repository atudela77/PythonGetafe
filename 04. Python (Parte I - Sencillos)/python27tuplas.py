print("Tuplas de Python")
# Las tuplas no se pueden modificar
productos = ("Leche", "Cacao", "Avellanas", "Azucar")
numeroElementos = len(productos)
# No se puede modificar, es una constante de elementos
# productos[0] = "Almendras"
print("Elementos tupla: ", numeroElementos)
print("----------------")
for i in range(numeroElementos):
    print(productos[i])
print("----------------")
for producto in productos:
    print(producto)
print("----------------")
cadena = "Hola que tal"
for cad in cadena:
    print(cad)
print("----------------")
