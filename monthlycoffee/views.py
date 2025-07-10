from django.shortcuts import render, redirect
from django.templatetags.static import static
from . import get_roasters_data
from . import set_roaster_data
import random

from .models import CoffeeRoaster


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
        action_name = request.POST.get('id')
        if action_name == "rate":
            return redirect('rate', last_month_id)
        else:
            next_roaster = get_roasters_data.get_next_roaster()
            set_roaster_data.transfer_last_time_tag(next_roaster.id, last_month_id)
            return redirect('roaster', next_roaster.id)
    return redirect('index')

def roaster(request, roaster_id):
    roaster = get_roasters_data.get_roaster(roaster_id)
    template = 'monthlycoffee/roaster.html'
    context = {"roaster": roaster}
    return render(request, template, context)

def rate(request, roaster_id):
    roaster = get_roasters_data.get_roaster(roaster_id)
    template = 'monthlycoffee/rate.html'
    context = {"last_month_roaster": roaster}
    return render(request, template, context)