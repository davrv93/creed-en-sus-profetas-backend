
from django.db import models
from django.db.models.deletion import ProtectedError
from .language import Language

class Application(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    version=models.CharField(
      max_length=10,
      blank=False, null=False
    )
    code=models.IntegerField(
      blank=False, null=False
    )
    content=models.TextField(
      blank=False, null=False
    )
    language = models.ForeignKey(
        Language,
        blank=False, null=False,
        db_column='language_id')
    is_active= models.CharField(
        max_length=1,
        blank=False, null=False,
        default='1'
    )

    class Meta:
        verbose_name = 'Application'
        db_table = 'believe_application'
        ordering=('version',)
        verbose_name_plural = 'Application'
        default_permissions = ()
        permissions = (
            ('add_application',
             'Puede agregar Application'),
            ('change_application',
             'Puede actualizar Application'),
            ('delete_application',
             'Puede eliminar Application'),
            ('list_application',
             'Puede listar Application'),
            ('get_application',
             'Puede obtener Application'),
            ('listform_application',
              'Puede listar Application en Formularios'),
        )

    def __str__(self):
        return  self.version

    def delete(self, *args, **kwargs):
        try:
            super(Application, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return self.version
