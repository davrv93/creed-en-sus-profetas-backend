from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.exceptions import ParseError
from django_rv_apps.apps.believe_his_prophets.models.language import Language
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_chapter import SpiritProphecyChapter
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_read import SpiritProphecyRead
from django_rv_apps.apps.believe_his_prophets_api.views.spirit_prophecy_view import SpiritProphecySerializer
from django_rv_apps.apps.believe_his_prophets_api.views.spirit_prophecy_chapter_view import SpiritProphecyChapterSerializer
from django_rv_apps.apps.believe_his_prophets_api.views.language_view import LanguageSerializer



from django_filters import rest_framework as django_filters
from rest_framework import filters
from datetime import datetime

class SpiritProphecyReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpiritProphecyRead
        fields=('id','spirit_prophecy','spirit_prophecy_chapter',
        'spirit_prophecy_chapter__chapter',
        'data','date_read','language')

class SpiritProphecyReadViewSet(viewsets.ModelViewSet):
    queryset = SpiritProphecyRead.objects.all()
    serializer_class = SpiritProphecyReadSerializer
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend,)
    filter_fields = ('id','date_read')
    search_fields = ('date_read')

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

        except SpiritProphecyRead.DoesNotExist:
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
        if param_language=='':
            param_language='ES'
        queryset_language = Language.objects.get(code_iso=param_language)
        serializer_language= LanguageSerializer(queryset_language,
                                    many=False)
        obj_language=serializer_language.data
        obj_reading=SpiritProphecyRead.objects.filter(language=obj_language['id'],
                        date_read=datenow).values()
        print('obj_reading',obj_reading)

        if obj_reading:
            # Get de Chapter
            queryset= SpiritProphecyChapter.objects.get(spirit_prophecy=obj_reading[0]['spirit_prophecy_id'],id=obj_reading[0]['spirit_prophecy_chapter_id'])
            print('queryset spirit',queryset)
            serializer_chapter= SpiritProphecyChapterSerializer(queryset,many=False)
            obj_chapter=serializer_chapter.data
            queryset = SpiritProphecy.objects.get(id=obj_reading[0]['spirit_prophecy_id'])
            serializer_book= SpiritProphecySerializer(queryset,many=False)
            obj_book=serializer_book.data
            print('obj_book',obj_book)
            # Build de Header
            obj_header={
                'book_name': obj_book['translate_name'],
                'book':obj_book['name'],
                #'chapter':str(reading[0]['start_chapter'])
            }

        content={
            'obj_reading': obj_reading,
            'obj_chapter': obj_chapter,
            'obj_header': obj_header,
            'obj_language':obj_language
        }
        return Response(content)
