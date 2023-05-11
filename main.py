## For the client config tool

class ClientConfig:
    
    def __init__(self, name, id, commisionTolerance, grossAmountTolerance) -> None:
        self.name = name
        self.id = id
        self.commisionTolerance = commisionTolerance
        self.grossAmountTolerance = grossAmountTolerance


def clientConfigChangeRequest(newClientConfig):
    pass

def clientConfigChangeApprove(newClientConfig):
    pass

def clientConfigChangeDeny(newClientConfig):
    pass

def getClientConfig(id):
    pass
