
from django.db import models
from django.db.models.deletion import ProtectedError
from .testament import Testament
from .verse import Verse

class SentimentalVerse(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    verse = models.ForeignKey(
        Verse, db_column='verse_id',
        blank=False, null=False)

    name = models.CharField(
        max_length=30,
        blank=False, null=False)
    abrev = models.CharField(
        max_length=15,
        blank=False, null=False)
    translate_abrev = models.CharField(
        max_length=50,
        blank=False, null=False)
    translate_name = models.CharField(
        max_length=50,
        blank=True, null=True)


    class Meta:
        verbose_name = 'Sentimental verse'
        db_table = 'believe_sentimental'
        verbose_name_plural = 'Sentimental verse'
        default_permissions = ()
        permissions = (
            ('add_sentimentalverse',
             'Puede agregar SentimentalVerse'),
            ('change_sentimentalverse',
             'Puede actualizar SentimentalVerse'),
            ('delete_sentimentalverse',
             'Puede eliminar SentimentalVerse'),
            ('list_sentimentalverse',
             'Puede listar SentimentalVerse'),
            ('get_sentimentalverse',
             'Puede obtener SentimentalVerse'),
            ('listform_sentimentalverse',
              'Puede listar SentimentalVerse en Formularios'),
        )

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        try:
            super(SentimentalVerse, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return self.name