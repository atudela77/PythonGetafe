import oracledb
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
sqlturnos = """
    select distinct
        turno,
        case turno
        when 'T' then 'Tarde'
        when 'M' then 'Mañana'
        when 'N' then 'Noche'
        else 'Vacio' end
    from plantilla
"""
cursor = conn.cursor()
cursor.execute(sqlturnos)
contador = 1
lista_turnos = []
for turno in cursor:
    print(f"{contador} - {turno[1]}")
    contador += 1
    lista_turnos.append(turno[0])
print("Seleccione una opción")
opcion = int(input()) - 1
cursor.close()
sqlplantilla = """
    select empleado_no, apellido, funcion, salario
    from plantilla
    where turno = :p1
"""
cursor = conn.cursor()
cursor.execute(sqlplantilla, (lista_turnos[opcion],))
for num, ape, fun, sal in cursor:
    print(f"Número empleado: {num:8} Apellido: {ape.title():16} Función: "
          f"{fun:16} Salario: {sal:10}")
cursor.close()
conn.close()
