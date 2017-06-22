from uuid import uuid4

from django.db import models
from django.db.models.deletion import ProtectedError

class Testament(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    name = models.CharField(
        unique=True, max_length=30,
        blank=False, null=False)
    abrev = models.CharField(
        max_length=20,
        blank=False, null=False)
    translate_abrev = models.CharField(
        max_length=50,
        blank=False, null=False)
    translate_name = models.CharField(
        max_length=50,
        blank=True, null=True)


    class Meta:
        verbose_name = 'Testament'
        db_table = 'believe_testament'
        verbose_name_plural = 'Testament'
        default_permissions = ()
        permissions = (
            ('add_testament',
             'Puede agregar Testament'),
            ('change_testament',
             'Puede actualizar Testament'),
            ('delete_testament',
             'Puede eliminar Testament'),
            ('list_testament',
             'Puede listar Testament'),
            ('get_testament',
             'Puede obtener Testament'),
            ('listform_testament',
              'Puede listar Testament en Formularios'),
        )

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        try:
            super(Testament, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return self.name