from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
from backend.api.models import Profile, ProfileDisplayFields, PostAggregateFields
from django.http import JsonResponse
from django.http import HttpRequest

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name="index.html"))


def profiles(request: HttpRequest) -> JsonResponse:
    """
    Data about profiles and their posts
    :param request: Request from the client
    :return: JsonResponse containing a list of dictionaries that
    represent profiles and their posts.

    EX:
        [
            {
            "name": "lifeoftanyamarie",
            "thumbnail": "thumbnail.com",
            "followers": 90900,
            "post_count": 2,
            "likes": 4310
            },...
        ]
    """
    fields = [
        display.value for display in [*ProfileDisplayFields, *PostAggregateFields]
    ]
    profiles_qs = (
        Profile.objects.all()
        .annotate(
            post_count=Coalesce(Count("post"), 0),
            likes=Coalesce(Sum("post__likes"), 0),
        )
        .values(*fields)
    )
    return JsonResponse(list(profiles_qs), safe=False)
