
class ClientProjection(object):
    def __init__(self, client, client_accounts=[]):        
        projection = {
            'clientID' : client.id,
            'name' : client.name,
            'email' : client.email,
            'accounts' : client_accounts
        }
        self.projection = projection