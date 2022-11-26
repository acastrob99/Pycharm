import sys
import MySQLdb
import psycopg2
import basededatos.utils.config_bbdd as conf
import logging as log


log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/carrera_caballos.log'),
                    log.StreamHandler()
                ])

def get_mysql_conection():
    return get_conection()


def get_conection(db=conf.BD_MYSQL, maquina=conf.BD_MAQUINA, usuario=conf.BD_USER, password=conf.BD_PASS, base_datos=conf.BD_BASE_DATOS,
                  puerto=conf.BD_PUERTO):
    try:
        if db == "mysql":
            conection = MySQLdb.connect(
                host=maquina,
                user=usuario,
                passwd=password,
                db=base_datos,
                port=puerto)
        else:
            conection = psycopg2.connect(
                user=usuario,
                password=password,
                host=maquina,
                port=puerto,
                database=base_datos
            )
    except MySQLdb.Error as mysqle:
        log.ERROR("No puedo conectar a la base de datos:", mysqle)

    except Exception as e:
        log.ERROR("No puedo conectar a la base de datos:", e)

    else:
        log.debug("Conexión correcta.")

    return conection
