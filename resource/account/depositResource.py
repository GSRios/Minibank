from flask_restful import Resource, reqparse
from service.account.accountService import AccountService
from flask import url_for
from model.account.account import Account
from service.account import AccountService
from service import AccountNotFoundException

class DepositAccountResource(Resource):
    
    def __init__(self):
        super(DepositAccountResource, self).__init__()
        self.__service = AccountService()
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('amount',
            type=float,
            required=True,
            help='This field cannot be empty'
        ) 
    
    def post(self, accountID):
        data = self.__parser.parse_args()
        amount = data['amount']
        try:
            self.__service.proccess_deposit(amount, accountID)
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found)}, 404    
        return {"Message":"Transaction completed with success"}