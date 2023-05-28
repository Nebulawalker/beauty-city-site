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
        service_title = request.POST.get('service')
        master_name = request.POST.get('master')

        orders = Order.objects.all()
        if service_title:
            orders = orders.filter(service__title=service_title)
        if master_name:
            orders = orders.filter(master__name=master_name)
        return HttpResponse(f'{orders}, {master_name}, {type(master_name)}, {len(master_name)}')

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