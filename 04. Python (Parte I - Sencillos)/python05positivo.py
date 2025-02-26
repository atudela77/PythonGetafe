
print("Número positivo/negativo/cero", "\n")

# Se solicita un núnero al usuario.
print("Introduzca un número: ")
numero = input()

# Se comprueba si el número es igual o mayor que cero.
if (int(numero) > 0):
    print("El número " + numero + " es positivo.")
elif (int(numero) == 0):
    print("El número es cero.")
else:
    print("El número " + numero + " es negativo.")

# Se sustituye el código siguiente por la opción anterior ELIF ELSE que 
#  es más clara.
# else:
#     if(int(numero) == 0):
#         print("El número es cero.")
#     else:
#         print("El número " + numero + " es negativo.")
# Se sustituye el código anterior por la opción ELIF ELSE que es más clara

print("Fin del programa")
