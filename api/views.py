from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
import json


def reverb(req: HttpRequest) -> JsonResponse:
    try:
        data = json.loads(req.body)
    except:
        data = {}
    return JsonResponse(data)
