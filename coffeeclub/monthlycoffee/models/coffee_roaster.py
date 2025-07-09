from django.templatetags.static import static
from django.db import models
from .tag import Tag
from django.db.models import Avg, Sum

class CoffeeRoaster(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    image = models.ImageField(upload_to="static/images/roasters_assets", null = True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

    def rating(self):
        all_ratings = self.ratings.all()
        rating = self.ratings.aggregate(Avg('score')).get('score__avg')
        rounded = round(rating, 0) if rating is not None else 0
        return f"{rounded:.0f}"

    def image_ref(self):
        if self.image:
            return static(f"monthlycoffee/images/roasters_assets/{self.image}")
        return None

    """Weight is how much a roaster will be chosen by random, higher is better goes up to 5"""
    def weight(self):
        all_tags = self.tags.all()
        result = all_tags.aggregate(total_value=Sum('value'))
        return float(result.get('total_value', 0))

    def last_feedback(self):
        last_rating = self.ratings.order_by('-created_at').first()
        if not last_rating: return 'No feedback yet'
        return last_rating.review