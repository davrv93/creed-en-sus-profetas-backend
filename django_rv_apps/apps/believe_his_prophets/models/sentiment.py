
from django.db import models
from django.db.models.deletion import ProtectedError
from .language import Language

class Sentiment(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    name=models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    description=models.CharField(
        max_length=350,
        blank=True,
        null=True
    )
    language = models.ManyToManyField(
        Language,
        related_name='language_sentiment_set',
        verbose_name='LanguageSentiment',
        through='LanguageSentiment')

    class Meta:
        verbose_name = 'Sentiment'
        db_table = 'believe_sentiment'
        verbose_name_plural = 'Sentiment'
        default_permissions = ()
        permissions = (
            ('add_sentiment',
             'Puede agregar Sentiment'),
            ('change_sentiment',
             'Puede actualizar Sentiment'),
            ('delete_sentiment',
             'Puede eliminar Sentiment'),
            ('list_sentiment',
             'Puede listar Sentiment'),
            ('get_sentiment',
             'Puede obtener Sentiment'),
            ('listform_sentiment',
              'Puede listar Sentiment en Formularios'),
        )

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        try:
            super(Sentiment, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return self.name



class LanguageSentiment(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    sentiment = models.ForeignKey(
        Sentiment,
        db_column='sentiment_id',
        related_name='sentiment_language_sentiment_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    language = models.ForeignKey(
        'Language',
        db_column='language_id',
        related_name='language_language_sentiment_set',
        blank=False, null=False,
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'LanguageSentiment'
        verbose_name_plural = 'LanguageSentiment'
        db_table = 'believe_lan_sentiment'
        default_permissions = ()
        permissions = (
            ('add_languagesentiment',
             'Puede agregar LanguageSentiment'),
            ('change_languagesentiment',
             'Puede actualizar LanguageSentiment'),
            ('delete_languagesentimentn',
             'Puede eliminar LanguageSentiment'),
            ('list_languagesentiment',
             'Puede listar LanguageSentiment'),
            ('get_languagesentiment',
             'Puede obtener LanguageSentiment'),
            ('listform_languagesentiment',
              'Puede listar LanguageSentiment en Formularios'),
        )
        unique_together = ('sentiment', 'language')

    def __str__(self):
        return (self.sentiment.__str__() +
                self.analysis_verse.__str__())

    def delete(self, *args, **kwargs):
        try:
            super(LanguageSentiment, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return (self.sentiment.__str__() +
                    self.analysis_verse.__str__())