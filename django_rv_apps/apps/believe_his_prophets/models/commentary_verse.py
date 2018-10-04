
from django.db import models
from django.db.models.deletion import ProtectedError
from .verse import Verse
from .language import Language

class CommentaryVerse(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    verse = models.ForeignKey(
        Verse, db_column='verse_id',
        related_name='commentary_verse_verse_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    order = models.IntegerField(
        blank=False, null=False)
    word = models.CharField(
        max_length=150,
        blank=False,null=False)
    data = models.TextField(
        blank=False, null=False)
    audio = models.FileField(
        blank=True, null=True)

    class Meta:
        verbose_name = 'CommentaryVerse'
        db_table = 'believe_commentary_verse'
        ordering=('verse__book__book_order','verse__chapter','verse__verse','order',)
        verbose_name_plural = 'CommentaryVerse'
        default_permissions = ()
        permissions = (
            ('add_commentaryverse',
             'Puede agregar CommentaryVerse'),
            ('change_commentaryverse',
             'Puede actualizar CommentaryVerse'),
            ('delete_commentaryverse',
             'Puede eliminar CommentaryVerse'),
            ('list_commentaryverse',
             'Puede listar CommentaryVerse'),
            ('get_commentaryverse',
             'Puede obtener CommentaryVerse'),
            ('listform_commentaryverse',
              'Puede listar CommentaryVerse en Formularios'),
        )

    def __str__(self):
        return (self.verse.__str__() + '-' + str(self.word)
                +':'+ str(self.order) +'-'+str(self.verse.id))

    def delete(self, *args, **kwargs):
        try:
            super(CommentaryVerse, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return (self.verse.__str__() + '-' + str(self.word)
                +':'+ str(self.order))