from utils.conexiones import get_mysql_conection
from datetime import datetime
try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO productos(nombre, precio, fecha_registro) VALUES(%s, %s, %s)'
            valores = (
                ('Producto 10', 1000, datetime.now()),
                ('Producto 11', 5000, datetime.now()),
                ('Producto 12', 10000, datetime.now()),
                ('Producto 13', 600, datetime.now())
            )
            cursor.executemany(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')