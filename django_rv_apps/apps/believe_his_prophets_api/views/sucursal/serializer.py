from rest_framework import serializers
from django_rv_apps.apps.believe_his_prophets.models.sucursal import Sucursal


class SucursalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sucursal
        fields = ('id', 'nombre',)
