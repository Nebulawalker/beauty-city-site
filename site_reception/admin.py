from django.contrib import admin
from .models import Client, Service, Master


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


class ServicesInline(admin.TabularInline):
    model = Master.service.through
    list_display = ('title')


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    raw_id_fields = ('service', )
    list_filter = ('service', )
    inlines = [ServicesInline]
