from django.urls import path
from . import views

urlpatterns = [
    path('', views.planta.as_view()),
]
