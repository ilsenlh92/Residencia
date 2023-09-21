from modelo.estudiante_nacional import EstudianteNacional
from modelo.estudiante_extranjero import EstudianteExtranjero

class ServicioResidencia:
    def __init__(self, repo):
        self.__repositorio = repo

    @property
    def repositorio(self):
        return self.__repositorio

    def actualizar_direccion(self, num_becado, nueva_direccion):
        ind = None
        for i in range(len(self.repositorio.lista_estudiantes)):
            if self.repositorio.lista_estudiantes[i].es_num_becado(num_becado):
                ind = i
                break
        if ind == None:
            raise Exception('El estudiante no existe')
        if not isinstance(self.repositorio.lista_estudiantes[ind], EstudianteNacional):
            raise Exception('El estudiante no es nacional')
        self.repositorio.lista_estudiantes[ind].direccion = nueva_direccion

    def porciento_ests_extranjeros(self, carrera, nacionalidad):
        total, parte, no_existe_carrera = 0,0, True
        for est in self.repositorio.lista_estudiantes:
            if est.es_carrera(carrera):
                no_existe_carrera = False
                if isinstance(est, EstudianteExtranjero):
                    total += 1
                    if est.es_nacionalidad(nacionalidad):
                        parte += 1
        if no_existe_carrera:
            raise Exception('La carrera {} no existe en el repositorio'.format(carrera))
        if total == 0:
            raise Exception('La carrera {} no tiene estudiantes extranjeros matriculados'.format(carrera))
        if parte == 0:
            raise Exception('La carrera {} no tiene estudiantes extranjeros matriculados de nacionalidad {}'.format(carrera, nacionalidad))
        return parte * 100 / total

    def promedio_edades_ests_extranjeros_autofinanciados(self, facultad):
        sum, cont, no_existe_facultad, no_tiene_extranjeros = 0,0, True, True
        for est in self.repositorio.lista_estudiantes:
            if est.es_facultad(facultad):
                no_existe_facultad = False
                if isinstance(est, EstudianteExtranjero):
                    no_tiene_extranjeros = False
                    if est.auto_financiado:
                        sum += est.edad()
                        cont += 1
        if no_existe_facultad:
            raise Exception('La facultad {} no existe en el repositorio'.format(facultad))
        if no_tiene_extranjeros:
            raise Exception('La facultad {} no tiene estudiantes extranjeros matriculados'.format(facultad))
        if cont == 0:
            raise Exception('La facultad {} no tiene estudiantes extranjeros autofinanciados'.format(facultad))
        return sum / cont

    def menor_est_sin_transporte(self, provinicia):
        menor_est, menor_edad, no_existe_prov = None, 120, True
        for est in self.repositorio.lista_estudiantes:
            if isinstance(est, EstudianteNacional) and est.es_provincia(provinicia):
                no_existe_prov = False
                if not est.tiene_contrato:
                    if est.edad() < menor_edad:
                        menor_edad = est.edad()
                        menor_est = est
        if no_existe_prov:
            raise Exception('No existen estudiantes de la provincia {} en el repositorio'.format(provinicia))
        if menor_est == None:
            raise Exception('No existen estudiantes de la provincia {} sin transportación en el repositorio'.format(provinicia))
        return menor_est

    def ests_nacs_ordenados_edad(self, facultad):
        no_existe_facultad = True
        lista = []
        for est in self.repositorio.lista_estudiantes:
            if est.es_facultad(facultad):
                no_existe_facultad = False
                if isinstance(est, EstudianteNacional):
                    lista.append(est)
        if no_existe_facultad:
            raise Exception('La facultad {} no existe en el repositorio'.format(facultad))
        if len(lista) == 0:
            raise Exception('La facultad {} no tiene estudiantes nacionales'.format(facultad))
        lista.sort()
        return lista

