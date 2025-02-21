# Importar libreria oracledb
import oracledb
from os import system

system("clear")
# Pedimos al usuario que introduzca el turno del que quiere la información
print("Introduzca el turno del que desea el listado de empleados: ")
turno = input().upper()
# Diccionario para recuperar el nombre del turno
nombre_turno = {"M": "mañana", "T": "tarde", "N": "noche"}
# Conexión a la base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
    )
# Construir la consulta
sql = f"select apellido, funcion from plantilla "\
      f"where turno = '{turno.upper()}'"
# Crear cursor
cursor = conn.cursor()
# Ejecutar consulta
cursor.execute(sql)
# Recuperar datos
plantilla = cursor.fetchall()
# Comprobar si ha devuelto algún registro
if plantilla:
    system("clear")
    print(f"Los empleados de plantilla del turno "
          f"de {nombre_turno.get(turno)} son: \n")
    for apellido, funcion in plantilla:
        print(f">> Apellido: {apellido} /// Función: {funcion}")
print("\n")

# Cerrar cursor
cursor.close()
# Desconectar la base de datos
conn.close()
