from django.shortcuts import render
from .orm_commands import *


def index(request):
    for saloon in get_saloons():
        print(saloon.photo.path)

    for master in get_masters():
        print(master.photo.path)

    for service in get_services():
        print(service.photo.path)

    return render(request, 'index.html')


def service(request):
    if request.method == 'POST':
        saloon_title = request.POST.get('saloon_title')
        service_title = request.POST.get('service_title')

        if saloon_title:
            saloon = get_saloons().filter(title__contains=saloon_title).first()
            context = {
                'saloon': saloon,
                'services': get_services(),
                'masters': get_masters().filter(saloons=saloon)
            }

        return render(request, 'service.html', context)
    else:
        context = {
            'saloons': get_saloons(),
            'services': get_services(),
            'masters': get_masters(),
            'time_slots': get_time_slots(),
        }
        return render(request, 'service.html', context)
