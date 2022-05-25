from django.urls import path, include
from .views import reverb
from memes.views import random_meme, random_meme_cbv, random_meme_cbv_list

urlpatterns = [
        path("reverb/", reverb),
        path("random_meme/", random_meme),
        path("random_meme_cbv/", random_meme_cbv_list.as_view()),
        path("random_meme_cbv/<int:pk>/", random_meme_cbv.as_view()),
        ]
