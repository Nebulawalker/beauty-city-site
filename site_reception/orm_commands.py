from .models import *


def get_masters():
    return Master.objects.all()

def get_saloons():
    return Saloon.objects.all()

def get_services():
    return Service.objects.all()

