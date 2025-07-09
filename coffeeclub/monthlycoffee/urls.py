from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("templates/roaster/<int:roaster_id>/", views.roaster, name="roaster"),
    path("action/<int:last_month_id>/", views.submit_action, name='submit_action'),
    path("templates/rate/<int:roaster_id>/", views.rate, name="rate")
]