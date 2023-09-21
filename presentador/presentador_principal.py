import sys
from PyQt5.QtWidgets import QApplication
from modelo.repositorio import Repositorio
from modelo.servicio_residencia import ServicioResidencia
from presentador.presentador_ests_nacs import PresentadorEstudiantesNacionales
from presentador.presentador_ests_exts import PresentadorEstudiantesExtranjeros
from presentador.presentador_act_dir import PresentadorActDireccion
from presentador.presentador_por_ciento_exts import PresentadorPorCientoExts
from presentador.presentador_rep_param import PresentadorReporte1Parametro
from presentador.presentador_datos_ests_nacs import PresentadorDatosEstsNacs
from vista.ventana_principal import VentanaPrincipal
from vista.acerca_de import AcercaDe


class PresentadorPrincipal:
    def __init__(self):
        self.__repositorio = Repositorio()
        self.__servicio_residencia = ServicioResidencia(self.__repositorio)

    def iniciar(self):
        app = QApplication(sys.argv)
        self.__vista = VentanaPrincipal(self)
        self.__vista.show()
        app.exec()

    def crud_ests_nacs(self):
        pen = PresentadorEstudiantesNacionales(self.__repositorio)
        pen.iniciar()

    def crud_ests_exts(self):
        pee = PresentadorEstudiantesExtranjeros(self.__repositorio)
        pee.iniciar()

    def act_dir(self):
        pad = PresentadorActDireccion(self.__repositorio)
        pad.iniciar()

    def por_ciento_exts(self):
        ppce = PresentadorPorCientoExts(self.__repositorio)
        ppce.iniciar()

    def promedio_edad_exts(self):
        prp = PresentadorReporte1Parametro(self.__repositorio)
        prp.iniciar_promedio_edad_exts()

    def menor_est_nac(self):
        prp = PresentadorReporte1Parametro(self.__repositorio)
        prp.iniciar_menor_est_nac()

    def ests_nacs_facultad(self):
        pden = PresentadorDatosEstsNacs(self.__repositorio)
        pden.iniciar()

    def acerca_de(self):
        ad = AcercaDe()
        ad.exec()
