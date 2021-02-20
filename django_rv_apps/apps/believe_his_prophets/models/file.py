
from django.db import models

from .book import Book
from .language import Language

from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class File(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    contenido = models.TextField(

    )
    
    audio = models.FileField(
        blank=True, null=True,
        upload_to = 'audios/', storage = gd_storage)

    class Meta:
        verbose_name = 'File'
        db_table = 'believe_file'
        verbose_name_plural = 'Files'


    def save(self, *args, **kwargs):
        if 'contenido' in kwargs:
            contenido=kwargs['contenido']

            import requests
            from django.core.files.base import ContentFile
            from gtts import gTTS
            from io import BytesIO
            from pydub import AudioSegment
            from pydub.utils import which
            from requests.packages.urllib3.exceptions import InsecureRequestWarning



        
            verses = contenido

            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

            audio_io = BytesIO()

            final_io = BytesIO()

            tts = gTTS(text=verses, lang='es',)

            tts.write_to_fp(audio_io)

            name = 'testfile.mp3'

            file = ContentFile(audio_io.getvalue())

            

            #mp3_file = AudioSegment.from_file(file, format="mp3")

            #slow_sound = speed_change(mp3_file, 0.98)

            #final_audio = slow_sound.export(name,format="mp3")

            self.audio.save(name,file)


       
        super(File, self).save(*args, **kwargs)
