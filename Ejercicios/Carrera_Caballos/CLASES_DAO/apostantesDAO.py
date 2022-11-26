from Ejercicios.Carrera_Caballos.CONEXION_BBDD.conexiones import get_mysql_conection
import logging as log
from Ejercicios.Carrera_Caballos.CLASES_POJO.apostantes import *


log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/carrera_caballos.log'),
                    log.StreamHandler()
                ])

class apostantesDAO:

    _CREAR_TABLA = 'CREATE TABLE apostantes(Id_apostante MEDIUMINT NOT NULL AUTO_INCREMENT,Nombre CHAR(30) NOT NULL,Saldo MEDIUMINT NOT NULL,PRIMARY KEY(Id_apostante));'
    _SELECCIONAR = 'SELECT Id_apostante,Nombre,Saldo FROM apostantes ORDER BY Id_apostante'
    _INSERTAR = 'INSERT INTO apostantes(Nombre,Saldo) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE apostantes SET Nombre=%s, Saldo=%s WHERE Id_apostante=%s'
    _ACTUALIZAR_SALDO = 'UPDATE apostantes SET Saldo=%s WHERE Id_apostante=%s'
    _ELIMINAR = 'DELETE FROM apostantes WHERE Id_apostante=%s'

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
                list_apostantes = []
                for registro in registros:
                    apostante = apostantes(registro[0], registro[1], registro[2])
                    list_apostantes.append(apostante)
                return list_apostantes

    @classmethod
    def insertar(cls,apostante):
        conexion = get_mysql_conection()
        with conexion.cursor() as cursor:
            valores = (apostante.Nombre,apostante.Saldo)
            cursor.execute(cls._INSERTAR,valores)
            log.info(f'apostantes insertados: {apostante.Nombre}')
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

    @classmethod
    def actualizar_saldo(cls,id,new_atributo ):
        conexion = get_mysql_conection()
        with conexion.cursor() as cursor:
            valores = (new_atributo,id)
            cursor.execute(cls._ACTUALIZAR_SALDO, valores)
            log.info(f'tabla apostante actualizada')
            conexion.commit()
            return cursor.rowcount

    @classmethod
    def eliminar(cls):
        conexion = get_mysql_conection()
        with conexion.cursor() as cursor:
            cursor.execute(cls._ELIMINAR, 2)
            log.info(f'Objeto eliminado con Id : {3}')
            conexion.commit()
            return cursor.rowcount




if __name__ == "__main__":

    # apostantesDAO.crear_tabla()                        #creamos la tabla apostantes
    # apostantes.crear_apostantes_fichero()              #creamos objetos de la clase apostantes a partir de un fichero
    # for apos in apostantes._LIST_APOSTANTES:           #recorremos la lista de objetos apostantes y añadamimos cada un a un registro de la base de datos en la tabla apostantes
    #      apostantesDAO.insertar(apos)                   #los añadimos
    #print(apostantesDAO.seleccionar()[0].Nombre)               #selecionamos la lista de apostantes de base de datos y mostramos el primero
    #apostante2 = apostantes(1, "Alvaro", 300)         #creamos un apostante a mano y le pasamos los valores para que los actualize segun el id que le pases
    #apostantesDAO.actualizar(apostante2)              ##llamamaos a la funcion y le pasamos el apostante
    #apostantesDAO.actualizar_saldo(1,5000)
    apostantesDAO.eliminar()



#joseluis.llorenteperales@gmail.com
