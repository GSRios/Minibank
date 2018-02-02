import uuid
from model.account import Account
from projection import AccountProjection
from service.exception import AccountNotFoundException
from store import MemoryStore
import smtplib
from datetime import datetime

class AccountService(object):
    """This class represent the services to account """
    def __init__(self):
        pass
   
    def proccess_new_account(self, clientID):
        """
            Method to create a new account

            Parameters
            -----------            
            clientID : str UUID
        """
        account = Account(uuid.uuid4(), uuid.UUID(clientID))
        #self.send_email(account)
        self.store_account(account)
        return account
      
    def get_account(self, accountID):
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
            account = MemoryStore.store[uuid.UUID(accountID)]
            if not isinstance(account, Account):
                raise AccountNotFoundException(accountID)
        except (KeyError, ValueError):
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

    def send_email(self, account):
        timestamp = 0
        try:
            user = 'minibank.system@gmail.com'
            password = 'password'
            to = 'cfo_email@gmail.com'
            msg = "\r\n".join([
                "From: {}".format(user),
                "To: {}".format(to),
                "Subject: A new account has been created with this ID: {}".format(account.id),
                "",
                "Hello, A new account has been create to the following client {} with this ID {}".format(account.clientID, account.id)
            ])
            smtp_server = smtplib.SMTP('smtp.gmail.com:587')
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(user, password)
            timestamp = datetime.now()
            smtp_server.sendmail(user, to, msg)
            smtp_server.close()
        except Exception as error:
            raise Exception(str(error))

        return timestamp