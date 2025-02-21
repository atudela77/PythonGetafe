import oracledb
# Se crea la conexión a la base de datos
connection = oracledb.connect(
    user='system',
    password='oracle',
    dsn='localhost:1521/xe'
)
# Escribimos consulta en variable sql
sql = "select * from dept"
# Creamos el cursor
cursor = connection.cursor()
# Ejecutamos el cursor
cursor.execute(sql)
# Para recorrer el cursor se utilizan bucles for de referencia
for row in cursor:
    print(row)
print("\n")
# sql = "select emp_no, apellido, oficio from emp"
# Ejecutamos el cursor de nuevo
cursor.execute(sql)
# Para recorrer el cursor se utilizan bucles for de referencia
for codigo_dept, nombre_dept, ciudad_dept in cursor:
    print("Código de departamento: ", codigo_dept)
    print("Nombre de departamento: ", nombre_dept)
    print("Ciudad del departamento: ", ciudad_dept, "\n")

# Cerramos cursor
cursor.close()

# Desconexión de la base de datos.
connection.close()
