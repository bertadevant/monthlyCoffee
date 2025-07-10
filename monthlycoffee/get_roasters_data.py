from .models import CoffeeRoaster, Tag
from django.shortcuts import get_object_or_404
import random


def get_last_month_roaster():
    last_month = CoffeeRoaster.objects.filter(tags__name='Last Time').first()
    return get_roaster(last_month.id)


def get_roaster(id):
    return get_object_or_404(CoffeeRoaster, pk=id)


def get_next_roaster():
    roasters = list(CoffeeRoaster.objects.all())
    weights = [roaster.weight() for roaster in roasters]
    result = random.choices(roasters, weights=weights, k=1)
    return result[0] if result else None

def get_last_time_tag():
    return get_object_or_404(Tag, name='Last Time')