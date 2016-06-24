from __future__ import unicode_literals
from django.db import models
from apps.accounts.models import EmailUser
from apps.character.models import Character
from apps.show.models import Show


class Img(models.Model):
    image = models.FileField(upload_to='uploads/')
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(EmailUser)
    popularity = models.IntegerField(default=0)
    character = models.ForeignKey(Character)
    show = models.ForeignKey(Show)

    def __str__(self):
        return self.character.name
