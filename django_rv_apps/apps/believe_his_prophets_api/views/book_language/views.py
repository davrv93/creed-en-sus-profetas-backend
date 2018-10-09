from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.book_language import BookLanguage
from .serializers import BookLanguageSerializer
from .filters import BookLanguageFilter


class BookLanguageViewSet(viewsets.ModelViewSet):

    queryset = BookLanguage.objects.all()
    serializer_class = BookLanguageSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = BookLanguageFilter
