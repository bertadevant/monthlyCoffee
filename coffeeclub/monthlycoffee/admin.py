from django.contrib import admin
from .models import CoffeeRoaster, Rating, Tag

admin.site.register(CoffeeRoaster)
admin.site.register(Rating)
admin.site.register(Tag)