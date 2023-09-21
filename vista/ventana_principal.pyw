from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QCloseEvent, QResizeEvent
from PyQt5 import uic


class VentanaPrincipal(QMainWindow):
    def __init__(self, presentador):
        self.__presentador = presentador
        QMainWindow.__init__(self)
        uic.loadUi('vista/ui/ventana_principal.ui', self)

        self.opc_salir.triggered.connect(self.close)
        self.opc_crud_est_nac.triggered.connect(self.__presentador.crud_ests_nacs)
        self.opc_crud_est_ext.triggered.connect(self.__presentador.crud_ests_exts)
        self.opc_act_dir.triggered.connect(self.__presentador.act_dir)
        self.opc_por_ciento.triggered.connect(self.__presentador.por_ciento_exts)
        self.opc_prom.triggered.connect(self.__presentador.promedio_edad_exts)
        self.opc_menor.triggered.connect(self.__presentador.menor_est_nac)
        self.opc_datos.triggered.connect(self.__presentador.ests_nacs_facultad)
        self.opc_acerca.triggered.connect(self.__presentador.acerca_de)

    def closeEvent(self, a0: QCloseEvent):
        QMainWindow.closeEvent(self, a0)

    def resizeEvent(self, a0: QResizeEvent):
        background = QPixmap('vista/imgs/background.jpg')
        background = background.scaled(self.size(), Qt.IgnoreAspectRatio)  # KeepAspectRatio, KeepAspectRatioByExpanding
        pal = self.palette()
        pal.setBrush(QPalette.Background, QBrush(background))
        self.setPalette(pal)
