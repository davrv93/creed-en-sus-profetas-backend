from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.exceptions import ParseError
from django_rv_apps.apps.believe_his_prophets.models.verse import Verse
from django_rv_apps.apps.believe_his_prophets.models.book import Book
from django_rv_apps.apps.believe_his_prophets.models.analysis_verse import AnalysisVerse
from django_rv_apps.apps.believe_his_prophets.models.analysis_chapter import AnalysisChapter
from django_rv_apps.apps.believe_his_prophets.models.sentiment import Sentiment
from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter
from django_rv_apps.apps.believe_his_prophets.models.language import Language
from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
from django_rv_apps.apps.believe_his_prophets.models.commentary_verse import CommentaryVerse
from django_rv_apps.apps.believe_his_prophets_api.views.book_view import BookSerializer
from django_rv_apps.apps.believe_his_prophets_api.views.language_view import LanguageSerializer

from django_filters import rest_framework as django_filters
from rest_framework import filters
from datetime import datetime
import unicodedata
import numpy as np


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields='__all__'

class AnalysisVerseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnalysisVerse
        fields='__all__'

class AnalysisChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnalysisChapter
        fields='__all__'


class VerseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verse
        fields=('id','book','language',
        'chapter','verse','data','highlight')

class CommentaryVerseSerializer(serializers.ModelSerializer):
    verse_number= serializers.SerializerMethodField()

    class Meta:
        model = CommentaryVerse
        fields=('id','order','verse','verse_number','data','word')

    def get_verse_number(self, obj):
        verse_number=obj.verse.verse
        return verse_number

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
        obj_chapter={}
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

        def remove_accents(data):
            return unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')

        if reading:
            # Get de Verse
            queryset = Verse.objects.filter(book=reading[0]['book_id'],
                            chapter=reading[0]['start_chapter'],
                            language=obj_language['id'])
            serializer = VerseSerializer(queryset, many=True)
            obj_reading=serializer.data
            count=0
            for x in obj_reading:
                obj_reading[count]['data_clean']=remove_accents(
                    obj_reading[count]['data'])
                count+=1
            # Get de Book
            book= Book.objects.filter(id=reading[0]['book_id']).values().first()
            # Get de Chapter
            queryset = Chapter.objects.filter(book_id=reading[0]['book_id'],
                            chapter=reading[0]['start_chapter'],
                            language=obj_language['id'])
            if queryset:
                serializer_chapter= ChapterSerializer(queryset,many=True)
                obj_chapter=serializer_chapter.data
            # Build de Header
            obj_header={
                'book': book,
                'chapter':str(reading[0]['start_chapter'])
            }
        if obj_chapter:
            content={
                'obj_reading': obj_reading,
                'audio': obj_chapter[0]['audio'],
                'obj_header': obj_header,
                'obj_language':obj_language,
                'commentary':obj_chapter[0]['commentary_url']
            }
        else:
            content={
                'obj_reading': obj_reading,
                #'obj_book': obj_book,
                'obj_header': obj_header,
                'obj_language':obj_language
            }
        return Response(content)


    @list_route(url_path='status')
    def get_status(self, request):
        # Declarando variables e instanciando
        param_date=request.query_params.get('date','')
        if param_date:
            datenow=param_date
            print('param_date', datenow)
        else:
            i = datetime.now()
            datenow=i.strftime('%Y-%m-%d')
        # Obteniendo idioma
        reading=BibleRead.objects.filter(
                        start_date=datenow).count()

        return Response({'count':reading})


    @list_route(url_path='get_verses_from_chap')
    def get_verses_from_chap(self, request):
        # Declarando variables e instanciando
        total_verses=0
        obj_header={}
        distinct_verses=[]
        param_date=request.query_params.get('date','')
        if param_date:
            datenow=param_date
            print('param_date', datenow)
        else:
            i = datetime.now()
            datenow=i.strftime('%Y-%m-%d')
        param_language=request.query_params.get('language','')
        #param_language='ES'
        queryset_language = Language.objects.get(code_iso=param_language)
        serializer_language= LanguageSerializer(queryset_language,
                                    many=False)
        obj_language=serializer_language.data
        reading=BibleRead.objects.filter(
                        start_date=datenow).values()
        if reading:
            # Get de Verse
            total_verses = Verse.objects.filter(book=reading[0]['book_id'],
                            chapter=reading[0]['start_chapter'],
                            language=obj_language['id'])
            total_count=  total_verses.count()
            my_arange_list = np.arange(1,total_count+1)
            # Obteniendo versiculos distintos id
            distinct_verses = Verse.objects.filter(book=reading[0]['book_id'],
                            chapter=reading[0]['start_chapter'],
                            language=obj_language['id'],
                            commentary_verse_verse_set__verse__verse__in=my_arange_list
                            ).values('id','verse').distinct()
            print('distinct_verses',distinct_verses)
            # distinct_verses_numbers = Verse.objects.filter(book=reading[0]['book_id'],
            #                 chapter=reading[0]['start_chapter'],
            #                 language=obj_language['id'],
            #                 commentary_verse_verse_set__in=my_arange_list).values_list('verse').distinct()









            # list_commentary_verse= CommentaryVerse.objects.filter(
            #     verse__book__id=reading[0]['book_id'],
            #     verse__chapter=reading[0]['start_chapter'],
            #     verse__language=obj_language['id'],
            #     verse__verse__in=distinct_verses).values('verse').distinct()
            # print('list_commentary_verse',list_commentary_verse)
            # serializer_commentary_verse= CommentaryVerseSerializer(
            #     list_commentary_verse,
            #     many=True)
            #obj_commentary_verse=serializer_commentary_verse.data

            #print('obj_commentary_verse',obj_commentary_verse)

            # for x in list_commentary_verse:
            #     print('list_commentary_verse', x)

            # Get de Book
            queryset = Book.objects.get(id=reading[0]['book_id'])
            serializer_book= BookSerializer(queryset,many=False)
            obj_book=serializer_book.data
            # Build de Header
            obj_header={
                'book_name': obj_book['translate_name'],
                'chapter':str(reading[0]['start_chapter']),
                'verses':total_count,
                'obj_verses':distinct_verses
            }



        return Response(obj_header)


    @list_route(url_path='get_commentary_from_verse')
    def get_commentary_from_verse(self, request):
        # Declarando variables e instanciando
        obj_header={}
        list_obj_commentary_verse=[]
        param_verse=request.query_params.get('id','')
        if param_verse:
            list_commentary_verse= CommentaryVerse.objects.filter(
                verse=param_verse)
            print('list_commentary_verse',list_commentary_verse)
            serializer_commentary_verse= CommentaryVerseSerializer(
                list_commentary_verse,
                many=True)
            list_obj_commentary_verse=serializer_commentary_verse.data

            print('obj_commentary_verse',list_obj_commentary_verse)
        return Response(list_obj_commentary_verse)


    @list_route(url_path='csv_genesis')
    def csv_view(self,request):
        from djqscsv import render_to_csv_response
        qs = AnalysisChapter.objects.filter(book=1).values('id','book__name','chapter', 'sentiment__name','value')
        return render_to_csv_response(qs)




    @list_route(url_path='genesis_analysis')
    def get_genesis_analysis(self, request):
        # Declarando variables e instanciando
        verse=''
        lista=[]
        for chapter in range(1,51):
            verse=''
            result=Verse.objects.values('data','id').filter(book__id='1',chapter=chapter,language__code_iso='en')

            for x in result:
                verse=verse+' '+x['data']
                verse=verse.strip()

            import json
            from watson_developer_cloud import NaturalLanguageUnderstandingV1
            from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions,EmotionOptions
            from watson_developer_cloud import WatsonException

            natural_language_understanding = NaturalLanguageUnderstandingV1(
              username='ca406eea-09d4-4ba0-a71d-eb16d2b3cce0',
              password='HrABND5rQtpQ',
              version='2017-02-27')
            try:
                response = natural_language_understanding.analyze(
                  text=verse,
                  features=Features(
                     emotion= EmotionOptions(document=True),
                     sentiment=SentimentOptions(document=True)))

                aux=str(json.dumps(response)).replace('\"', '"')
                sentiment=json.loads(aux)
                score=None
                label=None
                sentiment_value=None
                if 'sentiment' in sentiment:
                    if 'document' in sentiment['sentiment']:
                        if 'score' in sentiment['sentiment']['document']:
                            score= sentiment['sentiment']['document']['score']
                        if 'label' in sentiment['sentiment']['document']:
                            label= sentiment['sentiment']['document']['label']
                            sentiment_value=Sentiment.objects.values().get(name=label)
                        if (score != None) and (label != None):
                            data={}
                            data['value']=score
                            data['sentiment']=sentiment_value['id']
                            data['chapter']=chapter
                            data['book']='1'
                            serializer = AnalysisChapterSerializer(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                #return Response(serializer.data)
                            else:
                                return Response({'error':serializer.errors})
                obj={}
                obj['sentiment']=sentiment
                obj['verse']=verse
                lista.append(obj)


            except WatsonException:
                # data['value']=None
                # data['sentiment']=None
                # data['verse']=x['id']
                # serializer = AnalysisVerseSerializer(data=data)
                # if serializer.is_valid():
                #     serializer.save()
                #     #return Response(serializer.data)
                # else:
                #     return Response({'error':serializer.errors})

                pass


        return Response({'msg':'ok','lista':lista})






    @list_route(url_path='get_analysis_verse')
    def get_commentary_from_verse(self, request):
        # Declarando variables e instanciando
        verses=Verse.objects.values('data','id').filter(book__id='1',language__code_iso='en').exclude(
            chapter__in=['36','37','38','39','40','41','42','43','44','45','46','47','48','49','50'])
        import json
        from watson_developer_cloud import NaturalLanguageUnderstandingV1
        from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions,EmotionOptions
        from watson_developer_cloud import WatsonException

        natural_language_understanding = NaturalLanguageUnderstandingV1(
          username='ca406eea-09d4-4ba0-a71d-eb16d2b3cce0',
          password='HrABND5rQtpQ',
          version='2017-02-27')
        for x in verses:
            try:
                response = natural_language_understanding.analyze(
                  text=x['data'],
                  features=Features(
                     sentiment=SentimentOptions(document=True)))

                aux=str(json.dumps(response)).replace('\"', '"')
                sentiment=json.loads(aux)
                score=None
                label=None
                sentiment_value=None
                if 'sentiment' in sentiment:
                    if 'document' in sentiment['sentiment']:
                        if 'score' in sentiment['sentiment']['document']:
                            score= sentiment['sentiment']['document']['score']
                        if 'label' in sentiment['sentiment']['document']:
                            label= sentiment['sentiment']['document']['label']
                            sentiment_value=Sentiment.objects.values().get(name=label)
                        if (score != None) and (label != None):
                            data={}
                            data['value']=score
                            data['sentiment']=sentiment_value['id']
                            data['verse']=x['id']
                            serializer = AnalysisVerseSerializer(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                #return Response(serializer.data)
                            else:
                                return Response({'error':serializer.errors})

            except WatsonException:
                data['value']=None
                data['sentiment']=None
                data['verse']=x['id']
                serializer = AnalysisVerseSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    #return Response(serializer.data)
                else:
                    return Response({'error':serializer.errors})

                pass


        return Response({'msg':'ok'})
