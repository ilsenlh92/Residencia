from modelo.direccion import Direccion
from modelo.servicio_residencia import ServicioResidencia
from vista.actualizar_direccion import ActualizarDireccion


class PresentadorActDireccion:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__servicio_residencia = ServicioResidencia(self.__repositorio)

    def iniciar(self):
        self.__vista = ActualizarDireccion(self)
        self.__vista.show()

    def actualizar_direccion(self):
        try:
            self.__vista.validar_controles()
            num_becado = self.__vista.valor_num_becado
            calle = self.__vista.valor_calle
            numero = self.__vista.valor_numero
            reparto = self.__vista.valor_reparto
            mun = self.__vista.valor_municipio
            prov = self.__vista.valor_provincia
            direccion = Direccion(calle, numero, reparto, mun, prov)
            self.__servicio_residencia.actualizar_direccion(num_becado, direccion)
            self.__vista.mostrar_informacion('Actualizado', 'Dirección actualizada correctamente.')
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])