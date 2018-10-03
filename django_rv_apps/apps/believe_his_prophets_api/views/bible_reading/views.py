import unicodedata
from datetime import datetime

from django_filters import rest_framework as django_filters
from rest_framework import filters, serializers, status, viewsets
from rest_framework.decorators import list_route
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from django_rv_apps.apps.believe_his_prophets.models.bible_read import \
    BibleRead
from django_rv_apps.apps.believe_his_prophets.models.book import Book
from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter
from django_rv_apps.apps.believe_his_prophets.models.commentary_verse import \
    CommentaryVerse
from django_rv_apps.apps.believe_his_prophets.models.verse import Verse
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.serializers import (BookSerializer,
                                                                                          VerseSerializer,
                                                                                          ChapterSerializer)

from .filters import BibleReadFilter


class ReadingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BibleRead.objects.all()
    serializer_class = VerseSerializer
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend,)
    filterset_class = BibleReadFilter
    filter_fields = ('id','book','chapter','verse')
    search_fields = ('verse',)

    @list_route(url_path='reading')
    def list_reading_verse(self, request):
        # Declarando variables e instanciando
        def remove_accents(data):
            return unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')

        reading={}
        book={}
        chapter={}
        retorno={}
        
        # Obteniendo fecha por defecto
        p_date=request.query_params.get('date',None)
        i = datetime.now()
        datenow=i.strftime('%Y-%m-%d')
        
        if p_date:
            datenow=p_date
            print('p_date', datenow)
            
        # Obteniendo idioma
        language=request.query_params.get('language','EN')

        
        reading=BibleRead.objects.filter(start_date=datenow).first()
        

        if reading:
            # Get de Verse
            queryset = Verse.objects.filter(
                            book=reading.book_id,
                            chapter=reading.start_chapter,
                            language__code_iso=language)

            serializer = VerseSerializer(queryset, many=True)
            verse=serializer.data

            for x in verse:
                x['data_clean']=remove_accents(x['data'])

            retorno['verse']=verse

            # Get de Book
            queryset= Book.objects.filter(id=reading.book_id).first()

            serializer= BookSerializer(queryset)
            book=serializer.data
            retorno['book']=book


            # Get de Chapter
            queryset = Chapter.objects.filter(
                                        book_id=reading.book_id,
                                        chapter=reading.start_chapter,
                                        language__code_iso=language).first()

            serializer= ChapterSerializer(queryset)
            chapter=serializer.data
            retorno['chapter']=chapter

        return Response(retorno)
