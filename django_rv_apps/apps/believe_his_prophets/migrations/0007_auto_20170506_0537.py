# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-06 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0006_auto_20170506_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='abrev',
            field=models.CharField(max_length=15),
        ),
    ]
