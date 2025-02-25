# Importamos la librería oracledb
import oracledb


# Definimos la clase para la conexión
class ConexionOracleEnfermos:
    # En el constructor de la clase (__init__) se crea la
    #  conexión a la base de datos.
    def __init__(self):
        self.conn = oracledb.connect(
            user="system",
            password="oracle",
            dsn="localhost:1521/xe"
        )

    # Definimos un método para eliminar un registro de la
    #  table enfermo
    def eliminarEnfermo(self, inscripcion):
        cursor = self.conn.cursor()
        sql = "delete from enfermo where inscripcion = :p1"
        cursor.execute(sql, (inscripcion,))
        registros = cursor.rowcount
        cursor.close()
        self.conn.commit()
        return registros

    # Definimos un método que modifique el apellido de un
    #  enfermo por su inscripción
    def modificarApellido(self, apellido, inscripcion):
        cursor = self.conn.cursor()
        sql = "update enfermo set apellido = :p1 where inscripcion = :p2"
        cursor.execute(sql, (apellido, inscripcion))
        registros = cursor.rowcount
        cursor.close()
        self.conn.commit()
        return registros
