import oracledb
from os import system


def items_menu(tabla, campo):
    # Conexión con base de datos
    conn = oracledb.connect(
        user="system",
        password="oracle",
        dsn="localhost:1521/xe"
    )
    sqlselect = f"select distinct {campo} from {tabla}"
    print(sqlselect)
    # Creamos cursor
    cursor = conn.cursor()
    # Ejecutamos cursor
    cursor.execute(sqlselect)
    # Inicializamos lista resultado
    items = []
    # Guardamos los datos en una lista
    for dato in cursor:
        items.append(dato[0])
    # Cerramos cursor
    cursor.close()
    # Cerramos conexión
    conn.close()
    # Devolvemos la lista resultado
    return items


def print_menu(lista):
    system("clear")
    linea = " -----------------------"
    print(linea)
    print("| Seleccione una opción |")
    print(linea)
    for i in range(len(lista)):
        print(f"| {i} - {lista[i]:17} |")
    print(linea, "\n")


def main():
    print_menu(items_menu("emp", "oficio"))


main()
