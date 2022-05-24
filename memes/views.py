from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Meme
from .serializers import MemeSerializer
import json


# simple api
# def random_meme(req: HttpRequest) -> JsonResponse:
#     meme = Meme.objects.first()
#     # simplest version
#     # data = {'name': meme.name}
#     # second simplest version
#     data = model_to_dict(meme, fields=["name"])
#     return JsonResponse(data)

# drf api
@api_view(["GET"])
def random_meme(req: HttpRequest) -> Response:
    meme = Meme.objects.first()
    data = MemeSerializer(meme).data
    return Response(data)
