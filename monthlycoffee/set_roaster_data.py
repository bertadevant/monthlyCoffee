from .models import Rating, Tag
from . import get_roasters_data

def save_new_rating(roaster_id, score, review):
    roaster = get_roasters_data.get_roaster(roaster_id)
    rating = Rating.objects.create(roaster=roaster, score=score, review=review)

def transfer_last_time_tag(new_roaster_id, last_roaster_id):
    new_roaster = get_roasters_data.get_roaster(new_roaster_id)
    last_roaster = get_roasters_data.get_roaster(last_roaster_id)
    last_time_tag = get_roasters_data.get_last_time_tag()

    last_roaster.tags.remove(last_time_tag)
    new_roaster.tags.add(last_time_tag)