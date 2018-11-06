
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

    def __str__(self):
        return (self.spirit_prophecy_chapter.__str__() + '-'+str(self.date))
