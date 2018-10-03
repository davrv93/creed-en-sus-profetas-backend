import django_filters

from django_rv_apps.apps.believe_his_prophets.models.book import Book

from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead


class BibleReadFilter(django_filters.FilterSet):
   
    book = django_filters.ModelChoiceFilter(queryset=Book.objects.all())

    class Meta:
        model = BibleRead
        fields = ['id']

    