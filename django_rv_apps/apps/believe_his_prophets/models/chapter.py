
from django.db import models

from .book import Book
from .language import Language

from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()


class Chapter(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    book = models.ForeignKey(
        Book, db_column='book_id',
        blank=False, null=False,
        on_delete=models.PROTECT)
    language = models.ForeignKey(
        Language, db_column='language_id',
        blank=False, null=False,
        on_delete=models.PROTECT)
    chapter = models.IntegerField(
        blank=False, null=False)

    audio = models.FileField(
        blank=True, null=True,
        upload_to = 'audios/', storage = gd_storage)

    commentary_html= models.TextField(
        blank=True, null=True
    )
    commentary = models.NullBooleanField(
        blank=True, null=True)
    commentary_file = models.FileField(
        blank=True, null=True)
    commentary_url = models.CharField(
        max_length=500,
        blank=True, null=True)

    class Meta:
        verbose_name = 'Chapter'
        db_table = 'believe_chapter'
        ordering=('book__book_order','chapter',)
        verbose_name_plural = 'Chapter'
        default_permissions = ()
        permissions = (
            ('add_chapter',
             'Puede agregar Chapter'),
            ('change_chapter',
             'Puede actualizar Chapter'),
            ('delete_chapter',
             'Puede eliminar Chapter'),
            ('list_chapter',
             'Puede listar Chapter'),
            ('get_chapter',
             'Puede obtener Chapter'),
            ('listform_chapter',
              'Puede listar Chapter en Formularios'),
        )

    def __str__(self):
        return (self.book.__str__() + '-' + str(self.chapter)
                + '-'+str(self.language.__str__())
               )
