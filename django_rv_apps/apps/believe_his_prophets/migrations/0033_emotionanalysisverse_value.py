# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0032_auto_20180126_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='emotionanalysisverse',
            name='value',
            field=models.DecimalField(null=True, max_digits=38, decimal_places=2, blank=True),
        ),
    ]
