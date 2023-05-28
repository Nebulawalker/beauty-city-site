from django.shortcuts import render
from django.http import HttpResponse
from .orm_commands import get_saloons, get_masters, get_services, get_reviews, get_masters_with_counted_reviews


def index(request):
    saloons = []
    for saloon in get_saloons():
        saloon_properties = {'title': saloon.title, 'address': saloon.address, 'photo': saloon.photo.url}
        saloons.append(saloon_properties)

    masters = []
    for master in get_masters_with_counted_reviews():
        master_properties = {'name': master.name, 'photo': master.photo.url, 'reviews': master.review_master__count}  # Докинуть отзывы
        masters.append(master_properties)

    services = []
    for service in get_services():
        service_properties = {'title': service.title, 'price': service.price, 'photo': service.photo.url}
        services.append(service_properties)

    reviews = []
    for review in get_reviews():
        review_properties = {
            'client_name': review.client.name,
            'text': review.text,
            'rating': review.star,
            'created_at': review.created_at
        }
        reviews.append(review_properties)

    context = {'saloons': saloons, 'masters': masters, 'services': services, 'reviews': reviews}

    return render(request, 'index.html', context)


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
