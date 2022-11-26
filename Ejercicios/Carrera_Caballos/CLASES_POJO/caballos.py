import logging as log
from Ejercicios.Carrera_Caballos.ficheros.funciones_ficheros import *


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

    @classmethod
    def crear_caballos_fichero(cls):  # creamos los apostantes sacandolos de un fichero
        fich_caballos = ficheros.caballos  # elegimos el fichero
        list_caballos = ficheros.leer_fichero(fich_caballos)  # creamos una lista de caballos extraidos en el metodo leer.fichero de la clase ficheros pasando el fichero


        for caballo in list_caballos:  # recorremos apostantes
            obj_caballo = caballos(caballo[0], caballo[1][0],caballo[1][1],caballo[1][2],caballo[1][3],caballo[1][4],caballo[1][5]) #creamos el objeto
            caballos._LIST_CABALLOS.append(obj_caballo)# añadimos objeto a la lista de objetos caballos
            #primero crear gran premio para que la foreing key no de error



if __name__ == "__main__":
    pass



