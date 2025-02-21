# Importar la librearía oracledb
import oracledb

# Conexión a la base de datos
connection = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# Se pide un departamento al usuario.
print("Introduzca el número del departamento: ")
data = input()
# Consulta
sql = "select * from dept where dept_no = " + data
# sql = f"select * from dept where dept_no = {data}"
# Se crea el cursor
cursor = connection.cursor()
# Se ejecuta la consulta
cursor.execute(sql)
# La consulta es por la PK, entonces devuelve una sola fila.
row = cursor.fetchone()
if (not row):
    print("No existe el departamento")
else:
    # Mostramos los datos extraidos
    print(row[1] + ", " + row[2])
    # print(f"{row[1]}, {row[2]}")
# Se cierra el cursor
cursor.close()
# Desconexión de la base de datos
connection.close()
