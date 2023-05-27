from .models import *


def get_masters():
    return Master.objects.all()

def get_saloons():
    return Saloon.objects.all()

def get_services():
    return Service.objects.all()

def get_time_slots():
    return Order.TIME_SLOTS_NEW

# for time in time_slots:
#     if time not in Order.objects.filter(a)
#         print(time)