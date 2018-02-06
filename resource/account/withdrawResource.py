from flask_restful import Resource, reqparse
from flask import url_for
from model.account import Account
from service.account import AccountService
from service import AccountNotFoundException

class WithdrawAccountResource(Resource):

    def __init__(self):
        super(WithdrawAccountResource, self).__init__()
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('amount',
            type=float,
            required=True,
            help='This field cannot be empty'
        ) 
        self.__service = AccountService()
    
    def post(self, accountID):
        data = self.__parser.parse_args()
        amount = data['amount']
        try:
            self.__service.proccess_withdraw(amount, accountID)      
        except ValueError as value_error:
            return {'Message': str(value_error)}, 403
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found) }, 404    
        return {"Message":"Transaction completed with success"}
        

