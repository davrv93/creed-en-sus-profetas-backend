
from django.db import models
from django.db.models.deletion import ProtectedError
from django_rv_apps.apps.believe_his_prophets.models.language import Language


class SpiritProphecy(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    name = models.CharField(
        max_length=150,
        blank=False, null=False)
    language = models.ManyToManyField(
        'SpiritProphecyLanguage', blank=True,
        related_name='spirit_prophecy_language_set'

    )

    class Meta:
        verbose_name = 'SpiritProphecy'
        db_table = 'believe_spirit_prophecy'
        verbose_name_plural = 'SpiritProphecy'

    def __str__(self):
        return (self.name)


class SpiritProphecyLanguage(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    name = models.CharField(
        max_length=200,
        blank=False, null=False)
    spirit_prophecy = models.ForeignKey(
        'SpiritProphecy', db_column='spirit_prophecy_id',
        related_name='spirit_prophecy_language_spirit_prophecy_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    language = models.ForeignKey(
        Language, db_column='language_id',
        related_name='spirit_prophecy_language_language_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    translate_abrev = models.CharField(
        max_length=200,
        blank=True, null=True)
    translate_name = models.CharField(
        max_length=200,
        blank=True, null=True)

    class Meta:
        verbose_name = 'SpiritProphecyLanguage'
        db_table = 'believe_spirit_prophecy_lang'
        verbose_name_plural = 'SpiritProphecyLanguage'
