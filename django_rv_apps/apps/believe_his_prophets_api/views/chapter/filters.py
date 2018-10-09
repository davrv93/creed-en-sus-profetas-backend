import django_filters

from django_filters import rest_framework as filters


from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter


class ChapterFilter(django_filters.FilterSet):

    class Meta:
        model = Chapter
        fields = ('id', 'book')
