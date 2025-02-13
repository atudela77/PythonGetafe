# Los import se realizan al principio de nuestro código.
# Después irían los métodos.
# Finalmente el código lógico del programa principal.
# from libreria24matematicas import sumarNumeros, restarNumeros,
#  multiplicarNumeros, mostrarMenu
# La declaración anterior es muy larga. Utilizamos from/import
#  cuando se van a utilizar pocos métodos. Sino es mejor importar
#  la clase completa.
import libreria24matematicas

# Programa principal
print("Calculadora métodos")
numero1 = 9
numero2 = 19
# Se invoca el método así porque hemos utilizado import en
#  vez de from/import. No hay diferencia de funcionalidad.
libreria24matematicas.mostrarMenu()
opcion = int(input())
resultado = 0
if (opcion == 1):
    resultado = libreria24matematicas.sumarNumeros(numero1, numero2)
elif (opcion == 2):
    resultado = libreria24matematicas.restarNumeros(numero1, numero2)
elif (opcion == 3):
    resultado = libreria24matematicas.multiplicarNumeros(numero1, numero2)
else:
    print("No ha seleccionado una opción correcta")
print("Resultado ", resultado)
print("Fin de programa")
