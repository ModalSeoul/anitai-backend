# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-24 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='show',
        ),
    ]
