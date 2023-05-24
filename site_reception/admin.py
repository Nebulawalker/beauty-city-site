from django.contrib import admin
from .models import Client, Service, Master, Saloon, Order


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
    # raw_id_fields = ('service', )
    list_filter = ('service', )
    # inlines = [ServicesInline]


class MasterInline(admin.TabularInline):
    model = Saloon.master.through


@admin.register(Saloon)
class SaloonAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')
    search_fields = ('title', )
    # raw_id_fields = ('master', )
    # inlines = [MasterInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'saloon',
        'service',
        'client',
        'master',
    )
    raw_id_fields = ('client', )
