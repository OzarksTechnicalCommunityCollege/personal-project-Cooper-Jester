from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("games/<int:game_id>/", views.game_detail, name="game_detail"),
    path("search/", views.search, name="search"),
]