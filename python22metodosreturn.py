# A continiuación se definen varios métodos de return
def convertirMayusculas(texto):
    return texto.upper()


def convertirMinusculas(texto):
    return texto.lower()


def concatenar(texto1, texto2):
    resultado = texto1 + texto2
    return resultado


# Ahora un método de acción
def mostrarMenu():
    print("Seleccione una opción")
    print("1.- Convertir mayúsculas")
    print("2.- Convertir minúsculas")
    print("3.- Concatenar textos")


# Programa principal
print("Métodos return y acción")
print("Introduzca un texto")
valor = input()
mostrarMenu()
resultado = ""
opcion = int(input())
if (opcion == 1):
    resultado = convertirMayusculas(valor)
elif (opcion == 2):
    resultado = convertirMinusculas(valor)
else:
    print("Ponga otro texto")
    otro = input()
    resultado = concatenar(valor, otro)
print(resultado)
print("Fin del programa")
