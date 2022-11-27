from Ejercicios.Carrera_Caballos.CLASES_POJO import apostantes as apos,caballos,gran_premio
from Ejercicios.Carrera_Caballos.CLASES_DAO import apostantesDAO,caballosDAO,gran_premioDAO


def comenzar_carreras(gran_p,list_caballos,apostantes):
    for carrera in range(gran_p.Num_Carreras):
        carrera_apostada = gran_premio.gran_premio.pedir_apuestas(apostantes,gran_p,carrera,list_caballos)
        print("CORRIENDO", gran_p.Nombre,"carrera ",carrera +1)
        terminar_carrera = 0
        caballo_ganador = None
        while terminar_carrera < gran_p.Distancia:
            for caballo in list_caballos:
                if caballo.Id_Gran_Premio == gran_p.Id and terminar_carrera < gran_p.Distancia:
                    caballo.Distancia_Carrera = caballo.Distancia_Carrera + caballo.correr()
                    print(caballo.Nombre, ": ", caballo.Distancia_Carrera)
                    terminar_carrera = caballo.Distancia_Carrera
                    caballo_ganador = caballo

        print("Ganador {} Carrera {} {} {}".format(gran_p.Nombre,carrera+1,caballo_ganador.Nombre,caballo_ganador.Distancia_Carrera))
        caballos.caballos.sumar_exp_caballo(list_caballos,gran_p,caballo_ganador)
        apos.apostantes.sumar_saldo_apostante(apostantes,carrera_apostada,caballo_ganador,carrera)



def actulizar_datos(list_apostantes,list_caballos):          #pinta el saldo final
    for apostante in list_apostantes:
        apostantesDAO.apostantesDAO.actualizar_saldo(apostante.Id,apostante.Saldo)
        print("El saldo de {} es {}".format(apostante.Nombre, apostante.Saldo))
    for cab in list_caballos:
        caballosDAO.caballosDAO.actualizar(cab)
        print("Experiencia del caballo {} es {}".format(cab.Nombre, cab.Experiencia))



def comenzar_gran_premio():
    list_grandes_p = gran_premioDAO.gran_premioDAO.seleccionar() #lista de grandes premios
    list_caballos = caballosDAO.caballosDAO.seleccionar()              #lista de caballos
    list_apostantes = apostantesDAO.apostantesDAO.seleccionar()        #lista de apostantes

    for gran_p in list_grandes_p:
        comenzar_carreras(gran_p,list_caballos,list_apostantes)

    actulizar_datos(list_apostantes,list_caballos)


if __name__ == "__main__":
    comenzar_gran_premio()