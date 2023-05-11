from django.http import JsonResponse, HttpRequest
from client_configuration_tool.models import ClientConfigurations

def get_client_configurations(request):
    params = request.GET
    client_id = params["client_id"]
    try:
      client  = ClientConfigurations.objects.get(id=client_id)
    except ClientConfigurations.DoesNotExist:
      return JsonResponse({"commission_difference": None, "gross_amount_difference": None})    
    commission_difference_tolerance = client.commisionTolerance
    gross_amount_difference_tolerance = client.grossAmountTolerance
    return JsonResponse({"commission_difference_tolerance": commission_difference_tolerance, \
                         "gross_amount_difference_tolerance": gross_amount_difference_tolerance})