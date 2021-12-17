from django.contrib import admin
from .models import Song,history_listen
# Register your models here.
admin.site.register(Song)
admin.site.register(history_listen)