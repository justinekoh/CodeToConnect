from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.db import transaction

from client_configuration_tool.models import ClientConfigurations, AuditLogs, Requests, Users, Roles

@transaction.atomic
def clientConfigChangeRequest(clientConfigId, requesterId, grossAmountToleranceTo, commisionToleranceTo):
    timeNow = datetime.now()
    requestor = Users.objects.get(id=requesterId)
    if clientConfigId is None:
        request = Requests.objects.create(requestTime=timeNow, requesterId=requestor, clientConfigId_id=clientConfigId,\
                      grossAmountToleranceTo=grossAmountToleranceTo, commisionToleanceTo=commisionToleranceTo)
        AuditLogs.objects.create(createdAt=timeNow, statusId=1, requesterId=requestor, clientConfigId_id=clientConfigId,\
                       grossAmountToleranceTo=grossAmountToleranceTo, commisionToleanceTo=commisionToleranceTo, \
                       grossAmountToleranceFrom=None,
                       commisionToleranceFrom=None, requestId=request.id)
        return

    clientConfig = ClientConfigurations.objects.get(id=clientConfigId)
    if clientConfig is None:       
        raise Exception("Client config not found")
        
    request = Requests.objects.create(requestTime=timeNow, requesterId=requestor, clientConfigId_id=clientConfigId,\
                     grossAmountToleranceTo=grossAmountToleranceTo, commisionToleanceTo=commisionToleranceTo)
    # AuditLogs.objects.create(createdAt=timeNow, statusId=1, requesterId=requesterId, clientConfigId_id=clientConfigId,\
    #                   grossAmountToleranceTo=grossAmountToleranceTo, commisionToleranceTo=commisionToleranceTo, \
    #                   grossAmountToleranceFrom=clientConfig.grossAmountTolerance,\
    #                  commisionToleranceFrom=clientConfig.commisionTolerance, request_id=request.id)

def index(request):
    clientConfigChangeRequest(None, 1, 20, 30)
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