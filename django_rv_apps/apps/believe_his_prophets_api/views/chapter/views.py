from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter
from .serializers import ChapterSerializer
from .filters import ChapterFilter
from .mixins.audio import   AudioMixin

class ChapterViewSet(viewsets.ModelViewSet, AudioMixin):

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = ChapterFilter
