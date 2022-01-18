from django.db import models
from enum import Enum

class AmbassadorDisplayFields(Enum):
    NAME = 'name'
    THUMBNAIL = 'thumbnail'
    EMV = 'emv'
    POSTCOUNT = 'post_count'

class Ambassador(models.Model):
    name = models.CharField(max_length=200)
    thumbnail = models.TextField()

class Post(models.Model):
    ambassador = models.ForeignKey('Ambassador', on_delete=models.CASCADE)
    link = models.URLField()

    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    emv = models.IntegerField(default=0)