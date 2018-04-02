from store import AccountProjectionModel

class AccountProjection(object):
    def __init__(self, account_id):
        model = AccountProjectionModel.get(account_id)
        projection = {
            'account_id': model.account_id,            
            'balance'   : '%.3g'%(model.balance)
        }
        self.projection = projection