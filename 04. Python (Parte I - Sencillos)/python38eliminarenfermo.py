# Importamos la librería oracledb
import oracledb
print("Eliminar enfermo")
# Solicitamos un número de inscripción al usuario
print("Introduzca inscripción para borrar")
data = input()
# Escribimos la consulta
sql = f"delete from enfermo where inscripcion = {data}"
# Conectamos con la base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# Creamos el cursor
cursor = conn.cursor()
# Ejecutamos el cursor
cursor.execute(sql)
# Comprobamos si se ha borrado algún registro
afectados = cursor.rowcount
if (afectados > 0):
    print(f"Registros eliminados: {afectados}")
else:
    print(f"No se ha borrado ningún registro ({afectados})")
# Hay que hacer commit explícitamente (o rollback)
conn.commit()
# conn.rollback
# Cerramos el cursor
cursor.close()
# Una vez que hemos cerrado el cursor podemos hacer más consultas sobre
# el mismo objeto. Creando uno nuevo con la conexión.
sqlselect = "select * from enfermo"
# Creamos un cursor sobre la misma variable.
cursor = conn.cursor()
cursor.execute(sqlselect)
print("------------ENFERMOS-------------")
for row in cursor:
    print("Inscripción: " + str(row[0]) + " - " + row[1])
print("---------------------------------")
cursor.close()
# Desconectamos de la base de datos
conn.close()
