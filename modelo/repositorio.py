from modelo.estudiante_nacional import EstudianteNacional
from modelo.estudiante_extranjero import EstudianteExtranjero

class Repositorio:
    def __init__(self):
        self.__lista_estudiantes = []
        
    @property
    def lista_estudiantes(self):
        return self.__lista_estudiantes

    def ind_estudiante_x_ci(self, ci):
        for i in range(len(self.lista_estudiantes)):
            if self.lista_estudiantes[i].es_ci(ci):
                return i

    def ind_estudiante_x_num_becado(self, num_becado):
        for i in range(len(self.lista_estudiantes)):
            if self.lista_estudiantes[i].es_num_becado(num_becado):
                return i

    def insertar_estudiante(self, est):
        if self.ind_estudiante_x_ci(est.ci) != None or self.ind_estudiante_x_num_becado(est.num_becado) != None:
            raise Exception('El estudiante existe en el repositorio')
        self.lista_estudiantes.append(est)

    def actualizar_estudiante(self, ci_ant, est):
        ind_ant = self.ind_estudiante_x_ci(ci_ant)
        if ind_ant == None:
            raise Exception('El estudiante no existe')
        ind_nue1, ind_nue2 = self.ind_estudiante_x_ci(est.ci), self.ind_estudiante_x_num_becado(est.num_becado)
        if (ind_nue1 != None and ind_nue1 != ind_ant) or (ind_nue2 != None and ind_nue2 != ind_ant):
            raise Exception('El estudiante existe en el repositorio')
        self.lista_estudiantes[ind_ant] = est

    def eliminar_estudiante(self, ci):
        ind = self.ind_estudiante_x_ci(ci)
        if ind == None:
            raise Exception('El estudiante no existe')
        self.lista_estudiantes.remove(self.lista_estudiantes[ind])

    def lista_ests_nacionales(self):
        ests_nacs = []
        for est in self.lista_estudiantes:
            if isinstance(est, EstudianteNacional):
                ests_nacs.append(est)
        return ests_nacs

    def lista_ests_extranjeros(self):
        ests_exts = []
        for est in self.lista_estudiantes:
            if isinstance(est, EstudianteExtranjero):
                ests_exts.append(est)
        return ests_exts
