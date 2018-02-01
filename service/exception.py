class AccountNotFoundException(Exception):
    def __init__(self, accountID):
        super(AccountNotFoundException, self).__init__('Oops we\'re sorry about that, but we cannot find any account with the following ID: {}'.format(accountID))        


class ClientNotFoundException(Exception):
    def __init__(self, clientID):
        super(ClientNotFoundException, self).__init__('Oops we\'re sorry about that, but we cannot find any client with the following ID: {}'.format(clientID))