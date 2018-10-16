from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
from .serializers import BibleReadSerializer
from .filters import BibleReadFilter
from .mixins.reading import ReadingMixin


class ReadingViewSet(viewsets.ModelViewSet, ReadingMixin):

    queryset = BibleRead.objects.all()
    serializer_class = BibleReadSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = BibleReadFilter
