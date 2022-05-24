from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
from memes.models import Meme
import json


def reverb(req: HttpRequest) -> JsonResponse:
    try:
        data = json.loads(req.body)
    except json.JSONDecodeError:
        data = {}
    return JsonResponse(data)


def random_meme(req: HttpRequest) -> JsonResponse:
    meme = Meme.objects.first()
    data = {'name': meme.name}
    return JsonResponse(data)
