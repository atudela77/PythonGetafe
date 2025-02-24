# importar librerías necesarias
import oracledb
from os import system
# Borrar salida de terminal
system("clear")
# Conexión con base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# Crear cursor
cursor = conn.cursor()
# Se extrae la información de la tabla emp para meterla en un fichero
sql = "select emp_no, apellido, oficio, salario, dnombre "\
      "from emp e, dept d where e.dept_no = d.dept_no"
# Ejecutar cursor
cursor.execute(sql)
# Abrir fichero
f = open('fichero_empleados.txt', 'w')
f.writelines("NEMP APELLIDO     OFICIO        SALARIO DEPARTAMENTO" + "\n")
f.writelines("---- ------------ ------------- ------- ------------" + "\n")
for numemp, apellido, oficio, salario, nombredept in cursor:
    f.writelines(f"{numemp:4} {apellido.title():12} {oficio.title():12} "
                 f"{salario:8} "
                 f"{nombredept.title():12}" + "\n")
f.close()
cursor.close()
cursor = conn.cursor()
sqldelete = "delete from empleados"
cursor.execute(sqldelete)
print(f"{cursor.rowcount} registros eliminados")
cursor.close()
# Extraemos la información del fichero para insertarla en la tabla empleados
fich = open('fichero_empleados.txt')
sqlinsert = "insert into empleados (emp_no, apellido, oficio, salario, "\
            "dnombre) values (:p1, :p2, :p3, :p4, :p5)"
registros = 0
for linea in fich:
    cursor = conn.cursor()
    datos = linea.split()
    if (datos[0].isdigit()):
        cursor.execute(sqlinsert, (datos[0], datos[1], datos[2],
                                   int(datos[3]), datos[4]))
        registros += cursor.rowcount
    cursor.close()
print(f"{registros} registros insertados")
fich.close()
conn.commit()
conn.close()
