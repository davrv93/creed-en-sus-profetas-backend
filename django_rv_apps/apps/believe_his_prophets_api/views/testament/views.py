from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.testament import Testament
from .serializers import TestamentSerializer
from .filters import TestamentFilter


class TestamentViewSet(viewsets.ModelViewSet):

    queryset = Testament.objects.all()
    serializer_class = TestamentSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = TestamentFilter
