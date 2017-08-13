# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 14:35
from __future__ import unicode_literals
from django.db.models import Q
from django.db import migrations
from django.db import transaction
import re


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    User = apps.get_model("auth", "User")
    Fiscal = apps.get_model("fiscales", "Fiscal")

    for u in User.objects.filter(Q(username__contains='.') | Q(username__contains=',')) :
        u.username = re.sub("[^0-9]", "", u.username)
        with transaction.atomic():
            try:
                u.save(update_fields=['username'])
            except:
                print(f'{u} con dni {u.username} existe')
    for f in Fiscal.objects.filter(Q(dni__contains='.') | Q(dni__contains=',')):
        f.dni = re.sub("[^0-9]", "", f.dni)
        with transaction.atomic():
            try:
                f.save(update_fields=['dni'])
            except:
                print(f'{f} con dni {f.dni} existe')



class Migration(migrations.Migration):

    dependencies = [
        ('fiscales', '0014_auto_20170811_0207'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]