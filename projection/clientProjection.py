#from service import ClientService

#class ClientProjection(object):
#    def __init__(self, clientID):
#        client_service = ClientService()
#        client = client_service.get_client(clientID)
#        projection = {
#            'clientID' : clientID,
#            'name' : client.name,
#            'email' : client.email,
#            'accounts' : client_service.get_accounts(clientID)
#        }
#        self.projection = projection