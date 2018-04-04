import uuid
from model.account import Account
from projection import AccountProjection
from service.exception import AccountNotFoundException
from store import MemoryStore
from store import AccountModel
from store import EventModel
from store import AccountProjectionModel
from service.event import EventService
from flask_mail import Message
from datetime import datetime
import decimal


class AccountService(object):
    """This class represent the services to account """
       
    def proccess_new_account(self, clientID):
        """
            Method to create a new account

            Parameters
            -----------            
            clientID : str UUID
        """
        account = Account(uuid.uuid4(), uuid.UUID(clientID))
        #self.send_email(account)
        account_model = AccountModel(account)
        account_model.save()       
        projection = AccountProjectionModel(account._id, 0)
        projection.save()
        self.send_email(account)
        EventService.save_events(account._events)
        return account
      
    def get_account(self, account_id):
        """
            Method to get an account

            Parameters
            -----------
            accountID : str UUID

            Returns
            --------
            account
                an instance of Account
        """
        try:
            account = AccountModel.get(account_id)
            if not account:
                raise AccountNotFoundException(account_id)
        except (KeyError, ValueError):
            raise AccountNotFoundException(account_id)                       
        return account 


    def store_account(self, account):
        MemoryStore.store[account.id] = account


    def proccess_deposit(self, amount, account_id):        
        account_domain = self.get_domain(account_id)
        account_domain.deposit(amount)
        self.set_projection(account_id, amount)
        event_model = EventModel(account_domain._events[-1])
        event_model.save()


    def proccess_withdraw(self, amount, account_id):       
        projection = AccountProjectionModel.get(account_id)
        new_balance = projection.balance - decimal.Decimal(amount)
        if new_balance < 0:
            raise ValueError('You don\'t have that amount to withdraw.')
        account_domain = self.get_domain(account_id)
        account_domain.withdraw(amount)
        amount *= -1
        projection.balance += decimal.Decimal(amount)
        projection.save()
        event_model = EventModel(account_domain._events[-1])
        event_model.save()


    def set_projection(self, account_id, amount):
        projection = AccountProjectionModel.get(account_id)
        projection.balance += decimal.Decimal(amount)
        projection.save()


    def get_domain(self, account_id):
        account_model = self.get_account(account_id)
        events = EventModel.get(account_id)
        account_domain = Account(account_model.id, account_model.client_id, events)
        return account_domain


    def send_email(self, account):        
        try:
           from app import mail            
           msg = Message('A new account has been created',sender='minibank_system@gmail.com', recipients=['cfo@email']) 
           msg.body = 'A new account has been created with following number {}'.format(account._id)
           mail.send(msg)
           account.sent_email() 
        except Exception as error:
            raise Exception(error)    