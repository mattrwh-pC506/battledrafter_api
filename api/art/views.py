from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
import json

from art.models import Art


def art(request):
    body = json.loads(request.body.decode(encoding='UTF-8'))
    label = body.get("label", "")
    type = body.get("type", "clipart")
    user_id = body.get("userId", 0)

    user = User.objects.get(user_id)

    new_art = Art(user=user, label=label, type=type)
    new_art.save()

    response_body = model_to_dict(new_art)

    return JsonResponse(response_body)
