# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0035_auto_20180205_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisChapter',
            fields=[
                ('id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('chapter', models.IntegerField()),
                ('value', models.DecimalField(max_digits=38, null=True, blank=True, decimal_places=10)),
                ('book', models.ForeignKey(db_column='book_id', to='believe_his_prophets.Book')),
            ],
            options={
                'verbose_name': 'Analysis chapter',
                'db_table': 'believe_analysis_chapter',
                'verbose_name_plural': 'Analysis Chapter',
                'permissions': (('add_analysischapter', 'Puede agregar AnalysisChapter'), ('change_analysischapter', 'Puede actualizar AnalysisChapter'), ('delete_analysischapter', 'Puede eliminar AnalysisChapter'), ('list_analysischapter', 'Puede listar AnalysisChapter'), ('get_analysischapter', 'Puede obtener AnalysisChapter'), ('listform_analysischapter', 'Puede listar AnalysisChapter en Formularios')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='EmotionAnalysisChapter',
            fields=[
                ('id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('value', models.DecimalField(max_digits=38, null=True, blank=True, decimal_places=2)),
                ('analysis_chapter', models.ForeignKey(db_column='analysis_chapter_id', on_delete=django.db.models.deletion.PROTECT, to='believe_his_prophets.AnalysisChapter', related_name='analysis_chapter_emotion_analysis_chapter_set')),
                ('emotion', models.ForeignKey(db_column='emotion_id', on_delete=django.db.models.deletion.PROTECT, to='believe_his_prophets.Emotion', related_name='emotion_emotion_analysis_chapter_set')),
            ],
            options={
                'verbose_name': 'EmotionAnalysisChapter',
                'verbose_name_plural': 'EmotionAnalysisChapter',
                'permissions': (('add_emotionanalysischapter', 'Puede agregar EmotionAnalysisChapter'), ('change_emotionanalysischapter', 'Puede actualizar EmotionAnalysisChapter'), ('delete_emotionanalysischapter', 'Puede eliminar EmotionAnalysisChaper'), ('list_emotionanalysischapter', 'Puede listar EmotionAnalysisChapter'), ('get_emotionanalysischapter', 'Puede obtener EmotionAnalysisChapter'), ('listform_emotionanalysischapter', 'Puede listar EmotionAnalysisChapter en Formularios')),
                'db_table': 'believe_em_an_chapter',
                'default_permissions': (),
            },
        ),
        migrations.AlterModelOptions(
            name='analysisverse',
            options={'verbose_name': 'Analysis verse', 'verbose_name_plural': 'Analysis verse', 'default_permissions': (), 'permissions': (('add_analysisverse', 'Puede agregar AnalysisVerse'), ('change_analysisverse', 'Puede actualizar AnalysisVerse'), ('delete_analysisverse', 'Puede eliminar AnalysisVerse'), ('list_analysisverse', 'Puede listar AnalysisVerse'), ('get_analysisverse', 'Puede obtener AnalysisVerse'), ('listform_analysisverse', 'Puede listar AnalysisVerse en Formularios'))},
        ),
        migrations.AddField(
            model_name='analysischapter',
            name='emotion',
            field=models.ManyToManyField(verbose_name='EmotionAnalysisChapter', through='believe_his_prophets.EmotionAnalysisChapter', to='believe_his_prophets.Emotion', related_name='emotion_analysis_chapter_set'),
        ),
        migrations.AddField(
            model_name='analysischapter',
            name='sentiment',
            field=models.ForeignKey(blank=True, db_column='sentiment_id', null=True, to='believe_his_prophets.Sentiment'),
        ),
        migrations.AlterUniqueTogether(
            name='emotionanalysischapter',
            unique_together=set([('emotion', 'analysis_chapter')]),
        ),
    ]
