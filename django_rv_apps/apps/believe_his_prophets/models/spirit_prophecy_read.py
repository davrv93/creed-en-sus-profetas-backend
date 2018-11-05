
from django.db import models
from django.db.models.deletion import ProtectedError
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_chapter import SpiritProphecyChapter
from django_rv_apps.apps.believe_his_prophets.models.language import Language


class SpiritProphecyRead(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    spirit_prophecy_chapter = models.ForeignKey(
        SpiritProphecyChapter,
        db_column='spirit_prophecy_chapter_id',
        blank=True, null=True,
        on_delete=models.PROTECT)
    data = models.TextField(
        blank=False, null=False)
    date = models.DateField(
        blank=True, null=True)
    language = models.ForeignKey(
        Language, db_column='language_id',
        blank=True, null=True,
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'SpiritProphecyRead'
        db_table = 'believe_spirit_prophecy_read'
        verbose_name_plural = 'SpiritProphecyRead'
        default_permissions = ()
        permissions = (
            ('add_spiritprophecy',
             'Puede agregar SpiritProphecyRead'),
            ('change_spiritprophecy',
             'Puede actualizar SpiritProphecyRead'),
            ('delete_spiritprophecy',
             'Puede eliminar SpiritProphecyRead'),
            ('list_spiritprophecy',
             'Puede listar SpiritProphecyRead'),
            ('get_spiritprophecy',
             'Puede obtener SpiritProphecyRead'),
            ('listform_spiritprophecy',
             'Puede listar SpiritProphecyRead en Formularios'),
        )

    def __str__(self):
        return (self.spirit_prophecy_chapter.__str__() + '-'+str(self.date))
