from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework.response import Response

from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter

from django_rv_apps.apps.believe_his_prophets.models.language import Language

from .serializers import ChapterSerializer
from .filters import ChapterFilter
from .mixins.audio import   AudioMixin

class ChapterViewSet(viewsets.ModelViewSet, AudioMixin):

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = ChapterFilter

    def create(self, request):
        print('request',request)

        data = request.data

        obj = data

        code_iso = data.get('code_iso')

        language = Language.objects.get(code_iso=code_iso)

        obj.update(language=language.id)

        serializer = ChapterSerializer(
            data=data
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        retorno = serializer.data

        return Response(retorno)
