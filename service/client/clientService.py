import uuid
from model.client.client import Client
from store import MemoryStore
from model import Account
from service.exception import ClientNotFoundException
from projection import ClientProjection
import json

class ClientService(object):
    def __init__(self):
        pass

    def process_new_client(self, command):       
        client = Client(uuid.uuid4(), command['name'], command['email'])        
        self.store_client(client)              
        return client
    
    def store_client(self, client):
        #MemoryStore.store[client.id] = client        
        pass
  
    def get_client(self, clientID):
        try:
            client = MemoryStore.store[uuid.UUID(clientID)]
            if not isinstance(client, Client):
                raise ClientNotFoundException(clientID)
            client_accounts = self.get_accounts(clientID)            
        except (KeyError, ValueError):
            raise ClientNotFoundException(clientID)       
        return client, client_accounts
    
    def get_accounts(self, clientID):
        accounts = []
        for key, account in MemoryStore.store.iteritems():
            if isinstance(account, Account) and account.clientID == uuid.UUID(clientID):
                accounts.append(account.id)
        return accounts