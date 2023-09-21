from modelo.servicio_residencia import ServicioResidencia
from vista.ests_nacs_facultad import DatosEstsNacsFac


class PresentadorDatosEstsNacs:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__servicio_residencia = ServicioResidencia(self.__repositorio)

    def iniciar(self):
        self.__vista = DatosEstsNacsFac(self)
        self.__vista.show()

    def filtrar_x_facultad(self):
        try:
            self.__vista.vaciar_tabla()
            self.__vista.validar_controles()
            facultad = self.__vista.valor_facultad
            lista = self.__servicio_residencia.ests_nacs_ordenados_edad(facultad)
            for est_nac in lista:
                contrato = 'No'
                if est_nac.tiene_contrato:
                    contrato = 'Sí'
                i = self.__vista.tabla_est.rowCount()
                self.__vista.tabla_est.insertRow(i)
                self.__vista.agregar_elemento_tabla(i, 0, est_nac.nombre)
                self.__vista.agregar_elemento_tabla(i, 1, est_nac.ci)
                self.__vista.agregar_elemento_tabla(i, 2, str(est_nac.edad()))
                self.__vista.agregar_elemento_tabla(i, 3, est_nac.sexo)
                self.__vista.agregar_elemento_tabla(i, 4, est_nac.carrera)
                self.__vista.agregar_elemento_tabla(i, 5, est_nac.facultad)
                self.__vista.agregar_elemento_tabla(i, 6, str(est_nac.num_becado))
                self.__vista.agregar_elemento_tabla(i, 7, str(est_nac.albergue))
                self.__vista.agregar_elemento_tabla(i, 8, str(est_nac.cuarto))
                self.__vista.agregar_elemento_tabla(i, 9, str(est_nac.anio))
                self.__vista.agregar_elemento_tabla(i, 10, str(est_nac.direccion))
                self.__vista.agregar_elemento_tabla(i, 11, contrato)
            self.__vista.tabla_est.resizeColumnsToContents()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
