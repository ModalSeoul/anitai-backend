from __future__ import unicode_literals
from django.db import models
from apps.accounts.models import EmailUser


class Announcement(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(EmailUser)
    title = models.CharField(max_length=32)
    text = models.TextField()

    def __str__(self):
        return self.title
