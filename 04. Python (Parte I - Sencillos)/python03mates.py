print("Ejemplo mates variables")

print("Introduzca el número 1: ")
numero1 = int(input())
print("Introduzca el número 2: ")
numero2 = int(input())
print("\n")

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Mensajes
print("Mensajes: ")
print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", multiplicacion)
print("División: ", division)
print("División truncada: ", int(division), "\n")

# Operaciones
print("Operaciones: ")
print(str(numero1) + " + " + str(numero2) + " = " + str(suma))
print(str(numero1) + " - " + str(numero2) + " = " + str(resta))
print(str(numero1) + " * " + str(numero2) + " = " + str(multiplicacion))
print(str(numero1) + " / " + str(numero2) + " = " + str(division))
print("\n")
