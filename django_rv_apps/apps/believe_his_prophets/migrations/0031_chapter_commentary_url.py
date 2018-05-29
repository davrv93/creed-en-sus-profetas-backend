# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0030_chapter_commentary_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='commentary_url',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
    ]
