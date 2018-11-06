
from django.db import models
from django.db.models.deletion import ProtectedError
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy
from django_rv_apps.apps.believe_his_prophets.models.language import Language


class SpiritProphecyChapter(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    spirit_prophecy = models.ForeignKey(
        SpiritProphecy,
        db_column='spirit_prophecy_id',
        blank=False, null=False,
        on_delete=models.PROTECT)
    chapter = models.IntegerField(
        blank=True, null=True)
    language = models.ManyToManyField(
        Language,
        through='SpiritProphecyChapterLanguage', blank=True,
        related_name='spirit_prophecy_language_chapter_set'
    )
    start_date = models.DateField(
        blank=True, null=True
    )
    end_date = models.DateField(
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'SpiritProphecyChapter'
        db_table = 'believe_spirit_prophecy_chapter'
        verbose_name_plural = 'SpiritProphecyChapter'

    def __str__(self):
        return (self.spirit_prophecy.__str__() + ' ' + str(self.chapter))


class SpiritProphecyChapterLanguage(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    name = models.CharField(
        max_length=250,
        blank=False, null=False)
    spirit_prophecy_chapter = models.ForeignKey(
        'SpiritProphecyChapter', db_column='spirit_prophecy_chapter_id',
        related_name='spirit_prophecy_chapter_language_spirit_prophecy_chapter_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    language = models.ForeignKey(
        Language, db_column='language_id',
        related_name='spirit_prophecy_chapter_language_language_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    data = models.TextField(
        blank=False, null=False)

    class Meta:
        verbose_name = 'SpiritProphecyChapterLanguage'
        verbose_name_plural = 'SpiritProphecyChapterLanguage'
        db_table = 'believe_spirit_pr_chapter_lang'
