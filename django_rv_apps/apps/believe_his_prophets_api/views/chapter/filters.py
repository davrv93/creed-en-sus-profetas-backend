import django_filters

from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter
from django_rv_apps.apps.believe_his_prophets.models.language import Language


class ChapterFilter(django_filters.FilterSet):

    code_iso = django_filters.ModelMultipleChoiceFilter(
        queryset=Language.objects.all(),
        field_name='language__code_iso',
        to_field_name='code_iso'
    )

    class Meta:
        model = Chapter
        fields = ('id', 'book','chapter')
