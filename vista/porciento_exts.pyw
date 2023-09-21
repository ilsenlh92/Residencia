from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic


class PorCientoExts(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/porciento_exts.ui', self)

        self.btn_calcular.clicked.connect(self.__presentador.por_ciento_exts)
        self.btn_cancelar.clicked.connect(self.close)
        
    @property
    def valor_carrera(self):
        return self.txt_carrera.text().strip()

    @valor_carrera.setter
    def valor_carrera(self, value):
        self.txt_carrera.setText(value)
    
    @property
    def valor_nacionalidad(self):
        return self.txt_nacionalidad.text().strip()

    @valor_nacionalidad.setter
    def valor_nacionalidad(self, value):
        self.txt_nacionalidad.setText(value)

    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        if len(self.valor_carrera) == 0:
            raise Exception(msg.format('carrera'))
        if len(self.valor_nacionalidad) == 0:
            raise Exception(msg.format('nacionalidad'))

    def restablecer_controles(self):
        self.valor_carrera = ''
        self.valor_nacionalidad = ''

    def mostrar_informacion(self, titulo, msg):
        QMessageBox.information(self, titulo, msg)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)
