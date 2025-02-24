# Importar la librería oracledb
import oracledb
# Titulo del programa
print("Ejemplo de parámetros Oracle")
# Creamos conexión con la base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# Pedimos datos al usuario
print("Introduzca el número de departamento: ")
iddept = input()

# Consulta sobre la tabla de departamentos
# sql = f"select apellido, oficio, dept_no from emp where dept_no = {iddept}"
# Con la consulta anterior si ponemos "0 or 1=1" cuando nos pida el dato de
#  número de departamento, accedemos a todos los datos de la tabla.
# Esto se llama SQL INJECTION.

# Consulta con parámetros
sql = "select apellido, oficio, dept_no from emp where dept_no = :param1"
# Crear cursor
cursor = conn.cursor()
# Ejecutamos el cursor
cursor.execute(sql, (iddept,))
# Mostrar los resultados
for apellido, oficio, dept_no in cursor:
    print(f"Apellido : {apellido.title().ljust(10)}, Oficio: "
          f"{oficio.title().ljust(14)}, Departamento:  {dept_no}")
# Cerrar cursor
cursor.close()
# Desconexión de base de datos
conn.close()
