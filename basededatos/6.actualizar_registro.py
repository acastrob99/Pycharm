from utils.conexiones import get_mysql_conection
from datetime import datetime
try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE productos SET nombre=%s, precio=%s, fecha_registro=%s WHERE id=%s'
            valores = ('Otro Prodcuto', 15000, datetime.now(), 1)
            cursor.execute(sentencia, valores)
            conexion.commit()
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')