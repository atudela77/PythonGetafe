# Importar la librería oracledb
import oracledb
# Conexión con la base de datos
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
# Pedir la información al usuario
print("Introduzca el oficio: ")
oficio = input()
print("Introduzca el incremento de salario (%): ")
incremento = input()
# Update para actualizar el salario
sqlupdate = "update emp set salario = salario * :incremento "\
            "where oficio = :p1"
# Crear cursor
cursor = conn.cursor()
# Poner los datos en el formato adecuado
subida = 1 + (int(incremento)/100)
oficiomayus = oficio.upper()
# Ejecutar cursor
cursor.execute(sqlupdate, (subida, oficiomayus))
# Mostrar mensaje de registros actualizados
print(f"Empleados con incremento: {cursor.rowcount}")
# Cerrar cursor
cursor.close()
# Consulta a la tabla de empleados
sqlselect = "select apellido, oficio, salario from emp where oficio = :p1"
# Crear cursor
cursor = conn.cursor()
# Ejecutar cursor
cursor.execute(sqlselect, (oficiomayus,))
# Mostrar datos recuperados
for apellido, oficio, salario in cursor:
    print(f"Apellido: {apellido}, Oficio: {oficio}, Salario: {salario}")
# Cerrar cursor
cursor.close()
# Confirmar cambios en base de datos
conn.commit()
# Desconexión con base de datos
conn.close()
