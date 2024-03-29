# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-24 19:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('show', '0001_initial'),
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('popularity', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.Character')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.Show')),
            ],
        ),
    ]
