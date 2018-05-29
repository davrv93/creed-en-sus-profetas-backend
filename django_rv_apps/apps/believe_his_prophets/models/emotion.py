
from django.db import models
from django.db.models.deletion import ProtectedError
from .language import Language

class Emotion(models.Model):
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
        related_name='language_emotion_set',
        verbose_name='LanguageEmotion',
        through='LanguageEmotion')

    class Meta:
        verbose_name = 'Emotion'
        db_table = 'believe_emotion'
        verbose_name_plural = 'Emotion'
        default_permissions = ()
        permissions = (
            ('add_emotion',
             'Puede agregar Emotion'),
            ('change_emotion',
             'Puede actualizar Emotion'),
            ('delete_emotion',
             'Puede eliminar Emotion'),
            ('list_emotion',
             'Puede listar Emotion'),
            ('get_emotion',
             'Puede obtener Emotion'),
            ('listform_emotion',
              'Puede listar Emotion en Formularios'),
        )

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        try:
            super(Emotion, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return self.name



class LanguageEmotion(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    emotion = models.ForeignKey(
        'Emotion',
        db_column='emotion_id',
        related_name='emotion_language_emotion_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    language = models.ForeignKey(
        'Language',
        db_column='language_id',
        related_name='language_language_emotion_set',
        blank=False, null=False,
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'LanguageEmotion'
        verbose_name_plural = 'LanguageEmotion'
        db_table = 'believe_lan_emotion'
        default_permissions = ()
        permissions = (
            ('add_languageemotion',
             'Puede agregar LanguageEmotion'),
            ('change_languageemotion',
             'Puede actualizar LanguageEmotion'),
            ('delete_languageemotion',
             'Puede eliminar LanguageEmotion'),
            ('list_languageemotion',
             'Puede listar LanguageEmotion'),
            ('get_languageemotion',
             'Puede obtener LanguageEmotion'),
            ('listform_languageemotion',
              'Puede listar LanguageEmotion en Formularios'),
        )
        unique_together = ('emotion', 'language')

    def __str__(self):
        return (self.emotion.__str__() +
                self.analysis_verse.__str__())

    def delete(self, *args, **kwargs):
        try:
            super(LanguageEmotion, self).delete(*args, **kwargs)
        except ProtectedError as e:
            return (self.emotion.__str__() +
                    self.analysis_verse.__str__())