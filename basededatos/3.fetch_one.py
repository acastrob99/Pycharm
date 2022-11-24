from utils.conexiones import get_mysql_conection

try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM productos WHERE id = %s'
            id_producto = input('Proporciona el valor id: ')
            cursor.execute(sentencia, id_producto)
            registro = cursor.fetchone()
            print(registro)
except Exception as e:
    print(f'Ocurrió un error: {e}')