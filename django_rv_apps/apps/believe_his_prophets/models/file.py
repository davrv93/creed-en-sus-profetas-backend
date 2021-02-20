
from django.db import models

from .book import Book
from .language import Language
from django.db.models.signals import post_save
from django.dispatch import receiver
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
        upload_to = 'audios/', storage=gd_storage)

    class Meta:
        verbose_name = 'File'
        db_table = 'believe_file'
        verbose_name_plural = 'Files'

@receiver(post_save, sender=File)
def post_save(sender, instance=None, created=False, **kwargs):

    if not instance:
        return

    if hasattr(instance, '_dirty'):
        return

    contenido=instance.contenido

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


    try:
        instance._dirty = True
        instance.audio.save(name,file)

    finally:
        del instance._dirty
