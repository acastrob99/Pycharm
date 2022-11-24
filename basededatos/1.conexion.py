from utils.conexiones import get_mysql_conection

conexion = None
try:
    conexion = get_mysql_conection()
    cursor = conexion.cursor()
    sentencia = 'SELECT * FROM productos'
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    print(registros)

except Exception as e:
    print("Error", e )
finally:
    cursor.close()
    conexion.close()
    print("Fin")
