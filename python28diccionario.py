print("Diccionarios Python")
# Es necesario crear el objeto diccionario usando
#  el constructor dict()
provincias = dict()
# Después se asignan los datos clave/valor
provincias = {
              924: "Badajoz",
              956:  "Cádiz",
              958: "Granada",
              959: "Huelva",
              91: "Madrid",
              952: "Málaga",
              968: "Murcia",
              923: "Salamanca",
              95: "Sevilla",
              922: "Sta. Cruz de Tenerife",
              975: "Soria",
              96: "Valencia",
              976: "Zaragoza"}
print(provincias)
# get(clave) permite extraer un valor por su clave
dato = provincias.get(968)
print("El prefijo 968 corresponde a", dato)
# items() permite extraer las tuplas clave, valor
for clave, valor in provincias.items():
    print("La clave " + str(clave) + " corresponde al valor " + valor)
# len(diccionario) devuelve el número de tuplas clave/valor del dicionario
print(str(len(provincias)) + " tuplas en provincias")
# keys() permite iterar por clave
for clave in provincias.keys():
    print(clave)
# keys() permite iterar por valor
for valor in provincias.values():
    print(valor)
# setdefault(clave, valor) añade un elemento
provincias.setdefault(123, "Otro")
# pop elimina por clave y extrae el valor a una var si se quiere
var = provincias.pop(95)
print("W", var)
print(provincias)
provincias.clear()
print(provincias)
