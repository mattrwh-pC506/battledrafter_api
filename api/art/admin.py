from django.contrib import admin
from .models import Art


@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    pass
