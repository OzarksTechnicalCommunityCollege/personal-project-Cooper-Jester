from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Game, Review

# Create your views here.
def home(request):
    #this just links the template and the view function
    games = Game.objects.order_by("-created_at")
    return render(request, "reviews/home.html", {"games": games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = game.reviews.order_by("-created_at")
    return render(request, "reviews/game_detail.html", {"game": game, "reviews": reviews})

def search(request):
    q = request.GET.get("q", "").strip()

    games = Game.objects.none()
    reviews = Review.objects.none()

    if q:
        games = Game.objects.filter(
            Q(title__icontains=q) | Q(platform__icontains=q)
        ).order_by("-created_at")

        reviews = Review.objects.select_related("game").filter(
            Q(headline__icontains=q) | Q(body__icontains=q) | Q(game__title__icontains=q)
        ).order_by("-created_at")

    return render(request, "reviews/search.html", {"q": q, "games": games, "reviews": reviews})