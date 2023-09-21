from modelo.estudiante import Estudiante

class EstudianteExtranjero(Estudiante):
    def __init__(self, nombre, ci, sexo, carrera, facultad, num_becado, albergue, cuarto, anio, nacionalidad, auto_financiado):
        Estudiante.__init__(self, nombre, ci, sexo, carrera, facultad, num_becado, albergue, cuarto, anio)
        self.__nacionalidad = nacionalidad
        self.__auto_financiado = auto_financiado

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, value):
        self.__nacionalidad = value

    @property
    def auto_financiado(self):
        return self.__auto_financiado

    @auto_financiado.setter
    def auto_financiado(self, value):
        self.__auto_financiado = value

    def es_nacionalidad(self, nacionalidad):
        return self.nacionalidad == nacionalidad
