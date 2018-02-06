from flask_restful import Resource, reqparse
from flask import request, url_for, jsonify
from service.client import ClientService
from service import ClientNotFoundException
from projection import ClientProjection

class ClientResource(Resource):
    def __init__(self):
        super(ClientResource, self).__init__()        
        self.__service = ClientService()        
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('name',
            type=str,
            required=True,
            help="This field cannot be empty"
        )
        self.__parser.add_argument('email',
            type=str,
            required=True,
            help="This field cannot be empty"
        )   

    def get(self, id):
        try:        
            client, client_accounts = c_service.get_client(id)
            client_projection = ClientProjection(client, client_accounts)
        except (KeyError, ClientNotFoundException) as ex:
            return {'Message': str(ex)}, 404
        return jsonify(client_projection.projection)
        
   
    def post(self):        
        command = parser.parse_args()       
        client = c_service.process_new_client(command)      
        return url_for('client', id=client.id), 201
        
