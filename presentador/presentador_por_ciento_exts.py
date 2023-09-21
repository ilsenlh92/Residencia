from modelo.servicio_residencia import ServicioResidencia
from vista.porciento_exts import PorCientoExts


class PresentadorPorCientoExts:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__servicio_residencia = ServicioResidencia(self.__repositorio)

    def iniciar(self):
        self.__vista = PorCientoExts(self)
        self.__vista.show()

    def por_ciento_exts(self):
        try:
            self.__vista.validar_controles()
            carrera = self.__vista.valor_carrera
            nacionalidad = self.__vista.valor_nacionalidad
            por_ciento = self.__servicio_residencia.porciento_ests_extranjeros(carrera, nacionalidad)
            msg = 'El {}% de los estudiantes extranjeros de {} son de nacionalidad {}.'.format(por_ciento, carrera, nacionalidad)
            self.__vista.mostrar_informacion('Por ciento', msg)
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
