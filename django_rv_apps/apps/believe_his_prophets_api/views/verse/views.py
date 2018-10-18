from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.verse import Verse
from .serializers import VerseSerializer
from .filters import VerseFilter


class VerseViewSet(viewsets.ModelViewSet):

    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = VerseFilter

    def paginate_queryset(self, queryset):
        if 'no_page' in self.request.query_params:
            return None

        return super().paginate_queryset(queryset)
