from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def api(request: HttpRequest):
    params = request.GET
    client_id = params["client_id"]
    # todo: get client from database
    commission_difference = 20
    gross_amount_difference = 30
    return JsonResponse({"commission_difference": commission_difference, "gross_amount_difference": gross_amount_difference})