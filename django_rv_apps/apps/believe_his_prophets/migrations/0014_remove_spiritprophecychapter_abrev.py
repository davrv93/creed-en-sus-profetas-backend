# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-10 02:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0013_auto_20170610_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spiritprophecychapter',
            name='abrev',
        ),
    ]
