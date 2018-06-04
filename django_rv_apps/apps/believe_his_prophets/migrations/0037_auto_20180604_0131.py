# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0036_auto_20180209_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='spiritprophecyread',
            name='chapter_title',
            field=models.CharField(null=True, max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='spiritprophecyread',
            name='title',
            field=models.CharField(null=True, max_length=120, blank=True),
        ),
    ]
