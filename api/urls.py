from django.urls import path, include
from . import views

urlpatterns = [
        path("reverb/", views.reverb),
        path("random_meme/", views.random_meme),
        ]
