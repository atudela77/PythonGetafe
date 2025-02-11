print("Este programa muestra la tabla de multiplicar de un número dado.")
# Pedimos el número al usuario
print("Introduzca un número: ")
numero = int(input())
# Se realizan las operaciones y se van mostrando los resultados.
for i in range(1, 11):
    print(str(numero) + " x " + str(i) + " = " + str(numero * i))
print("Fin del programa.")
