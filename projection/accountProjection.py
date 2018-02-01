from model.account.account import AccountOpenedEvent

class AccountProjection(object):
    def __init__(self, account):        
        projection = {
            'ID' : account.id,
            'clientID' : account.clientID,
            'balance' : sum([event.amount for event in account.events if not isinstance(event, AccountOpenedEvent)])
        }
        self.projection = projection