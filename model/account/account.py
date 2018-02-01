from domain import Composite
from transactionEvent import AccountOpenedEvent, DepositEvent, WithdrawEvent
import datetime

class Account(Composite):
    def __init__(self, accountUUID, clientUUID, account_events=[]):
        super(Account, self).__init__(accountUUID, account_events)         
        self.clientID = clientUUID          
        self.events.append(AccountOpenedEvent(accountUUID, datetime.datetime.utcnow(), self.get_sequence(), clientUUID))
        

    def deposit(self, amount):
        self.events.append(DepositEvent (self.id, datetime.datetime.utcnow(), self.get_sequence(), amount))
       
    def withdraw(self, amount):        
        self.events.append(WithdrawEvent(self.id, datetime.datetime.utcnow(), self.get_sequence(), amount*-1))