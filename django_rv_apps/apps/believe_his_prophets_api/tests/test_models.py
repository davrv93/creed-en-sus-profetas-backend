
from django.test import TestCase

from django_rv_apps.apps.believe_his_prophets.models.sucursal import Sucursal


class TestSucursalModel(TestCase):
    def setUp(self):
        self.sucursal = Sucursal(
            nombre="Prueba",
            direccion="Direcciòn de prueba",
            referencia="Referencia",
            latitud="Latitud",
            longitud="Longitud"
        )
        self.sucursal.save()
        self.count = Sucursal.objects.count() + 1

    def test_sucursal_creation(self):
        count = Sucursal.objects.count()
        expected = count + 1

        self.assertEqual(self.count, expected)

    def test_sucursal_representation(self):
        print('Representación de la instancia: '+str(self.sucursal))
        print('Valor del objeto: '+str(self.sucursal))
        self.assertEqual(self.sucursal.nombre, str(self.sucursal))
