import django_filters

from django_filters import rest_framework as filters

from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_chapter import SpiritProphecyChapter, SpiritProphecyChapterLanguage
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy
from django_rv_apps.apps.believe_his_prophets.models.language import Language
from django.utils import timezone


class SpiritProphecyChapterLanguageFilter(django_filters.FilterSet):

    code_iso = filters.ModelMultipleChoiceFilter(
        queryset=Language.objects.all(),
        field_name='language__code_iso',
        to_field_name='code_iso'
    )

    start_date = filters.CharFilter(method='filter_date')



 
    class Meta:
        model = SpiritProphecyChapterLanguage
        fields = ('id' ,'code_iso','start_date')


    def filter_date(self, queryset, name, value):
        t = timezone.localtime(timezone.now())
        return queryset.filter(
            spirit_prophecy_chapter__start_date__year = t.year,
            spirit_prophecy_chapter__start_date__month = t.month, spirit_prophecy_chapter__start_date__day = t.day,
        )