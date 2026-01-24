from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Review
from .forms import GameForm, ReviewForm

# Create your views here.
def home(request):
    #this just links the template and the view function
    games = Game.objects.order_by("-created_at")
    recent_reviews = Review.objects.select_related("game").order_by("-created_at")[:10]
    return render(request, "reviews/home.html", {"games": games, "recent_reviews": recent_reviews})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = game.reviews.order_by("-created_at")
    return render(request, "reviews/game_detail.html", {"game": game, "reviews": reviews})

def game_create(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = GameForm()

    return render(request, "reviews/form.html", {"form": form, "title": "Add Game"})

def review_create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ReviewForm()

    return render(request, "reviews/form.html", {"form": form, "title": "Add Review"})