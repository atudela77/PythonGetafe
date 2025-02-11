print("Conjetura de Collatz.")
# La conjetura de Collatz dice que todo número acaba siendo uno si
#  se va multiplicando.
#  por 3 y se le suma 1 si es impar, y se divide entre dos si el número es par.
print("Introduzca un número: ")
numero = int(input())
# Bucle while para comprobar que el número es distinto de uno
while (numero != 1):
    if (numero % 2 == 0):
        numero = int(numero / 2)
    else:
        numero = numero * 3 + 1
    print(numero)
print("FIn del programa.")
