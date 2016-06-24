from __future__ import unicode_literals
from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=32)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
