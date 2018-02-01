from model.account.account import AccountOpenedEvent

class TransactionProjection(object):
    def __init__(self, account):
        transactions = []       
        for event in account.events:
            if not isinstance(event, AccountOpenedEvent):
                transactions.append({
                    'type' : type(event).__name__,
                    'amount' : event.amount,
                    'sequence' : event.sequence
                })
        projection = {
            'ID' : account.id,            
            'trasactions' : transactions
        }
        self.projection = projection