import logging as log
import random

from Ejercicios.Carrera_Caballos.ficheros.funciones_ficheros import *
from datetime import datetime
from datetime import date
from datetime import timedelta


log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/carrera_caballos.log'),
                    log.StreamHandler()
                ])


class caballos:

    _LIST_CABALLOS = []  # lista de apostantes que luego utilizaremos para insertar en la base de datos

    def __init__(self,Id,Nombre,Fecha_Nac,Velocidad,Experiencia,Valor_Apuesta,Id_Gran_Premio):
        self._Id = Id
        self._Nombre = Nombre
        self._Fecha_Nac = Fecha_Nac
        self._Velocidad = Velocidad
        self._Experiencia = Experiencia
        self._Valor_Apuesta = Valor_Apuesta
        self._Id_Gran_Premio = Id_Gran_Premio
        self._Distancia_Carrera = 0


    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, id):
        self._Id = id

    @property
    def Nombre(self):
        return self._Nombre

    @Nombre.setter
    def Nombre(self,nombre):
        self._Nombre = nombre

    @property
    def Fecha_Nac(self):
        return self._Fecha_Nac

    @Fecha_Nac.setter
    def Fecha_Nac(self, fecha_Nac):
        self._Fecha_Nac = fecha_Nac

    @property
    def Velocidad(self):
        return self._Velocidad

    @Velocidad.setter
    def Velocidad(self, velocidad):
        self._Velocidad = velocidad

    @property
    def Experiencia(self):
        return self._Experiencia

    @Experiencia.setter
    def Experiencia(self, experiencia):
        self._Experiencia = experiencia

    @property
    def Valor_Apuesta(self):
        return self._Valor_Apuesta

    @Valor_Apuesta.setter
    def Valor_Apuesta(self, valor_Apuesta):
        self._Valor_Apuesta = valor_Apuesta

    @property
    def Id_Gran_Premio(self):
        return self._Id_Gran_Premio

    @Id_Gran_Premio.setter
    def Id_Gran_Premio(self, id_Gran_Premio):
        self._Id_Gran_Premio = id_Gran_Premio

    @property
    def Distancia_Carrera(self):
        return self._Distancia_Carrera

    @Distancia_Carrera.setter
    def Distancia_Carrera(self, distancia_carrera):
        self._Distancia_Carrera = distancia_carrera

    def calcular_edad(self):
        #año_caballo = int(self._Fecha_Nac.split('-')[0])
        año_caballo = int(self._Fecha_Nac.year)
        hoy = int(datetime.now().year)
        return hoy - año_caballo


    def correr(self):            #retorna un valor que se añadira a la distancia recorrida por el caballo en la carrera
        return self.Velocidad+self.Experiencia-self.calcular_edad()+random.randint(1,50)
    @classmethod
    def sumar_exp_caballo(cls,list_caballos,gran_p,caballo_ganador):
        for caballo in list_caballos:
            caballo.Distancia_Carrera = 0
            if caballo.Id_Gran_Premio == gran_p.Id and caballo_ganador is not caballo:
                caballo.Experiencia = caballo.Experiencia + 1
            elif caballo.Id_Gran_Premio == gran_p.Id:
                caballo_ganador.Experiencia = caballo.Experiencia + 5


    @classmethod
    def crear_caballos_fichero(cls):  # creamos los apostantes sacandolos de un fichero
        fich_caballos = ficheros.caballos  # elegimos el fichero
        list_caballos = ficheros.leer_fichero(fich_caballos)  # creamos una lista de caballos extraidos en el metodo leer.fichero de la clase ficheros pasando el fichero

        for caballo in list_caballos:  # recorremos caballos
            obj_caballo = caballos(caballo[0], caballo[1][0],caballo[1][1],caballo[1][2],caballo[1][3],caballo[1][4],caballo[1][5]) #creamos el objeto
            caballos._LIST_CABALLOS.append(obj_caballo)# añadimos objeto a la lista de objetos caballos
            #primero crear gran premio para que la foreing key no de error


    @classmethod
    def mostrar_caballos_carrera(cls,list_caballos,gran_p): ##muestra una lista con los nombres de caballo para que el apostante pueda ver a que caballos puede apostar
        nombres_caballos = []
        for caballo in list_caballos :
            if caballo.Id_Gran_Premio == gran_p.Id:
                nombres_caballos.append(caballo.Nombre)
        return nombres_caballos



if __name__ == "__main__":
    #pass
    obj_caballo = caballos(1,"Pepe","2007-03-19",34,33,1,1)
    print("ha corrido: ",obj_caballo.correr())





