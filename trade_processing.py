import requests

## Trade processing engine CLI

def getClientConfig(clientId) -> tuple[float, float] | None:
    # query client config tool for client's commisionDifferenceTolerance and grossAmountDifferenceTolerance
    response = requests.get("http://127.0.0.1:8000/client_configuration_tool/api?client_id=" + clientId)
    if response.status_code != 200:
        return None
    print(response.json())
    return response.json()["commission_difference_tolerance"], response.json()["gross_amount_difference_tolerance"]

def processUserInput(clientId, commisionDifference, grossAmountDifference) -> bool:
    # query client config tool for client's commisionDifferenceTolerance and grossAmountDifferenceTolerance
    tpl = getClientConfig(clientId)
    if tpl[0] is None and tpl[1] is None:
        return False
    commDiffTolerance, grossDiffTolerance = tpl
    return commisionDifference <= commDiffTolerance and grossAmountDifference <= grossDiffTolerance

if __name__ == "__main__":
    while True:
        clientId = input("Enter your client id or 'q' to quit: ")
        if clientId == 'q':
            break
        commisionDifference = input("Enter the commision difference: ")
        grossAmountDifference = input("Enter the gross amount difference: ")
        if processUserInput(clientId, float(commisionDifference), float(grossAmountDifference)):
            print("Trade accepted")
        else:
            print("Trade rejected")

