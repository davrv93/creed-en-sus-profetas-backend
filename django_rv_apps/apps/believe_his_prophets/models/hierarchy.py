from uuid import uuid4
from datetime import datetime, timedelta
from django.db import models
# models

from .hierarchy_type import HierarchyType

from .entidad import Entidad

from .sucursal import Sucursal


class Hierarchy(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid4, editable=False)

    logo = models.ImageField(
        upload_to='logos',
        default='logo/default.png',
        null=True, blank=True
    )
    code = models.CharField(
        max_length=60, null=False,
        blank=False, unique=True
    )
    fiscal_creation_date = models.DateField(
        null=True, blank=True
    )
    fiscal_address = models.CharField(
        max_length=40,
        blank=True, null=True
    )
    resolution = models.CharField(
        max_length=60, null=True,
        blank=True
    )
    authorization = models.CharField(
        max_length=60, null=True, blank=True
    )
    is_active = models.BooleanField(
        default=True,
        null=False, blank=False
    )
    order = models.IntegerField(
        default=1
    )
    latitude = models.CharField(
        max_length=1000,
        blank=True, null=True
    )
    longitude = models.CharField(
        max_length=1000,
        blank=True, null=True
    )
    entity = models.ForeignKey(
        Entidad,
        blank=True, null=True,
        on_delete=models.PROTECT,
        db_column='entity_id'
    )

    parent = models.ForeignKey(
        'self', related_name='childrens',
        null=True, blank=True,
        db_column='parent_id',
        on_delete=models.PROTECT
    )
    sucursal = models.ForeignKey(
        Sucursal,
        db_column='sucursal_id',
        blank=True, null=True,
        on_delete=models.PROTECT
    )

    # hierarchy_type = models.ForeignKey(
    #     HierarchyType,
    #     db_column='hierarchy_type_id',
    #     null=False, blank=False,
    #     on_delete=models.PROTECT
    # )
    ubigeo = models.UUIDField(
        null=True, blank=True,
        db_column='ubigeo_id'
    )
    legal_person = models.UUIDField(
        null=True, blank=True,
        db_column='legal_person_id'
    )
    area_desempenio = models.UUIDField(
        null=True, blank=True,
        db_column='area_desempenio_id'
    )

    class Meta:
        verbose_name = "hierarchy"
        verbose_name_plural = "hierarchys"
        db_table = 'AUTH_XE_HIERARCHY'

    def __str__(self):
        return str(self.id)
