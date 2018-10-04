
from django.db import models
from django.db.models.deletion import ProtectedError
from .book import Book
from .language import Language

class Commentary(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    book = models.ForeignKey(
        Book, db_column='verse_id',
        related_name='book_commentary_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    chapter= models.IntegerField(
        blank=True, null=True
        )
    file = models.FileField(
        blank=True, null=True
        )
    language = models.ForeignKey(
        Language, db_column='language_id',
        related_name='language_commentary_set',
        blank=True, null=True,
        on_delete=models.PROTECT
        )

    class Meta:
        verbose_name = 'Commentary'
        db_table = 'believe_commentary'
        ordering=('book__book_order','chapter',)
        verbose_name_plural = 'Commentary'
        default_permissions = ()
        permissions = (
            ('add_commentary',
             'Puede agregar Commentary'),
            ('change_commentary',
             'Puede actualizar Commentary'),
            ('delete_commentary',
             'Puede eliminar Commentary'),
            ('list_commentary',
             'Puede listar Commentary'),
            ('get_commentary',
             'Puede obtener Commentary'),
            ('listform_commentary',
              'Puede listar Commentary en Formularios'),
        )

    def __str__(self):
        return (self.book.__str__() + ' ' + str(self.chapter) + ' ' + self.language.__str__() )

    def delete(self, *args, **kwargs):
        try:
            super(Commentary, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return (self.verse.__str__() + '-' + str(self.word)
                +':'+ str(self.order))