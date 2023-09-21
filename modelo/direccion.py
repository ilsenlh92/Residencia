class Direccion:
    def __init__(self, calle, num, rep, mun, prov):
        self.__calle = calle
        self.__numero = num
        self.__reparto = rep
        self.__municipio = mun
        self.__provincia = prov

    def es_provincia(self, prov):
        return self.provinica == prov

    @property
    def calle(self):
        return self.__calle

    @calle.setter
    def calle(self, value):
        self.__calle = value

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def reparto(self):
        return self.__reparto

    @reparto.setter
    def reparto(self, value):
        self.__reparto = value

    @property
    def municipio(self):
        return self.__municipio

    @municipio.setter
    def municipio(self, value):
        self.__municipio = value

    @property
    def provinica(self):
        return self.__provincia

    @provinica.setter
    def provinica(self, value):
        self.__provincia = value

    def __str__(self):
        if self.reparto != None and self.reparto != '':
            rep = 'Rpto. {}, '.format(self.reparto)
        else:
            rep = ''
        return '{} #{}, {}{}, {}'.format(self.calle, self.numero,rep, self.municipio, self.provinica)