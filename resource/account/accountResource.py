from flask_restful import Resource, reqparse
from flask import url_for, jsonify
from model.account.account import Account
from service import AccountNotFoundException, AccountService
from projection.accountProjection import AccountProjection

class AccountResource(Resource):
    def __init__(self):
        super(AccountResource, self).__init__()
        self.__service = AccountService()
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('clientID',
            type=str,
            required=True,
            help="This field cannot be empty"
        ) 

    def get(self, id):
        try:            
            account = self.__service.get_account(id)
            account_projection = AccountProjection(account)
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found)}, 404

        return jsonify(account_projection.projection)

    def post(self):
        data = self.__parser.parse_args()
        try:
            account = self.__service.proccess_new_account(data.get('clientID'))
        except Exception:
            return {'Message' : 'An error ocurred'}, 404
        return url_for('account', id=account.id), 201
        


