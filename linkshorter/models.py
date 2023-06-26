from django.db import models

# Create your models here.


class Urls(models.Model):
    originalURL = models.TextField(null=False, unique=False)
    shortURL = models.TextField(null=False, unique=True)
    clicks = models.IntegerField(default=0, null=False)

    CreatedAT = models.DateTimeField(auto_now=True)
    LastUpdate = models.DateTimeField(auto_now_add=True)
