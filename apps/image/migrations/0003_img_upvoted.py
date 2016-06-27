# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-27 19:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image', '0002_img_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='upvoted',
            field=models.ManyToManyField(related_name='upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]