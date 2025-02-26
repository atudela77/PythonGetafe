import oracledb
from os import system
system("clear")
# Obtenemos la información necesaria del usuario
print(">> Introduzca el apellido del doctor: ")
doc_ape = input()
print(">> Introduzca la especialidad del doctor: ")
doc_esp = input()
print(">> Introduzca el salario del doctor: ")
doc_sal = input()

# Conexión con base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)

# Recuperamos los datos para el menú
sqlselect = "select distinct hospital_cod, nombre from hospital"
# Creamos cursor
cursor = conn.cursor()
# Ejecutamos cursor
cursor.execute(sqlselect)
# Inicializamos lista resultado

list_hospital = []
# # Guardamos los datos en una lista
for hospital in cursor:
    list_hospital.append(hospital)

# Cerramos cursor
cursor.close()

# Pintamos el menú
linea = " ------------------------"
print(linea)
print(" Seleccione un hospital ")
print(linea)
for i in range(len(list_hospital)):
    print(f" {i+1} - {list_hospital[i][1].title()}")
print(linea)
opcion = int(input()) - 1

# Recuperamos el máximo id de los doctores
sqldoctorid = "select max(doctor_no) + 1 as maximo from doctor"
# Creamos cursor
cursor = conn.cursor()
# Ejecutamos el cursor
cursor.execute(sqldoctorid)
doc_id = cursor.fetchone()[0]
# Cerramos cursor
cursor.close()

# Insertamos el nuevo doctor con los datos obtenidos
sqlinsert = """
        insert into doctor
            (hospital_cod, doctor_no, apellido, especialidad, salario)
        values
            (:p1, :p2, :p3, :p4, :p5)
"""
# Crear cursor
cursor = conn.cursor()
# Ejecutar cursor
cursor.execute(sqlinsert, (list_hospital[opcion][0], doc_id, doc_ape,
                           doc_esp, doc_sal))
# Comprobar resultado
if (cursor.rowcount == 1):
    print("Registro insertado correctamente", "\n")
else:
    print("No se ha insertado el registro.", "\n")
# Cerrar cursor
cursor.close()
# Confirmar los cambios
conn.commit()

# Mostrar tabla doctores
sqlmostrar = """
    select hospital_cod, doctor_no, apellido, especialidad, salario
    from doctor
    order by especialidad
"""
# Crear cursor
cursor = conn.cursor()
# Ejecutar cursor
cursor.execute(sqlmostrar)
# Mostrar resultados
print("HOSP DOC_ID APELLIDO           ESPECIALIDAD       SALARIO   ")
print("---- ------ ------------------ ------------------ ----------")
for h, d, a, e, s in cursor:
    if (d == doc_id):
        h = f"> {h}"
    print(f"{h:4} {d:6} {a:18} {e:18} {s:10}")
print("---- ------ ------------------ ------------------ ----------", "\n")
# Cerramos cursor
cursor.close()

# Cerramos conexión
conn.close()
