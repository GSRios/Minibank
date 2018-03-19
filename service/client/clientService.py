import uuid
from model.client.client import Client
from store import MemoryStore
from store import ClientModel
from store import EventModel
from model import Account
from service.exception import ClientNotFoundException
from projection import ClientProjection
import json

class ClientService(object):
    def __init__(self):
        pass

    def process_new_client(self, command):       
        client = Client(uuid.uuid4(), **command)        
        model_client = ClientModel(client._id, client._name, client._email)
        model_client.save()
        for event in client._events:
            event_model = EventModel(event._composite_id, event._timestamp, event._sequence, type(event).__name__)
            event_model.save()
        return client
    
    def store_client(self, client):
        #MemoryStore.store[client.id] = client        
        pass
  
    def get_client(self, clientID):
        try:
            #client = MemoryStore.store[uuid.UUID(clientID)]
            #if not isinstance(client, Client):
            #    raise ClientNotFoundException(clientID)
            #client_accounts = self.get_accounts(clientID)
            client = ClientModel.get(uuid.UUID(clientID))
        except (KeyError, ValueError):
            raise ClientNotFoundException(clientID)       
        return client
    
    def get_accounts(self, clientID):
        accounts = []
        for key, account in MemoryStore.store.iteritems():
            if isinstance(account, Account) and account.clientID == uuid.UUID(clientID):
                accounts.append(account.id)
        return accounts