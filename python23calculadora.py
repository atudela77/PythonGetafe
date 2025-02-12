# Método para calcular operaciones de dos números
# Método para sumar dos números
def sumaNumeros(a, b):
    return a + b


# Método para restar dos numeros
def restarNumeros(a, b):
    return a - b


# Método para multiplicar dos números
def multiplicarNumeros(a, b):
    return a * b


# Método para mostrar el menú de opciones
def mostrarMenu():
    print("Seleccione una opción")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")


# Comprobación de numérico
def compruebaNumerico(variable):
    if (variable.isnumeric()):
        return int(variable)


# Programa principal
print("Introduzca el primer número: ")
num1 = int(input())
print("Introduzca el segundo número: ")
num2 = int(input())

# Se muestra el menú de opciones
mostrarMenu()
opcion = 0
while (opcion != 1 and opcion != 2 and opcion != 3):
    entrada = input()
    opcion = compruebaNumerico(entrada)


# Se selecciona la operación correspondiente
resultado = 0
texto = ""
if (opcion == 1):
    texto = " + "
    resultado = sumaNumeros(num1, num2)
elif (opcion == 2):
    texto = " - "
    resultado = restarNumeros(num1, num2)
else:
    texto = " * "
    resultado = multiplicarNumeros(num1, num2)

# print(str(num1) + texto + str(num2) + " = " + str(resultado))
print(f"{str(num1)}{texto}{str(num2)} = {str(resultado)}")

print("Fin del programa")
