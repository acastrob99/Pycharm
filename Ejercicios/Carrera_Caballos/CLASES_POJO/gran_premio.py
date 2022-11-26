import logging as log
from Ejercicios.Carrera_Caballos.ficheros.funciones_ficheros import *


log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/carrera_caballos.log'),
                    log.StreamHandler()
                ])


class gran_premio:

    _LIST_GRANDES_PREMIOS = []  # lista de grandes premios que luego utilizaremos para insertar en la base de datos

    def __init__(self,Id,Nombre,Distancia,Num_Carreras):
        self._Id = Id
        self._Nombre = Nombre
        self._Distancia = Distancia
        self._Num_Carreras = Num_Carreras

    @property
    def Id(self):
        return self.Id()

    @property
    def Nombre(self):
        return self._Nombre

    @Nombre.setter
    def Nombre(self,nombre):
        self._Nombre = nombre

    @property
    def Distancia(self):
        return self._Distancia

    @Distancia.setter
    def Distancia(self, distancia):
        self._Distancia = distancia

    @property
    def Num_Carreras(self):
        return self._Num_Carreras

    @Num_Carreras.setter
    def Num_Carreras(self, num_Carreras):
        self._Num_Carreras = num_Carreras

    @classmethod
    def crear_gran_premio_fichero(cls):  # creamos los apostantes sacandolos de un fichero
        ficha_gran_premio = ficheros.grandes_premios  # elegimos el fichero
        list_gran_premio = ficheros.leer_fichero(ficha_gran_premio)  # creamos una lista de caballos extraidos en el metodo leer.fichero de la clase ficheros pasando el fichero

        for gran in list_gran_premio:  # recorremos apostantes
            obj_gran_premio = gran_premio(gran[0], gran[1][0], gran[1][1], gran[1][2])  # metemos los demas atributos de caballos
            print(obj_gran_premio.Num_Carreras)
            gran_premio._LIST_GRANDES_PREMIOS.append(obj_gran_premio)  # instaciamos un objeto de apostantes con datos del fichero


if __name__ == "__main__":
    gran_premio.crear_gran_premio_fichero()





