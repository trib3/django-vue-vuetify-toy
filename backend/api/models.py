from django.db import models
from enum import Enum

class Ambassador(models.Model):
    """
    Simple representation of a content creator
    """
    name = models.CharField(max_length=200)
    thumbnail = models.TextField()

class Post(models.Model):
    """
    Simple representation of a piece of content created by an Ambassador
    """
    ambassador = models.ForeignKey('Ambassador', on_delete=models.CASCADE)
    link = models.URLField()

    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    emv = models.IntegerField(default=0)


class AmbassadorDisplayFields(Enum):
    """
    Fields that can be queried from a set of Ambassadors
    """
    NAME = 'name'
    THUMBNAIL = 'thumbnail'
    EMV = 'emv'
    POSTCOUNT = 'post_count'