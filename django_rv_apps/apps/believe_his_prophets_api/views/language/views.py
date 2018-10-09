from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.language import Language
from .serializers import LanguageSerializer
from .filters import LanguageFilter


class LanguageViewSet(viewsets.ModelViewSet):

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = LanguageFilter
