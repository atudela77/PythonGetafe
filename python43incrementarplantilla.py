# importar librería oracledb
import oracledb
from os import system
system("clear")
# Conexión con la base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# Pedir la información al usuario
print("Introduzca el código del hospital: ")
hospital = input()
print("Introduzca el incremento del salario: ")
incremento = input()
# Construir el sql update
sqlupdate = "update plantilla set salario = salario + :p1 "\
            "where hospital_cod = :p2"
# Creamos cursor
cursor = conn.cursor()
# Ejecutamos el cursor
cursor.execute(sqlupdate, (incremento, hospital))
# Mostramos el número de registros actualizados
print(f"{cursor.rowcount} registros actualizados")
# Cerramos el cursor
cursor.close()
# Consulta sql select
sqlselect = "select apellido, funcion, salario from plantilla "\
            "where hospital_cod = :p1"
# Creamos el cursor
cursor = conn.cursor()
# Ejecutamos el cursor
cursor.execute(sqlselect, (hospital,))
# Mostramos los datos obtenidos
for apellido, funcion, salario in cursor:
    print(f"Apellido: {apellido}, Función: {funcion}, Salario: {salario}")
# Cerramos el cursor
cursor.close()
# Confirmamos los cambios
conn.commit()
# Desconexión de la base de datos
conn.close()
