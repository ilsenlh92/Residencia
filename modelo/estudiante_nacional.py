from modelo.estudiante import Estudiante


class EstudianteNacional(Estudiante):
    def __init__(self, nombre, ci, sexo, carrera, facultad, num_becado, albergue, cuarto, anio, direccion,
                 tiene_contrato):
        Estudiante.__init__(self, nombre, ci, sexo, carrera, facultad, num_becado, albergue, cuarto, anio)
        self.__direccion = direccion
        self.__tiene_contrato = tiene_contrato

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @property
    def tiene_contrato(self):
        return self.__tiene_contrato

    @tiene_contrato.setter
    def tiene_contrato(self, value):
        self.__tiene_contrato = value

    def es_provincia(self, prov):
        return self.direccion.provinica == prov

    def str_varias_lineas(self):
        contrato = 'No'
        if self.tiene_contrato:
            contrato = 'Sí'
        return '{}\nDirección: {}\nTiene contrato para el transporte oficial: {}'.format(
            Estudiante.str_varias_lineas(self), self.direccion, contrato)
