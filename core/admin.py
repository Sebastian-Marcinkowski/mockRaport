from django.contrib import admin
from .models import Raport
# Register your models here.

class Raports(admin.ModelAdmin):
    list_display = ['id', 'name', 'formatR', 'email', 'scheduleType',
                    'scheduleTime', 'scheduleDay', 'scheduleDate']
    ordering = ['id']
admin.site.register(Raport, Raports)