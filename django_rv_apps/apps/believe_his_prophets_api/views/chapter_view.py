from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.exceptions import ParseError
from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter
from django_rv_apps.apps.believe_his_prophets.models.book import Book
from django_rv_apps.apps.believe_his_prophets.models.language import Language
from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
# from django_rv_apps.apps.believe_his_prophets_api.views.book_view import BookSerializer
# from django_rv_apps.apps.believe_his_prophets_api.views.language_view import LanguageSerializer

from django_filters import rest_framework as django_filters
from rest_framework import filters
from datetime import datetime


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = ('id', 'book', 'language',
                  'chapter', 'audio')


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all().prefetch_related('book', 'language')
    serializer_class = ChapterSerializer
    filter_backends = (filters.SearchFilter,
                       django_filters.DjangoFilterBackend,)
    filter_fields = ('id', 'book', 'chapter')
    search_fields = ('chapter',)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        except Chapter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        return instance.delete()

    @list_route(url_path='destroy', methods=['post'])
    def destroy_multiple(self, request):
        results = self.get_queryset().filter(id__in=request.data['bulk_id'])
        promise_list = []
        for i in results:
            promise = self.perform_destroy(i)
            if promise is not None:
                promise_list.append(str(promise))
        if len(promise_list) == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ParseError(', '.join(list(promise_list)))

    @list_route(url_path='reading')
    def list_reading_verse(self, request):
        # Declarando variables e instanciando
        obj_reading = {}
        obj_book = {}
        language = ''
        # Obteniendo fecha por defecto
        param_date = request.query_params.get('date', '')
        if param_date:
            datenow = param_date
            print('param_date', datenow)
        else:
            i = datetime.now()
            datenow = i.strftime('%Y-%m-%d')
        # Obteniendo idioma
        param_language = request.query_params.get('language', '')
        queryset_language = Language.objects.get(code_iso=param_language)
        serializer_language = LanguageSerializer(queryset_language,
                                                 many=False)
        obj_language = serializer_language.data
        reading = BibleRead.objects.filter(
            start_date=datenow).values()

        if reading:
            # Get de Verse
            queryset = Chapter.objects.filter(book=reading[0]['book_id'],
                                              chapter=reading[0]['start_chapter'],
                                              language=obj_language['id'])
            serializer = ChapterSerializer(queryset, many=True)
            obj_reading = serializer.data

        content = {
            'obj_reading': obj_reading,
            'obj_language': obj_language
        }
        return Response(content)
