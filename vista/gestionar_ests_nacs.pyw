from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class CRUDEstsNacs(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        QWidget.__init__(self)
        uic.loadUi('vista/ui/gestionar_ests_nacs.ui', self)

        self.btn_insertar.clicked.connect(self.__presentador.insertar_est_nac)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_est_nac)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_est_nac)
        self.btn_cerrar.clicked.connect(self.close)
        self.tabla_est.itemClicked.connect(self.__presentador.llenar_formulario_x_tabla)

        self.tabla_est.setColumnCount(12)
        self.tabla_est.setHorizontalHeaderLabels(['Nombre', 'CI', 'Edad', 'Sexo', 'Carrera', 'Facultad', '# Becado', '# Albergue', '# Cuarto', 'Año Escolar', 'Dirección', 'Tiene contrato transporte'])
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
    
    @property
    def valor_tiene_trans(self):
        return self.chb_tiene_trans.isChecked()

    @valor_tiene_trans.setter
    def valor_tiene_trans(self, value):
        self.chb_tiene_trans.setChecked(value)

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
        self.valor_nombre = ''
        self.valor_ci = ''
        self.valor_sexo = 'M'
        self.valor_carrera = ''
        self.valor_facultad = ''
        self.valor_num_becado = 0
        self.valor_num_albergue = 0
        self.valor_num_cuarto = 0
        self.valor_anio_esc = 1
        self.valor_calle = ''
        self.valor_numero = ''
        self.valor_reparto = ''
        self.valor_municipio = ''
        self.valor_provincia = ''
        self.valor_tiene_trans = False

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):
        while self.tabla_est.rowCount() > 0:
            self.tabla_est.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_est.setItem(fila, columna, QTableWidgetItem(texto))