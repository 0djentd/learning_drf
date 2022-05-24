from django.http import JsonResponse
from django.http import HttpRequest
import json


def reverb(req: HttpRequest) -> JsonResponse:
    try:
        data = json.loads(req.body)
    except json.JSONDecodeError:
        data = {}
    return JsonResponse(data)
