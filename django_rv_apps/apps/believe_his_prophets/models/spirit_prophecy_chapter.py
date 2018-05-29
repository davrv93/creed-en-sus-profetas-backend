
from django.db import models
from django.db.models.deletion import ProtectedError
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy
from django_rv_apps.apps.believe_his_prophets.models.language import Language

class SpiritProphecyChapter(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    spirit_prophecy = models.ForeignKey(
        SpiritProphecy,
        db_column='spirit_prophecy_id',
        blank=False, null=False)
    name = models.CharField(
        max_length=150,
        blank=False, null=False)
    translate_abrev = models.CharField(
        max_length=50,
        blank=True, null=True)
    translate_name = models.CharField(
        max_length=50,
        blank=True, null=True)
    language = models.ForeignKey(
        Language, db_column='language_id',
        blank=True, null=True)
    chapter = models.IntegerField(
        blank=True, null=True)

    class Meta:
        verbose_name = 'SpiritProphecyChapter'
        db_table = 'believe_spirit_prophecy_chapter'
        verbose_name_plural = 'SpiritProphecyChapter'
        default_permissions = ()
        permissions = (
            ('add_spiritprophecy',
             'Puede agregar SpiritProphecyChapter'),
            ('change_spiritprophecy',
             'Puede actualizar SpiritProphecyChapter'),
            ('delete_spiritprophecy',
             'Puede eliminar SpiritProphecyChapter'),
            ('list_spiritprophecy',
             'Puede listar SpiritProphecyChapter'),
            ('get_spiritprophecy',
             'Puede obtener SpiritProphecyChapter'),
            ('listform_spiritprophecy',
              'Puede listar SpiritProphecyChapter en Formularios'),
        )

    def __str__(self):
        return (self.spirit_prophecy.__str__() + ' ' + self.name + '-' + str(self.chapter))

    def delete(self, *args, **kwargs):
        try:
            super(SpiritProphecyChapter, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return (self.spirit_prophecy.__str__() + ' ' + self.name + '-' + str(self.chapter))