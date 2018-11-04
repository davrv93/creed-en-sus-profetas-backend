import django_filters

from django_filters import rest_framework as filters

from django_rv_apps.apps.believe_his_prophets.models.hierarchy import Hierarchy


class HierarchyFilter(django_filters.FilterSet):

    code = filters.CharFilter(
        field_name='code')

    class Meta:
        model = Hierarchy
        fields = ('id', 'code')
