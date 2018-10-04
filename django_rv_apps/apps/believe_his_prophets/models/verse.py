
from django.db import models
from django.db.models.deletion import ProtectedError
from .book import Book
from .language import Language

class Verse(models.Model):
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
    verse = models.IntegerField(
        blank=False, null=False)
    data = models.TextField(
        blank=False, null=False)
    highlight = models.IntegerField(
        blank=True, null=True)
    audio = models.FileField(
        blank=True, null=True)

    class Meta:
        verbose_name = 'Verse'
        db_table = 'believe_verse'
        ordering=('book__book_order','chapter','verse',)
        verbose_name_plural = 'Verse'
        default_permissions = ()
        permissions = (
            ('add_verse',
             'Puede agregar Verse'),
            ('change_verse',
             'Puede actualizar Verse'),
            ('delete_verse',
             'Puede eliminar Verse'),
            ('list_verse',
             'Puede listar Verse'),
            ('get_verse',
             'Puede obtener Verse'),
            ('listform_verse',
              'Puede listar Verse en Formularios'),
        )

    def __str__(self):
        return (self.book.__str__() + '-' + str(self.chapter)
                +':'+ str(self.verse))

    def delete(self, *args, **kwargs):
        try:
            super(Verse, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return (self.book.__str__() + '-' + self.chapter
                + self.verse)