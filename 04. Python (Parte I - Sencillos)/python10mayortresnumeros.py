print("Ejemplo mayor tres números.")
print("Introduzca el primer número: ")
numero1 = int(input())
print("Introduzca el segundo número: ")
numero2 = int(input())
print("Introduzca el tercer número: ")
numero3 = int(input())
mayor = 0
menor = 0
intermedio = 0
# Comparamos cada número con los otros dos para buscar el mayor
if (numero1 >= numero2 and numero1 >= numero3):
    mayor = numero1
elif (numero2 >= numero1 and numero2 >= numero3):
    mayor = numero2
else:
    mayor = numero3
    
# Misma comparación pero para encontrar el menor de los tres
if (numero1 <= numero2 and numero1 <= numero3):
    menor = numero1
elif (numero2 <= numero1 and numero2 <= numero3):
    menor = numero2
else:
    menor = numero3

suma = numero1 + numero2 + numero3
intermedio = suma - mayor - menor
print("Mayor: ", mayor)
print("Menor: ", menor)
print("Intermedio: ", intermedio)

print("Fin de programa.")