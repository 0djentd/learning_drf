from django.urls import path, include

from memes.views import random_meme
from memes.views import meme_detail_view, meme_list_create_view
# from memes.views import meme_create_view

from .views import reverb

urlpatterns = [
        path("reverb/", reverb),
        path("random_meme/", random_meme),
        path("memes/", meme_list_create_view),
        # path("memes/create/", meme_create_view),
        path("memes/<int:pk>/", meme_detail_view),
        ]
