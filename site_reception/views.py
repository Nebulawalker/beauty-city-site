from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .orm_commands import get_saloons, get_masters, get_services, get_reviews, get_masters_with_counted_reviews, get_timeslots
from site_reception.models import Order, Saloon, Master, Service, Client
from django.template.loader import render_to_string
from datetime import datetime


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


def service_finally(request, pk):
    order = Order.objects.all().order_by('created_at').last()
    context  = {'order': order}
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        tel = request.POST.get('tel')
        client, created = Client.objects.get_or_create(
            name=fname,
            phone_number=tel
        )
        order.client = client
        order.save()
    return render(request, 'serviceFinally.html', context)


def service(request):
    context = {
        'saloons': get_saloons(),
        'services': get_services(),
        'masters': get_masters(),
        'time_slots': get_timeslots(),
        'ordered_timeslots': [],
        'pk': '0'
    }
    return render(request, 'service.html', context)


def handle_schedule(request):
    service_title = request.POST.get('service')
    master_name = request.POST.get('master').strip()
    date = request.POST.get('date')
    date = datetime.strptime(date, '%Y-%m-%d').date()
    time = request.POST.get('time')
    saloon = request.POST.get('saloon')

    if service_title and master_name and date and time and saloon:
        Order.objects.create(
            saloon=Saloon.objects.get(title=saloon),
            service=Service.objects.get(title=service_title),
            master=Master.objects.get(name=master_name),
            appointment_date=date,
            appointment_time=time,
        )

    
    orders = Order.objects.all()
    if service_title:
        orders = orders.filter(service__title=service_title)
    if master_name:
        orders = orders.filter(master__name=master_name)

    ordered_timeslots = []
    for order in orders:
        if order.appointment_date == date:
            ordered_timeslots.append(order.appointment_time)
    html = render_to_string(
        'timeslots.html',
        {
            'ordered_timeslots': ordered_timeslots,
            'time_slots': get_timeslots(),
            'pk': '3'
        }
    )
    return JsonResponse(html, safe=False)
