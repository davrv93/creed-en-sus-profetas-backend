# Generated by Django 2.0.9 on 2018-11-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('believe_his_prophets', '0010_spiritprophecychapterlanguage_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='spiritprophecychapter',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spiritprophecychapter',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
