from django.db import models
from django.contrib.auth.models import User

ART_TYPES = (
        ("clipart", "Art"),
        ("texture", "Texture"),
        ("brush", "brush"),
        )

class Art(models.Model):
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=ART_TYPES)
    file = models.ImageField()
    file_name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User)
