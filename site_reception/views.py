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


def service_finally(request, pk):
    order = Order.objects.get(id=pk)
    data = {'order': order}
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        tel = request.POST.get('tel')

        client, created = Client.objects.get_or_create(
            name=fname,
            phone_number=tel
        )
        order.save()
    return render(request, 'serviceFinally.html', context=data)

def service(request):
    context = {
        'masters': get_masters(),
        'saloon': get_saloons()[0],
        'services': get_services(),
    }
    return render(request, 'service.html', context)

