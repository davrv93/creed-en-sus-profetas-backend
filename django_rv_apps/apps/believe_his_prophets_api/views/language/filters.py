import django_filters

from django_filters import rest_framework as filters


from django_rv_apps.apps.believe_his_prophets.models.language import Language


class LanguageFilter(django_filters.FilterSet):

    class Meta:
        model = Language
        fields = ('id', 'name',
                  'code_iso')
