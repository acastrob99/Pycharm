from clases_colegio import *

#leer achivo.txt y guardar linea a linea separando campos y cada campo lo metemos en la variable de instancia de la clase alumno


colegios = {}
COLEGIO = 0
NOMBRE_ALUM = 1
APELL_ALUM = 2
DNI_ALUM = 3
ASIG_ALUM = 4


with open('datos.txt','r', encoding='utf8') as archivo:
    for linea in archivo:
        datos = linea.split("|")
        #colegio = Colegio(datos[COLEGIO])
        colegio_nom = datos[COLEGIO]
        alumno = Alumno(datos[NOMBRE_ALUM],datos[APELL_ALUM],datos[DNI_ALUM],datos[ASIG_ALUM].split(';'))
        if colegio_nom in colegios:
            colegios[colegio_nom].append(alumno)
        else:
            colegios[colegio_nom] = [alumno]
















