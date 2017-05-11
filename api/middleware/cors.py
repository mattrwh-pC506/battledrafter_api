from django.conf import settings
from urllib.parse import urlparse


def cors_middleware(get_response):

    def middleware(request):
        referer = urlparse(request.META.get("HTTP_REFERER", ""))
        host = referer.hostname
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=referer)
        response = get_response(request);
        if host in settings.ALLOWED_CORS_HOSTS or domain in settings.ALLOWED_CORS_HOSTS:
            if domain[-1] == "/": domain = domain[:-1]
            response["Access-Control-Allow-Origin"] = domain
        return response

    return middleware
