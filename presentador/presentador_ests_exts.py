from modelo.estudiante_extranjero import EstudianteExtranjero
from modelo.servicio_residencia import ServicioResidencia
from vista.gestionar_ests_exts import CRUDEstsExts


class PresentadorEstudiantesExtranjeros:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__servicio_residencia = ServicioResidencia(self.__repositorio)

    def iniciar(self):
        self.__vista = CRUDEstsExts(self)
        self.cargar_datos()
        self.__vista.show()

    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        for est_ext in self.__repositorio.lista_ests_extranjeros():
            auto_financiado = 'No'
            if est_ext.auto_financiado:
                auto_financiado = 'Sí'
            i = self.__vista.tabla_est.rowCount()
            self.__vista.tabla_est.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, est_ext.nombre)
            self.__vista.agregar_elemento_tabla(i, 1, est_ext.ci)
            self.__vista.agregar_elemento_tabla(i, 2, str(est_ext.edad()))
            self.__vista.agregar_elemento_tabla(i, 3, est_ext.sexo)
            self.__vista.agregar_elemento_tabla(i, 4, est_ext.carrera)
            self.__vista.agregar_elemento_tabla(i, 5, est_ext.facultad)
            self.__vista.agregar_elemento_tabla(i, 6, str(est_ext.num_becado))
            self.__vista.agregar_elemento_tabla(i, 7, str(est_ext.albergue))
            self.__vista.agregar_elemento_tabla(i, 8, str(est_ext.cuarto))
            self.__vista.agregar_elemento_tabla(i, 9, str(est_ext.anio))
            self.__vista.agregar_elemento_tabla(i, 10, est_ext.nacionalidad)
            self.__vista.agregar_elemento_tabla(i, 11, auto_financiado)
        self.__vista.tabla_est.resizeColumnsToContents()

    def insertar_est_ext(self):
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
            nacionalidad = self.__vista.valor_nacionalidad
            auto_financiado = self.__vista.valor_autofinanciado
            est = EstudianteExtranjero(nombre, ci, sexo, carrera, facultad, num_becado, num_albergue, num_cuarto, anio, nacionalidad, auto_financiado)
            self.__repositorio.insertar_estudiante(est)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def actualizar_est_ext(self):
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
            nacionalidad = self.__vista.valor_nacionalidad
            auto_financiado = self.__vista.valor_autofinanciado
            est = EstudianteExtranjero(nombre, ci, sexo, carrera, facultad, num_becado, num_albergue, num_cuarto, anio, nacionalidad, auto_financiado)
            self.__repositorio.actualizar_estudiante(ci_ant, est)
            self.cargar_datos()
            self.__vista.restablecer_controles()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar_est_ext(self):
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
            nacionalidad = self.__vista.tabla_est.item(ind, 10).text()
            auto_financiado = True
            if self.__vista.tabla_est.item(ind, 11).text() == 'No':
                auto_financiado = False
            self.__vista.valor_nombre = nombre
            self.__vista.valor_ci = ci
            self.__vista.valor_sexo = sexo
            self.__vista.valor_carrera = carrera
            self.__vista.valor_facultad = facultad
            self.__vista.valor_num_becado = int(num_becado)
            self.__vista.valor_num_albergue = int(num_albergue)
            self.__vista.valor_num_cuarto = int(num_cuarto)
            self.__vista.valor_anio_esc = int(anio)
            self.__vista.valor_nacionalidad = nacionalidad
            self.__vista.valor_autofinanciado = auto_financiado
