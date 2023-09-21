from unittest import TestCase
from modelo.direccion import Direccion

class TestDireccion(TestCase):
    def setUp(self):
        self.dir1 = Direccion('San Esteban', '234', '', 'Camagüey', 'Camagüey')
        self.dir2 = Direccion('Sta Rita', '397A', 'América Latina', 'Camagüey', 'Camagüey')
        self.dir3 = Direccion('Joaquín de Agüero', '1203', '', 'Cienfuegos', 'Cienfuegos')
        self.dir4 = Direccion('Leoncio Vidal', '673B', 'Buen Viaje', 'Sta Clara', 'Villa Clara')
        self.dir5 = Direccion('Calle C', '641', '', 'Varadero', 'Matanzas')

    def test_properties(self):
        self.assertEqual(self.dir1.calle, 'San Esteban')
        self.assertEqual(self.dir3.calle, 'Joaquín de Agüero')
        self.dir1.calle = 'San Patricio'
        self.assertEqual(self.dir1.calle, 'San Patricio')

        self.assertEqual(self.dir2.numero, '397A')
        self.assertEqual(self.dir3.numero, '1203')
        self.dir4.numero = '493C'
        self.assertEqual(self.dir4.numero, '493C')

        self.assertEqual(self.dir3.reparto, '')
        self.assertEqual(self.dir4.reparto, 'Buen Viaje')
        self.dir3.reparto = 'Costa Blanca'
        self.assertEqual(self.dir3.reparto, 'Costa Blanca')

        self.assertEqual(self.dir4.municipio, 'Sta Clara')
        self.assertEqual(self.dir2.municipio, 'Camagüey')
        self.dir5.municipio = 'Cárdenas'
        self.assertEqual(self.dir5.municipio, 'Cárdenas')

        self.assertEqual(self.dir5.provinica, 'Matanzas')
        self.assertEqual(self.dir4.provinica, 'Villa Clara')
        self.dir2.provinica = 'Santiago de Cuba'
        self.assertEqual(self.dir2.provinica, 'Santiago de Cuba')

    def test_es_provincia(self):
        self.assertTrue(self.dir1.es_provincia('Camagüey'))
        self.assertFalse(self.dir2.es_provincia('Las Tunas'))
        self.assertTrue(self.dir3.es_provincia('Cienfuegos'))
        self.assertFalse(self.dir4.es_provincia('Pinar del Rio'))
        self.assertTrue(self.dir5.es_provincia('Matanzas'))

    def test_str(self):
        self.assertEqual(str(self.dir1), 'San Esteban #234, Camagüey, Camagüey')
        self.assertEqual(str(self.dir2), 'Sta Rita #397A, Rpto. América Latina, Camagüey, Camagüey')
        self.assertEqual(str(self.dir3), 'Joaquín de Agüero #1203, Cienfuegos, Cienfuegos')
        self.assertEqual(str(self.dir4), 'Leoncio Vidal #673B, Rpto. Buen Viaje, Sta Clara, Villa Clara')
        self.assertEqual(str(self.dir5), 'Calle C #641, Varadero, Matanzas')
