import datetime
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
import json

from art.models import Art


def art(request):
    print ("coming in", request.FILES, request.POST, request.GET)
    if request.POST:
        data = json.loads(request.POST.get("data", "{}"))
        file_name = data.get(
                "label", str(datetime.datetime.now())
                )
        print ("file name!", file_name)
        type = data.get("type", "clipart")
        print ("type!", type)
        user_id = data.get("userId", 1)
        print ("userId", user_id)

        f = request.FILES["file"]
        print ("file", f)
        with open('media/{}'.format(file_name), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


    return JsonResponse({"message": "success!"})
