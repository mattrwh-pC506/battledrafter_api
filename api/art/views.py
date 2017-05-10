import datetime
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
import json

from art.models import Art


def art_post(request):
    data = json.loads(request.POST.get("data", "{}"))
    file_name = data.get("label", str(datetime.datetime.now()))
    label = data.get("label", str(datetime.datetime.now()))
    type = data.get("type", "clipart")
    user_id = data.get("userId", 1)
    f = request.FILES["file"]

    with open('media/{}'.format(file_name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    new_art = Art(
            label=label,
            file_name=file_name,
            type=type,
            file=f,
            user_id=user_id)

    new_art.save()

def art(request, user_id=None):
    if request.POST:
        art_post(request)
        return JsonResponse({"message": "success!"})
    else:
        system_and_user_art = Art.objects.filter(user_id__in=[1, user_id]).values()
        return JsonResponse({"data": [art for art in system_and_user_art]})

