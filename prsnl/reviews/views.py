from django.shortcuts import render
from .models import Game

# Create your views here.
def home(request):
    games = Game.objects.order_by("-created_at")
    return render(request, "reviews/home.html", {"games": games})