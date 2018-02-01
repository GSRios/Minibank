from flask_restful import Resource, reqparse
from service.account.accountService import AccountService
from flask import url_for
from model.account.account import Account
from service.account import AccountService
from service import AccountNotFoundException

class DepositAccountResource(Resource):
    
    global parser
    parser = reqparse.RequestParser()
    parser.add_argument('amount',
        type=float,
        required=True,
        help='This field cannot be empty'
    )

    def post(self, accountID):
        data = parser.parse_args()
        amount = data['amount']
        account_service = AccountService()
        try:
            account = account_service.proccess_deposit(amount, accountID)
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found)}, 404    
        return {"Message":"Transaction completed with success"}