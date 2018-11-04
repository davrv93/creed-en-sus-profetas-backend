import django_filters

from django_filters import rest_framework as filters

from django_rv_apps.apps.believe_his_prophets.models.sucursal import Sucursal


class SucursalFilter(django_filters.FilterSet):

    nombre = filters.CharFilter(
        field_name='nombre')

    class Meta:
        model = Sucursal
        fields = ('id', 'nombre')
