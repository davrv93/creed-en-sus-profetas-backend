# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0028_auto_20180120_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(editable=False, serialize=False, primary_key=True)),
                ('chapter', models.IntegerField(null=True, blank=True)),
                ('file', models.FileField(null=True, blank=True, upload_to='')),
                ('book', models.ForeignKey(to='believe_his_prophets.Book', db_column='verse_id', related_name='book_commentary_set')),
                ('language', models.ForeignKey(null=True, to='believe_his_prophets.Language', blank=True, db_column='language_id', related_name='language_commentary_set')),
            ],
            options={
                'verbose_name_plural': 'Commentary',
                'default_permissions': (),
                'db_table': 'believe_commentary',
                'permissions': (('add_commentary', 'Puede agregar Commentary'), ('change_commentary', 'Puede actualizar Commentary'), ('delete_commentary', 'Puede eliminar Commentary'), ('list_commentary', 'Puede listar Commentary'), ('get_commentary', 'Puede obtener Commentary'), ('listform_commentary', 'Puede listar Commentary en Formularios')),
                'verbose_name': 'Commentary',
                'ordering': ('book__book_order', 'chapter'),
            },
        ),
    ]
