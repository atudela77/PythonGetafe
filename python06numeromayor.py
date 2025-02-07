# Se pide la usuario dos números y mostramos qué número es mayor o mostramos su los números son iguales.
print("Comparación de dos números", "\n")

# Solicitamos dos números al usuario.
print("Introduzca el primer número: ")
numero1 = int(input())
print("Introduzca el segundo número: ")
numero2 = int(input())

# Se comparan los números introducidos.
if (numero1 == numero2):
    print("Los números son iguales.", "\n")
elif (numero1 > numero2):
    print("El número " +  str(numero1) + " es mayor que el número " + str(numero2) + "." + "\n")
else:
    print("El número " +  str(numero1) + " es menor que el número " + str(numero2) + ".", "\n")

print("Fin del programa.")
