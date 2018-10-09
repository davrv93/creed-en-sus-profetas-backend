import django_filters

from django_filters import rest_framework as filters


from django_rv_apps.apps.believe_his_prophets.models.testament import Testament


class TestamentFilter(django_filters.FilterSet):

    class Meta:
        model = Testament
        fields = '__all__'
