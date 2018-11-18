from rest_framework.response import Response

from rest_framework.decorators import action

from django_rv_apps.apps.believe_his_prophets.models.chapter import  Chapter

from django_rv_apps.apps.believe_his_prophets.models.verse import  Verse

from django_rv_apps.apps.believe_his_prophets_api.views.chapter.serializers import AudioSerializer

class AudioMixin(object):

    @action(url_path='audio', methods=['GET'], detail=True)
    def audio(self, request, pk=None):

        instance = self.get_queryset().get(pk=pk)
        retorno = dict()

        if instance.audio:
            retorno.update(
                url=instance.audio.url
            )
        else:

            import requests
            from gtts import gTTS
            from io import BytesIO
            from pydub import AudioSegment
            from requests.packages.urllib3.exceptions import InsecureRequestWarning
            from pydub.utils import which
            from django.core.files.base import ContentFile

            #AudioSegment.converter = which("ffmpeg")

            verses = Verse.objects.filter(
                book=instance.book_id,
                chapter=instance.chapter,
                language__code_iso=instance.language.code_iso).values_list('data',flat=True)


            verses = ' '.join([x for x in verses])


            data = dict()

            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

            audio_io = BytesIO()

            tts = gTTS(text=verses, lang='es')
            tts.write_to_fp(audio_io)

            name = str(instance.book_id) + '_' + str(instance.chapter)+'_'+str(instance.language.code_iso)

            file = ContentFile(audio_io.getvalue())

            audio =  AudioSegment.from_file(file, format="mp3")

            instance.audio.save(name,audio)


            serializer = AudioSerializer(instance)

            retorno = serializer.data


        return Response(data=retorno)