# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-27 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='title',
            field=models.CharField(default='Announcement boi', max_length=32),
            preserve_default=False,
        ),
    ]
