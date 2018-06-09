# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0037_auto_20180604_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='spiritprophecyread',
            name='chapter',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
