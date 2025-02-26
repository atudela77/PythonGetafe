# Importar la librería oracledb
import oracledb
print("----Buscador oficios empleados---")

# Conexión con base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# Consulta de oficios para el menú
sqloficios = "select distinct oficio from emp"
# Creamos el cursore
cursor = conn.cursor()
# Ejecutamos el cursor
cursor.execute(sqloficios)
# Mostramos el menú
listaoficios = []
contador = 1
for ofi in cursor:
    print(f"{contador} - {ofi[0]}")
    listaoficios.append(ofi[0])
    contador += 1
# Cerramos el cursor
cursor.close()
print("Seleccione una opción.")
opcion = int(input()) - 1
# Consulta empleados por oficio
sqlempleados = "select * from emp where oficio = :p1"
# Creamos el cursor
cursor = conn.cursor()
# Ejecutamos el cursor
cursor.execute(sqlempleados, (listaoficios[opcion],))
# Mostramos los datos
for row in cursor:
    print(row)
# Cerramos el cursor
cursor.close()
# Cerramos la conexión
conn.close()
print("Fin de programa")
