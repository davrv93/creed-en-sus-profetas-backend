# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0040_chapter_commentary_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookLanguage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('abreviation', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Book language',
                'verbose_name': 'Book language',
                'db_table': 'believe_book_lang',
            },
        ),
        migrations.AlterField(
            model_name='book',
            name='translate_abrev',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='booklanguage',
            name='book',
            field=models.ForeignKey(to='believe_his_prophets.Book', db_column='book_id'),
        ),
        migrations.AddField(
            model_name='booklanguage',
            name='language',
            field=models.ForeignKey(to='believe_his_prophets.Language', db_column='language_id'),
        ),
    ]
