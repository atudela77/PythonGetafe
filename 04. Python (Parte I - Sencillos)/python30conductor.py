from class30coche import Coche
from os import system
system("clear")
print("Programa para probar la clase Coche")

# car = Coche()
# car.arrancar()
# car.acelerar()
# car.acelerar()

print("Conduciendo mi coche")
car = Coche()
car.marca = "Volkswagen"
car.modelo = "Escarabajo"
opcion = -1
while (opcion != 0):
    print("------------------")
    print("0.- Salir")
    print("1.- Arrancar")
    print("2.- Acelerar")
    print("3.- Frenar")
    print("4.- Detener coche")
    print("Seleccione una opción")
    opcion = int(input())
    if (opcion == 1):
        car.arrancar()
    elif (opcion == 2):
        car.acelerar()
    elif (opcion == 3):
        car.frenar()
    elif (opcion == 4):
        car.detener()
    elif (opcion == 0):
        print("Saliendo del programa")
    else:
        print("Opción incorrecta")
