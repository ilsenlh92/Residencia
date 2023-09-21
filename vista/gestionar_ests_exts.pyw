from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class CRUDEstsExts(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        QWidget.__init__(self)
        uic.loadUi('vista/ui/gestionar_ests_exts.ui', self)

        self.btn_insertar.clicked.connect(self.__presentador.insertar_est_ext)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_est_ext)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_est_ext)
        self.btn_cerrar.clicked.connect(self.close)
        self.tabla_est.itemClicked.connect(self.__presentador.llenar_formulario_x_tabla)

        self.tabla_est.setColumnCount(12)
        self.tabla_est.setHorizontalHeaderLabels(
            ['Nombre', 'CI', 'Edad', 'Sexo', 'Carrera', 'Facultad', '# Becado', '# Albergue', '# Cuarto', 'Año Escolar',
             'Nacionalidad', 'Es autofinanciado'])
        self.tabla_est.horizontalHeaderItem(1).setToolTip('Carné de Identidad')
        self.tabla_est.resizeColumnsToContents()

    @property
    def valor_nombre(self):
        return self.txt_nombre.text().strip()

    @valor_nombre.setter
    def valor_nombre(self, value):
        self.txt_nombre.setText(value)

    @property
    def valor_ci(self):
        return self.txt_ci.text().strip()

    @valor_ci.setter
    def valor_ci(self, value):
        self.txt_ci.setText(value)

    @property
    def valor_sexo(self):
        if self.rbtn_mas.isChecked():
            sex = 'M'
        else:
            sex = 'F'
        return sex

    @valor_sexo.setter
    def valor_sexo(self, value):
        if value == 'M':
            self.rbtn_mas.setChecked(True)
        else:
            self.rbtn_fem.setChecked(True)

    @property
    def valor_carrera(self):
        return self.txt_carrera.text().strip()

    @valor_carrera.setter
    def valor_carrera(self, value):
        self.txt_carrera.setText(value)

    @property
    def valor_facultad(self):
        return self.txt_facultad.text().strip()

    @valor_facultad.setter
    def valor_facultad(self, value):
        self.txt_facultad.setText(value)

    @property
    def valor_num_becado(self):
        return self.spn_num_becado.value()

    @valor_num_becado.setter
    def valor_num_becado(self, value):
        self.spn_num_becado.setValue(value)

    @property
    def valor_num_albergue(self):
        return self.spn_num_albergue.value()

    @valor_num_albergue.setter
    def valor_num_albergue(self, value):
        self.spn_num_albergue.setValue(value)

    @property
    def valor_num_cuarto(self):
        return self.spn_num_cuarto.value()

    @valor_num_cuarto.setter
    def valor_num_cuarto(self, value):
        self.spn_num_cuarto.setValue(value)

    @property
    def valor_anio_esc(self):
        return self.spn_anio_esc.value()

    @valor_anio_esc.setter
    def valor_anio_esc(self, value):
        self.spn_anio_esc.setValue(value)

    @property
    def valor_nacionalidad(self):
        return self.txt_nacionalidad.text().strip()

    @valor_nacionalidad.setter
    def valor_nacionalidad(self, value):
        self.txt_nacionalidad.setText(value)

    @property
    def valor_autofinanciado(self):
        return self.chb_autofinanciado.isChecked()

    @valor_autofinanciado.setter
    def valor_autofinanciado(self, value):
        self.chb_autofinanciado.setChecked(value)

    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        if len(self.valor_nombre) == 0:
            raise Exception(msg.format('nombre'))
        ci = self.valor_ci
        if len(ci) == 0:
            raise Exception(msg.format('carné de identidad'))
        if len(ci) != 11 and len(ci) != 6:
            raise Exception('El carné de identidad debe tener 6 u 11 dígitos.')
        if not ci.isdigit():
            raise Exception('El carné de identidad sólo puede contener números.')
        if len(self.valor_carrera) == 0:
            raise Exception(msg.format('carrera'))
        if len(self.valor_facultad) == 0:
            raise Exception(msg.format('facultad'))
        if len(self.valor_nacionalidad) == 0:
            raise Exception(msg.format('nacionalidad'))

    def restablecer_controles(self):
        self.valor_nombre = ''
        self.valor_ci = ''
        self.valor_sexo = 'M'
        self.valor_carrera = ''
        self.valor_facultad = ''
        self.valor_num_becado = 0
        self.valor_num_albergue = 0
        self.valor_num_cuarto = 0
        self.valor_anio_esc = 1
        self.valor_nacionalidad = ''
        self.valor_autofinanciado = False

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):
        while self.tabla_est.rowCount() > 0:
            self.tabla_est.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_est.setItem(fila, columna, QTableWidgetItem(texto))
