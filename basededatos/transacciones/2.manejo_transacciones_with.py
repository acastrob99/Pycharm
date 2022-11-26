from basededatos.utils.conexiones import get_mysql_conection
from datetime import datetime
try:
    conexion = get_mysql_conection()
    with conexion: 
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO productos(nombre, precio, fecha_registro) VALUES(%s, %s, %s)'
            valores = ('Producto', 12314, datetime.now())
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE productos SET nombre=%s, precio=%s, fecha_registro=%s WHERE id=%s'
            valores = ('Producto1234', 21314, datetime.now(), 1)
            cursor.execute(sentencia, valores)

            conexion.commit()
except Exception as e:
    print(f'Ocurrió un error, se hizo rollback: {e}')

print('Termina la transacción, se hizo commit')
    