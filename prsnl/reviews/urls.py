from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("games/<int:game_id>/", views.game_detail, name="game_detail"),
    path("games/new/", views.game_create, name="game_create"),
    path("reviews/new/", views.review_create, name="review_create"),
]