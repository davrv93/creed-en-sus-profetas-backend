from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.book import Book
from .serializers import BookSerializer
from .filters import BookFilter


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = BookFilter
