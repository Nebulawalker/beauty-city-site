from django.shortcuts import render
from .orm_commands import *
from django.http import HttpResponse


def index(request):
    for saloon in get_saloons():
        print(saloon.photo.path)

    for master in get_masters():
        print(master.photo.path)

    for service in get_services():
        print(service.photo.path)

    return render(request, 'index.html')


def service_finally(request):
    return render(request, 'serviceFinally.html')


def service(request):
    if request.method == 'POST':
        saloon_title = request.POST.get('saloon')
        service_name = request.POST.get('service')
        master_name = request.POST.get('master')
        return HttpResponse(f'{saloon_title}, {service_name}, {master_name}')

    else:
        context = {
            'saloons': get_saloons(),
            'services': get_services(),
            'masters': get_masters(),
            'time_slots': get_time_slots(),
        }
        return render(request, 'service.html', context)

# timeslots = []
# orders = Order.objects.filter(Saloon=saloon & master=master & service=service)
# for order in orders:
#     timeslots.append(order.time)