# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0033_emotionanalysisverse_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisverse',
            name='value',
            field=models.DecimalField(max_digits=38, decimal_places=10),
        ),
    ]
