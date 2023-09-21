from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic


class ActualizarDireccion(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/actualizar_direccion.ui', self)

        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_direccion)
        self.btn_cancelar.clicked.connect(self.close)

    @property
    def valor_num_becado(self):
        return self.spn_num_becado.value()

    @valor_num_becado.setter
    def valor_num_becado(self, value):
        self.spn_num_becado.setValue(value)

    @property
    def valor_calle(self):
        return self.txt_calle.text().strip()

    @valor_calle.setter
    def valor_calle(self, value):
        self.txt_calle.setText(value)

    @property
    def valor_numero(self):
        return self.txt_numero.text().strip()

    @valor_numero.setter
    def valor_numero(self, value):
        self.txt_numero.setText(value)

    @property
    def valor_reparto(self):
        return self.txt_reparto.text().strip()

    @valor_reparto.setter
    def valor_reparto(self, value):
        self.txt_reparto.setText(value)

    @property
    def valor_municipio(self):
        return self.txt_municipio.text().strip()

    @valor_municipio.setter
    def valor_municipio(self, value):
        self.txt_municipio.setText(value)

    @property
    def valor_provincia(self):
        return self.txt_provincia.text().strip()

    @valor_provincia.setter
    def valor_provincia(self, value):
        self.txt_provincia.setText(value)

    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        if len(self.valor_calle) == 0:
            raise Exception(msg.format('calle'))
        if self.valor_calle.find(',') != -1 or self.valor_calle.find('#') != -1:
            raise Exception('La calle no puede contener # o ,')
        if len(self.valor_numero) == 0:
            raise Exception(msg.format('número'))
        if self.valor_numero.find(',') != -1 or self.valor_numero.find('#') != -1:
            raise Exception('El número no puede contener # o ,')
        if self.valor_reparto.find(',') != -1:
            raise Exception('El reparto no puede contener ,')
        if len(self.valor_municipio) == 0:
            raise Exception(msg.format('municipio'))
        if self.valor_municipio.find(',') != -1:
            raise Exception('El municipio no puede contener ,')
        if len(self.valor_provincia) == 0:
            raise Exception(msg.format('provincia'))
        if self.valor_provincia.find(',') != -1:
            raise Exception('La provincia no puede contener ,')

    def restablecer_controles(self):
        self.valor_num_becado = 0
        self.valor_calle = ''
        self.valor_numero = ''
        self.valor_reparto = ''
        self.valor_municipio = ''
        self.valor_provincia = ''

    def mostrar_informacion(self, titulo, msg):
        QMessageBox.information(self, titulo, msg)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)