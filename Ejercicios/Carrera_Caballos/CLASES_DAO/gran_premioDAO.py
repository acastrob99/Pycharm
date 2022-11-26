from Ejercicios.Carrera_Caballos.CONEXION_BBDD.conexiones import get_mysql_conection
import logging as log
from Ejercicios.Carrera_Caballos.CLASES_POJO.gran_premio import *


log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/carrera_caballos.log'),
                    log.StreamHandler()
                ])

class gran_premioDAO:

    _CREAR_TABLA = 'CREATE TABLE Gran_Premio(Id_Gran_Premio MEDIUMINT NOT NULL AUTO_INCREMENT,Nombre CHAR(30) NOT NULL,Distancia MEDIUMINT NOT NULL,' \
                         'Num_Carreras MEDIUMINT  NOT NULL,PRIMARY KEY (Id_Gran_Premio));'

    _SELECCIONAR = 'SELECT Id_Gran_Premio,Nombre,Distancia,Num_Carreras FROM Gran_Premio ORDER BY Id_Gran_Premio'
    _INSERTAR = 'INSERT INTO Gran_Premio(Nombre,Distancia,Num_Carreras) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE Gran_Premio SET Nombre=%s, Distancia=%s, Num_Carreras=%s WHERE Id_Gran_Premio=%s'
    _ELIMINAR = 'DELETE FROM Gran_Premio WHERE Id_Gran_Premio=%s'

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
                list_gran_premio = []
                for registro in registros:
                    gran_pre = gran_premio(registro[0], registro[1], registro[2],registro[3])
                    list_gran_premio.append(gran_pre)
                return list_gran_premio

    @classmethod
    def insertar(cls,gran_premio):
        conexion = get_mysql_conection()
        with conexion.cursor() as cursor:
            valores = (gran_premio.Nombre,gran_premio.Distancia,gran_premio.Num_Carreras)
            cursor.execute(cls._INSERTAR,valores)
            log.info(f'apostantes insertados: {gran_premio.Nombre}')
            conexion.commit()
            return cursor.rowcount

    @classmethod
    def actualizar(cls, apostante):
        conexion = get_mysql_conection()
        with conexion.cursor() as cursor:
            valores = (apostante.Nombre,apostante.Saldo,apostante.Id)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.info(f'tabla apostante actualizada: Nombre: {apostante.Nombre}, Saldo:{apostante.Saldo}')
            conexion.commit()
            return cursor.rowcount



if __name__ == "__main__":
    #gran_premioDAO.crear_tabla()            #creamos la tabla gran_premio
    # gran_premio.crear_gran_premio_fichero()              #creamos objetos de la clase apostantes a partir de un fichero
    # for gran in gran_premio._LIST_GRANDES_PREMIOS:           #recorremos la lista de objetos apostantes y añadamimos cada un a un registro de la base de datos en la tabla apostantes
    #      gran_premioDAO.insertar(gran)                   #los añadimos
    print(gran_premioDAO.seleccionar()[0].Nombre)               #selecionamos la lista de apostantes de base de datos y mostramos el primero
    #apostante2 = apostantes(1, "Alvaro", 300)         #creamos un apostante a mano y le pasamos los valores para que los actualize segun el id que le pases
    #apostantesDAO.actualizar(apostante2)              ##llamamaos a la funcion y le pasamos el apostante



#joseluis.llorenteperales@gmail.com
