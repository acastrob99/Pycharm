from conexiones import get_mysql_conection


sentencia_insertar = 'INSERT INTO Personas (nombre'


def crear_tabla():
    sentencia_crear_tabla = 'CREATE TABLE Personas(id MEDIUMINT NOT NULL AUTO_INCREMENT,nombre CHAR(30) NOT NULL,apellidos CHAR(30) NOT NULL,email CHAR(30) NOT NULL,PRIMARY KEY (id));'
    try:
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = sentencia_crear_tabla
                cursor.execute(sentencia)
                conexion.commit()
    except Exception as e:
        print(f'Ocurrió un error: {e}')

def insertar():
    sentencia_insertar = 'INSERT INTO Personas (nombre, apellidos, email) VALUES(%s,%s,%s)'
    try:
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = sentencia_insertar
                valores = (
                    ('Nombre1','Apellido1','corre1@gmail.com'),
                    ('Nombre2', 'Apellido2', 'corre1@g.com'),
                    ('Nombre3', 'Apellido3', 'corre1@gmailcom'),
                )
                cursor.executemany(sentencia, valores)
                conexion.commit()
                registros_insertados = cursor.rowcount
                print(f'Registros Insertados: {registros_insertados}')

    except Exception as e:
        print(f'Ocurrió un error: {e}')


def consulta():
    try:
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:
                #sentencia = 'SELECT nombre FROM personas'
                sentencia = 'SELECT nombre, email  FROM personas where email like "%@gmail.com" '
                cursor.execute(sentencia)
                registros = cursor.fetchall()
                print(registros)
                return registros
    except Exception as e:
        print(f'Ocurrió un error: {e}')


def actulizar():
    try:
        new_Value = "%gmail.com"
        to_change = "@gmail.com"
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:

                #valores = ""
                cursor.execute(sentencia)
                conexion.commit()
                registros_actualizados = cursor.rowcount
                print(f'Registros Actualizados: {registros_actualizados}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

def borrar_todo():
    try:
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'DELETE * from Personas'
                cursor.execute(sentencia)
                conexion.commit()
                registros_eliminados = cursor.rowcount
                print(f'Registros Eliminados: {registros_eliminados}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

#insertar()
#consulta()
actulizar()
#borrar_todo()