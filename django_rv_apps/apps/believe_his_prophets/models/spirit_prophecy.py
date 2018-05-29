
from django.db import models
from django.db.models.deletion import ProtectedError
from django_rv_apps.apps.believe_his_prophets.models.language import Language

class SpiritProphecy(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    name = models.CharField(
        max_length=30,
        blank=False, null=False)
    abrev = models.CharField(
        max_length=15,
        blank=True, null=True)
    translate_abrev = models.CharField(
        max_length=50,
        blank=True, null=True)
    translate_name = models.CharField(
        max_length=50,
        blank=True, null=True)
    language = models.ForeignKey(
        Language, db_column='language_id',
        blank=True, null=True)

    class Meta:
        verbose_name = 'SpiritProphecy'
        db_table = 'believe_spirit_prophecy'
        verbose_name_plural = 'SpiritProphecy'
        default_permissions = ()
        permissions = (
            ('add_spiritprophecy',
             'Puede agregar SpiritProphecy'),
            ('change_spiritprophecy',
             'Puede actualizar SpiritProphecy'),
            ('delete_spiritprophecy',
             'Puede eliminar SpiritProphecy'),
            ('list_spiritprophecy',
             'Puede listar SpiritProphecy'),
            ('get_spiritprophecy',
             'Puede obtener SpiritProphecy'),
            ('listform_spiritprophecy',
              'Puede listar SpiritProphecy en Formularios'),
        )

    def __str__(self):
        return (self.name)

    def delete(self, *args, **kwargs):
        try:
            super(SpiritProphecy, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return (self.name)