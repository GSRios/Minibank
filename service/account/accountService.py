import uuid
from model.account import Account
from projection import AccountProjection
from service.exception import AccountNotFoundException
from store import MemoryStore
class AccountService(object):
    
    def __init__(self):
        pass
   
    def proccess_new_account(self, clientID):
        account = Account(uuid.uuid4(), uuid.UUID(clientID))
        self.store_account(account)
        return account
      
    def get_account(self, accountID):
        try:
            account = MemoryStore.store[uuid.UUID(accountID)]
        except KeyError:
            raise AccountNotFoundException(accountID)                       
        return account 

    def store_account(self, account):
        MemoryStore.store[account.id] = account

    def proccess_deposit(self, amount, accountID):
        account = self.get_account(accountID)
        account.deposit(amount)        
        return account

    def proccess_withdraw(self, amount, accountID):
        account = self.get_account(accountID)
        projection = AccountProjection(account)
        balance = projection.projection.get('balance') - amount
        if balance < 0:
            raise ValueError('You don\'t have that amount to withdraw.')
        account.withdraw(amount)
