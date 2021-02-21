from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

import pyttsx3

from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

from django_rv_apps.apps.believe_his_prophets.models.verse import Verse
from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter
from django_rv_apps.apps.believe_his_prophets.models.file import File
from django_rv_apps.apps.believe_his_prophets.models.language import Language
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.serializers\
    import BibleReadSerializer
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.filters \
    import BibleReadFilter
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.mixins.reading \
    import ReadingMixin
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.mixins.picture \
    import PictureMixin
from django_rv_apps.apps.believe_his_prophets_api.views.chapter.serializers import AudioSerializer
from django_rv_apps.apps.believe_his_prophets_api.views.chapter.serializers import FileSerializer

from django_rv_apps.apps.believe_his_prophets_api.views.verse.serializers import VerseSerializer

from django_rv_apps.apps.believe_his_prophets_api.views.book.serializers import BookSerializer

class ReadingViewSet(viewsets.ModelViewSet, ReadingMixin, PictureMixin):

    queryset = BibleRead.objects.all()
    serializer_class = BibleReadSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = BibleReadFilter

    def paginate_queryset(self, queryset):
        if self.paginator and self.request.query_params.get(self.paginator.page_query_param, None) is None:
            return None
        return super().paginate_queryset(queryset)


class BibleReadingView(APIView):
    #authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = ()

    def get(self, request, format=None):

        retorno = dict()

        date = request.query_params.get('date')

        code_iso = request.query_params.get('code_iso','').upper()

        bible_read = BibleRead.objects.get(start_date=date)

        book = bible_read.book

        serializer = BookSerializer(book, context={
            'code_iso':code_iso
        })

        retorno.update(
            book=serializer.data
        )

        chapter = bible_read.start_chapter

        retorno.update(
            chapter=chapter
        )

        verses = Verse.objects.filter(
            book=book,
            language__code_iso = code_iso,
            chapter = chapter
        )

        serializer = VerseSerializer(
            verses, many=True
        )

        retorno.update(
            verses=serializer.data
        )

        language = Language.objects.get(code_iso=code_iso)



        i_chapter, condition = Chapter.objects.get_or_create(
            book=book,
            language=language,
            chapter=chapter
        )

        print(i_chapter,'i_chapter')

        retorno.update(
            chapter_id=i_chapter.id
        )


        return Response(retorno)

class AudioView(APIView):
    #authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = ()

    def get(self, request, format=None):


        import requests
        from django.core.files.base import ContentFile
        from gtts import gTTS
        from io import BytesIO
        from pydub import AudioSegment
        from pydub.utils import which
        from requests.packages.urllib3.exceptions import InsecureRequestWarning
        import uuid
        import os

        PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
        module_dir = os.path.dirname(__file__)  # get current directory

        filename = str(uuid.uuid4())
        engine = pyttsx3.init()
        engine.setProperty('rate', 110)
        engine.setProperty('voice', 'spanish')
        engine.setProperty('volume', 1)
        nombre = filename+".mp3"

        engine.save_to_file(text="Hola que tal",filename=nombre)
        engine.runAndWait()
        file_path = os.path.join(PROJECT_PATH, nombre)
        from os.path import basename
        from django.core.files import File as File2

        instance = File()

        instance.save


        instance.audio.save(basename(file_path), content=File2(open(file_path, 'rb')))

        serializer = FileSerializer(instance)

        retorno = serializer.data

        return Response(data=retorno)

    @csrf_exempt
    def post(self, request, format=None):
        '''
        import requests
        from django.core.files.base import ContentFile
        from gtts import gTTS
        from io import BytesIO
        from pydub import AudioSegment
        from pydub.utils import which
        from requests.packages.urllib3.exceptions import InsecureRequestWarning
        import uuid
        import os

        PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
        module_dir = os.path.dirname(__file__)  # get current directory

        filename = str(uuid.uuid4())
        engine = pyttsx3.init()
        engine.setProperty('rate', 110)
        engine.setProperty('voice', 'spanish')
        engine.setProperty('volume', 1)
        nombre = filename+".mp3"
        verses = request.data.get("contenido", "")

        engine.save_to_file(text=verses,filename=nombre)
        engine.runAndWait()
        file_path = os.path.join(PROJECT_PATH, nombre)
        from os.path import basename
        from django.core.files import File as File2

        instance = File()
        import time


        instance.save

        time.sleep(3)


        instance.audio.save(basename(file_path), content=File2(open(file_path, 'rb')))

        serializer = FileSerializer(instance)

        retorno = serializer.data

        return Response(data=retorno)
        '''


        import requests
        from django.core.files.base import ContentFile
        from gtts import gTTS
        from io import BytesIO
        from pydub import AudioSegment
        from pydub.utils import which
        from requests.packages.urllib3.exceptions import InsecureRequestWarning


        verses = request.data.get("contenido", "")

        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        audio_io = BytesIO()

        final_io = BytesIO()

        tts = gTTS(text=verses, lang='es',)

        tts.write_to_fp(audio_io)

        name = 'testfile.mp3'

        file = ContentFile(audio_io.getvalue())

        instance = File()

        instance.save

        #mp3_file = AudioSegment.from_file(file, format="mp3")

        #slow_sound = speed_change(mp3_file, 0.98)

        #final_audio = slow_sound.export(name,format="mp3")

        instance.audio.save(name,file)

        serializer = FileSerializer(instance)

        retorno = serializer.data


        return Response(data=retorno)