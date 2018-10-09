import django_filters

from django_filters import rest_framework as filters

from django_rv_apps.apps.believe_his_prophets.models.book import Book

from django_rv_apps.apps.believe_his_prophets.models.language import Language


from django_rv_apps.apps.believe_his_prophets.models.book_language import BookLanguage


class BookLanguageFilter(django_filters.FilterSet):

    book = filters.ModelChoiceFilter(
        queryset=Book.objects.all())

    code_iso = filters.ModelMultipleChoiceFilter(
        queryset=Language.objects.all(),
        field_name='language__code_iso',
        to_field_name='code_iso'
    )

    class Meta:
        model = BookLanguage
        fields = ('id', 'book', 'name',
                  'abreviation')
