print("Programa que muestra los pares entre dos númeres.")
print("Introduzca el número inicial: ")
inicio = int(input())
print("Introduzca el número final: ")
final = int(input())
for i in range(inicio, final + 1):
    # Miramos si el número es par
    if (i % 2 == 0):
        print(i)
print("Fin del programa.")
