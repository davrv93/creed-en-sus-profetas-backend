from uuid import uuid4
from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list


class HierarchyType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    name = models.CharField(
        max_length=60,
        blank=False, null=False,
    )

    state = models.CharField(
        max_length=10,
        blank=True, null=True
    )
    connector = models.CharField(
        max_length=30, blank=True, null=True
    )
    abbreviation = models.CharField(
        max_length=10, blank=True, null=True
    )
    code_hierarchy_type = models.CharField(
        max_length=50, blank=True, null=True
    )

    class Meta:
        verbose_name = _("hierarchy type")
        verbose_name_plural = _("hierarchy types")
        db_table = 'AUTH_XE_HIERARCHY_TYPE'
