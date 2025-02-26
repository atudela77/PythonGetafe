# Se importa la libreria de Python Oracle
import oracledb

print("Inicio BBDD")
# Tenemos un objeto connection (user, password, server)
# Nos conectamos a la base de datos
connection = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# print("¡¡Conectado!!",'\n')
# Para hacer una consulta se utiliza un objeto CURSOR a partir de connection
# Se escribe la cadena en una variable de texto.
sql = "select * from dept"
# Se crea el objeto cursor
cursor = connection.cursor()
# Se ejecuta el cursor
cursor.execute(sql)
# Una vez tenemos los datos los extraemos del cursor.
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
# Cerrar el cursor
cursor.close()
# Cerrar la conexión
connection.close()
print("Fin de BBDD")
