# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-24 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('popularity', models.IntegerField(default=0)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.Show')),
            ],
        ),
    ]