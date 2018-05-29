# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0027_chapter_commentary'),
    ]

    operations = [
        migrations.AddField(
            model_name='spiritprophecy',
            name='language',
            field=models.ForeignKey(blank=True, null=True, to='believe_his_prophets.Language', db_column='language_id'),
        ),
        migrations.AddField(
            model_name='spiritprophecychapter',
            name='language',
            field=models.ForeignKey(blank=True, null=True, to='believe_his_prophets.Language', db_column='language_id'),
        ),
        migrations.AlterField(
            model_name='spiritprophecy',
            name='abrev',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spiritprophecy',
            name='translate_abrev',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spiritprophecychapter',
            name='translate_abrev',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
