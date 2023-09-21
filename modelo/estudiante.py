from datetime import date


class Estudiante:
    def __init__(self, nombre, ci, sexo, carrera, facultad, num_becado, albergue, cuarto, anio):
        self.__nombre = nombre
        self.__ci = ci
        self.__sexo = sexo
        self.__carrera = carrera
        self.__facultad = facultad
        self.__num_becado = num_becado
        self.__albergue = albergue
        self.__cuarto = cuarto
        self.__anio = anio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def ci(self):
        return self.__ci

    @ci.setter
    def ci(self, value):
        self.__ci = value

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, value):
        self.__sexo = value

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, value):
        self.__carrera = value

    @property
    def facultad(self):
        return self.__facultad

    @facultad.setter
    def facultad(self, value):
        self.__facultad = value

    @property
    def num_becado(self):
        return self.__num_becado

    @num_becado.setter
    def num_becado(self, value):
        self.__num_becado = value

    @property
    def albergue(self):
        return self.__albergue

    @albergue.setter
    def albergue(self, value):
        self.__albergue = value

    @property
    def cuarto(self):
        return self.__cuarto

    @cuarto.setter
    def cuarto(self, value):
        self.__cuarto = value

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, value):
        self.__anio = value

    def __str__(self):
        return self.nombre

    def es_num_becado(self, num_becado):
        return self.num_becado == num_becado

    def es_ci(self, ci):
        return self.ci == ci

    def es_carrera(self, carrera):
        return self.carrera == carrera

    def es_facultad(self, facultad):
        return self.facultad == facultad

    def edad(self):
        hoy = date.today()
        anio_nac = int(self.ci[0:2])
        mes_nac = int(self.ci[2:4])
        dia_nac = int(self.ci[4:6])
        edad = hoy.year - (anio_nac + 1900)
        if edad > 100:
            edad -= 100
        if hoy.month < mes_nac:
            edad -= 1
        elif hoy.month == mes_nac and hoy.day < dia_nac:
            edad -= 1
        return edad

    def __gt__(self, other):
        return self.edad() > other.edad()

    def str_varias_lineas(self):
        return 'Nombre: {}\nCarné de Identidad: {}\nEdad: {}\nSexo: {}\nCarrera: {}\nFacultad: {}\nNúmero de becado: {}\nAlbergue: {}\nCuarto: {}\nAño escolar: {}'.format(
            self.nombre, self.ci, self.edad(), self.sexo, self.carrera, self.facultad, self.num_becado, self.albergue,
            self.cuarto, self.anio)
