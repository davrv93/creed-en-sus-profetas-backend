import django_filters

from django_filters import rest_framework as filters


from django_rv_apps.apps.believe_his_prophets.models.book import Book

from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
from django.utils import timezone


class BibleReadFilter(django_filters.FilterSet):

    book = filters.ModelChoiceFilter(
        queryset=Book.objects.all())
    start_date = filters.DateFilter(method='filter_date')



    class Meta:
        model = BibleRead
        fields = ('id', 'book', 'start_date')

    def filter_date(self, queryset, value):
        t = timezone.localtime(timezone.now())
        return queryset.filter(
            start_date__year = t.year,
            start_date__month = t.month, start_date__day = t.day,
        )