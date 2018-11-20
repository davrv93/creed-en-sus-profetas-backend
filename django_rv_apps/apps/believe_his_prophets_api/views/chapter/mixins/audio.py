from rest_framework.response import Response

from rest_framework.decorators import action

from django_rv_apps.apps.believe_his_prophets.models.chapter import  Chapter

from django_rv_apps.apps.believe_his_prophets.models.verse import  Verse

from django_rv_apps.apps.believe_his_prophets_api.views.chapter.serializers import AudioSerializer

class AudioMixin(object):

    @action(url_path='audio', methods=['GET'], detail=True)
    def audio(self, request, pk=None):

        def speed_change(sound, speed=1.0):
            # Manually override the frame_rate. This tells the computer how many
            # samples to play per second
            sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
                "frame_rate": int(sound.frame_rate * speed)
            })

            # convert the sound with altered frame rate to a standard frame rate
            # so that regular playback programs will work right. They often only
            # know how to play audio at standard frame rate (like 44.1k)
            return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

        instance = self.get_queryset().get(pk=pk)
        retorno = dict()

        if instance.audio:
            retorno.update(
                url=instance.audio.url
            )
        else:

            import requests
            from django.core.files.base import ContentFile
            from gtts import gTTS
            from io import BytesIO
            from pydub import AudioSegment
            from pydub.utils import which
            from requests.packages.urllib3.exceptions import InsecureRequestWarning



            code_iso = str(instance.language.code_iso).lower()

            #AudioSegment.converter = which("ffmpeg")

            verses = Verse.objects.filter(
                book=instance.book_id,
                chapter=instance.chapter,
                language__code_iso=instance.language.code_iso).values_list('data',flat=True)


            verses = ' '.join([x for x in verses])

            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

            audio_io = BytesIO()

            final_io = BytesIO()

            tts = gTTS(text=verses, lang=code_iso,)

            tts.write_to_fp(audio_io)

            name = str(instance.book_id) + '_' + str(instance.chapter)+'_'+str(instance.language.code_iso)+'.mp3'

            file = ContentFile(audio_io.getvalue())

            mp3_file = AudioSegment.from_file(file, format="mp3")

            slow_sound = speed_change(mp3_file, 0.98)

            final_audio = slow_sound.export(name,format="mp3")

            instance.audio.save(name,final_audio)

            serializer = AudioSerializer(instance)

            retorno = serializer.data


        return Response(data=retorno)