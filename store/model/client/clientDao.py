from store import Connection

class ClientDAO(Connection):
    def __init__(self):
        super(ClientDAO, self).__init__()

    def save_client(self, client):
        pass
    
    def get_client(self, clientID):
        pass

