from django.db import models
from .coffee_roaster import CoffeeRoaster

class Rating(models.Model):
    roaster = models.ForeignKey(CoffeeRoaster, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField()
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.score}/5 for {self.roaster.name}"