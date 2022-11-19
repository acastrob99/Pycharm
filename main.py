from modulo_clases import *

#METEMOS VALORES A CADA UNO DE LOS OBJETOS

doctor1 = doctor("Pepe","Lopez Garcia","1111A","Medico_General")
doctor2 = doctor("Javier","Martinez Garrido","2222B","Medico_General")
doctores = [doctor1,doctor2]
enfermero1 = enfermero("Enrique","Calvo Garcia","3333C","Planta1")
enfermero2 = enfermero("Paco","Perez Lopez","4444D","Planta2")
enfermeros = [enfermero1,enfermero2]
enfermedades = ["Covid","Anginas","Gastronteritis","Migrañas"]
paciente1 = paciente("Luis","Martos Lopez","5555E","Dolor de cabeza",enfermedades)
paciente2 = paciente("Chema","Canovas Garcia","6666F","Migrañas",enfermedades)
paciente3 = paciente("Lucas","Martinez Pozo","7777G","Dolor de cabeza",enfermedades)
paciente4 = paciente("Ana","Rodriguez Moranchel","8888H","Dolor de garganta",enfermedades)
pacientes = [paciente1,paciente2,paciente3,paciente4]
sala_espera1 = sala_espera(1,4)
sala_espera1.pacientes = pacientes
consulta1 = consulta(1,doctor1)
consulta2 = consulta(2,doctor2)
consultas = [consulta1,consulta2]
habitacion1 = habitacion(1)
habitacion2 = habitacion(2)
habitacion3 = habitacion(3)
habitaciones = [habitacion1,habitacion2,habitacion3]
hospital1 = hospital(doctores,enfermeros,sala_espera1,consultas,habitaciones)
hospital1.pacientes = pacientes
hospital1.salas_espera.pacientes = pacientes #metemos los pacientes en la sala de espera
hospital1.salas_espera.hueco_disponible = sala_espera1.hueco_disponible - len(sala_espera1.pacientes)
doctor1.fichar("entrada")
doctor2.fichar("entrada")
hospital1.atender_pacientes()
doctor1.fichar("salida")
doctor2.fichar("salida")






