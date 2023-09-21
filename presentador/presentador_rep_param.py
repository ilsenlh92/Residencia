from modelo.servicio_residencia import ServicioResidencia
from vista.reporte_parametro import Reporte1Parametro


class PresentadorReporte1Parametro:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__servicio_residencia = ServicioResidencia(self.__repositorio)

    def iniciar_promedio_edad_exts(self):
        self.__vista = Reporte1Parametro(self, 1, 'Promedio de edad de extranjeros', 'Facultad', 'Calcular')
        self.__vista.show()

    def iniciar_menor_est_nac(self):
        self.__vista = Reporte1Parametro(self, 2, 'Datos del menor estudiante nacional', 'Provincia', 'Buscar')
        self.__vista.show()

    def accion(self):
        try:
            self.__vista.validar_controles()
            if self.__vista.num_func == 1:
                fac = self.__vista.valor_texto
                prom = self.__servicio_residencia.promedio_edades_ests_extranjeros_autofinanciados(fac)
                msg = 'El promedio de edad de los estudiantes extranjeros de la facultad {} que son autofinanciados es {}'.format(fac, prom)
                self.__vista.mostrar_informacion('Promedio', msg)
            else:
                prov = self.__vista.valor_texto
                est = self.__servicio_residencia.menor_est_sin_transporte(prov)
                msg = 'Los datos del menor estudiante nacional de la provincia {} que no cuenta con transportación son:\n{}'.format(prov, est.str_varias_lineas())
                self.__vista.mostrar_informacion('Datos del menor estudiante', msg)
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
