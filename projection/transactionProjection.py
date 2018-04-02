from model.account.account import AccountOpenedEvent
from store import EventModel

class TransactionProjection(object):
    def __init__(self, account_id):
        events = EventModel.get(account_id)
        transactions = [{'type' : event.type, 'amount' : '%.2g'%(event.amount)} for event in events if event.type == 'DepositEvent' or event.type == 'WithdrawEvent']       
        projection = {
            'account_id' : account_id,            
            'trasactions' : transactions
        }
        self.projection = projection