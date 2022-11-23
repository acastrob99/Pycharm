# import utils.logging_general as log

import logging as log
import random
from abc import ABC, abstractmethod

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('logs/instrumentos.log'),
                    log.StreamHandler()
                ])


class Instrumento(ABC):
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo
        self._afinado = False

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre


    @abstractmethod #implementar en hijas para que funcione
    def afinar(self):
        print("afinando {}".format(self._nombre))  # log.warn
        num_random = random.randint(1, 10)
        if num_random > 5:
            self._afinado = True
        else:
            self._afinado = False

    def tocar(self):
        print("tocando {}".format(self._nombre))
        if self._afinado == False:
            raise Exception("{} mal afinado".format(self._nombre))


class Guitarra(Instrumento):

    def __init__(self, nombre, tipo, num_cuerdas):
        super().__init__(nombre=nombre, tipo=tipo)
        self._num_cuerdas = num_cuerdas


class Guitarra_Electrica(Guitarra):

    def __init__(self, nombre, tipo, num_cuerdas, potencia):
        Guitarra.__init__(self,nombre=nombre, tipo=tipo, num_cuerdas=num_cuerdas)
        self._potencia = potencia


class Piano(Instrumento):
    def __init__(self, nombre, tipo, num_teclas):
        super().__init__(nombre=nombre, tipo=tipo)
        self._num_teclas = num_teclas


class Tambor(Instrumento):
    def __init__(self, nombre, tipo, tamanio):
        super().__init__(nombre=nombre, tipo=tipo)
        self._tamanio = tamanio

    def aporrear(self):
        print("aporreando {}".format(self._nombre))
        if self._afinado == False:
            raise Exception("{} mal afinado".format(self._nombre))


class Orquesta:

    def __init__(self):
        self._instrumentos = []  # meter set

    # @set
    def crear_orquesta(self):
        guitarra1 = Guitarra("guitarra1", "guiatarra_esp", 5)
        guitarra_electrica1 = Guitarra_Electrica("guitarra_electrica1", "guiatarra_elec_roja",5,100)
        piano1 = Piano("piano1", "piano_mediano", 30)
        tambor1 = Tambor("tambor1", "tambor", "500cm")

        self._instrumentos.append(guitarra1)
        self._instrumentos.append(guitarra_electrica1)
        self._instrumentos.append(piano1)
        self._instrumentos.append(tambor1)
        log.warning("Orquesta creada correctamente")


    def iniciar_concierto(self):  # dar una vuelta a decoradores
        for instrumento in self._instrumentos:
            instrumento.afinar()
            try:
                if instrumento._tipo == "tambor":
                    instrumento.aporrear()
                else:
                    instrumento.tocar()
            except Exception as e:
                log.error(e)
            else:
                pass



orquesta1 = Orquesta()
orquesta1.crear_orquesta()
orquesta1.iniciar_concierto()






