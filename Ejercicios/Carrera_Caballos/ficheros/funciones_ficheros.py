import logging as log
#from Ejercicios.Carrera_Caballos.CLASES_POJO.apostantes import *


log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/carrera_caballos.log'),
                    log.StreamHandler()
                ])


class ficheros:

    fich_apostantes = "../ficheros/apostantes.txt"
    caballos = "../ficheros/caballos.txt"
    grandes_premios = "../ficheros/grandes_premios.txt"

    @classmethod
    def leer_fichero(cls,fichero):
        list_datos = []                                             #lista de datos a retornar lista (id,(nombre,saldo)) lista dentro de otra
        with open(fichero,'r', encoding='utf8') as archivo:         ##leemos fichero que le pasamos al metodo
            contador_id = 1                                         #Contador para los Ids
            for linea in archivo.readlines():                       #Recoremos las lineas en el archivo.txt
                datos = (contador_id),linea.split('|')              #añadimos atributos seprandose en una tupla por el un separador y contador para id en una tupla
                list_datos.append(datos)                            #añadir a la lista de datos el objeto para crear
                contador_id = contador_id + 1                       #se van incrementando el id en 1
            return list_datos                                       # retornamos la lista de datos de los objetos a crear en una lista dentro de otra lista de atributos



if __name__ == "__main__":
    apos = ficheros.leer_fichero(ficheros.grandes_premios)
    print(apos)
    print(type(apos))
    print(apos[0][0],apos[0][1])
    print(apos[1][0],apos[1][1])
    print(apos[2][0],apos[2][1])
