# Guardar en objetos
# Generar archivos con el nombre del colegio con los datos de los alumnos de cada colegio


class Colegio:
    def __init__(self,nombre):
        self._nombre = nombre
        self._alumno = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def alumno(self):
        return self._alumno

    @alumno.setter
    def alumno(self,alumno):
        self._alumno = alumno


class Alumno:
    def __init__(self,nombre,apellidos,dni,asignaturas):
        self._nombre = nombre
        self._apellidos = apellidos
        self._dni = dni
        self._asignaturas = asignaturas

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def alumno(self, nombre):
        self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def asignaturas(self):
        return self._asignaturas

    @asignaturas.setter
    def asignaturas(self, asignaturas):
        self._asignaturas = asignaturas


