
from django.shortcuts import reverse

from rest_framework.test import APITestCase


from django_rv_apps.apps.believe_his_prophets.models.sucursal import Sucursal


class TestNoteApi(APITestCase):
    def setUp(self):
        self.condition = False
        self.logged = False

    def test_getting_sucursals(self):
        self.logged = self.client.login(username='root', password='root')

        print('Inicio de sesión:',  self.logged)

        self.assertEqual(True, self.logged)

        response = self.client.get(reverse('sucursales'), format="json")

        data = response.data.get('results', None)

        if data and len(data) > 0:
            self.condition = True
        else:
            self.condition = False

        # print('data', data)
        self.assertEqual(True, self.condition)
