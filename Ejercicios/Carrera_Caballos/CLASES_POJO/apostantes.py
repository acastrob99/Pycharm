import logging as log
from Ejercicios.Carrera_Caballos.ficheros.funciones_ficheros import *


log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/carrera_caballos.log'),
                    log.StreamHandler()
                ])


class apostantes:

    _LIST_APOSTANTES = []   #lista de apostantes que luego utilizaremos para insertar en la base de datos


    def __init__(self,Id,Nombre,Saldo):
        self._Id = Id
        self._Nombre = Nombre
        self._Saldo = Saldo



    @property
    def Id(self):
        return self._Id

    @property
    def Nombre(self):
        return self._Nombre

    @Nombre.setter
    def Nombre(self,nombre):
        self._Nombre = nombre

    @property
    def Saldo(self):
        return self._Saldo

    @Saldo.setter
    def Saldo(self, saldo):
        self._Saldo = saldo

    @classmethod
    def crear_apostantes_fichero(cls):                              #creamos los apostantes sacandolos de un fichero
        #fich_apostantes = "../ficheros/apostantes.txt"
        fich_apostantes = ficheros.fich_apostantes                  #elegimos el fichero
        list_apostantes = ficheros.leer_fichero(fich_apostantes)    #creamos una lista de apostantes extraidos en el metodo leer.fichero de la clase ficheros

        for apostante in list_apostantes:                                                       #recorremos apostantes
            obj_apostante = apostantes(apostante[0], apostante[1][0], apostante[1][1])          #instaciamos un objeto de apostantes con datos del fichero
            apostantes._LIST_APOSTANTES.append(obj_apostante)                                   #añadimos los apostantes a la lista de objetos










if __name__ == "__main__":
    apostantes.crear_apostantes_fichero()
    for apos in apostantes._LIST_APOSTANTES:
        print(apos.Nombre)





