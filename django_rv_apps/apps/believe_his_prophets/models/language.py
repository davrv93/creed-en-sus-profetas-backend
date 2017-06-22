
from django.db import models
from django.db.models.deletion import ProtectedError

class Language(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    name = models.CharField(
        unique=True, max_length=30,
        blank=False, null=False)
    translate_name = models.CharField(
        max_length=30,
        blank=True, null=True)
    code_iso = models.CharField(
        unique=True, max_length=2,
        blank=False, null=False,
        default='ES')


    class Meta:
        verbose_name = 'Language'
        db_table = 'believe_language'
        verbose_name_plural = 'Language'
        default_permissions = ()
        permissions = (
            ('add_language',
             'Puede agregar Language'),
            ('change_language',
             'Puede actualizar Language'),
            ('delete_language',
             'Puede eliminar Language'),
            ('list_language',
             'Puede listar Language'),
            ('get_language',
             'Puede obtener Language'),
            ('listform_language',
              'Puede listar Language en Formularios'),
        )

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        try:
            super(Language, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return self.name