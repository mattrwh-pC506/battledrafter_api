from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User

from django.db import models


class Draft(models.Model):
    user = models.ForeignKey(User, default=lambda: User.objects.get(1))
    label = models.CharField(max_length=100, default="Unnamed Draft - {}".format(datetime.now()))
    description = models.TextField(null=True, blank=True)
    art_store = models.TextField()
