from __future__ import unicode_literals
from django.db import models
from apps.character.models import Character


class Show(models.Model):
    title = models.CharField(max_length=32)
    popularity = models.IntegerField(default=0)
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return self.title
