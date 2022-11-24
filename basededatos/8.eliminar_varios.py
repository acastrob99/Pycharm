from utils.conexiones import get_mysql_conection
from datetime import datetime
try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM productos WHERE id IN %s'
            entrada = input('Proporciona los ids a eliminar (separados por coma): ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            conexion.commit()
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
