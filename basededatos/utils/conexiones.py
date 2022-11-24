import sys
import MySQLdb
import psycopg2
import basededatos.utils.config_bbdd as conf


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
        print("No puedo conectar a la base de datos:", mysqle)

    except Exception as e:
        print("No puedo conectar a la base de datos:", e)

    else:
        print("Conexión correcta.")

    return conection
