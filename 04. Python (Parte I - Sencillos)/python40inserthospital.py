# importar la librería oracledb
import oracledb
from os import system

system("clear")
# Conexión con la base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# Pedir los datos necesarios al usuario
print("Introduzca el código del hospital: ")
hospital_id = input()
print("Introduzca el nombre del hospital: ")
hospital_nom = input()
print("Introduzca la dirección del hospital: ")
hospital_dir = input()
print("Introduzca el teléfono del hospital: ")
hospital_tel = input()
print("Introduzca el número de camas del hospital: ")
hospital_bed = input()
# Montar la sentencia sql para insertar el nuevo registro
# sqlinsert = "insert into hospital "\
#     "(hospital_cod, nombre, direccion, telefono, num_cama) values ("\
#     + hospital_id + ", '" + hospital_nom + "', '" + hospital_dir + "', '"\
#     + hospital_tel + "', " + hospital_bed + ")"
sqlinsert_f = f"insert into hospital "\
              f"(hospital_cod, nombre, direccion, telefono, num_cama) values "\
              f"({hospital_id},'{hospital_nom}','{hospital_dir}',"\
              f"'{hospital_tel}',{hospital_bed})"
# Crear cursor
cursor = conn.cursor()
# Ejecutar cursor
cursor.execute(sqlinsert_f)
# Mostrar el número de registros insertados
print("Hospitales insertados: " + str(cursor.rowcount))
# Cerrar el cursor
cursor.close()
# Nueva variable para la consulta sql
sqlselect = "select * from hospital order by hospital_cod"
# Crear cursor
cursor = conn.cursor()
# Ejecutar cursor
cursor.execute(sqlselect)
# Mostrar los resultados obtenidos de la consulta
print("----------------------HOSPITALES----------------------")
for cod, nom, dir, tel, num in cursor:
    print(str(cod) + " " + nom.title().rjust(14) + " "
          + dir.title().rjust(20) + " "
          + tel.title().rjust(9) + " " + str(num))
print("------------------------------------------------------")
# Confirmar los cambios en base de datos
conn.commit()
# Desconexión de la base de datos
conn.close()
