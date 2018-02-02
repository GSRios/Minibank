from store import Connection

class AccountDAO(Connection):
    def __init__(self):
        super(AccountDAO, self).__init__()

    def save_account(self, account):
        pass
    
    def get_account(self, accoutID):
        pass