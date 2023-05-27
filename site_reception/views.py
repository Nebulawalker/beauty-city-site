from django.shortcuts import render
from .orm_commands import get_saloons, get_masters, get_services, get_reviews


def index(request):
    saloons = []
    for saloon in get_saloons():
        saloon_properties = {'title': saloon.title, 'address': saloon.address, 'photo': saloon.photo.url}
        saloons.append(saloon_properties)

    masters = []
    for master in get_masters():
        master_properties = {'name': master.name, 'photo': master.photo.url}  # Докинуть отзывы и стаж работы
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

    return render(request, 'index.html', context=context)
