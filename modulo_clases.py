# hospital
# Doctores 2 --nombre, apleiido, dni , especialidad y tienen q fichar cuando empieze y cuando acabe
# Enfermeros igual que doctores menos especialidad y mas planta
# Pacientes  nombre apellidos dni y sintoma
# Enfermos nombre tal tal y enfermedad(aleatoria de una lista)
# hospital tiene sala de espera -- con 4 pacientes q entran en la sala de espera
# dos consultas en cada consulta un doctor
# enfermeros atiende al paciente(es decir lleva al paciente a la consulta) y cuando esta en la consulta lo diagnostica(de manera aleatoria se genera una enfermedad o nada si sale mas de 7 enfermo si sale menos se va a casa)
# si se genera mas de 7 el paciente pasa a enfermos y le pasamos a una habitacion
# habitaciones 3 si hay 4 enfermos y no entran el ultimo en entrar es derivado a otro hospital

# 6 clases 1 hospital y persona de la cual derivan (doctor,enfermero,paciente,enfermo) y otras clases (consulta,sala_espera,habitacion)

import random


class hospital:

    def __init__(self, doctores, enfermeros, salas_espera, consultas, habitaciones):
        self.doctor = doctores
        self.enfermeros = enfermeros
        self.pacientes = []
        self.enfermos = []
        self.salas_espera = salas_espera
        self.consultas = consultas
        self.habitaciones = habitaciones

    def atender_pacientes(self):
        while (self.hay_pacientes() > 0):  # miramos si hay pacientes en la sala de espera
            for consulta in self.consultas:  # recorremos las consultas
                for enfermero in self.enfermeros:  # recorremos enfermeros para atender a pacientes
                    if self.hay_pacientes() > 0:
                        paciente = self.pacientes.pop(
                            0)  # guardamos en paciente el paciente posicion 0 y lo borramos de los pacientes en sala de espera
                        consulta.paciente = paciente  # guardamos en consulta el paciente que esta siendo atendido
                        print("El enfermero {} ha llevado al paciente {} a la consulta {}".format(enfermero.nombre,
                                                                                                  paciente.nombre,
                                                                                                  consulta.id))
                        if consulta.id == 1:  # si la consulta es la uno le atendera el doctor1
                            enfermo = self.doctor[0].diagnosticar_paciente(self.doctor[0],
                                                                           paciente)  # diagnostica al paciente y devuelve el paciente para que le pasemos a enfermo o devuelve none
                            if enfermo != None:  # si es diferente none es que al paciente se le ha mandado a casa si no añadimos el paciente a enfermo
                                self.enfermos.append(
                                    enfermo)  # añadimos a la lista de enfermos el nuevo paciente que ha sido diagnosticado enfermo

                        else:
                            enfermo = self.doctor[1].diagnosticar_paciente(self.doctor[1],
                                                                           paciente)  # si es la consulta 2 hara lo mismo que en el if anterior
                            if enfermo != None:
                                self.enfermos.append(enfermo)
                    else:
                        print("No quedan pacientes por atender")

                    self.llevar_habitacion()  # llevamos los enfermos a la habitacion

    def llevar_habitacion(self):
        for habitacion in self.habitaciones:  # recorremos habitaciones para ver si estan vacias
            for enfermo in self.enfermos:  # recorremos enfermos para ver si tienen asignados una habitacion
                if habitacion.ocupada == True or enfermo.habitacion != None:  # si la habitacion esta ocupada o el enfermo tiene asignada una habitacion no hara nada
                    pass
                else:  # en caso contrario es que una habitacion esta libre para el enfermo
                    habitacion.enfermo = enfermo  # asignamos a una habitacion el enfermo
                    habitacion.ocupada = True  # cambiamos el valor de la habitacion ocupada a true
                    enfermo.habitacion = habitacion.id  # asignamos al enfermo una habitacion
                    print("el enfermo {} ha sido mandado a la habitacion {}".format(enfermo.nombre, habitacion.id))

        for enfermo in self.enfermos:  # recorremos los enfermos a ver cual se ha quedado sin habitacion
            if enfermo.habitacion == None:
                print("Habitaciones llenas se ha mandado al paciente {} a otro hospital".format(enfermo.nombre))

    def hay_pacientes(self):  # miramos si hay pacientes en la sala de espera
        if len(self.salas_espera.pacientes) > 0:
            return len(self.salas_espera.pacientes)  # retornamos el numero de pacientes a espera
        else:
            print("No hay pacientes en la sala de espera")
            return 0


class sala_espera:  # una sala de espera donde estan los 4 pacientes y son llamados a la consulta por orden

    def __init__(self, id, huecos_disponibles):
        self.id = id
        self.hueco_disponible = huecos_disponibles
        self.pacientes = []


class consulta:

    def __init__(self, id, doctor):
        self.id = id
        self.doctor = doctor
        self.paciente = None


class habitacion:

    def __init__(self, id, ocupada=False):
        self.id = id
        self.ocupada = ocupada
        self.enfermo = None


class persona:  # creamos la clase de la cual derivan doctor,paciente,enfermero y enfermo

    def __init__(self, nombre, apellidos, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni


class doctor(persona):

    def __init__(self, nombre, apellidos, dni, especialidad):
        persona.__init__(self, nombre, apellidos, dni)
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.especialidad = especialidad

    def fichar(self,entrada):
        if entrada == "entrada":
            print("El doctor {} ha fichado el principio de su jornada laboral".format(self.nombre))
            
        elif entrada == "salida":
            print("El doctor {} ha fichado el final de su jornada laboral".format(self.nombre))

    def diagnosticar_paciente(self, doctor, paciente):  # diagnosticamos pacientes
        num_random = random.randrange(1,
                                      10)  # generamos numero random si es mayor de 7 le asignamos una enfermedad si no a casa a reposar
        if num_random > 0:
            enfermedad_random = random.randrange(0,
                                                 3)  # elegir una enfermedad aleatoria de la lista de enfermedades creada en el main
            enfermo1 = enfermo(paciente.nombre, paciente.apellidos, paciente.dni,
                               enfermedad_random)  # creamos un objeto de la clase enfermo para luego añadirlo a la lista de enfermos del hospital
            print("El doctor {} ha diagnosticado al paciente {} la enfermedad de {}".format(doctor.nombre,
                                                                                            paciente.nombre,
                                                                                            paciente.enfermedades[
                                                                                                random.randrange(0,
                                                                                                                 3)]))
            return enfermo1
        else:
            "Se le ha mandado unas pastillas al paciente y ha sido mandado a casa"
            return None


class enfermero(persona):

    def __init__(self, nombre, apellidos, dni, planta):
        persona.__init__(self, nombre, apellidos, dni)
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.planta = planta


class paciente(persona):

    def __init__(self, nombre, apellidos, dni, sintomas, enfermedades):
        persona.__init__(self, nombre, apellidos, dni)
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.sintomas = sintomas
        self.enfermedades = enfermedades


class enfermo(persona):

    def __init__(self, nombre, apellidos, dni, enfermedad):
        persona.__init__(self, nombre, apellidos, dni)
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.enfermedad = enfermedad
        self.habitacion = None