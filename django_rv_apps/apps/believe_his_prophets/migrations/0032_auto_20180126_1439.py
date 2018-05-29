# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0031_chapter_commentary_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisVerse',
            fields=[
                ('id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('value', models.DecimalField(max_digits=38, decimal_places=2)),
            ],
            options={
                'db_table': 'believe_sentimental',
                'default_permissions': (),
                'verbose_name_plural': 'Sentimental verse',
                'verbose_name': 'Sentimental verse',
                'permissions': (('add_analysisverse', 'Puede agregar AnalysisVerse'), ('change_analysisverse', 'Puede actualizar AnalysisVerse'), ('delete_analysisverse', 'Puede eliminar AnalysisVerse'), ('list_analysisverse', 'Puede listar AnalysisVerse'), ('get_analysisverse', 'Puede obtener AnalysisVerse'), ('listform_analysisverse', 'Puede listar AnalysisVerse en Formularios')),
            },
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=350, null=True)),
            ],
            options={
                'db_table': 'believe_emotion',
                'default_permissions': (),
                'verbose_name_plural': 'Emotion',
                'verbose_name': 'Emotion',
                'permissions': (('add_emotion', 'Puede agregar Emotion'), ('change_emotion', 'Puede actualizar Emotion'), ('delete_emotion', 'Puede eliminar Emotion'), ('list_emotion', 'Puede listar Emotion'), ('get_emotion', 'Puede obtener Emotion'), ('listform_emotion', 'Puede listar Emotion en Formularios')),
            },
        ),
        migrations.CreateModel(
            name='EmotionAnalysisVerse',
            fields=[
                ('id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('analysis_verse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, db_column='analysis_verse_id', related_name='analysis_verse_emotion_analysis_verse_set', to='believe_his_prophets.AnalysisVerse')),
                ('emotion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, db_column='emotion_id', related_name='emotion_emotion_analysis_verse_set', to='believe_his_prophets.Emotion')),
            ],
            options={
                'default_permissions': (),
                'verbose_name_plural': 'EmotionAnalysisVerse',
                'db_table': 'believe_em_an_verse',
                'permissions': (('add_emotionanalysisverse', 'Puede agregar EmotionAnalysisVerse'), ('change_emotionanalysisverse', 'Puede actualizar EmotionAnalysisVerse'), ('delete_emotionanalysisverse', 'Puede eliminar EmotionAnalysisVerse'), ('list_emotionanalysisverse', 'Puede listar EmotionAnalysisVerse'), ('get_emotionanalysisverse', 'Puede obtener EmotionAnalysisVerse'), ('listform_emotionanalysisverse', 'Puede listar EmotionAnalysisVerse en Formularios')),
                'verbose_name': 'EmotionAnalysisVerse',
            },
        ),
        migrations.CreateModel(
            name='LanguageEmotion',
            fields=[
                ('id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('emotion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, db_column='emotion_id', related_name='emotion_language_emotion_set', to='believe_his_prophets.Emotion')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, db_column='language_id', related_name='language_language_emotion_set', to='believe_his_prophets.Language')),
            ],
            options={
                'default_permissions': (),
                'verbose_name_plural': 'LanguageEmotion',
                'db_table': 'believe_lan_emotion',
                'permissions': (('add_languageemotion', 'Puede agregar LanguageEmotion'), ('change_languageemotion', 'Puede actualizar LanguageEmotion'), ('delete_languageemotion', 'Puede eliminar LanguageEmotion'), ('list_languageemotion', 'Puede listar LanguageEmotion'), ('get_languageemotion', 'Puede obtener LanguageEmotion'), ('listform_languageemotion', 'Puede listar LanguageEmotion en Formularios')),
                'verbose_name': 'LanguageEmotion',
            },
        ),
        migrations.CreateModel(
            name='LanguageSentiment',
            fields=[
                ('id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, db_column='language_id', related_name='language_language_sentiment_set', to='believe_his_prophets.Language')),
            ],
            options={
                'default_permissions': (),
                'verbose_name_plural': 'LanguageSentiment',
                'db_table': 'believe_lan_sentiment',
                'permissions': (('add_languagesentiment', 'Puede agregar LanguageSentiment'), ('change_languagesentiment', 'Puede actualizar LanguageSentiment'), ('delete_languagesentimentn', 'Puede eliminar LanguageSentiment'), ('list_languagesentiment', 'Puede listar LanguageSentiment'), ('get_languagesentiment', 'Puede obtener LanguageSentiment'), ('listform_languagesentiment', 'Puede listar LanguageSentiment en Formularios')),
                'verbose_name': 'LanguageSentiment',
            },
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=350, null=True)),
                ('language', models.ManyToManyField(through='believe_his_prophets.LanguageSentiment', to='believe_his_prophets.Language', related_name='language_sentiment_set', verbose_name='LanguageSentiment')),
            ],
            options={
                'db_table': 'believe_sentiment',
                'default_permissions': (),
                'verbose_name_plural': 'Sentiment',
                'verbose_name': 'Sentiment',
                'permissions': (('add_sentiment', 'Puede agregar Sentiment'), ('change_sentiment', 'Puede actualizar Sentiment'), ('delete_sentiment', 'Puede eliminar Sentiment'), ('list_sentiment', 'Puede listar Sentiment'), ('get_sentiment', 'Puede obtener Sentiment'), ('listform_sentiment', 'Puede listar Sentiment en Formularios')),
            },
        ),
        migrations.AddField(
            model_name='languagesentiment',
            name='sentiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, db_column='sentiment_id', related_name='sentiment_language_sentiment_set', to='believe_his_prophets.Sentiment'),
        ),
        migrations.AddField(
            model_name='emotion',
            name='language',
            field=models.ManyToManyField(through='believe_his_prophets.LanguageEmotion', to='believe_his_prophets.Language', related_name='language_emotion_set', verbose_name='LanguageEmotion'),
        ),
        migrations.AddField(
            model_name='analysisverse',
            name='emotion',
            field=models.ManyToManyField(through='believe_his_prophets.EmotionAnalysisVerse', to='believe_his_prophets.Emotion', related_name='emotion_analysis_verse_set', verbose_name='EmotionAnalysisVerse'),
        ),
        migrations.AddField(
            model_name='analysisverse',
            name='sentiment',
            field=models.ForeignKey(to='believe_his_prophets.Sentiment', db_column='sentiment_id'),
        ),
        migrations.AddField(
            model_name='analysisverse',
            name='verse',
            field=models.ForeignKey(to='believe_his_prophets.Verse', db_column='verse_id'),
         ),
        migrations.AlterUniqueTogether(
            name='languagesentiment',
            unique_together=set([('sentiment', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='languageemotion',
            unique_together=set([('emotion', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='emotionanalysisverse',
            unique_together=set([('emotion', 'analysis_verse')]),
        ),
    ]
