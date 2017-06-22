from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.exceptions import ParseError
from django_rv_apps.apps.believe_his_prophets.models.verse import Verse
from django_rv_apps.apps.believe_his_prophets.models.book import Book
from django_rv_apps.apps.believe_his_prophets.models.language import Language
from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
from django_rv_apps.apps.believe_his_prophets_api.views.book_view import BookSerializer
from django_rv_apps.apps.believe_his_prophets_api.views.language_view import LanguageSerializer

from django_filters import rest_framework as django_filters
from rest_framework import filters
from datetime import datetime

class VerseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verse
        fields=('id','book','language',
        'chapter','verse','data','highlight')

class VerseViewSet(viewsets.ModelViewSet):
    queryset = Verse.objects.all().prefetch_related('book','language')
    serializer_class = VerseSerializer
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend,)
    filter_fields = ('id','book','chapter','verse')
    search_fields = ('verse',)

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

        except Verse.DoesNotExist:
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
        obj_reading={}
        obj_book={}
        language=''
        # Obteniendo fecha por defecto
        param_date=request.query_params.get('date','')
        if param_date:
            datenow=param_date
            print('param_date', datenow)
        else:
            i = datetime.now()
            datenow=i.strftime('%Y-%m-%d')
        # Obteniendo idioma
        param_language=request.query_params.get('language','')
        queryset_language = Language.objects.get(code_iso=param_language)
        serializer_language= LanguageSerializer(queryset_language,
                                    many=False)
        obj_language=serializer_language.data
        reading=BibleRead.objects.filter(
                        start_date=datenow).values()

        if reading:
            # Get de Verse
            queryset = Verse.objects.filter(book=reading[0]['book_id'],
                            chapter=reading[0]['start_chapter'],
                            language=obj_language['id'])
            serializer = VerseSerializer(queryset, many=True)
            obj_reading=serializer.data
            # Get de Book
            queryset = Book.objects.get(id=reading[0]['book_id'])
            serializer_book= BookSerializer(queryset,many=False)
            obj_book=serializer_book.data
            # Build de Header
            obj_header={
                'book_name': obj_book['translate_name'],
                'chapter':str(reading[0]['start_chapter'])
            }

        content={
            'obj_reading': obj_reading,
            #'obj_book': obj_book,
            'obj_header': obj_header,
            'obj_language':obj_language
        }
        return Response(content)
