# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0014_auto_20170809_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='opcion',
            name='nombre_corto',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='partido',
            name='nombre_corto',
            field=models.CharField(default='', max_length=10),
        ),
    ]
