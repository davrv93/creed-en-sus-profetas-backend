
from django.db import models
from django.db.models.deletion import ProtectedError
from .book import Book
from .emotion import Emotion
from .sentiment import Sentiment


class AnalysisChapter(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    book = models.ForeignKey(
        Book,
        db_column='book_id',
        blank=False,
        null=False)
    chapter= models.IntegerField(
        blank=False,
        null=False
        )
    sentiment= models.ForeignKey(
        Sentiment,
        db_column='sentiment_id',
        blank=True,
        null=True
    )
    value = models.DecimalField(
        null=True, blank=True,
        max_digits=38, decimal_places=10)
    emotion = models.ManyToManyField(
        Emotion,
        related_name='emotion_analysis_chapter_set',
        verbose_name='EmotionAnalysisChapter',
        through='EmotionAnalysisChapter')

    class Meta:
        verbose_name = 'Analysis chapter'
        db_table = 'believe_analysis_chapter'
        verbose_name_plural = 'Analysis Chapter'
        default_permissions = ()
        permissions = (
            ('add_analysischapter',
             'Puede agregar AnalysisChapter'),
            ('change_analysischapter',
             'Puede actualizar AnalysisChapter'),
            ('delete_analysischapter',
             'Puede eliminar AnalysisChapter'),
            ('list_analysischapter',
             'Puede listar AnalysisChapter'),
            ('get_analysischapter',
             'Puede obtener AnalysisChapter'),
            ('listform_analysischapter',
              'Puede listar AnalysisChapter en Formularios'),
        )

    def __str__(self):
        return self.book.__str__() + ' ' + str(self.chapter)

    def delete(self, *args, **kwargs):
        try:
            super(AnalysisChapter, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return self.name


class EmotionAnalysisChapter(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    emotion = models.ForeignKey(
        Emotion,
        db_column='emotion_id',
        related_name='emotion_emotion_analysis_chapter_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    analysis_chapter = models.ForeignKey(
        'AnalysisChapter',
        db_column='analysis_chapter_id',
        related_name='analysis_chapter_emotion_analysis_chapter_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    value = models.DecimalField(
        null=True, blank=True,
        max_digits=38, decimal_places=2)

    class Meta:
        verbose_name = 'EmotionAnalysisChapter'
        verbose_name_plural = 'EmotionAnalysisChapter'
        db_table = 'believe_em_an_chapter'
        default_permissions = ()
        permissions = (
            ('add_emotionanalysischapter',
             'Puede agregar EmotionAnalysisChapter'),
            ('change_emotionanalysischapter',
             'Puede actualizar EmotionAnalysisChapter'),
            ('delete_emotionanalysischapter',
             'Puede eliminar EmotionAnalysisChaper'),
            ('list_emotionanalysischapter',
             'Puede listar EmotionAnalysisChapter'),
            ('get_emotionanalysischapter',
             'Puede obtener EmotionAnalysisChapter'),
            ('listform_emotionanalysischapter',
              'Puede listar EmotionAnalysisChapter en Formularios'),
        )
        unique_together = ('emotion', 'analysis_chapter')

    def __str__(self):
        return (self.emotion.__str__() +
                self.analysis_chapter.__str__())

    def delete(self, *args, **kwargs):
        try:
            super(EmotionAnalysisChapter, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return (self.emotion.__str__() +
                    self.analysis_chapter.__str__())