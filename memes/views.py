import json

from django.http import JsonResponse
from django.http import HttpRequest
from django.forms.models import model_to_dict

from rest_framework import generics, mixins, permissions, response, decorators, authentication

from .models import Meme
from .serializers import MemeSerializer
from .permissions import IsMemeAuthorPermission

# TODO:
# check out drf api doc for:
# mixins attrs
# permissions classes (also check out django obj permissions asap)
# authentication classes
# how to deploy django (wsgi asgi nginx apache docker)

# ===========
# basic api.
# ===========
# def random_meme(req: HttpRequest) -> JsonResponse:
#     meme = Meme.objects.first()
#     # simplest version.
#     # data = {'name': meme.name}
#     # second simplest version.
#     data = model_to_dict(meme, fields=["name"])
#     return JsonResponse(data)

# ===========
# api_view decorator + basic serializers usage.
# ===========
@decorators.api_view(["GET", "POST"])
def random_meme(req: HttpRequest) -> response.Response:
    data = {}
    if req.method == "GET":
        meme = Meme.objects.all().order_by("?").first()
        data = MemeSerializer(meme).data
    else:
        meme = MemeSerializer(data=req.data)
        # returns useful response when error.
        if meme.is_valid(raise_exception=True):
            meme.save()
            data = meme.data
    return response.Response(data)


# ===========
# Class-based views.
# ===========
# Concrete views.
# ============
# get
# class random_meme_cbv(generics.RetrieveAPIView):
# get, put
# class random_meme_cbv(generics.RetrieveUpdateAPIView):
# get, delete
# class random_meme_cbv(generics.RetrieveDestroyAPIView):
# get, put, delete
# class _MemeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
class _MemeDetailAPIView(
        generics.RetrieveUpdateDestroyAPIView):
    # essential
    queryset = Meme.objects.all()
    # essential
    serializer_class = MemeSerializer
    # gotta add dat so that there is auth to begin with
    # This list means that if there is at least one auth method that is working, it will allow auth. Same thing for permissions.
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    # gotta add dat so that permissions is not default (777)
    permission_classes = [permissions.IsAdminUser, IsMemeAuthorPermission]

meme_detail_view = _MemeDetailAPIView.as_view()


# get
# class random_meme_cbv_list(generics.ListAPIView):
# get, post
class _MemeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsMemeAuthorPermission]

meme_list_create_view = _MemeListCreateAPIView.as_view()


# no need if using ListCreateAPIView.
# post
# class _MemeCreateAPIView(generics.CreateAPIView):
#     queryset = Meme.objects.all()
#     serializer_class = MemeSerializer
#
# meme_create_view = _MemeCreateAPIView.as_view()


# ===========
# Mixins
# ===========
# basically the same thing as previous type of views.
# kinda better idk, might as well use it.
# actually prev. thing is just a class like this one.
# class _MemeListCreateAPIView(
#         mixins.ListModelMixin,
#         mixins.CreateModelMixin,
#         generics.GenericAPIView):
#     pass

# ===========
# Basic APIView
# ===========
# kinda same thing, but without default implementation. idk why tho.
# class _MemeListCreateAPIView(generics.APIView):
#   get(req) -> res:
