
from django.db import models
from django.db.models.deletion import ProtectedError
from .verse import Verse
from .emotion import Emotion
from .sentiment import Sentiment


class AnalysisVerse(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    verse = models.ForeignKey(
        Verse,
        db_column='verse_id',
        blank=False,
        null=False)
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
        related_name='emotion_analysis_verse_set',
        verbose_name='EmotionAnalysisVerse',
        through='EmotionAnalysisVerse')

    class Meta:
        verbose_name = 'Analysis verse'
        db_table = 'believe_sentimental'
        verbose_name_plural = 'Analysis verse'
        default_permissions = ()
        permissions = (
            ('add_analysisverse',
             'Puede agregar AnalysisVerse'),
            ('change_analysisverse',
             'Puede actualizar AnalysisVerse'),
            ('delete_analysisverse',
             'Puede eliminar AnalysisVerse'),
            ('list_analysisverse',
             'Puede listar AnalysisVerse'),
            ('get_analysisverse',
             'Puede obtener AnalysisVerse'),
            ('listform_analysisverse',
              'Puede listar AnalysisVerse en Formularios'),
        )

    def __str__(self):
        return self.verse.__str__()

    def delete(self, *args, **kwargs):
        try:
            super(AnalysisVerse, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return self.name


class EmotionAnalysisVerse(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    emotion = models.ForeignKey(
        Emotion,
        db_column='emotion_id',
        related_name='emotion_emotion_analysis_verse_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    analysis_verse = models.ForeignKey(
        'AnalysisVerse',
        db_column='analysis_verse_id',
        related_name='analysis_verse_emotion_analysis_verse_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    value = models.DecimalField(
        null=True, blank=True,
        max_digits=38, decimal_places=2)

    class Meta:
        verbose_name = 'EmotionAnalysisVerse'
        verbose_name_plural = 'EmotionAnalysisVerse'
        db_table = 'believe_em_an_verse'
        default_permissions = ()
        permissions = (
            ('add_emotionanalysisverse',
             'Puede agregar EmotionAnalysisVerse'),
            ('change_emotionanalysisverse',
             'Puede actualizar EmotionAnalysisVerse'),
            ('delete_emotionanalysisverse',
             'Puede eliminar EmotionAnalysisVerse'),
            ('list_emotionanalysisverse',
             'Puede listar EmotionAnalysisVerse'),
            ('get_emotionanalysisverse',
             'Puede obtener EmotionAnalysisVerse'),
            ('listform_emotionanalysisverse',
              'Puede listar EmotionAnalysisVerse en Formularios'),
        )
        unique_together = ('emotion', 'analysis_verse')

    def __str__(self):
        return (self.emotion.__str__() +
                self.analysis_verse.__str__())

    def delete(self, *args, **kwargs):
        try:
            super(EmotionAnalysisVerse, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return (self.emotion.__str__() +
                    self.analysis_verse.__str__())