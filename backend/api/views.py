from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.db.models import Count, Sum
from backend.api.models import Ambassador, AmbassadorDisplayFields
from django.http import JsonResponse
from django.http import HttpRequest

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


def ambassadors(request: HttpRequest) -> JsonResponse:
    """
    Data about ambassadors and their posts
    :param request: Request from the client
    :return: JsonResponse containing a list of dictionaries that represent ambassadors
    and their posts. Dictionary keys are AmbassadorDisplayFields

    EX:
        [
            {
                "name":"Adele Lynch",
                "thumbnail":"https://dc-img.trib3.com/media_outlet/89249/images/98f3cc05-ce9a-4c5b-9806-6bdac59e821f.jpeg",
                "post_count":2,
                "emv":5100
            }, ...
        ]
    """
    fields = [display.value for display in AmbassadorDisplayFields]
    ambassador_qs = Ambassador.objects.all().annotate(
        post_count=Count('post'),
        emv=Sum('post__emv'),
    ).values(*fields)
    return JsonResponse(list(ambassador_qs), safe=False)