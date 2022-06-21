from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon.as_view()),
    path('detalle/<int:id>/', views.PokemonDetail.as_view()),
]
