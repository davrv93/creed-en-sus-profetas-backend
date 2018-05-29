# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0034_auto_20180205_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisverse',
            name='sentiment',
            field=models.ForeignKey(null=True, to='believe_his_prophets.Sentiment', db_column='sentiment_id', blank=True),
        ),
        migrations.AlterField(
            model_name='analysisverse',
            name='value',
            field=models.DecimalField(max_digits=38, decimal_places=10, null=True, blank=True),
        ),
    ]
