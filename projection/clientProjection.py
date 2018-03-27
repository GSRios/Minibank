
class ClientProjection(object):
    def __init__(self, client):        
        projection = {
            'client_id' : client.id,
            'name' : client.name,
            'email' : client.email,
            'accounts' : [account.id for account in client.accounts.all()]
        }
        self.projection = projection