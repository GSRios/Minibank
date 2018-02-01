from flask_restful import Resource, reqparse
from flask import url_for, jsonify
from model.account.account import Account
from service.account import AccountService
from service import AccountNotFoundException
from projection.accountProjection import AccountProjection

class AccountResource(Resource):
    global parser
    parser = reqparse.RequestParser()
    parser.add_argument('clientID',
        type=str,
        required=True,
        help="This field cannot be empty"
    )

    global account_service
    account_service = AccountService()

    def get(self, id):
        try:            
            account = account_service.get_account(id)
            account_projection = AccountProjection(account)
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found)}, 404

        return jsonify(account_projection.projection)

    def post(self):
        data = parser.parse_args()
        try:
            account = account_service.proccess_new_account(data.get('clientID'))
        except Exception:
            return {'Message' : 'An error ocurred'}, 404
        return url_for('account', id=account.id), 201
        


