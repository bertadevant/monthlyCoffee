from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("templates/roaster/<int:roaster_id>/", views.roaster, name="roaster"),
    path("templates/roaster/<int:roaster_id>/rate/", views.roaster_with_rating, name="roaster_with_rating"),
    path("action/<int:last_month_id>/", views.submit_action, name='submit_action'),
    path("submit_rating/<int:roaster_id>/", views.submit_rating, name="submit_rating")
]