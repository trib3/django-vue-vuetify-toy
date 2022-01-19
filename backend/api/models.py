from django.db import models
from enum import Enum


class Profile(models.Model):
    """
    Simple representation of a content creator
    EX. Raw Schema:
    {
      "channel": "instagram"
      "thumbnail": "https://ciq.s3.aws.com/posts/instagram/CTAVGT5nQtr.jpg",
      "name": "lifeoftanyamarie",
      "ext_id": 241343254,
      "link": "https://www.instagram.com/lifeoftanyamarie/"
      "followers": 90900
    }
    """

    name = models.CharField(max_length=200, help_text="Name of the channel.")

    channel = models.CharField(max_length=30, help_text="YouTube, Facebook, etc.")
    ext_id = models.TextField(unique=True, help_text="Profile id on the channel.")
    link = models.URLField(help_text="Profile link on the channel.")

    followers = models.IntegerField(default=0, help_text="Most recent follower count.")
    thumbnail = models.TextField(help_text="URI to a profile image")

    is_business = models.NullBooleanField(help_text="IG business account if True.")
    is_public = models.NullBooleanField(help_text="Public profile if True.")


class Post(models.Model):
    """
    Simple representation of a piece of content created by an Ambassador
    EX. Raw Schema:
    {
      "user_tags": "@nike,@sephora",
      "profile_ext_id": 241343254,
      "views": 18095,
      "likes": 2155,
      "shares": null,
      "comments": 60,
      "thumbnail": "https://ciq.s3.aws.com/posts/instagram/CTAVGT5nQtr.jpg"
      "ext_id": "241343254_6378462387",
      "link": "https://www.instagram.com/tv/CTAVGT5nQtr",
      "message": "Queens! I know you've been waiting for this video, so I'm so happy I could walk you through how I am currently doing my brows. I have linked all the products for you as well in my bio😘 feel free to ask questions in the comments! \n\n#eyebrows #eyebrowtutorial #brow #browtutorial #makeup #makeuptutorial #makeupartist #makeuplife #makeupartist #mua #makeuptutorials #lifeoftanyamarie",
      "request_time": "2021-11-17 21:30:33.217662Z",
      "publish_time": "2021-08-25 17:09:45Z",
      "title": null,
      "media_type": "video",
      "channel": "instagram"
    }
    """

    profile = models.ForeignKey(
        Profile,
        to_field="ext_id",
        on_delete=models.CASCADE,
        help_text="Profile id on the channel.",
    )

    ext_id = models.TextField(unique=True)
    link = models.URLField(help_text="Profile link on the channel.")

    title = models.TextField(help_text="Title of the post.")
    message = models.TextField(help_text="The description or caption.")

    # Using a comma separated list to store these for now
    user_tags = models.TextField(help_text="User tags in an image.")

    views = models.IntegerField(default=0, help_text="Number of views on the post.")
    likes = models.IntegerField(default=0, help_text="Number of likes on the post.")
    shares = models.IntegerField(default=0, help_text="Number of shares on the post.")
    comments = models.IntegerField(
        default=0, help_text="Number of comments on the post."
    )

    thumbnail = models.TextField(help_text="URI to an image.")

    publish_time = models.DateTimeField(help_text="time published on channel in UTC")
    request_time = models.DateTimeField(
        help_text="Time requested by our collector in UTC."
    )

    media_type = models.TextField(help_text="Image, video, etc...")
    channel = models.CharField(max_length=30, help_text="YouTube, Facebook, etc.")


class ProfileDisplayFields(Enum):
    """
    Fields that can be displayed on a Profile
    """

    NAME = "name"
    THUMBNAIL = "thumbnail"
    FOLLOWERS = "followers"


class PostAggregateFields(Enum):
    """
    Fields that can be aggregated when group on a Profile
    """

    LIKES = "likes"
    POSTCOUNT = "post_count"
    # VIEWS = 'views'
    # SHARES = "shares"
    # COMMENTS = "comments"
