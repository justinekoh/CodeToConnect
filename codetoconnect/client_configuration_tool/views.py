from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.db import transaction

from client_configuration_tool.models import ClientConfigurations, AuditLogs, Requests, Users

@transaction.atomic
def clientConfigChangeRequest(clientConfigId, requesterId, grossAmountToleranceTo, commisionToleranceTo):
    timeNow = datetime.now()
    requestor = Users.objects.get(id=requesterId)
    if clientConfigId is None:
        request = Requests.objects.create(requestTime=timeNow, requesterId=requestor, clientConfigId_id=clientConfigId,\
                      grossAmountToleranceTo=grossAmountToleranceTo, commisionToleanceTo=commisionToleranceTo)
        AuditLogs.objects.create(createdAt=timeNow, statusId=1, requesterId=requestor, clientConfigId_id=clientConfigId,\
                       grossAmountToleranceTo=grossAmountToleranceTo, commisionToleanceTo=commisionToleranceTo, \
                       grossAmountToleranceFrom=None,\
                       commisionToleranceFrom=None, requestId=request.id)
        return True

    clientConfig = ClientConfigurations.objects.get(id=clientConfigId)
    if clientConfig is None:       
        raise Exception("Client config not found")
        
    request = Requests.objects.create(requestTime=timeNow, requesterId=requestor, clientConfigId_id=clientConfigId,\
                     grossAmountToleranceTo=grossAmountToleranceTo, commisionToleanceTo=commisionToleranceTo)
    AuditLogs.objects.create(createdAt=timeNow, statusId=1, requesterId=requesterId, clientConfigId_id=clientConfigId,\
                      grossAmountToleranceTo=grossAmountToleranceTo, commisionToleranceTo=commisionToleranceTo, \
                      grossAmountToleranceFrom=clientConfig.grossAmountTolerance,\
                     commisionToleranceFrom=clientConfig.commisionTolerance, request_id=request.id)
    return True
    
def clientConfigChangeApprove(request, verifier_id):
    # check verifier_id != requeter_id
    requestor_id = request.requesterId
    if verifier_id == requestor_id:
        raise Exception("Verifier and requester cannot be same")

    timeNow = datetime.now()
    clientConfigId = request.clientConfigId
    if clientConfigId is None:
        # creating new client config
        clientConfig = ClientConfigurations.objects.create(name="ClientDummyName", commisionTolerance=request.commisionToleanceTo, grossAmountTolerance=request.grossAmountToleranceTo)
        AuditLogs.objects.create(createdAt=timeNow, statusId=2, requesterId=request.requesterId, clientConfigId_id=clientConfig.id,\
                      grossAmountToleranceTo=request.grossAmountToleranceTo, commisionToleanceTo=request.commisionToleanceTo, \
                      grossAmountToleranceFrom=clientConfig.grossAmountTolerance,\
                     commisionToleranceFrom=clientConfig.commisionTolerance, requestId=request.id)
        return True

    # updating existing client config
    clientConfig = ClientConfigurations.objects.get(id=clientConfigId)
    clientConfig.update(commisionTolerance=request.commisionToleanceTo, grossAmountTolerance=request.grossAmountToleranceTo)
    # create audit log
    AuditLogs.objects.create(createdAt=timeNow, statusId=2, requesterId=request.requesterId, clientConfigId_id=request.clientConfigId,\
                      grossAmountToleranceTo=request.grossAmountToleranceTo, commisionToleanceTo=request.commisionToleanceTo, \
                      grossAmountToleranceFrom=clientConfig.grossAmountTolerance,\
                     commisionToleranceFrom=clientConfig.commisionTolerance, requestId=request.id)
    # update client config
    return True

def clientConfigChangeReject(request):
    # create a audittrail
    AuditLogs.objects.create(createdAt=datetime.now(), statusId=3, requesterId=request.requesterId, clientConfigId_id=request.clientConfigId)

def index(request):
    clientConfigChangeRequest(None, 1, 20, 30)
    clientConfigChangeApprove(request=Requests.objects.get(id=1), verifier_id=2)
    # clientConfigChangeReject(request=Requests.objects.get(id=1))
    return HttpResponse("Hello, world. You're at the polls index.")

def api(request: HttpRequest):
    params = request.GET
    client_id = params["client_id"]
    try:
      client  = ClientConfigurations.objects.get(id=client_id)
    except ClientConfigurations.DoesNotExist:
      return JsonResponse({"commission_difference": None, "gross_amount_difference": None})    
    commission_difference_tolerance = client.commisionTolerance
    gross_amount_difference_tolerance = client.grossAmountTolerance
    return JsonResponse({"commission_difference_tolerance": commission_difference_tolerance, "gross_amount_difference_tolerance": gross_amount_difference_tolerance})