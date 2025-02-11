print("Este programa suma los números de una cadena numérica")
print("Introduce una cadena numérica: ")
cadena = input()
suma = 0
# Un bucle for para ir caracter a caracter
for i in range(len(cadena)):
    suma += int(cadena[i])
# Mostramos la suma total
print("La suma es ", suma)
print("Fin del programa.")
