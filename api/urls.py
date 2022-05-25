from django.urls import path, include

from memes.views import random_meme
from memes.views import meme_detail_view, meme_list_create_view
# from memes.views import meme_create_view
from rest_framework.authtoken.views import obtain_auth_token

from .views import reverb

urlpatterns = [
        path("reverb/", reverb),
        path("random_meme/", random_meme),
        path("memes/", meme_list_create_view),
        path("memes/<int:pk>/", meme_detail_view),
        # not really needed
        # path("memes/create/", meme_create_view),
        # This thing is to get new (or existing token)
        path("auth_token_obtain/", obtain_auth_token)
        ]
