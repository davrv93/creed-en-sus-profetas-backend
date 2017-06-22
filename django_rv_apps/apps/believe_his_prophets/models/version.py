from uuid import uuid4

from django.db import models
from django.db.models.deletion import ProtectedError

class Version(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    name = models.CharField(
        unique=True, max_length=30,
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
        verbose_name = 'Version'
        db_table = 'believe_version'
        verbose_name_plural = 'Version'
        default_permissions = ()
        permissions = (
            ('add_version',
             'Puede agregar Version'),
            ('change_version',
             'Puede actualizar Version'),
            ('delete_version',
             'Puede eliminar Version'),
            ('list_version',
             'Puede listar Version'),
            ('get_version',
             'Puede obtener Version'),
            ('listform_version',
              'Puede listar Version en Formularios'),
        )

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        try:
            super(Version, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return self.name