# Importamos la clase creada para trabajar con Oracle
from conexionoracle47eliminarenfermos import ConexionOracleEnfermos

print("Probando clases de Oracle: Enfermos")
# Mostramos el menú al usuario
print("Seleccione una opción: ")
print(" 1. Modificar el apellido de un enfermo")
print(" 2. Eliminar un enfermo")
opcion = int(input())

# Ejecutamos la opción seleccionada
if (opcion == 1):
    # Solicitamos el código de inscripción al usuario
    print("Introduzca una inscripción: ")
    inscripcion = input()
    # Opción para modificar un apellido
    print("Introduzca el nuevo apellido: ")
    apellido = input()
    # Creamos un objeto  de la clase creada
    connection = ConexionOracleEnfermos()
    # Ejecutamos el método para actulizar el apellido
    actualizados = connection.modificarApellido(apellido, inscripcion)
    print(f"Enfermos modificados: {actualizados}")
elif (opcion == 2):
    # Solicitamos el código de inscripción al usuario
    print("Introduzca una inscripción: ")
    inscripcion = input()
    # Creamos un objeto  de la clase creada
    connection = ConexionOracleEnfermos()
    # Ejecutamos el método para eliminar enfermos
    eliminados = connection.eliminarEnfermo(inscripcion)
    # Mostramos el número de registros eliminados
    print(f"Enfermos eliminados: {eliminados}")
else:
    print("Opción inválida")

print("Fin de programa")
