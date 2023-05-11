## Trade processing engine CLI

def getClientConfig(clientId) -> tuple[float, float] | None:
    # query client config tool for client's commisionDifferenceTolerance and grossAmountDifferenceTolerance
    return (1.1, 2.1)

def processUserInput(clientId, commisionDifference, grossAmountDifference) -> bool:
    # query client config tool for client's commisionDifferenceTolerance and grossAmountDifferenceTolerance
    tpl = getClientConfig(clientId)
    if tpl is None:
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

