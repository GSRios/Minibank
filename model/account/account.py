from domain import Composite
from transactionEvent import AccountOpenedEvent, DepositEvent, WithdrawEvent
from emailDispatcherEvent import DispatcherEmailEvent
import datetime

class Account(Composite):
    def __init__(self, accountID, clientID, account_events=[]):
        super(Account, self).__init__(accountID, account_events)         
        self.clientID = clientID          
        self._events.append(AccountOpenedEvent(accountID, datetime.datetime.utcnow(), self.get_sequence()))
        

    def deposit(self, amount):
        self._events.append(DepositEvent (self._id, datetime.datetime.utcnow(), self.get_sequence(), amount))
       
    def withdraw(self, amount):        
        self._events.append(WithdrawEvent(self._id, datetime.datetime.utcnow(), self.get_sequence(), amount*-1))

    def sent_email(self, sent_at):
        self._events.append(DispatcherEmailEvent(self._id, self.get_sequence, sent_at))