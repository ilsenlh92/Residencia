from modelo.direccion import Direccion
from modelo.estudiante_nacional import EstudianteNacional
from modelo.servicio_residencia import ServicioResidencia
from vista.gestionar_ests_nacs import CRUDEstsNacs


class PresentadorEstudiantesNacionales:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__servicio_residencia = ServicioResidencia(self.__repositorio)

    def iniciar(self):
        self.__vista = CRUDEstsNacs(self)
        self.cargar_datos()
        self.__vista.show()

    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        for est_nac in self.__repositorio.lista_ests_nacionales():
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

    def insertar_est_nac(self):
        try:
            self.__vista.validar_controles()
            nombre = self.__vista.valor_nombre
            ci = self.__vista.valor_ci
            sexo = self.__vista.valor_sexo
            carrera = self.__vista.valor_carrera
            facultad = self.__vista.valor_facultad
            num_becado = self.__vista.valor_num_becado
            num_albergue = self.__vista.valor_num_albergue
            num_cuarto = self.__vista.valor_num_cuarto
            anio = self.__vista.valor_anio_esc
            calle = self.__vista.valor_calle
            numero = self.__vista.valor_numero
            reparto = self.__vista.valor_reparto
            mun = self.__vista.valor_municipio
            prov = self.__vista.valor_provincia
            tiene_contrato = self.__vista.valor_tiene_trans
            direccion = Direccion(calle, numero, reparto, mun, prov)
            est = EstudianteNacional(nombre, ci, sexo, carrera, facultad, num_becado, num_albergue, num_cuarto, anio, direccion, tiene_contrato)
            self.__repositorio.insertar_estudiante(est)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_est_nac(self):
        try:
            ind = self.__vista.tabla_est.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla.')
            ci_ant = self.__vista.tabla_est.item(ind, 1).text()

            self.__vista.validar_controles()
            nombre = self.__vista.valor_nombre
            ci = self.__vista.valor_ci
            sexo = self.__vista.valor_sexo
            carrera = self.__vista.valor_carrera
            facultad = self.__vista.valor_facultad
            num_becado = self.__vista.valor_num_becado
            num_albergue = self.__vista.valor_num_albergue
            num_cuarto = self.__vista.valor_num_cuarto
            anio = self.__vista.valor_anio_esc
            calle = self.__vista.valor_calle
            numero = self.__vista.valor_numero
            reparto = self.__vista.valor_reparto
            mun = self.__vista.valor_municipio
            prov = self.__vista.valor_provincia
            tiene_contrato = self.__vista.valor_tiene_trans
            direccion = Direccion(calle, numero, reparto, mun, prov)
            est = EstudianteNacional(nombre, ci, sexo, carrera, facultad, num_becado, num_albergue, num_cuarto, anio, direccion, tiene_contrato)
            self.__repositorio.actualizar_estudiante(ci_ant, est)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_est_nac(self):
        try:
            ind = self.__vista.tabla_est.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para eliminarla.')
            ci = self.__vista.tabla_est.item(ind, 1).text()

            self.__repositorio.eliminar_estudiante(ci)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):
        ind = self.__vista.tabla_est.currentRow()
        if ind != -1:
            nombre = self.__vista.tabla_est.item(ind, 0).text()
            ci = self.__vista.tabla_est.item(ind, 1).text()
            sexo = self.__vista.tabla_est.item(ind, 3).text()
            carrera = self.__vista.tabla_est.item(ind, 4).text()
            facultad = self.__vista.tabla_est.item(ind, 5).text()
            num_becado = self.__vista.tabla_est.item(ind, 6).text()
            num_albergue = self.__vista.tabla_est.item(ind, 7).text()
            num_cuarto = self.__vista.tabla_est.item(ind, 8).text()
            anio = self.__vista.tabla_est.item(ind, 9).text()
            direccion = self.__vista.tabla_est.item(ind, 10).text().split(',')
            tiene_reparto = False
            if len(direccion) == 3:
                calle, mun, prov = direccion
            else:
                tiene_reparto = True
                calle, reparto, mun, prov = direccion
            direccion = calle.split('#')
            calle, numero = direccion
            tiene_contrato = True
            if self.__vista.tabla_est.item(ind, 11).text() == 'No':
                tiene_contrato = False
            self.__vista.valor_nombre = nombre
            self.__vista.valor_ci = ci
            self.__vista.valor_sexo = sexo
            self.__vista.valor_carrera = carrera
            self.__vista.valor_facultad = facultad
            self.__vista.valor_num_becado = int(num_becado)
            self.__vista.valor_num_albergue = int(num_albergue)
            self.__vista.valor_num_cuarto = int(num_cuarto)
            self.__vista.valor_anio_esc = int(anio)
            self.__vista.valor_calle = calle.strip()
            self.__vista.valor_numero = numero.strip()
            if tiene_reparto:
                self.__vista.valor_reparto = reparto.strip()[5:].strip()
            else:
                self.__vista.valor_reparto = ''
            self.__vista.valor_municipio = mun.strip()
            self.__vista.valor_provincia = prov.strip()
            self.__vista.valor_tiene_trans = tiene_contrato
