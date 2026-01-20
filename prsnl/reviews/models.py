from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=100, blank=True)
    hours_played = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()
    headline = models.CharField(max_length=200)
    body = models.TextField()
    finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game.title} - {self.rating}/10"
