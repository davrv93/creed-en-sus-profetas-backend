import django_filters

from django_filters import rest_framework as filters

from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_read import SpiritProphecyRead
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy


class SpiritProphecyReadFilter(django_filters.FilterSet):

    spirit_prophecy = filters.ModelChoiceFilter(
        queryset=SpiritProphecy.objects.all(),
        field_name='spirit_prophecy',
        to_field_name='spirit_prophecy_chapter__')

    class Meta:
        model = SpiritProphecyRead
        fields = ('id', 'book', 'start_date')
