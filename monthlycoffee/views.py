from django.shortcuts import render, redirect
from django.templatetags.static import static
from . import get_roasters_data
from . import set_roaster_data
import random

from .models import CoffeeRoaster, Tag


def index(request):
    roasters = CoffeeRoaster.objects.all()
    roaster = get_roasters_data.get_last_month_roaster()
    banner_num = random.randint(1, 30)
    banner_url = static(f"monthlycoffee/images/banner_images/{banner_num}.jpg")
    template = 'monthlycoffee/index.html'
    context = {
        "roasters": roasters,
        "last_month_roaster": roaster,
        "banner_url": banner_url
    }
    return render(request, template, context)

def submit_action(request, last_month_id):
    if request.method == 'POST':
        if 'Rate' in request.POST:
            return redirect('roaster_with_rating', last_month_id)
        elif 'Next' in request.POST:
            next_roaster = get_roasters_data.get_next_roaster()
            set_roaster_data.transfer_last_time_tag(next_roaster.id, last_month_id)
            set_roaster_data.delete_new_tag_after_last_time_tag(next_roaster.id)
            return redirect('roaster', next_roaster.id)
    return redirect('index')

def roaster(request, roaster_id, show_rating=False):
    roaster = get_roasters_data.get_roaster(roaster_id)
    available_tags = Tag.objects.exclude(name='Last Time').order_by('name')
    template = 'monthlycoffee/roaster.html'
    context = {
        "roaster": roaster,
        "show_rating": show_rating,
        "available_tags": available_tags
    }
    return render(request, template, context)

def roaster_with_rating(request, roaster_id):
    return roaster(request, roaster_id, show_rating=True)

def submit_rating(request, roaster_id):
    if request.method == 'POST':
        score = request.POST.get('score')
        review = request.POST.get('review', '')
        set_roaster_data.save_new_rating(roaster_id, int(score), review)
        return redirect('roaster', roaster_id)

    return redirect('roaster', roaster_id)