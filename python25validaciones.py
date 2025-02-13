# Importamos la librería con los métodos
from librerias25validaciones import validarISBN, letraDNI

print("Inicio de programa de validaciones")
# Probamos la validación del ISBN
print("Introduzca un ISBN: ")
isbn = input()
if (validarISBN(isbn)):
    print("ISBN Correcto")
else:
    print("ISBN Incorrecto")

# Probamos el cálculo de la letra del DNI
print("Introduzca el DNI sin letra: ")
dni = input()
print("La letra del DNI es la", letraDNI(dni))

print("Fin de programa")
