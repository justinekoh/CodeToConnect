from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest

from client_configuration_tool.models import ClientConfigurations


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def api(request: HttpRequest):
    params = request.GET
    client_id = params["client_id"]
    try:
      client  = ClientConfigurations.objects.get(id=client_id)
    except ClientConfigurations.DoesNotExist:
      return JsonResponse({"commission_difference": None, "gross_amount_difference": None})    
    # client = ClientConfigurations.objects.create(name="Client1", commisionTolerance=30, grossAmountTolerance=20)
    commission_difference_tolerance = client.commisionTolerance
    gross_amount_difference_tolerance = client.grossAmountTolerance
    return JsonResponse({"commission_difference_tolerance": commission_difference_tolerance, "gross_amount_difference_tolerance": gross_amount_difference_tolerance})