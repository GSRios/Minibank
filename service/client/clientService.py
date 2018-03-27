from model import Client
from store import MemoryStore
from store import ClientModel
from model import Account
from service.exception import ClientNotFoundException
from service.event import EventService
from projection import ClientProjection
import json
import uuid

class ClientService(object):
    def __init__(self):
        pass

    def process_new_client(self, command):       
        client = Client(uuid.uuid4(), **command)        
        model_client = ClientModel(client)
        model_client.save()
        EventService.save(client._events)
        return client
    
    def store_client(self, client):
        #MemoryStore.store[client.id] = client        
        pass
  
    def get_client(self, client_id):
        try:           
            client = ClientModel.get(uuid.UUID(client_id))
            if not client:
                 raise ClientNotFoundException(client_id)
        except (KeyError, ValueError):
            raise ClientNotFoundException(client_id)       
        return client