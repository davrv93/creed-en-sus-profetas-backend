from uuid import uuid4
from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list


class Sucursal(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    nombre = models.CharField(
        max_length=100,
        blank=False, null=False,
    )

    direccion = models.CharField(
        max_length=300,
        blank=False, null=False,
    )

    referencia = models.CharField(
        max_length=300,
        blank=False, null=False,
    )

    latitud = models.CharField(
        max_length=500,
        blank=False, null=False,
    )
    longitud = models.CharField(
        max_length=500,
        blank=False, null=False,
    )
    estado = models.CharField(
        max_length=2,
        blank=True, null=True
    )
    tipo_sucursal = models.UUIDField(
        db_column='tipo_sucursal_id',
        blank=True, null=True
    )
    ubigeo = models.UUIDField(
        db_column='ubigeo_id',
        blank=True, null=True
    )

    class Meta:
        verbose_name = "sucursal"
        verbose_name_plural = "sucursal"
        db_table = 'AUTH_XE_SUCURSAL'
        ordering = ('nombre',)

    def __str__(self):
        return str(self.nombre)
