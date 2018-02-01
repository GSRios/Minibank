from flask_restful import Resource, reqparse
from flask import request, url_for, jsonify
from service.client.clientService import ClientService
#from projection import ClientProjection

class ClientResource(Resource):
    global c_service
    c_service = ClientService() 
    global parser
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be empty"
    )
    parser.add_argument('email',
        type=str,
        required=True,
        help="This field cannot be empty"
    )   
    def get(self, id):        
        #client_projection = ClientProjection(id)
        #return jsonify(client_projection.projection)
        pass
   
    def post(self):        
        command = parser.parse_args()       
        client = c_service.process_new_client(command)      
        return url_for('client', id=client.id), 201
        
