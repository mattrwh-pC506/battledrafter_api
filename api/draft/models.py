from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User

from django.db import models


class Draft(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    label = models.CharField(max_length=100, default="Unnamed Draft - {}".format(datetime.now()))
    description = models.TextField(null=True, blank=True)
    art_store = models.TextField()

    def save(self, *args, **kwargs):
        if self.user is None:
            self.user = User.objects.get(id=1)
        super().save(*args, **kwargs)
