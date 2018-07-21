# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0039_auto_20180604_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='commentary_html',
            field=models.TextField(blank=True, null=True),
        ),
    ]
