from django.shortcuts import render
from .orm_commands import *


def index(request):
    saloons = []
    for saloon in get_saloons():
        saloon_properties = {'title': saloon.title, 'address': saloon.address, 'photo': saloon.photo.url}
        saloons.append(saloon_properties)

    masters = []
    for master in get_masters():
        master_properties = {'name': master.name, 'photo': master.photo.url}    # Докинуть отзывы и стаж работы
        masters.append(master_properties)

    services = []
    for service in get_services():
        service_properties = {'title': service.title, 'price': service.price, 'photo': service.photo.url}
        services.append(service_properties)

    context = {'saloons': saloons, 'masters': masters, 'services': services}

    return render(request, 'index.html', context=context)
