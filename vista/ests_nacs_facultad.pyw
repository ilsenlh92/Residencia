from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class DatosEstsNacsFac(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        QWidget.__init__(self)
        uic.loadUi('vista/ui/ests_nacs_facultad.ui', self)

        self.btn_filtrar.clicked.connect(self.__presentador.filtrar_x_facultad)
        self.btn_cancelar.clicked.connect(self.close)

        self.tabla_est.setColumnCount(12)
        self.tabla_est.setHorizontalHeaderLabels(
            ['Nombre', 'CI', 'Edad', 'Sexo', 'Carrera', 'Facultad', '# Becado', '# Albergue', '# Cuarto', 'Año Escolar',
             'Dirección', 'Tiene contrato transporte'])
        self.tabla_est.horizontalHeaderItem(1).setToolTip('Carné de Identidad')
        self.tabla_est.resizeColumnsToContents()

    @property
    def valor_facultad(self):
        return self.txt_facultad.text().strip()

    def validar_controles(self):
        if len(self.valor_facultad) == 0:
            raise Exception('El atributo facultad es obligatorio.')

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):
        while self.tabla_est.rowCount() > 0:
            self.tabla_est.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_est.setItem(fila, columna, QTableWidgetItem(texto))
