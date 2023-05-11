import requests
from codetoconnect.client_configuration_tool.models import Requests

from codetoconnect.client_configuration_tool.views import clientConfigChangeApprove, clientConfigChangeRequest

## Trade processing engine CLI

def getClientConfig(clientId) -> tuple[float, float] | None:
    # query client config tool for client's commisionDifferenceTolerance and grossAmountDifferenceTolerance
    # TODO: send http get request to get client config based on clientId
    response = requests.get("http://127.0.0.1:8000/client_configuration_tool/api?client_id=" + clientId)
    print(response)
    if response.status_code != 200:
        return None
    print(response.json())
    return response.json()["commission_difference_tolerance"], response.json()["gross_amount_difference_tolerance"]

def processUserInput(clientId, commisionDifference, grossAmountDifference) -> bool:
    # query client config tool for client's commisionDifferenceTolerance and grossAmountDifferenceTolerance
    tpl = getClientConfig(clientId)
    if tpl is None:
        return False
    commDiffTolerance, grossDiffTolerance = tpl
    return commisionDifference <= commDiffTolerance and grossAmountDifference <= grossDiffTolerance

if __name__ == "__main__":
    while True:
        action = input("Enter R to submit a new request, A to approve an existing request or q to quit: ")
        userid = input("Enter your user id: ")
        if action == 'q':
            break
        
        isSuccess = False
        if action == 'R':
            grossAmountToleranceTo = input("Enter the initial gross amount tolerance: ")
            commisionToleranceTo = input("Enter the initial commision tolerance: ")
            isSuccess = clientConfigChangeRequest(None, userid, grossAmountToleranceTo, commisionToleranceTo)
        elif action == 'A':
            requestid = input("Enter the request id: ")
            isSuccess = clientConfigChangeApprove(request=Requests.objects.get(id=requestid), verifier_id=userid)
        
        if isSuccess:
            print("Request submitted")
        else:
            print("Request failed")