from django.db.models import Count

from .models import Master, Saloon, Service, Review


def get_masters():
    return Master.objects.all()


def get_masters_with_counted_reviews():
    return Master.objects.annotate(Count('review_master'))


def get_saloons():
    return Saloon.objects.all()


def get_services():
    return Service.objects.all()


def get_reviews():
    return Review.objects.select_related('client').all()
