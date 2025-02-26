# Importar la librería oracledb
import oracledb
# Realizar la conexión con la base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# Pedimos los datos al usuario
print("Introduzca un ID de departamento: ")
iddept = input()
print("Introduzca el nombre del departamento: ")
nombre = input()
print("Introduzca la localidad del departamento: ")
localidad = input()
# Variable para almacenar la instrucción sql
sqlinsert = f"insert into dept (dept_no, dnombre, loc) "\
            f"values ({iddept}, '{nombre}', '{localidad}')"
# sqlinsert = "insert into dept (dept_no, dnombre, loc) values "
#             "(" + iddept + ", '" +   nombre + "', '" + localidad + "')"
# Crear cursor
cursor = conn.cursor()
# Ejecutar cursor
cursor.execute(sqlinsert)
# Mostramos el número de registros afectados por la sentencia
print("Departamentos insertados: " + str(cursor.rowcount))
# Cerrar cursor
cursor.close()
# Creamos otro cursor
cursor = conn.cursor()
# Instrucción sql
sql = "select * from dept"
# Ejectuar el cursor
cursor.execute(sql)
# Mostrar los registros obtenidos
for row in cursor:
    print(row)
# Cerrar el cursor
cursor.close()
# Confirmar la inserción
conn.commit()
# Realizar la desconexión de la base de datos
conn.close()
