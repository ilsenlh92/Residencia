from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic


class Reporte1Parametro(QDialog):
    def __init__(self, presentador, num_func, titulo, etiqueta, boton):
        self.__presentador = presentador
        self.__num_func = num_func
        QDialog.__init__(self)
        uic.loadUi('vista/ui/reporte_parametro.ui', self)
        self.setWindowTitle(titulo)
        self.label_texto.setText(etiqueta)
        self.btn_accion.setText(boton)

        self.btn_accion.clicked.connect(self.__presentador.accion)
        self.btn_cancelar.clicked.connect(self.close)

    @property
    def num_func(self):
        return self.__num_func

    @property
    def valor_texto(self):
        return self.txt_texto.text().strip()

    @valor_texto.setter
    def valor_texto(self, value):
        self.txt_texto.setText(value)

    def validar_controles(self):
        if len(self.valor_texto) == 0:
            raise Exception('El atributo {} es obligatorio.'.format(self.label_texto.text().lower()))

    def restablecer_controles(self):
        self.valor_texto = ''

    def mostrar_informacion(self, titulo, msg):
        QMessageBox.information(self, titulo, msg)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)
