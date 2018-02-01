import uuid
from model.client.client import Client
from store import MemoryStore
from model.account.transactionEvent import AccountOpenedEvent
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
        MemoryStore.store[client.id] = client        
  
    def get_client(self, clientID):
        try:
            client = MemoryStore.store[uuid.UUID(clientID)]
            client_accounts = self.get_accounts(clientID)            
        except KeyError:
            raise ClientNotFoundException(clientID)
        return client, client_accounts
    
    def get_accounts(self, clientID):
        accounts = []
        for key, account in MemoryStore.store.iteritems():
            if isinstance(account, AccountOpenedEvent) and account.clientUUID == uuid.UUID(clientID):
                accounts.append(account.compositeUUID)
        return accounts