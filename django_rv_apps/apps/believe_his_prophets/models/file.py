
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
