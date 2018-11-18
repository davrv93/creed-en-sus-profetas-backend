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
            from requests.packages.urllib3.exceptions import InsecureRequestWarning

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

            data.update(
                audio=audio_io
            )

            serializer = AudioSerializer(instance,data=data, partial=True)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            retorno = serializer.data


        return Response(data=retorno)