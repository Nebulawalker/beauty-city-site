from django.contrib import admin
from .models import Client, Service


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ('name', 'phone_number')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'duration',
        'price',
    )
    search_fields = ('title', )
    list_editable = ('duration', 'price')
