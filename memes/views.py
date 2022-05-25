import json

from django.http import JsonResponse
from django.http import HttpRequest
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import Meme
from .serializers import MemeSerializer


# simple api
# def random_meme(req: HttpRequest) -> JsonResponse:
#     meme = Meme.objects.first()
#     # simplest version
#     # data = {'name': meme.name}
#     # second simplest version
#     data = model_to_dict(meme, fields=["name"])
#     return JsonResponse(data)

# drf api basic serializer
@api_view(["GET", "POST"])
def random_meme(req: HttpRequest) -> Response:
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
    return Response(data)


# Class-based view.
# class random_meme_cbv(generics.RetrieveAPIView):
# class random_meme_cbv(generics.RetrieveUpdateAPIView):
# class random_meme_cbv(generics.RetrieveDestroyAPIView):
class random_meme_cbv(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer


# class random_meme_cbv_list(generics.ListAPIView):
class random_meme_cbv_list(generics.ListCreateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
