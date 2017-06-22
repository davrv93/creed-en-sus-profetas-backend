
from django.db import models
from django.db.models.deletion import ProtectedError
from .book import Book

class BibleRead(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    start_date = models.DateField(
        blank=False, null=False
        )
    book = models.ForeignKey(
        Book, db_column='book_id',
        blank=False, null=False)
    start_chapter = models.IntegerField(
        blank=False, null=False)
    end_chapter = models.IntegerField(
        blank=False, null=False)

    class Meta:
        verbose_name = 'BibleRead'
        db_table = 'bible_read'
        verbose_name_plural = 'BibleRead'
        default_permissions = ()
        permissions = (
            ('add_bibleread',
             'Puede agregar BibleRead'),
            ('change_bibleread',
             'Puede actualizar BibleRead'),
            ('delete_bibleread',
             'Puede eliminar BibleRead'),
            ('list_bibleread',
             'Puede listar BibleRead'),
            ('get_bibleread',
             'Puede obtener BibleRead'),
            ('listform_bibleread',
              'Puede listar BibleRead en Formularios'),
        )

    def __str__(self):
        return (self.book.__str__() +
                str(self.start_chapter))

    def delete(self, *args, **kwargs):
        try:
            super(Book, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return (self.book.__str__() +
                str(self.start_chapter))