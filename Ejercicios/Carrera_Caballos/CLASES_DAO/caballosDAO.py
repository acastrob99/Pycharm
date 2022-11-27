from Ejercicios.Carrera_Caballos.CONEXION_BBDD.conexiones import get_mysql_conection
import logging as log
from Ejercicios.Carrera_Caballos.CLASES_POJO.caballos import *


log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/carrera_caballos.log'),
                    log.StreamHandler()
                ])

class caballosDAO:

    _CREAR_TABLA =  'CREATE TABLE Caballos(Id_Caballo MEDIUMINT NOT NULL AUTO_INCREMENT,Nombre CHAR(30) NOT NULL,Fecha_Nac DATETIME NOT NULL,' \
                     'Velocidad MEDIUMINT  NOT NULL, Experiencia MEDIUMINT NOT NULL,Valor_Apuesta MEDIUMINT NOT NULL, Id_Gran_Premio MEDIUMINT NOT NULL, PRIMARY KEY (Id_Caballo),INDEX (Id_Gran_Premio),FOREIGN KEY (Id_Gran_Premio) REFERENCES gran_premio(Id_Gran_Premio));'
    _SELECCIONAR = 'SELECT Id_Caballo,Nombre,Fecha_Nac,Velocidad,Experiencia,Valor_Apuesta,Id_Gran_Premio FROM Caballos ORDER BY Id_Caballo'
    _INSERTAR = 'INSERT INTO Caballos(Nombre,Fecha_Nac,Velocidad,Experiencia,Valor_Apuesta,Id_Gran_Premio) VALUES(%s,%s,%s,%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE Caballos SET Nombre=%s, Fecha_Nac=%s, Velocidad=%s, Experiencia=%s, Valor_Apuesta=%s, Id_Gran_Premio=%s WHERE Id_Caballo=%s'
    _ELIMINAR = 'DELETE FROM Caballos WHERE Id_Caballo=%s'

    @classmethod
    def crear_tabla(cls):
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._CREAR_TABLA)
                conexion.commit()
        log.info("Tabla creada correctamente")

    @classmethod
    def seleccionar(cls):
        conexion = get_mysql_conection()
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                list_caballos = []
                for registro in registros:
                    caballo = caballos(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6])
                    list_caballos.append(caballo)
                return list_caballos

    @classmethod
    def insertar(cls,caballo):
        conexion = get_mysql_conection()
        with conexion.cursor() as cursor:
            valores = (caballo.Nombre,caballo.Fecha_Nac,caballo.Velocidad,caballo.Experiencia,caballo.Valor_Apuesta,caballo.Id_Gran_Premio)
            cursor.execute(cls._INSERTAR,valores)
            log.info(f'caballos insertados: {caballo.Nombre}')
            conexion.commit()
            return cursor.rowcount

    @classmethod
    def actualizar(cls, caballo):
        conexion = get_mysql_conection()
        with conexion.cursor() as cursor:
            valores = (caballo.Nombre,caballo.Fecha_Nac,caballo.Velocidad,caballo.Experiencia,caballo.Valor_Apuesta,caballo.Id_Gran_Premio,caballo.Id)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.info(f'tabla caballos actualizada: Nombre: {caballo.Nombre}, Fecha_Nac:{caballo.Fecha_Nac}')
            conexion.commit()
            return cursor.rowcount



if __name__ == "__main__":
    pass
    # caballosDAO.crear_tabla()                        #creamos la tabla apostantes
    # caballos.crear_caballos_fichero()              #creamos objetos de la clase apostantes a partir de un fichero
    # for caballo in caballos._LIST_CABALLOS:           #recorremos la lista de objetos apostantes y añadamimos cada un a un registro de la base de datos en la tabla apostantes
    #      caballosDAO.insertar(caballo)                   #los añadimos
    #print(caballosDAO.seleccionar()[0][2])               #selecionamos la lista de apostantes de base de datos y mostramos el primero
    # caballos = caballosDAO.seleccionar()
    # for caballo in caballos:
    #     print(caballo.Nombre)
    #         print(dato)
    #caballo2 = caballos(1,"caballopepe","2007-3-19",33,22,4,2)      #creamos un apostante a mano y le pasamos los valores para que los actualize segun el id que le pases
    #caballosDAO.actualizar(caballo2)              ##llamamaos a la funcion y le pasamos el apostante

