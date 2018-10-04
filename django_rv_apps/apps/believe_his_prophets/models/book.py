
from django.db import models
from django.db.models.deletion import ProtectedError
from .testament import Testament

class Book(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    testament = models.ForeignKey(
        Testament, db_column='testament_id',
        blank=False, null=False,
        on_delete=models.PROTECT)
    name = models.CharField(
        max_length=30,
        blank=False, null=False)
    abrev = models.CharField(
        max_length=15,
        blank=False, null=False)
    translate_abrev = models.CharField(
        max_length=50,
        blank=True, null=True)
    translate_name = models.CharField(
        max_length=50,
        blank=True, null=True)
    book_order = models.IntegerField(
        blank=False,null=False)


    class Meta:
        verbose_name = 'Book'
        db_table = 'believe_book'
        verbose_name_plural = 'Book'
        default_permissions = ()
        permissions = (
            ('add_book',
             'Puede agregar Book'),
            ('change_book',
             'Puede actualizar Book'),
            ('delete_book',
             'Puede eliminar Book'),
            ('list_book',
             'Puede listar Book'),
            ('get_book',
             'Puede obtener Book'),
            ('listform_book',
              'Puede listar Book en Formularios'),
        )

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        try:
            super(Book, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return self.name