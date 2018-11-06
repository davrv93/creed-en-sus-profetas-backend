import django_filters

from django_filters import rest_framework as filters

from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_chapter import SpiritProphecyChapter, SpiritProphecyChapterLanguage
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy
from django_rv_apps.apps.believe_his_prophets.models.language import Language


class SpiritProphecyChapterLanguageFilter(django_filters.FilterSet):

    code_iso = filters.ModelMultipleChoiceFilter(
        queryset=Language.objects.all(),
        field_name='language__code_iso',
        to_field_name='code_iso'
    )

    start_date = filters.DateFilter(
        field_name='spirit_prophecy_chapter__start_date',
        lookup_expr='lte'
    )
    end_date = filters.DateFilter(
        field_name='spirit_prophecy_chapter__end_date',
        lookup_expr='gte'

    )

    class Meta:
        model = SpiritProphecyChapterLanguage
        fields = ('id', 'spirit_prophecy_chapter__start_date',
                  'spirit_prophecy_chapter__end_date')
