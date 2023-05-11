from datetime import datetime
from django.db import transaction
from client_configuration_tool.models import ClientConfigurations, Requests, AuditLogs

@transaction.atomic
def clientConfigChangeRequest(clientConfigId, requesterId, grossAmountToleranceTo, commisionToleranceTo):
    timeNow = datetime.now()
    if clientConfigId is None:
      request = Requests.create(requestTime=timeNow, requesterId=requesterId, clientConfigId_id=clientConfigId,\
                      grossAmountToleranceTo=grossAmountToleranceTo, commisionToleranceTo=commisionToleranceTo)
      AuditLogs.create(createdAt=timeNow, statusId=1, requesterId=requesterId, clientConfigId_id=clientConfigId,\
                      grossAmountToleranceTo=grossAmountToleranceTo, commisionToleranceTo=commisionToleranceTo,
                      grossAmountToleranceFrom=None,
                      commisionToleranceFrom=None, request_id=request.id)
      return
        
    clientConfig = ClientConfigurations.objects.get(id=clientConfigId)
    if clientConfig is None:
      raise Exception("Client config not found")

    request = Requests.create(requestTime=timeNow, requesterId=requesterId, clientConfigId_id=clientConfigId,\
                    grossAmountToleranceTo=grossAmountToleranceTo, commisionToleranceTo=commisionToleranceTo)
    AuditLogs.create(createdAt=timeNow, statusId=1, requesterId=requesterId, clientConfigId_id=clientConfigId,\
                     grossAmountToleranceTo=grossAmountToleranceTo, commisionToleranceTo=commisionToleranceTo,
                     grossAmountToleranceFrom=clientConfig.grossAmountTolerance,
                    commisionToleranceFrom=clientConfig.commisionTolerance, request_id=request.id)

def clientConfigChangeHandler(newClientConfig, isApproved):
    if isApproved:
        return clientconfigChangeApprove(newClientConfig)
    else:
        return clientConfigChangeDeny(newClientConfig)

@transaction.atomic
def clientConfigChangeApprove(newClientConfig):
    pass

@transaction.atomic
def clientConfigChangeDeny(newClientConfig):
    pass

def getClientConfig(id):
    pass
