from django.contrib import admin
from .models import Client


@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
