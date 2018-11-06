import django_filters

from django_filters import rest_framework as filters


from django_rv_apps.apps.believe_his_prophets.models.book import Book

from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead

from django_rv_apps.apps.believe_his_prophets.models.testament import Testament


class BookFilter(django_filters.FilterSet):

    testament = filters.ModelChoiceFilter(
        queryset=Testament.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'testament',
                  'book_order')
