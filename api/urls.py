from django.urls import path, include
from .views import reverb
from memes.views import random_meme

urlpatterns = [
        path("reverb/", reverb),
        path("random_meme/", random_meme),
        ]
