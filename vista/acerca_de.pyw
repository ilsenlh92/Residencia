from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


class AcercaDe(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('vista/ui/acerca_de.ui', self)
