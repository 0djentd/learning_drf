from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
from .models import Meme
import json


def random_meme(req: HttpRequest) -> JsonResponse:
    meme = Meme.objects.first()
    data = {'name': meme.name}
    return JsonResponse(data)
