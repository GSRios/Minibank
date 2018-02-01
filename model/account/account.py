from domain import Composite
from transactionEvent import AccountOpenedEvent, DepositEvent, WithdrawEvent
from emailDispatcherEvent import DispatcherEmailEvent
import datetime

class Account(Composite):
    def __init__(self, accountID, clientID, account_events=[]):
        super(Account, self).__init__(accountID, account_events)         
        self.clientID = clientID          
        self.events.append(AccountOpenedEvent(accountID, datetime.datetime.utcnow(), self.get_sequence(), clientID))
        

    def deposit(self, amount):
        self.events.append(DepositEvent (self.id, datetime.datetime.utcnow(), self.get_sequence(), amount))
       
    def withdraw(self, amount):        
        self.events.append(WithdrawEvent(self.id, datetime.datetime.utcnow(), self.get_sequence(), amount*-1))

    def sent_email(self, sent_at):
        self.events.append(DispatcherEmailEvent(self.id, self.get_sequence, sent_at))