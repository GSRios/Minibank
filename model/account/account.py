from domain import Composite
from transactionEvent import AccountOpenedEvent
from transactionEvent import DepositEvent
from transactionEvent import WithdrawEvent
from emailDispatcherEvent import DispatcherEmailEvent
import datetime

class Account(Composite):
    def __init__(self, account_id, clientID, account_events=[]):
        super(Account, self).__init__(account_id, account_events)         
        self.clientID = clientID   
        account_opened_event = AccountOpenedEvent(account_id, datetime.datetime.utcnow(), self.get_sequence())
        self._events.append(account_opened_event)
        
    def deposit(self, amount):
        deposit_event = DepositEvent (self._id, datetime.datetime.utcnow(), self.get_sequence(), amount)
        self._events.append(deposit_event)
       
    def withdraw(self, amount):
        withdraw_event = WithdrawEvent(self._id, datetime.datetime.utcnow(), self.get_sequence(), amount)         
        self._events.append(withdraw_event)

    def sent_email(self, sent_at):
        self._events.append(DispatcherEmailEvent(self._id, self.get_sequence, sent_at))