# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0038_spiritprophecyread_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spiritprophecyread',
            name='spirit_prophecy_chapter',
            field=models.ForeignKey(null=True, to='believe_his_prophets.SpiritProphecyChapter', blank=True, db_column='spirit_prophecy_chapter_id'),
        ),
    ]
