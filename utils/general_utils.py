import random



def generar_aleatorio_booleano (rango_true, inicio=0, fin=10):
    """Método que devuelve true si se obtiene un valor mayor o igual
     a rango_true a partir de un numero aleatorio generado
    entre el inicio (0 por defecto) y el fin (10 por defecto)"""

    aleatorio = random.randint(inicio, fin)
    log.debug("Numero aleatorio: ", aleatorio)
    reply = aleatorio > rango_true
    log.debug("respuesta ", reply)

    return reply

def pide_datos(texto , tipo_a_devolver="str" ):
    #Pedimos información al usuario
    valor_introducido = input (texto)
    if tipo_a_devolver=="str":
        return valor_introducido
    elif tipo_a_devolver=="int":
        if(valor_introducido.isdigit()):
            return int(valor_introducido)
        else:
            print("Valor incorrecto, vuelve a intentarlo")
            return pide_datos(texto,tipo_a_devolver)
