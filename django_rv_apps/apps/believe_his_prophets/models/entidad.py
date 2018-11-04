from uuid import uuid4
from datetime import datetime, timedelta
from django.db import models
# models

from .hierarchy_type import HierarchyType


class Entidad(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid4, editable=False)

    nombre = models.CharField(
        max_length=60, null=False,
        blank=False
    )
    nombre_corto = models.CharField(
        max_length=60, null=False,
        blank=False
    )
    logo = models.ImageField(
        upload_to='entidad',
        default='logo/default.png',
        null=True, blank=True
    )
    estado = models.CharField(
        max_length=1,
        blank=True, null=True
    )
    hierarchy_type = models.ForeignKey(
        HierarchyType,
        db_column='hierarchy_type_id',
        null=False, blank=False,
        on_delete=models.PROTECT
    )
    nombre_variante = models.UUIDField(
        null=True, blank=True,
        db_column='nombre_variante_id'
    )

    class Meta:
        verbose_name = "entidad"
        verbose_name_plural = "entidad"
        db_table = 'AUTH_XE_ENTIDAD'

    def __str__(self):
        return str(self.nombre)
