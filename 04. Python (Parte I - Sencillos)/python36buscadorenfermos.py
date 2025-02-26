# Importamos la librería oracledb
import oracledb

# Pedimos el código de inscripción al usuario.
print("Introduzca el número de inscripción del paciente: ")
inscripcion = input()
# Conectamos con la base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# Construimos la consulta
sql = f"select apellido, direccion from enfermo where "\
      f"inscripcion = {inscripcion}"

# sql = f"select apellido, direccion from enfermo where sexo = '{inscripcion}'"

# Creamos el cursor
cursor = conn.cursor()
# Ejecutamos la consulta
cursor.execute(sql)
# Como accedemos por PK es un solo registro
# registro = cursor.fetchone()
registro = cursor.fetchall()

# if not registro:
#     print("El paciente no existe.")
# else:
#     for reg in registro:
#         print(f"Datos del paciente >> Nombre: {reg[0]}, Dirección: {reg[1]}")

# Comprobamos si ha devuelto un registro
if (not registro):
    print("El paciente no existe.")
else:
    print(f"Datos del paciente >> Nombre: {registro[0]}, "
          f"Dirección: {registro[1]}")
# Cerramos el cursor
cursor.close()
# Desconectamos la base de datos
conn.close()
