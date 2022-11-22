from abc import ABC, abstractmethod
from utils.general_utils import pide_datos
import logging as log
import random
from TemperatureException import TemperatureException, TooHotTemperatureException,TooColdTemperatureException


log.basicConfig(filename='logs/Bar_Cafe.log', encoding='utf-8', level=log.DEBUG)

class TazaCafe:
    def __init__(self,tipocafe,temperatura):
        self.tipocafe = tipocafe
        self.temperatura = temperatura

class Persona(ABC):
    def __init__(self,nombre):
        self.nombre = nombre

class Cliente(Persona):
    def __init__(self,nombre):
        super().__init__(nombre = nombre)
    
    def tomar_taza(self,tazacafe):
        log.info("El cliente {} se ha tomado la taza de cafe".format(self.nombre))
        try:
            if tazacafe.temperatura >70:
                log.info("El cliente {} ha dicho que el cafe estaba muy caliente".format(self.nombre))
                raise TooHotTemperatureException("Cafe muy caliente")
            else:
                log.info("El cliente {} ha dicho que el cafe estaba muy frio".format(self.nombre))
                raise TooColdTemperatureException("Cafe muy frio")
        except ZeroDivisionError as e:
            print(f'ZeroDivisionError - Ocurrió un error: {e} , {type(e)}')
        except TypeError as e:
            print(f'TypeError - Ocurrió un error: {e} , {type(e)}')
        except Exception as e:
            print(f'Exception - Ocurrió un error: {e} , {type(e)}')
        else:
            print('No se arrojó ninguna excepción')
        finally:
            print('Ejecución del bloque finally')


class Camarero(Persona):
    def __init__(self,nombre):
        super().__init__(nombre = nombre)

    def servir_taza(self,tazacafe,cliente):
        pass
        log.info("Se ha servido el cafe")


class Bar:
    def __init__(self,cliente,camarero):
        self.cliente = cliente
        self.camarero = camarero
    
    def atender_cliente(self,camarero,cliente):
        tipo_cafe = pide_datos("Preguntar al cliente como quiere el cafe: {}  :".format(tipos_cafe))
        taza_cafe = TazaCafe(tipo_cafe,random.randint(1,100))
        camarero.servir_taza(taza_cafe,cliente)
        cliente.tomar_taza(taza_cafe)



tipos_cafe = ["CafeSolo","CafeConLeche","Cortado"]
cliente1 = Cliente("Pepe")
camarero1 = Camarero("Carlos")
bar1 = Bar(cliente1,camarero1)
bar1.atender_cliente(camarero1,cliente1)
