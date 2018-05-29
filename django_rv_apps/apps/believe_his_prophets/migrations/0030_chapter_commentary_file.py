# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0029_commentary'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='commentary_file',
            field=models.FileField(null=True, blank=True, upload_to=''),
        ),
    ]
