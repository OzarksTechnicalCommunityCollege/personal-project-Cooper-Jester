from django.shortcuts import render
from .models import Game, Review

# Create your views here.
def home(request):
    #this just links the template and the view function
    games = Game.objects.order_by("-created_at")
    return render(request, "reviews/home.html", {"games": games})
    #        PLEASE tell me if ^^^this^^^ is correct. i tried just using home.html, but it wouildnt work and i dont know why.